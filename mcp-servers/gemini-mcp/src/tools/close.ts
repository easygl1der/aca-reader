import { closeBrowser } from '../browser/manager.js';

export async function closeGeminiBrowser(): Promise<{ success: boolean; message: string }> {
  try {
    await closeBrowser();
    return { success: true, message: 'Browser closed successfully' };
  } catch (error) {
    return {
      success: false,
      message: error instanceof Error ? error.message : String(error),
    };
  }
}
