from langchain.llms import HuggingFaceHub
from langchain.chains import RetrievalQA
from langchain_community.retrievers import TavilySearchAPIRetriever
import os

def create_search_engine():
    # Set the HuggingFaceHub API token explicitly, or it will be retrieved from the environment variable
    huggingface_api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")  # Get from environment variable
    
    if not huggingface_api_token:
        raise ValueError("Hugging Face API token is missing. Please set the HUGGINGFACEHUB_API_TOKEN environment variable.")
    
    # Initialize the retriever with Tavily API key
    retriever = TavilySearchAPIRetriever(api_key="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")

    # Initialize Mistral LLM via HuggingFaceHub and pass the token explicitly
    llm = HuggingFaceHub(
        repo_id="mistralai/Mistral-7B", 
        model_kwargs={"temperature": 0.7}, 
        huggingfacehub_api_token=huggingface_api_token  # Explicitly pass the token
    )

    # Create a RetrievalQA chain with the LLM and the retriever
    search_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return search_chain
