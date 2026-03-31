'use client';

import { useState, useRef, useEffect } from 'react';
import { Send, Sparkles, User, Bot, RefreshCw } from 'lucide-react';
import { useChatStore, Message } from '@/store/use-chat-store';

interface ChatAreaProps {
  pdfFileName: string | null;
}

const MOCK_AI_RESPONSES = [
  "Based on the PDF content, this paper discusses important concepts in machine learning. The authors present novel approaches to handling complex datasets efficiently.",
  "I found several key insights in this paper. The methodology section provides a thorough explanation of the proposed algorithm and its theoretical foundations.",
  "This research builds upon previous work in the field and introduces innovative techniques that could have significant practical applications.",
  "Looking at the results, the paper demonstrates strong empirical performance across multiple benchmarks. The ablation studies help understand the contribution of each component.",
  "The paper's main contribution lies in the proposed architecture, which achieves state-of-the-art results while maintaining computational efficiency.",
];

const BRAINSTORM_QUESTIONS = [
  "What are the main contributions of this paper?",
  "How does the proposed method compare to existing approaches?",
  "What are the limitations of the approach presented?",
  "What future research directions are suggested?",
  "How might this research apply to my work?",
];

export default function ChatArea({ pdfFileName }: ChatAreaProps) {
  const [inputValue, setInputValue] = useState('');
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLTextAreaElement>(null);

  const {
    messages,
    isLoading,
    addMessage,
    setIsLoading,
    scope,
  } = useChatStore();

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSend = async () => {
    if (!inputValue.trim() || isLoading) return;

    const userMessage = inputValue.trim();
    setInputValue('');
    addMessage('user', userMessage);
    setIsLoading(true);

    // Simulate AI response
    setTimeout(() => {
      const randomResponse =
        MOCK_AI_RESPONSES[
          Math.floor(Math.random() * MOCK_AI_RESPONSES.length)
        ];
      addMessage('ai', randomResponse);
      setIsLoading(false);
    }, 1500);
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const handleBrainstorm = () => {
    if (isLoading) return;

    addMessage(
      'user',
      'Can you suggest some questions I should ask about this paper?'
    );
    setIsLoading(true);

    setTimeout(() => {
      const questionsText = BRAINSTORM_QUESTIONS.map((q) => `- ${q}`).join(
        '\n'
      );
      addMessage(
        'ai',
        `Here are some questions you might want to explore:\n\n${questionsText}\n\nFeel free to click on any of these to start our discussion!`
      );
      setIsLoading(false);
    }, 1500);
  };

  const handleNewChat = () => {
    if (isLoading) return;
    useChatStore.getState().clearMessages();
  };

  return (
    <div className="flex flex-col h-full bg-zinc-900 rounded-xl border border-zinc-700 overflow-hidden">
      {/* Header */}
      <div className="flex items-center justify-between px-4 py-3 bg-zinc-800 border-b border-zinc-700">
        <div className="flex items-center gap-2">
          <Bot className="w-5 h-5 text-violet-400" />
          <span className="font-medium text-white">
            {pdfFileName ? 'Chat about this paper' : 'AI Assistant'}
          </span>
        </div>
        <button
          onClick={handleNewChat}
          disabled={isLoading || messages.length === 0}
          className={`
            flex items-center gap-1 px-2 py-1 rounded-lg text-xs
            transition-colors duration-200
            ${
              messages.length === 0 || isLoading
                ? 'text-zinc-600 cursor-not-allowed'
                : 'text-zinc-400 hover:text-white hover:bg-zinc-700'
            }
          `}
        >
          <RefreshCw className="w-3 h-3" />
          New Chat
        </button>
      </div>

      {/* Messages Area */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.length === 0 && (
          <div className="flex flex-col items-center justify-center h-full text-center">
            <div className="w-16 h-16 rounded-full bg-zinc-800 flex items-center justify-center mb-4">
              <Sparkles className="w-8 h-8 text-violet-400" />
            </div>
            <h3 className="text-lg font-medium text-white mb-2">
              Start exploring this paper
            </h3>
            <p className="text-zinc-400 text-sm max-w-xs">
              Upload a PDF and ask questions to get insights, or let me
              brainstorm questions for you.
            </p>
            {!pdfFileName && (
              <p className="text-zinc-500 text-xs mt-4">
                (Upload a PDF to enable paper-specific discussions)
              </p>
            )}
          </div>
        )}

        {messages.map((message: Message) => (
          <div
            key={message.id}
            className={`
              flex gap-3
              ${message.role === 'user' ? 'flex-row-reverse' : 'flex-row'}
            `}
          >
            {/* Avatar */}
            <div
              className={`
                flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center
                ${
                  message.role === 'user'
                    ? 'bg-violet-600'
                    : 'bg-zinc-700'
                }
              `}
            >
              {message.role === 'user' ? (
                <User className="w-4 h-4 text-white" />
              ) : (
                <Bot className="w-4 h-4 text-violet-400" />
              )}
            </div>

            {/* Message Bubble */}
            <div
              className={`
                flex-1 max-w-[80%] px-4 py-3 rounded-2xl
                ${
                  message.role === 'user'
                    ? 'bg-violet-600 text-white rounded-tr-sm'
                    : 'bg-zinc-800 text-zinc-100 rounded-tl-sm'
                }
              `}
            >
              <p className="text-sm leading-relaxed whitespace-pre-wrap">
                {message.content}
              </p>
              <p
                className={`
                  text-xs mt-1
                  ${
                    message.role === 'user'
                      ? 'text-violet-200'
                      : 'text-zinc-500'
                  }
                `}
              >
                {message.timestamp.toLocaleTimeString([], {
                  hour: '2-digit',
                  minute: '2-digit',
                })}
              </p>
            </div>
          </div>
        ))}

        {isLoading && (
          <div className="flex gap-3">
            <div className="flex-shrink-0 w-8 h-8 rounded-full bg-zinc-700 flex items-center justify-center">
              <Bot className="w-4 h-4 text-violet-400" />
            </div>
            <div className="flex-1 max-w-[80%] px-4 py-3 rounded-2xl rounded-tl-sm bg-zinc-800">
              <div className="flex items-center gap-2">
                <div className="w-2 h-2 rounded-full bg-violet-400 animate-bounce" />
                <div
                  className="w-2 h-2 rounded-full bg-violet-400 animate-bounce"
                  style={{ animationDelay: '0.1s' }}
                />
                <div
                  className="w-2 h-2 rounded-full bg-violet-400 animate-bounce"
                  style={{ animationDelay: '0.2s' }}
                />
              </div>
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      {/* Brainstorm Button */}
      {messages.length === 0 && !isLoading && pdfFileName && (
        <div className="px-4 pb-2">
          <button
            onClick={handleBrainstorm}
            className="w-full flex items-center justify-center gap-2 px-4 py-2.5
              bg-zinc-800 hover:bg-zinc-700 text-zinc-300 rounded-xl
              transition-colors duration-200 border border-zinc-700"
          >
            <Sparkles className="w-4 h-4 text-violet-400" />
            <span className="text-sm font-medium">Brainstorm Questions</span>
          </button>
        </div>
      )}

      {/* Input Area */}
      <div className="p-4 bg-zinc-800 border-t border-zinc-700">
        <div className="flex items-end gap-3">
          <div className="flex-1 relative">
            <textarea
              ref={inputRef}
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder={
                pdfFileName
                  ? `Ask about "${pdfFileName}"...`
                  : 'Ask a question...'
              }
              className="w-full px-4 py-3 bg-zinc-900 border border-zinc-600 rounded-xl
                text-white placeholder-zinc-500 text-sm resize-none
                focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent
                transition-all duration-200"
              rows={1}
              style={{
                minHeight: '48px',
                maxHeight: '120px',
              }}
            />
          </div>
          <button
            onClick={handleSend}
            disabled={!inputValue.trim() || isLoading}
            className={`
              flex-shrink-0 p-3 rounded-xl transition-all duration-200
              ${
                inputValue.trim() && !isLoading
                  ? 'bg-violet-600 hover:bg-violet-500 text-white'
                  : 'bg-zinc-700 text-zinc-500 cursor-not-allowed'
              }
            `}
          >
            <Send className="w-5 h-5" />
          </button>
        </div>

        {/* Scope indicator */}
        <div className="flex items-center justify-between mt-2 px-1">
          <span className="text-xs text-zinc-500">
            Searching:{' '}
            <span className="text-zinc-400">
              {scope === 'this-paper' ? 'Only This Paper' : 'All Papers'}
            </span>
          </span>
          <span className="text-xs text-zinc-500">
            Press Enter to send, Shift+Enter for new line
          </span>
        </div>
      </div>
    </div>
  );
}
