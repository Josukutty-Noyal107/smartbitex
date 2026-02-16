
import React from 'react';

const MarkdownRenderer = ({ content }) => {
  const parseMarkdown = (text) => {
    let html = text
      .replace(/^### (.*$)/gim, '<h3 class="text-xl font-bold mt-6 mb-2">$1</h3>')
      .replace(/^## (.*$)/gim, '<h2 class="text-2xl font-bold mt-8 mb-3">$1</h2>')
      .replace(/^# (.*$)/gim, '<h1 class="text-3xl font-bold mt-10 mb-4">$1</h1>')
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/^\s*[-*+]\s+(.*)$/gim, '<li class="ml-4 list-disc">$1</li>')
      .replace(/(<li.*<\/li>)/gms, '<ul class="my-4">$1</ul>')
      .replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer" class="text-amber-600 hover:underline font-medium">$1</a>')
      .replace(/\n/g, '<br />');

    return { __html: html };
  };

  return (
    <div 
      className="markdown-content prose prose-stone max-w-none text-stone-700"
      dangerouslySetInnerHTML={parseMarkdown(content)}
    />
  );
};

export default MarkdownRenderer;