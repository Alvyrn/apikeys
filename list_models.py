import google.generativeai as genai
import json

with open("key.json") as f:
    key = json.load(f)["api_key"]

genai.configure(api_key=key)

def list_models():
    try:
        models_generator = genai.list_models()
        print("Available models:")
        for model in models_generator:
            print(f" - {model.name}")
    except Exception as e:
        print(f"Error listing models: {e}")

if __name__ == "__main__":
    list_models()
