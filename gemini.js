let API_KEY = "";

fetch("key.json")
  .then(res => res.json())
  .then(data => {
    API_KEY = data.api_key;
  })
  .catch(err => {
    console.error("Failed to load API key:", err);
  });

async function sendToGemini() {
  const input = document.getElementById("userInput");
  const chatBox = document.getElementById("chat-box");
  const prompt = input.value.trim();

  if (!prompt) return;

  chatBox.innerHTML += `<div class="user-msg"><strong>You:</strong> ${prompt}</div>`;
  input.value = "";

  const body = {
    contents: [{ parts: [{ text: prompt }] }]
  };

  try {
    const res = await fetch(
      `https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key=${API_KEY}`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body)
      }
    );

    const data = await res.json();
    const responseText = data?.candidates?.[0]?.content?.parts?.[0]?.text || "No response from Gemini.";

    chatBox.innerHTML += `<div class="ai-msg"><strong>Gemini:</strong> ${responseText}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
  } catch (err) {
    chatBox.innerHTML += `<div class="ai-msg"><strong>Error:</strong> ${err.message}</div>`;
  }
}
