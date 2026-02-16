
import React, { useState } from 'react';

const SearchBox = ({ onSearch, isLoading }) => {
  const [query, setQuery] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (query.trim() && !isLoading) {
      onSearch(query.trim());
      setQuery('');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="w-full max-w-2xl mx-auto">
      <div className="relative group">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Enter a food item (e.g., Masala Dosa)"
          className="w-full px-6 py-5 text-lg bg-white border border-stone-200 rounded-3xl shadow-sm focus:outline-none focus:ring-2 focus:ring-amber-500 focus:border-transparent transition-all placeholder:text-stone-400 group-hover:shadow-md"
          disabled={isLoading}
        />
        <button
          type="submit"
          disabled={isLoading || !query.trim()}
          className={`absolute right-3 top-3 bottom-3 px-6 rounded-2xl font-semibold transition-all flex items-center justify-center
            ${isLoading || !query.trim() 
              ? 'bg-stone-100 text-stone-400 cursor-not-allowed' 
              : 'bg-stone-900 text-white hover:bg-stone-800 active:scale-95'}`}
        >
          {isLoading ? (
            <div className="flex items-center space-x-2">
              <svg className="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
            </div>
          ) : (
            'Ask SmartBite'
          )}
        </button>
      </div>
    </form>
  );
};

export default SearchBox;