# ProfessorGPT
An AI-driven Employee Training Assistant leveraging OpenAI's APIs for interactive tutoring, comprehension assessment and continuous improvement/quality control. 


# Interactive Employee Training Assistant

## Project Overview

### Objective
Develop an AI assistant leveraging OpenAI's APIs, integrating text-to-speech (TTS), speech-to-text (STT), and other tools to streamline employee training, tutor users interactively, and assess their understanding.

### Workflow

1. **Document Intake & Processing**
    - **Document Upload:** Allow users to upload various document types.
    - **Content Analysis:** Utilize OpenAI's document analysis API for comprehension and goal identification.

2. **Goal Formation**
    - **Objective Derivation:** Use the content analysis to generate a structured list of learning objectives or goals.

3. **Interactive Tutoring Session**
    - **Text-to-Speech Conversion:** Convert textual content to speech for audio-based interaction.
    - **Speech-to-Text Input:** Enable users to respond orally, transcribing their speech to text for the assistant's comprehension.
    - **Tutoring Session:** Initiate an interactive session where the assistant verbally tutors users about the document content and learning goals.
    - **Engagement:** Engage users through conversational styles, explanations, Q&A, or summaries using speech.

4. **Understanding Assessment**
    - **Speech-to-Text for Responses:** Convert user audio responses to text.
    - **Evaluation:** Analyze and assess user comprehension through their oral responses or follow-up questions.

### APIs Utilized
- 
- **Text-to-Speech:** Employ TTS APIs to convert textual content into speech for interactive tutoring.
- **Speech-to-Text:** STT APIs for transcribing user's oral responses into text for assessment.

## User Stories

| User Story ID | User Story Description                                                                                   | Features                                             |
|---------------|----------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| 1             | As a user, I want to upload diverse documents for training material, allowing the AI assistant to comprehend and structure content.| Document upload & processing                           |
| 2             | As a user, I want the assistant to analyze and identify learning objectives or goals based on the uploaded document's content.| Learning objectives identification                     |
| 3             | As a user, I want to engage in interactive tutoring sessions where the assistant verbally explains content and learning goals.| Interactive tutoring sessions                         |
| 4             | As a user, I want the assistant to ask questions or prompt discussions about the content to enhance my understanding.| Content engagement prompts                            |
| 5             | As a user, I want the assistant to summarize or clarify complex sections of the document using speech for better comprehension.| Speech-based document summarization                   |
| 6             | As a user, I want to respond orally during the tutoring session, expecting the assistant to transcribe my responses for evaluation.| Oral response transcription                           |
| 7             | As a user, I want the assistant to evaluate my responses against the learning goals derived from the document.| Response evaluation against learning goals             |
| 8             | As a user, I want feedback from the assistant to understand my level of understanding and areas that need improvement.| Understanding feedback                                |
| 9             | As a user, I want the assistant to convert textual content to speech for an engaging audio-based interaction during the tutoring session.| Text-to-speech conversion                             |
| 10            | As a user, I expect a user-friendly interface allowing seamless interaction via both speech and text inputs during the session.| Speech and text interface                             |
| 11            | As an administrator, I want to manage the documents uploaded for training materials and their associated learning goals.| Document and goal management                          |
| 12            | As a user, I want the assistant's functionalities accessible across various devices or interfaces for flexible usage.| Multi-device accessibility                             |
| 13            | As a user, I want the assistant to handle errors gracefully, providing clear prompts or explanations in case of misunderstandings.| Error handling and guidance                           |
| 14            | As a user, I expect support documentation or assistance if I encounter issues during the interaction with the assistant.| Support and assistance                                 |


## Project Structure
```
project_root/
│
├── backend/
│   ├── app/
│   │   ├── document_processing/
│   │   │   ├── upload_handler.py       # Backend logic for handling document uploads
│   │   │   └── analysis_service.py    # Service to interact with OpenAI's document analysis API
│   │   │
│   │   ├── goal_formation/
│   │   │   └── goal_derivation.py     # Algorithm/service for deriving learning objectives from analysis results
│   │   │
│   │   ├── tutoring_session/
│   │   │   ├── tts_service.py         # Service to interact with TTS API
│   │   │   ├── stt_service.py         # Service to interact with STT API
│   │   │   └── tutoring_logic.py      # Backend logic for managing tutoring sessions
│   │   │
│   │   ├── understanding_assessment/
│   │   │   └── evaluation_service.py  # Algorithm/service for evaluating user responses against learning objectives
│   │   │
│   │   ├── main.py                    # FastAPI main application entry point
│   │   └── error_handling.py          # Error handling logic for API requests and user inputs
│   │
│   ├── requirements.txt               # Backend Python dependencies
│   └── Dockerfile                     # Docker configuration for the FastAPI backend
│
├── frontend/
│   ├── public/
│   │   ├── index.html                 # Frontend HTML file
│   │   └── ...                        # Other public assets
│   ├── src/
│   │   ├── components/                # React components
│   │   ├── styles/                    # Stylesheets for React components
│   │   ├── App.js                     # Main React component
│   │   └── index.js                  
│   ├── package.json                   # Frontend Node.js dependencies
│   └── Dockerfile                     # Docker configuration for the React frontend
│
└── README.md                          # Project documentation
```
### tutoring_logic.py      # Backend logic for managing tutoring sessions
```
class TutoringLogic:
    def __init__(self, tts_service, stt_service, evaluation_service):
        self.tts_service = tts_service
        self.stt_service = stt_service
        self.evaluation_service = evaluation_service

    def initiate_tutoring_session(self, document_content):
        # Logic to initiate a tutoring session with document content
        pass

    def explain_document_content(self):
        # Logic to explain the document content verbally
        pass

    def prompt_discussions(self):
        # Logic to prompt discussions or questions during the session
        pass

    def summarize_sections(self):
        # Logic to summarize complex sections using speech
        pass

    def transcribe_user_responses(self, user_audio):
        # Logic to transcribe user audio responses to text
        pass

    def assess_user_understanding(self, user_responses):
        # Logic to assess user understanding against learning objectives
        pass

    def provide_feedback(self, user_understanding):
        # Logic to provide feedback on user understanding
        pass

```

### GoalDerivation 

```
from typing import List

class GoalDerivation:
    def __init__(self):
        # Initialize necessary components or services here
        pass

    def derive_learning_objectives(self, analysis_results: dict) -> List[str]:
        # Logic to extract learning objectives from document analysis data
        # Replace this with the actual algorithm or logic based on your requirements
        
        # For instance, let's say the analysis results have a 'key_phrases' field
        # We extract key phrases to form learning objectives
        if 'key_phrases' in analysis_results:
            learning_objectives = analysis_results['key_phrases']
            return learning_objectives
        
        # Return default objectives if no key phrases are found
        return ["Objectives not found"]
```




