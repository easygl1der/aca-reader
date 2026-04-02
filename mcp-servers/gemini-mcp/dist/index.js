import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { CallToolRequestSchema, ListToolsRequestSchema, } from '@modelcontextprotocol/sdk/types.js';
import { geminiAsk } from './tools/gemini-ask.js';
import { checkLoginStatus } from './tools/check-login.js';
import { closeGeminiBrowser } from './tools/close.js';
import { initializeBrowser } from './browser/manager.js';
// 定义工具列表
const GEMINI_TOOLS = [
    {
        name: 'gemini_ask',
        description: 'Ask Gemini AI a question via browser. Returns the AI response.',
        inputSchema: {
            type: 'object',
            properties: {
                question: {
                    type: 'string',
                    description: 'The question to ask Gemini',
                },
                mode: {
                    type: 'string',
                    enum: ['fast', 'thinking', 'pro'],
                    default: 'fast',
                    description: 'Response mode: fast (quick), thinking (deep reasoning), pro (most capable)',
                },
                timeout: {
                    type: 'number',
                    default: 60000,
                    description: 'Timeout in milliseconds',
                },
            },
            required: ['question'],
        },
    },
    {
        name: 'gemini_check_login',
        description: 'Check if Gemini browser is logged in and has PRO status',
        inputSchema: {
            type: 'object',
            properties: {},
        },
    },
    {
        name: 'gemini_close',
        description: 'Close the Gemini browser and clean up resources',
        inputSchema: {
            type: 'object',
            properties: {},
        },
    },
];
// 创建 MCP Server
const server = new Server({
    name: 'gemini-mcp',
    version: '1.0.0',
}, {
    capabilities: {
        tools: {},
    },
});
// 注册工具列表处理器
server.setRequestHandler(ListToolsRequestSchema, async () => {
    return { tools: GEMINI_TOOLS };
});
// 注册工具调用处理器
server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { name, arguments: args } = request.params;
    try {
        switch (name) {
            case 'gemini_ask': {
                const { question, mode = 'fast', timeout = 60000 } = args;
                const result = await geminiAsk(question, { mode, timeout });
                return {
                    content: [
                        {
                            type: 'text',
                            text: JSON.stringify(result),
                        },
                    ],
                };
            }
            case 'gemini_check_login': {
                const status = await checkLoginStatus();
                return {
                    content: [
                        {
                            type: 'text',
                            text: JSON.stringify(status),
                        },
                    ],
                };
            }
            case 'gemini_close': {
                const result = await closeGeminiBrowser();
                return {
                    content: [
                        {
                            type: 'text',
                            text: JSON.stringify(result),
                        },
                    ],
                };
            }
            default:
                return {
                    content: [
                        {
                            type: 'text',
                            text: `Unknown tool: ${name}`,
                        },
                    ],
                    isError: true,
                };
        }
    }
    catch (error) {
        return {
            content: [
                {
                    type: 'text',
                    text: JSON.stringify({
                        success: false,
                        error: error instanceof Error ? error.message : String(error),
                    }),
                },
            ],
            isError: true,
        };
    }
});
// 启动服务器
async function main() {
    // 初始化浏览器
    try {
        await initializeBrowser();
        console.error('Gemini browser initialized with Puppeteer');
    }
    catch (error) {
        console.error('Failed to initialize browser:', error);
    }
    // 连接 stdio transport
    const transport = new StdioServerTransport();
    await server.connect(transport);
    console.error('Gemini MCP Server running on stdio');
}
main().catch(console.error);
