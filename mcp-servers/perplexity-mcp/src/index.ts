import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from '@modelcontextprotocol/sdk/types.js';

import { perplexityAsk } from './tools/perplexity-ask.js';
import { checkLoginStatus } from './tools/perplexity-check-login.js';
import { closePerplexityBrowser } from './tools/perplexity-close.js';
import { initializeBrowser } from './browser/manager.js';

// 定义工具列表
const PERPLEXITY_TOOLS = [
  {
    name: 'perplexity_ask',
    description: 'Ask Perplexity AI a question via browser. Returns the AI response with citations.',
    inputSchema: {
      type: 'object',
      properties: {
        question: {
          type: 'string',
          description: 'The question to ask Perplexity',
        },
        mode: {
          type: 'string',
          enum: ['focused', 'pro'],
          default: 'focused',
          description: 'Response mode: focused (quick) or pro (detailed)',
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
    name: 'perplexity_check_login',
    description: 'Check if Perplexity browser is logged in',
    inputSchema: {
      type: 'object',
      properties: {},
    },
  },
  {
    name: 'perplexity_close',
    description: 'Close the Perplexity browser and clean up resources',
    inputSchema: {
      type: 'object',
      properties: {},
    },
  },
];

// 创建 MCP Server
const server = new Server(
  {
    name: 'perplexity-mcp',
    version: '1.0.0',
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// 注册工具列表处理器
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return { tools: PERPLEXITY_TOOLS };
});

// 注册工具调用处理器
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  try {
    switch (name) {
      case 'perplexity_ask': {
        const { question, mode = 'focused', timeout = 60000 } = args as {
          question: string;
          mode?: 'focused' | 'pro';
          timeout?: number;
        };
        const result = await perplexityAsk(question, { mode, timeout });
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(result),
            },
          ],
        };
      }

      case 'perplexity_check_login': {
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

      case 'perplexity_close': {
        const result = await closePerplexityBrowser();
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
  } catch (error) {
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
    console.error('Perplexity browser initialized with Puppeteer');
  } catch (error) {
    console.error('Failed to initialize browser:', error);
  }

  // 连接 stdio transport
  const transport = new StdioServerTransport();
  await server.connect(transport);

  console.error('Perplexity MCP Server running on stdio');
}

main().catch(console.error);
