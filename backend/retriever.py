from langchain_community.retrievers import TavilySearchAPIRetriever
from langchain.agents import tool

# Setup Tavily API retriever with LangChain's retriever class
class WebSearchRetriever:
    def __init__(self, api_key):
        self.retriever = TavilySearchAPIRetriever(api_key=api_key)

    def retrieve(self, query):
        """
        Fetch the top relevant documents from Tavily (or another search service).
        """
        results = self.retriever.retrieve(query=query)
        return [result['text'] for result in results]  # Assuming 'results' is a list of document dicts

# LangChain wrapper to use the retriever in a chain
@tool
def web_search(query: str) -> str:
    """
    This tool will be used within the LangChain process to fetch relevant documents.
    """
    retriever = WebSearchRetriever(api_key="")
    documents = retriever.retrieve(query)
    return "\n".join(documents)
