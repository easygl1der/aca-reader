import { getPage } from '../browser/manager.js';
import { SELECTORS } from '../utils/selectors.js';
const wait = (ms) => new Promise(resolve => setTimeout(resolve, ms));
export async function perplexityAsk(question, options = {}) {
    const { timeout = 60000 } = options;
    const page = await getPage();
    try {
        // 1. 找到输入框
        const inputSelector = SELECTORS.inputBox;
        await page.waitForSelector(inputSelector, { timeout: 10000, visible: true });
        // 2. 点击并输入问题
        await page.click(inputSelector);
        // 清空可能存在的旧内容
        await page.keyboard.down('Control');
        await page.keyboard.press('a');
        await page.keyboard.up('Control');
        await page.keyboard.type(question);
        // 3. 提交（按 Enter）
        await page.keyboard.press('Enter');
        // 4. 等待响应出现
        await waitForResponse(page, timeout);
        // 5. 提取响应内容
        const response = await extractResponse(page);
        return {
            success: true,
            response,
        };
    }
    catch (error) {
        return {
            success: false,
            error: error instanceof Error ? error.message : String(error),
        };
    }
}
async function waitForResponse(page, timeout) {
    const startTime = Date.now();
    while (Date.now() - startTime < timeout) {
        try {
            // 检查是否有响应内容出现
            const responseElement = await page.$(SELECTORS.responseContent);
            if (responseElement) {
                const isVisible = await responseElement.isVisible();
                if (isVisible) {
                    await wait(1000); // 等待内容稳定
                    return;
                }
            }
            // 检查是否有加载中的 spinner
            const isLoading = await page.evaluate(() => {
                const spinner = document.querySelector(SELECTORS.loadingSpinner);
                return spinner !== null;
            });
            if (!isLoading) {
                // 等待一下确保内容已加载
                await wait(1500);
                return;
            }
        }
        catch {
            // 继续等待
        }
        await wait(500);
    }
    throw new Error(`Response timeout after ${timeout}ms`);
}
async function extractResponse(page) {
    const selectors = [
        SELECTORS.responseContent,
        SELECTORS.responseContentAlt,
        SELECTORS.responseContentAlt2,
    ];
    for (const selector of selectors) {
        try {
            const element = await page.$(selector);
            if (element && await element.isVisible()) {
                const text = await page.evaluate((el) => el.textContent || '', element);
                if (text)
                    return text;
            }
        }
        catch {
            // 继续尝试下一个选择器
        }
    }
    // 回退：获取页面主内容区域文本
    try {
        const bodyText = await page.evaluate(() => {
            const main = document.querySelector('main, [role="main"], article');
            return main?.textContent || document.body.textContent || '';
        });
        return bodyText;
    }
    catch {
        return '';
    }
}
