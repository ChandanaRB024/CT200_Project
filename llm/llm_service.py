from groq import Groq
from config.settings import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def generate_test_cases(text):
    prompt = f"""
You are a Senior Software Test Engineer with expertise in embedded systems and software quality assurance.

Your task is to generate comprehensive functional test cases for the given document section.

Instructions:
- Generate at least 5 functional test cases.
- Use only the information available in the document.
- Do not assume features that are not mentioned.
- Keep the test cases clear and professional.

For each test case include:

Test Case ID:
Title:
Objective:
Preconditions:
Test Steps:
Expected Result:
Priority:

Document Section:
{text}
"""

    try:
        print("=" * 60)
        print("Calling Groq API...")
        print("=" * 60)

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

        print("Groq Response Received Successfully")
        print("=" * 60)

        return completion.choices[0].message.content

    except Exception as e:
        print("=" * 60)
        print("GROQ ERROR")
        print(type(e))
        print(e)
        print("=" * 60)
        raise