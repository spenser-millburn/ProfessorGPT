import constants
from request_wrapper import RequestsWrapper
tg_r = RequestsWrapper(base_url= constants.TEXT_GENERATION_API_URL)
stt_r = RequestsWrapper(base_url= constants.SPEECH_TO_TEXT_API_URL)
tts_r = RequestsWrapper(base_url= constants.TEXT_TO_SPEECH_API_URL)

# wrapper.post(base_url= "localhost:8001", payload = {"user_prompt": "make a table", "system_prompt": "" })
# print(stt_api.post(endpoint="record/transcribe", payload = {"duration": 5}))

print(tg_r.post(endpoint="generate/json", payload = {"user_prompt": "what are tardigrades in 5 words"}))
print(tts_r.post(endpoint="generate_speech", payload = {"text": "an apple fell from the tree ans hit isaac newton", "output_file_name": "apples"}))