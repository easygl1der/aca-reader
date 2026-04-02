export declare const SELECTORS: {
    readonly inputBox: "[placeholder=\"Ask anything…\"]";
    readonly inputBoxAlt: "textarea[placeholder*=\"Ask\"]";
    readonly submitButton: "[class*=\"submit\"]";
    readonly submitButtonAlt: "[class*=\"send\"]";
    readonly responseContent: "[class*=\"response\"]";
    readonly responseContentAlt: "article";
    readonly responseContentAlt2: "[class*=\"answer\"]";
    readonly loggedInAvatar: "[class*=\"avatar\"]";
    readonly loggedInUserButton: "[class*=\"user-menu\"]";
    readonly loggedOutSignIn: "text=Sign in";
    readonly loadingSpinner: "[class*=\"loading\"]";
    readonly loadingSpinnerAlt: "[class*=\"spinner\"]";
};
export type SelectorKey = keyof typeof SELECTORS;
