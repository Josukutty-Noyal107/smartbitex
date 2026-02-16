
import React from 'react';
import MarkdownRenderer from './MarkdownRenderer';

const ResultCard = ({ result }) => {
  return (
    <div className="bg-white rounded-[2rem] p-8 border border-stone-100 shadow-sm mb-8 animate-in fade-in slide-in-from-bottom-6 duration-700">
      <div className="flex justify-between items-start mb-6 border-b border-stone-50 pb-6">
        <div>
          <h2 className="text-4xl text-stone-900 capitalize font-bold mb-2">{result.query}</h2>
          <span className="text-stone-400 text-sm font-medium uppercase tracking-widest">
            {new Date(result.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
          </span>
        </div>
        <div className="bg-amber-100 text-amber-900 px-5 py-2 rounded-full text-sm font-bold flex items-center shadow-sm">
          <svg className="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20">
            <path d="M11 3a1 1 0 10-2 0v1a1 1 0 102 0V3zM15.657 5.757a1 1 0 00-1.414-1.414l-.707.707a1 1 0 001.414 1.414l.707-.707zM18 10a1 1 0 01-1 1h-1a1 1 0 110-2h1a1 1 0 011 1zM5.05 6.464A1 1 0 106.464 5.05l-.707-.707a1 1 0 00-1.414 1.414l.707.707zM5 10a1 1 0 01-1 1H3a1 1 0 110-2h1a1 1 0 011 1zM8 16v-1a1 1 0 112 0v1a1 1 0 11-2 0zM13.536 14.95a1 1 0 010-1.414l.707-.707a1 1 0 011.414 1.414l-.707.707a1 1 0 01-1.414 0zM6.464 14.95a1 1 0 01-1.414 0l-.707-.707a1 1 0 011.414-1.414l.707.707a1 1 0 010 1.414z" />
          </svg>
          Smart Analysis
        </div>
      </div>
      <MarkdownRenderer content={result.content} />
    </div>
  );
};

export default ResultCard;