from fastapi import FastAPI

app = FastAPI()

# デコレータ
@app.get("/hello")
async def hello():
  return {"message": "hello world!"}
