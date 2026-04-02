import puppeteer, { type Browser, type Page } from 'puppeteer';
import path from 'path';
import fs from 'fs';

const PERPLEXITY_URL = 'https://www.perplexity.ai';

// 独立的 Chrome profile 目录，避免与正在运行的 Chrome 冲突
const PERPLEXITY_PROFILE_PATH = path.join(
  process.env.HOME || '/Users/yueyh',
  'Library/Application Support/Google/Chrome',
  'PerplexityProfile'
);

// Chrome 可执行文件路径
const CHROME_EXECUTABLE = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

let browser: Browser | null = null;
let page: Page | null = null;

export async function initializeBrowser(): Promise<{ browser: Browser; page: Page }> {
  if (browser && page) {
    return { browser, page };
  }

  // 确保 profile 目录存在
  if (!fs.existsSync(PERPLEXITY_PROFILE_PATH)) {
    fs.mkdirSync(PERPLEXITY_PROFILE_PATH, { recursive: true });
    console.error(`Created Perplexity profile directory: ${PERPLEXITY_PROFILE_PATH}`);
  }

  // 使用 Puppeteer 启动 Chrome，复用独立 profile
  browser = await puppeteer.launch({
    executablePath: CHROME_EXECUTABLE,
    userDataDir: PERPLEXITY_PROFILE_PATH,  // 复用 profile 保持登录状态
    headless: false,
    args: [
      '--disable-blink-features=AutomationControlled',
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-dev-shm-usage',
    ],
  });

  // 创建新页面
  page = await browser.newPage();

  // 隐藏 webdriver 特征
  await page.evaluateOnNewDocument(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });

  // 设置视口
  await page.setViewport({ width: 1920, height: 1080 });

  // 打开 Perplexity
  await page.goto(PERPLEXITY_URL, { waitUntil: 'networkidle2' });

  return { browser, page };
}

export async function getPage(): Promise<Page> {
  if (!page) {
    await initializeBrowser();
  }
  return page!;
}

export async function closeBrowser(): Promise<void> {
  if (browser) {
    await browser.close();
    browser = null;
    page = null;
  }
}

export function isBrowserInitialized(): boolean {
  return browser !== null && page !== null;
}
