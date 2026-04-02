import { getPage, isBrowserInitialized } from '../browser/manager.js';
import { SELECTORS } from '../utils/selectors.js';
import type { LoginStatus } from '../types/index.js';

export async function checkLoginStatus(): Promise<LoginStatus> {
  if (!isBrowserInitialized()) {
    return { isLoggedIn: false, hasPro: false };
  }

  const page = await getPage();

  try {
    // 检查是否有 "PRO" 徽章
    const proBadge = await page.$(SELECTORS.proBadge);
    const hasPro = proBadge !== null && await proBadge.isVisible().catch(() => false);

    // 检查是否有登录的用户信息
    const accountButton = await page.$(SELECTORS.accountButton);
    const hasAccount = accountButton !== null && await accountButton.isVisible().catch(() => false);

    // 尝试获取邮箱
    let email: string | undefined;
    if (accountButton) {
      const ariaLabel = await accountButton.evaluate((el: Element) => el.getAttribute('aria-label') || '');
      const match = ariaLabel.match(/[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/);
      email = match ? match[0] : undefined;
    }

    return {
      isLoggedIn: hasAccount || hasPro,
      hasPro,
      email,
    };
  } catch {
    return { isLoggedIn: false, hasPro: false };
  }
}
