# api/chat.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
from greetingsModel import get_greeting
from translationService import translate_text
import uvicorn
import json

# (Assume you have your GODEL inference code wrapped in a function called `generate_response`.)
def generate_response(prompt: str) -> str:
    # Placeholder for your GODEL model inference.
    # In practice, load your fine-tuned model and generate a response.
    return f"Response to: {prompt}"

app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str
    user_name: str = None
    target_language: str = None  # e.g., 'sw' for Swahili

@app.post("/")
async def chat_endpoint(req: ChatRequest):
    greeting = get_greeting(req.user_name)
    bot_response = generate_response(req.prompt)
    
    # Optionally, translate the bot response if target language is provided.
    if req.target_language:
        bot_response = translate_text(bot_response, target_lang=req.target_language)
    
    return {"greeting": greeting, "response": bot_response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
