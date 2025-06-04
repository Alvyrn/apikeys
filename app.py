from flask import Flask, request, jsonify, send_from_directory
import google.generativeai as genai
import json

# Load API Key
with open("key.json") as f:
    api_key = json.load(f)["api_key"]

genai.configure(api_key=api_key)

# Use correct model from your working list
model = genai.GenerativeModel("models/gemini-1.5-pro")

# Flask app setup
app = Flask(__name__)

# Serve index.html
@app.route("/")
def index():
    return send_from_directory('.', "index.html")

# Serve style.css
@app.route("/style.css")
def css():
    return send_from_directory('.', "style.css")

# Handle prompt
@app.route("/ask", methods=["POST"])
def ask():
    try:
        prompt = request.json.get("prompt", "")
        response = model.generate_content(prompt)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run app with debug ON
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
