import os
from fastapi import FastAPI, Request, Header, HTTPException
from dotenv import load_dotenv

from .line_handler import handle_line_event

load_dotenv()
app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request, x_line_signature: str = Header(None)):
    body = await request.body()
    try:
        await handle_line_event(body.decode("utf-8"), x_line_signature)
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=400, detail=str(e))
    return "OK"
