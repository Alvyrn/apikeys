from flask import Flask, request, jsonify
import google.generativeai as genai

# Load API key
with open("key.txt", "r") as file:
    api_key = file.read().strip()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask_gemini():
    data = request.get_json()
    prompt = data.get("question", "")

    try:
        response = model.generate_content(prompt)
        return jsonify({"answer": response.text})
    except Exception as e:
        return jsonify({"answer": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
