import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sentientresearchagent import SentientAgent

app = FastAPI()

@app.post("/")
async def run(request: Request):
 data = await request.json()
 prompt = (data.get("prompt") or "").strip()
 api_key = os.getenv("OPENAI_API_KEY") or os.getenv("sentient")
 if not prompt:
  return JSONResponse({"error": "Missing 'prompt'."}, status_code=400)
 if not api_key:
  return JSONResponse({"error": "OPENAI_API_KEY not set."}, status_code=500)
 if os.getenv("OPENAI_BASE_URL") is None and api_key.startswith("sk-or-"):
  return JSONResponse({"error": "Set OPENAI_BASE_URL=https://openrouter.ai/api/v1"}, status_code=500)
 agent = SentientAgent.create()
 result = await agent.run(prompt)
 return {"result": result}
