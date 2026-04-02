// Gemini 页面元素选择器
export const SELECTORS = {
    // 输入框 - Gemini 使用 rich-textarea（无placeholder）或 contenteditable div
    inputBox: 'rich-textarea, textarea[placeholder*="prompt"], div[contenteditable="true"][role="textbox"], div[contenteditable="true"]',
    // 模式选择按钮
    modeButton: '[aria-label*="mode"], button[aria-label*="mode"], [class*="mode-picker"]',
    // 模式选项
    modeOptions: {
        fast: 'text=Fast, [role="option"]:has-text("Fast")',
        thinking: 'text=Thinking, [role="option"]:has-text("Thinking")',
        pro: 'text=Pro, [role="option"]:has-text("Pro")',
    },
    // 响应内容 - Gemini 的回复在 response-content 类中
    responseContent: '[class*="response-content"], [class*="presented-response"], article.response-body, [data-testid="gemini-response"]',
    // 登录状态检测
    signInLink: 'a:has-text("Sign in"), button:has-text("Sign in")',
    accountButton: '[aria-label*="Account"], button[aria-label*="@"]',
    proBadge: 'text=PRO, [aria-label*="PRO"]',
};
export const GEMINI_URL = 'https://gemini.google.com';
