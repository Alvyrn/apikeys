from flask import Flask, request, jsonify, render_template
import requests
import json

app = Flask(__name__)

with open("key.json") as f:
    data = json.load(f)
    API_KEY = data["key"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    prompt = request.json.get("prompt")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        try:
            reply = data['choices'][0]['message']['content']
        except Exception:
            reply = "[Unexpected response structure]"
    else:
        reply = f"[API Error {response.status_code}]"

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
