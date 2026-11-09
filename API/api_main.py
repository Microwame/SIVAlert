import fastapi

app = fastapi.FastAPI()

@app.get("/")
async def test():
    return {"message": "Hello World"}