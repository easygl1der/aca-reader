export interface AskOptions {
    mode?: 'focused' | 'pro';
    timeout?: number;
}
export interface AskResult {
    success: boolean;
    response?: string;
    error?: string;
    mode?: string;
}
export declare function perplexityAsk(question: string, options?: AskOptions): Promise<AskResult>;
