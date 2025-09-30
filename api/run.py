import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sentientresearchagent import SentientAgent

app = FastAPI()

@app.post("/")
async def run(request: Request):
 data = await request.json()
 prompt = (data.get("prompt") or "").strip()
 if not prompt:
  return JSONResponse({"error": "Missing 'prompt'."}, status_code=400)
 if not os.getenv("OPENAI_API_KEY"):
  return JSONResponse({"error": "OPENAI_API_KEY not set."}, status_code=500)
 agent = SentientAgent.create()
 result = await agent.run(prompt)
 return {"result": result}
