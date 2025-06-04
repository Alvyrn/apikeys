import google.generativeai as genai

# Your Gemini API key here
API_KEY = "AIzaSyDvbVLalzhZZq2z4rgs84QupN83ZoOIZEY"

genai.configure(api_key=API_KEY)

# Use the generate_text method from the client, not the model instance
response = None

while True:
    prompt = input("\nEnter your prompt (or 'exit' to quit): ")
    if prompt.lower() == "exit":
        break
    try:
        response = genai.generate_text(
            model="models/gemini-1.5-pro-001",
            prompt=prompt,
        )
        print("\nGemini says:\n" + response.candidates[0].output)
    except Exception as e:
        print(f"\nError: {e}")
