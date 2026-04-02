export interface LoginStatus {
    isLoggedIn: boolean;
    displayName?: string;
    error?: string;
}
export declare function checkLoginStatus(): Promise<LoginStatus>;
