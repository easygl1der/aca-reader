import { getPage } from '../browser/manager.js';
import { SELECTORS } from '../utils/selectors.js';
const wait = (ms) => new Promise(resolve => setTimeout(resolve, ms));
export async function geminiAsk(question, options = {}) {
    const { mode = 'fast', timeout = 120000 } = options;
    const page = await getPage();
    try {
        // 1. 切换模式（如需要）
        if (mode !== 'fast') {
            await switchMode(page, mode);
        }
        // 2. 找到输入框
        const inputSelector = SELECTORS.inputBox;
        await page.waitForSelector(inputSelector, { timeout: 10000, visible: true });
        // 3. 点击并输入问题
        await page.click(inputSelector);
        // 清空可能存在的旧内容
        await page.keyboard.down('Control');
        await page.keyboard.press('a');
        await page.keyboard.up('Control');
        await page.keyboard.type(question);
        // 4. 提交（按 Enter）
        await page.keyboard.press('Enter');
        // 5. 等待响应出现 - 改进的等待逻辑
        await waitForResponseImproved(page, timeout);
        // 6. 提取响应内容
        const response = await extractResponse(page);
        return {
            success: true,
            response,
            mode,
        };
    }
    catch (error) {
        return {
            success: false,
            error: error instanceof Error ? error.message : String(error),
            mode,
        };
    }
}
async function switchMode(page, mode) {
    try {
        // 点击模式选择器
        const modeButton = await page.$(SELECTORS.modeButton);
        if (modeButton) {
            await modeButton.click();
            await wait(500);
            // 选择对应模式
            const modeOption = SELECTORS.modeOptions[mode];
            const optionElement = await page.$(modeOption);
            if (optionElement) {
                await optionElement.click();
                await wait(300);
            }
        }
    }
    catch {
        // 模式切换失败，继续使用默认模式
    }
}
async function waitForResponseImproved(page, timeout) {
    const startTime = Date.now();
    while (Date.now() - startTime < timeout) {
        try {
            const pageText = await page.evaluate(() => document.body.innerText);
            // 如果页面不再显示 "typing"，认为响应完成
            const isTyping = pageText.includes('typing');
            if (!isTyping) {
                // 额外等待确保内容完全加载
                await wait(1000);
                return;
            }
            await wait(2000);
        }
        catch {
            await wait(1000);
        }
    }
    // 超时检查
    const finalText = await page.evaluate(() => document.body.innerText);
    if (!finalText.includes('Gemini said')) {
        throw new Error(`Response timeout after ${timeout}ms`);
    }
}
async function extractResponse(page) {
    // 方法1：从 presented-response-container 提取（包含最新回复）
    try {
        const containers = await page.$$('[class*="presented-response-container"]');
        for (const container of containers) {
            const text = await page.evaluate((el) => el.textContent || '', container);
            // 清理并返回
            const cleaned = text
                .replace(/Show thinking\s*/gi, '')
                .replace(/\n+/g, ' ')
                .replace(/Pro\s*/g, '')
                .replace(/Gemini is AI and can make mistakes\.\s*/gi, '')
                .replace(/^\s*Gemini said\s*/gi, '')
                .trim();
            if (cleaned.length > 0 && !cleaned.includes('Sign in')) {
                return cleaned;
            }
        }
    }
    catch {
        // 继续
    }
    // 方法2：从页面文本提取 "Gemini said" 后的内容
    const pageText = await page.evaluate(() => document.body.innerText);
    const lines = pageText.split('\n');
    let inGeminiResponse = false;
    let responseLines = [];
    for (const line of lines) {
        if (line.trim().startsWith('Gemini said')) {
            inGeminiResponse = true;
            continue;
        }
        if (inGeminiResponse) {
            if (line.trim() === '' && responseLines.length > 0)
                break;
            if (line.includes('PRO') || line.includes('Sign in') || line.includes('Gemini is AI'))
                continue;
            responseLines.push(line.trim());
            if (responseLines.length > 10)
                break;
        }
    }
    if (responseLines.length > 0) {
        return responseLines.join(' ').trim();
    }
    return pageText.substring(0, 500);
}
