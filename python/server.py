from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get('/test')
def test():
    return PlainTextResponse('test')
