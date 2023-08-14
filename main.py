from fastapi import FastAPI

app = FastAPI()

@app.get("/product")
async def product():
	return "List of products"


