
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#origins = [
 #   "http://localhost",
  #  "http://localhost:8000",
 #   "file://"
  #  "file:///Users/m./PycharmProjects/fastAPI/",
#]
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__=="__main__":
    uvicorn.run("hello_word:app", host="127.0.0.1", port=8000, log_level="info")



