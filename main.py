from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def hello_world():
    return "hello world from devops.."

