import { useState } from "react";
import '../index.css'
const SearchInput = ({ onSearch }) => {
    const [query, setQuery] = useState("");

    const handleSearch = () => {
        if (query.trim()) onSearch(query);
    };

    return (
        <div>
            <textarea
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Enter your query..."
                className="search-textarea"  // Add a class for styling
            />
            <button onClick={handleSearch}>Search</button>
        </div>
    );
};

export default SearchInput;
