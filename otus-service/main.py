import json
import os

from fastapi import FastAPI

app = FastAPI()

config = {
    'DATABASE_URI': os.environ.get('DATABASE_URI', ''),
    'HOSTNAME': os.environ.get('HOSTNAME', ''),
    'GREETING': os.environ.get('GREETING', 'Hello'),
}


@app.get("/health/")
async def health():
    return {"status": "OK"}


@app.get("/config/")
async def configuration():
    return json.dumps(config)
