import { useState } from "react";
import './App.css'
import SearchInput from "./components/SearchInput";
import SearchResults from "./components/SearchResults";
import axios from "axios";

const App = () => {
    const [results, setResults] = useState([]);

    const handleSearch = async (query) => {
        try {
            const response = await axios.post("http://localhost:5000/search", { query });
            setResults(response.data.results);
        } catch (error) {
            console.error("Error fetching search results:", error);
        }
    };

    return (
        <div>
            <h1>Web Search App</h1>
            <SearchInput onSearch={handleSearch} />
            <SearchResults results={results} />
        </div>
    );
};

export default App;
