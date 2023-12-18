# external imports
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# custom imports
from tg import TextGeneration

app = FastAPI()
tg = TextGeneration("tardigrades") # TODO pass this in from an environment variable

class GenerateRequest(BaseModel):
    user_prompt: str
    system_prompt: str = None

@app.post("/generate/json")
def generate_json(request: GenerateRequest):
    response = tg.generate_json(request.user_prompt, request.system_prompt)
    return response

@app.post("/generate/text")
def generate_text(request: GenerateRequest):
    response = tg.generate_text(request.user_prompt, request.system_prompt)
    return {"text": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
