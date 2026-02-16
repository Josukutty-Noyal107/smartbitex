
import React, { useState, useCallback } from 'react';
import { FoodResult, AppState } from './types';
import { fetchFoodInfo } from './geminiService';
import SearchBox from './components/SearchBox';
import ResultCard from './components/ResultCard';

const App = () => {
  const [state, setState] = useState({
    results: [],
    isLoading: false,
    error: null,
  });

  const handleSearch = useCallback(async (query) => {
    setState(prev => ({ ...prev, isLoading: true, error: null }));
    
    try {
      const content = await fetchFoodInfo(query);
      
      const newResult = {
        id: crypto.randomUUID(),
        query,
        content,
        timestamp: Date.now(),
      };

      setState(prev => ({
        ...prev,
        results: [newResult, ...prev.results],
        isLoading: false,
      }));
    } catch (err) {
      setState(prev => ({
        ...prev,
        isLoading: false,
        error: err instanceof Error ? err.message : 'An unexpected error occurred.',
      }));
    }
  }, []);

  return (
    <div className="min-h-screen bg-stone-50 pb-20">
      <header className="pt-20 pb-16 px-6">
        <div className="max-w-4xl mx-auto text-center">
          <div className="inline-block bg-amber-100 text-amber-800 px-4 py-1.5 rounded-full text-xs font-bold uppercase tracking-wider mb-6">
            Bilingual AI Assistant
          </div>
          <h1 className="text-6xl md:text-7xl font-bold text-stone-900 mb-6 tracking-tight">
            Smart<span className="text-amber-600">Bite</span>
          </h1>
          <p className="text-xl md:text-2xl text-stone-500 font-light max-w-2xl mx-auto">
            Actionable food insights in English and Malayalam.
          </p>
        </div>
      </header>

      <main className="max-w-4xl mx-auto px-6">
        <div className="sticky top-8 z-50 mb-16">
          <SearchBox onSearch={handleSearch} isLoading={state.isLoading} />
        </div>

        {state.error && (
          <div className="bg-red-50 border border-red-100 text-red-800 px-6 py-4 rounded-3xl mb-12 flex items-center shadow-sm">
            <svg className="w-6 h-6 mr-3 text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <p className="font-medium">{state.error}</p>
          </div>
        )}

        <div className="space-y-12">
          {state.results.length === 0 && !state.isLoading && (
            <div className="text-center py-24 bg-white rounded-[3rem] border border-stone-100 shadow-sm border-dashed">
              <div className="text-stone-200 mb-6">
                <svg className="w-20 h-20 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="1" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                </svg>
              </div>
              <h3 className="text-2xl font-bold text-stone-400">Discover something tasty</h3>
              <p className="text-stone-400 mt-2">Enter any food name to get detailed bilingual guides.</p>
            </div>
          )}

          {state.results.map(result => (
            <ResultCard key={result.id} result={result} />
          ))}
        </div>
      </main>

      <footer className="mt-24 py-12 border-t border-stone-100 text-center text-stone-400">
        <p className="text-sm font-medium tracking-wide">SMARTBITE &copy; {new Date().getFullYear()}</p>
        <p className="text-xs mt-1">Intelligence by Gemini 3</p>
      </footer>
    </div>
  );
};

export default App;