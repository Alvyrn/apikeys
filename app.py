from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

# ✅ Read API key from key.json
try:
    with open("key.txt") as f:
        API_KEY = f.read().strip()
except Exception as e:
    print(f"Failed to read key.txt: {e}")
    API_KEY = None


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    if not API_KEY:
        return jsonify({"response": "[Error: API key not loaded]"})

    user_input = request.json.get("prompt", "")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",  # change model if needed
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }

    try:
        r = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        data = r.json()
        if r.status_code != 200:
            return jsonify({"response": f"[API Error {r.status_code}: {data.get('error', {}).get('message', 'Unknown')}]"})
        return jsonify({"response": data["choices"][0]["message"]["content"]})
    except Exception as e:
        return jsonify({"response": f"[Internal Error: {str(e)}]"})

if __name__ == "__main__":
    app.run(debug=True)
