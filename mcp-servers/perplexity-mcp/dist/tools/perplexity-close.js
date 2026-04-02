import { closeBrowser } from '../browser/manager.js';
export async function closePerplexityBrowser() {
    try {
        await closeBrowser();
        return { success: true };
    }
    catch (error) {
        return {
            success: false,
            error: error instanceof Error ? error.message : String(error),
        };
    }
}
