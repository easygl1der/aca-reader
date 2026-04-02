import { type Browser, type Page } from 'puppeteer';
export declare function initializeBrowser(): Promise<{
    browser: Browser;
    page: Page;
}>;
export declare function getPage(): Promise<Page>;
export declare function closeBrowser(): Promise<void>;
export declare function isBrowserInitialized(): boolean;
