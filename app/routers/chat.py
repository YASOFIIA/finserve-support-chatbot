from google import genai
from pydantic import BaseModel
from fastapi import APIRouter
from app.prompts import SYSTEM_PROMPT
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()


class ChatRequest(BaseModel):
    messages: list


@router.post("/chat")
def chat(request: ChatRequest):
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

    history = [
        {"role": m["role"], "parts": [{"text": m["content"]}]}
        for m in request.messages[:-1]
    ]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            {"role": "user" if m["role"] == "user" else "model",
             "parts": [{"text": m["content"]}]}
            for m in request.messages
        ],
        config={
            "system_instruction": SYSTEM_PROMPT,
            "max_output_tokens": 300
        }
    )

    return {"reply": response.text}