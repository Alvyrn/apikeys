from flask import Flask, request, jsonify, send_from_directory
import google.generativeai as genai
import json
import os

app = Flask(__name__)

with open("key.json") as f:
    key = json.load(f)["api_key"]

genai.configure(api_key=key)
model = genai.GenerativeModel("models/gemini-1.5-pro-001") 

@app.route("/")
def index():
    return send_from_directory('.', 'index.html')

@app.route("/style.css")
def style():
    return send_from_directory('.', 'style.css')

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    prompt = data.get("prompt", "")
    try:
        response = model.generate_content(prompt)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
