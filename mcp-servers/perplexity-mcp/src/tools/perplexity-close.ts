import { closeBrowser } from '../browser/manager.js';

export interface CloseResult {
  success: boolean;
  error?: string;
}

export async function closePerplexityBrowser(): Promise<CloseResult> {
  try {
    await closeBrowser();
    return { success: true };
  } catch (error) {
    return {
      success: false,
      error: error instanceof Error ? error.message : String(error),
    };
  }
}
