# translationService.py
import requests

def translate_text(text: str, source_lang: str = "en", target_lang: str = "sw") -> str:
    url = "https://libretranslate.com/translate"
    payload = {
        "q": text,
        "source": source_lang,
        "target": target_lang,
        "format": "text"
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        return response.json().get("translatedText", "")
    else:
        return "Translation error"

# Example usage:
if __name__ == "__main__":
    translated = translate_text("Hello, how are you?", target_lang="sw")
    print(translated)
