export type GeminiMode = 'fast' | 'thinking' | 'pro';

export interface AskOptions {
  mode?: GeminiMode;
  timeout?: number;
}

export interface LoginStatus {
  isLoggedIn: boolean;
  hasPro: boolean;
  email?: string;
}

export interface AskResult {
  success: boolean;
  response?: string;
  error?: string;
  mode: GeminiMode;
}

export interface BrowserState {
  browser: import('puppeteer').Browser | null;
  context: import('puppeteer').BrowserContext | null;
  page: import('puppeteer').Page | null;
  isInitialized: boolean;
}
