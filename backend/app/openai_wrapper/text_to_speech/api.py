from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tts import TextToSpeech

app = FastAPI()
tts = TextToSpeech()

class SpeechGenerationRequest(BaseModel):
    text: str
    output_file_name: str

@app.post("/generate_speech")
def generate_speech(request: SpeechGenerationRequest):
    try:
        tts.generate_speech(input_text=request.text, output_file_name=request.output_file_name)
        return {"message": f"Speech generated successfully at {tts.get_output_file_path()}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Speech generation failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)