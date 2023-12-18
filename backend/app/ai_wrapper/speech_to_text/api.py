from fastapi import FastAPI, File, HTTPException
from pydantic import BaseModel
from stt import SpeechToText

app = FastAPI()
stt = SpeechToText()

class AudioRecordRequest(BaseModel):
    duration: int = 5

class TranscriptionResponse(BaseModel):
    transcript: str

@app.post("/record/transcribe")
def record_and_transcribe_audio(request: AudioRecordRequest):
    try:
        audio_path = stt.record_audio(request.duration,)
        transcript = stt.transcribe_audio(audio_path)
        return {"transcript": transcript}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
