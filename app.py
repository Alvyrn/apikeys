from flask import Flask, request, jsonify
import google.generativeai as genai
import json

app = Flask(__name__)

with open("key.json") as f:
    key = json.load(f)["api_key"]

genai.configure(api_key=key)

model = genai.GenerativeModel("models/gemini-1.5-pro-001")  # or your chosen model

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    prompt = data.get("prompt", "")
    try:
        response = model.generate_text(prompt=prompt)
        return jsonify({"response": response.text})
    except Exception as e:
        # This is the fallback for quota errors or others
        return jsonify({"response": "Sorry, API quota exceeded. Try again later!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
