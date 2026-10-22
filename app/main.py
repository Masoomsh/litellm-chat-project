from fastapi import FastAPI
app=FastAPI(title="GenAI Chat API")

@app.get("/")
def home():
    return {"message": "GenAI Chat API is running!"}

@app.get("/health")
def health():
    return {"status": "healthy"}