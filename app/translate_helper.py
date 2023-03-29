from google.cloud import translate_v2
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\KEY\key.json"

def translate_text(text, target_language="en"):
    client = translate_v2.Client()
    result = client.translate(text, target_language)
    return result['translatedText']
