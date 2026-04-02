// Perplexity UI 选择器
// 注意：Perplexity 可能更新 UI，选择器可能需要调整
export const SELECTORS = {
    // 主输入框 - placeholder="Ask anything…"
    inputBox: '[placeholder="Ask anything…"]',
    inputBoxAlt: 'textarea[placeholder*="Ask"]',
    // 提交按钮（回车提交）
    submitButton: '[class*="submit"]',
    submitButtonAlt: '[class*="send"]',
    // 响应内容
    responseContent: '[class*="response"]',
    responseContentAlt: 'article',
    responseContentAlt2: '[class*="answer"]',
    // 登录状态检测
    loggedInAvatar: '[class*="avatar"]',
    loggedInUserButton: '[class*="user-menu"]',
    loggedOutSignIn: 'text=Sign in',
    // 加载状态
    loadingSpinner: '[class*="loading"]',
    loadingSpinnerAlt: '[class*="spinner"]',
};
