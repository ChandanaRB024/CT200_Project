import google.generativeai as genai

API_KEY = "PASTE_YOUR_NEW_API_KEY_HERE"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("models/gemini-2.0-flash-001")

response = model.generate_content("Hello")

print(response.text)