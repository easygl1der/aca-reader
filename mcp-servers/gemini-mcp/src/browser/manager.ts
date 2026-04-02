import puppeteer from 'puppeteer';
import path from 'path';
import fs from 'fs';

const GEMINI_URL = 'https://gemini.google.com';

// Puppeteer profile 路径 - 复用 ms-playwright 的 Edge profile
// 因为 Edge 和 Chrome 都基于 Chromium，profile 格式兼容
const EDGE_PROFILE_PATH = path.join(
  process.env.HOME || '/Users/yueyh',
  'Library/Caches/ms-playwright/mcp-msedge-b2a6ca1'
);

let browser: puppeteer.Browser | null = null;
let page: puppeteer.Page | null = null;

export async function initializeBrowser(): Promise<{ browser: puppeteer.Browser; page: puppeteer.Page }> {
  if (browser && page) {
    return { browser, page };
  }

  // 检查 profile 是否存在
  if (!fs.existsSync(EDGE_PROFILE_PATH)) {
    throw new Error(`Edge profile not found at: ${EDGE_PROFILE_PATH}`);
  }

  // Edge 可执行文件路径
  const edgeExecutable = '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge';

  // 使用 Puppeteer 启动 Edge，复用已有 profile
  browser = await puppeteer.launch({
    executablePath: edgeExecutable,
    userDataDir: EDGE_PROFILE_PATH,  // 复用 profile 保持登录状态
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

  // 打开 Gemini
  await page.goto(GEMINI_URL, { waitUntil: 'networkidle2' });

  return { browser, page };
}

export async function getPage(): Promise<puppeteer.Page> {
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
