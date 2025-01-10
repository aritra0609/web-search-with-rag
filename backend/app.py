from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from search_engine import create_search_engine

# Initialize FastAPI app
app = FastAPI()

# Define Pydantic model for request body
class QueryRequest(BaseModel):
    query: str

# Initialize search engine
search_engine = create_search_engine()

@app.post("/search")
async def search(request: QueryRequest):
    query = request.query

    if not query:
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    # Run the search engine and get the response
    response = search_engine.run(query)

    # Adjust based on the response format (likely a dictionary with 'result' and 'source_documents')
    result = response.get('result', '')
    if result == '':
        raise HTTPException(status_code=500, detail="No result generated")

    # Return the result and optionally, the source documents
    return {
        "results": result,
        "source_documents": response.get('source_documents', [])
    }

# To run the FastAPI app, use the command: uvicorn <filename>:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
