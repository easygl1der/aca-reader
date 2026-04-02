import { getPage } from '../browser/manager.js';
import { SELECTORS } from '../utils/selectors.js';
export async function checkLoginStatus() {
    try {
        const page = await getPage();
        // 检查是否显示登录按钮（未登录）
        const signInButton = await page.$(SELECTORS.loggedOutSignIn);
        if (signInButton) {
            return { isLoggedIn: false };
        }
        // 检查是否有用户头像/菜单（已登录）
        const userButton = await page.$(SELECTORS.loggedInUserButton);
        if (userButton) {
            // 尝试获取用户名
            const displayName = await page.evaluate(() => {
                const avatar = document.querySelector('[class*="avatar"]');
                const userName = document.querySelector('[class*="display-name"]');
                return userName?.textContent || avatar?.getAttribute('alt') || 'Logged in';
            });
            return { isLoggedIn: true, displayName };
        }
        // 默认视为未登录
        return { isLoggedIn: false };
    }
    catch (error) {
        return {
            isLoggedIn: false,
            error: error instanceof Error ? error.message : String(error),
        };
    }
}
