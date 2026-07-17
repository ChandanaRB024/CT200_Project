from groq import Groq
from config.settings import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def generate_test_cases(text):
    prompt = f"""
You are an experienced Software Test Engineer.

Generate functional test cases for the following document.

Return ONLY in this format:

Test Case ID:
Title:
Precondition:
Steps:
Expected Result:

Document:

{text}
"""

    try:
        print("=" * 50)
        print("Calling Groq...")
        print("=" * 50)

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        print("Groq Success")

        return completion.choices[0].message.content

    except Exception as e:
        print("=" * 50)
        print("GROQ ERROR")
        print(type(e))
        print(e)
        print("=" * 50)
        raise