---
name: gemini-browser-chat
description: Use when user wants to ask Gemini AI questions via Playwright browser, especially for math problems, complex reasoning, or tasks where local models are weak
---

# Gemini Browser Chat

## Overview

Use **Playwright MCP** to open Gemini webpage and get AI responses. This provides access to Google's Gemini model (including PRO version when logged in) for tasks where local models like minimax are weak.

## When to Use

**Trigger phrases:**
- "用 Gemini" / "用gemini" / "ask Gemini"
- "我的数学不太好" / "minimax 数学弱"
- "让 Gemini 来做" / "让 AI 来做"
- "这个题怎么做" (when user wants AI reasoning)
- User complains local model is weak at math/coding/reasoning

**Use for:**
- Complex math problems (integrals, proofs, etc.)
- Coding tasks requiring advanced reasoning
- Any question requiring stronger AI model
- Explanations with step-by-step reasoning

**NOT for:**
- Simple factual questions (use WebSearch)
- Direct API calls (no Gemini API key available)

## Quick Reference

| Step | Action | MCP Tool |
|------|--------|----------|
| 1 | **Open browser** to Gemini | `browser_navigate` |
| 2 | Find input textbox | Check snapshot for ref |
| 3 | Type question + submit | `browser_type` with `submit: true` |
| 4 | Wait for response | `browser_wait_for` or wait for "Gemini said" |
| 5 | Extract answer | Read from snapshot |

## Implementation

### Step 1: Open Gemini in Browser

**URL:** `https://gemini.google.com`

```javascript
mcp__plugin_playwright_playwright__browser_navigate
url: "https://gemini.google.com"
```

### Step 1.5: Check Login Status (Auto)

After navigation, check the snapshot for login status:

**Logged in (shows PRO):**
- Look for: `button "Google Account: ..."` or `button "PRO"`
- Then: Can use PRO mode

**Not logged in:**
- Look for: `link "Sign in"` in the page
- Then: Need to automate login

### Step 1.6: Auto Login (If Not Logged In)

If not logged in, click "Sign in" and follow the flow:

```javascript
// Click Sign in button
mcp__plugin_playwright_playwright__browser_click
element: "Sign in"
ref: "<sign-in-button-ref>"

// Wait for login page to load
mcp__plugin_playwright_playwright__browser_wait_for
text: "Email or phone"
time: 10

// Note: Playwright cannot see Google login credentials
// User needs to manually complete login ONCE
// After first manual login, browser will remember cookies
```

**Important:**
- Use **Edge browser** (Playwright MCP configured with Edge)
- Browser session persists between questions
- Login state is remembered (user is logged in with PRO)
- **First time:** User must manually complete login
- **Subsequent times:** Cookies are remembered, auto-login works

### Step 2: Find Input Box

After navigation, snapshot will contain a textbox with placeholder "Enter a prompt for Gemini". Note the ref (e.g., `e350`).

### Step 3: Type and Submit Question

```javascript
mcp__plugin_playwright_playwright__browser_type
element: "question input"
ref: "<textbox-ref>"  // e.g., e350
submit: true
text: "<user's question in English for better results>"
```

**Tip:** Translate user's question to English for better Gemini responses.

### Step 4: Wait for Response

```javascript
mcp__plugin_playwright_playwright__browser_wait_for
text: "Gemini said"  // or specific expected text
time: 15  // seconds
```

### Step 5: Extract Answer

Take a new snapshot and read from elements under "Gemini said" heading (level 2 or 3).

## Complete Example

**User says:** "帮我算一下这道数学题..."

**Actions:**
1. Navigate to `https://gemini.google.com`
2. Find textbox ref (e.g., `e350`)
3. Type: "Solve this problem: [user's math problem]" with `submit: true`
4. Wait ~10-15 seconds for response
5. Extract answer from elements under "Gemini said"

## Common Issues

| Issue | Solution |
|-------|----------|
| Page not loaded | Wait for textbox to be active (ref visible in snapshot) |
| Not logged in | Click "Sign in", ask user to complete manual login once |
| After first login | Cookies are remembered, auto-login works |
| Slow response | Use `browser_wait_for` to wait for "Gemini said" |
| Response truncated | Wait longer or scroll to load more |

## Login Status Detection

**Logged in (can use PRO):**
- Look for: `button "Google Account: ..."` or `button "PRO"`
- Status: ✅ Logged in

**Not logged in:**
- Look for: `link "Sign in"`
- Action: Click "Sign in", then ask user to complete login manually

**Note:** After first manual login, Google cookies are stored. Next time, browser will auto-detect login state.

## Workflow

1. User requests Gemini help → Recognize trigger phrase
2. Navigate to `https://gemini.google.com`
3. **Check login status** in snapshot:
   - If "Google Account" or "PRO" button exists → Logged in ✓
   - If "Sign in" link exists → Not logged in
4. If not logged in:
   - Click "Sign in" button
   - Ask user to complete manual login (first time only)
   - After login, cookies will be remembered
5. Check/select mode based on question difficulty
6. Type question and submit
7. Wait for response and extract answer
8. Return answer to user

## Key Points

- **Playwright MCP required:** This skill uses `mcp__plugin_playwright_playwright__` tools
- **Browser session persists:** Can continue conversation in same browser session
- **Login state remembered:** If user is logged in, Gemini PRO is available
- **Math/Reasoning:** Gemini excels at complex math and step-by-step reasoning

## Mode Settings (Auto-Select Based on Difficulty)

Gemini supports three modes. **For math problems, auto-select based on difficulty:**

| Mode | Description | Math Difficulty |
|------|-------------|-----------------|
| **Fast** | Quick answers | Simple calculations (arithmetic, basic algebra) |
| **Thinking** | Deep reasoning | Medium difficulty (proofs, derivations, medium integrals) |
| **Pro** | Gemini 3.1 Pro | Complex (advanced proofs, research-level math) |

### Auto-Select Logic for Math Problems

1. **Simple** (arithmetic, basic equations): Use **Fast** (default)
2. **Medium** (proofs, integrals, derivations): Switch to **Thinking**
3. **Complex** (research-level, multi-step theorems): Switch to **Pro**

### How to Change Mode

1. Click "Open mode picker" button (ref e290) next to input box
2. Select desired mode from dropdown menu
3. Selected mode applies to next question

**Mode Selection via Playwright:**
```javascript
// Click mode picker
mcp__plugin_playwright_playwright__browser_click
element: "mode picker"
ref: "e290"  // "Open mode picker" button

// Select mode
mcp__plugin_playwright_playwright__browser_click
element: "Thinking mode" or "Pro mode"
ref: "e445"  // or "e452" for Pro
```

**Note:** Pro mode requires Google AI subscription (user is logged in with PRO shown in sidebar).
