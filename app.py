from flask import Flask, request, jsonify, send_from_directory
import google.generativeai as genai
import os

# Load API key
with open("key.txt", "r") as file:
    api_key = file.read().strip()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

app = Flask(__name__)

# Serve index.html
@app.route("/")
def index():
    return send_from_directory(".", "index.html")

# Serve CSS
@app.route("/style.css")
def css():
    return send_from_directory(".", "style.css")

# API route
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    prompt = data.get("question", "")

    try:
        response = model.generate_content(prompt)
        return jsonify({"answer": response.text})
    except Exception as e:
        return jsonify({"answer": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
