export interface CloseResult {
    success: boolean;
    error?: string;
}
export declare function closePerplexityBrowser(): Promise<CloseResult>;
