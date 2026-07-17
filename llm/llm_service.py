from groq import Groq
from config.settings import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def generate_test_cases(text):
    prompt = f"""
You are a Senior Software Test Engineer.

Generate exactly 5 high-quality functional test cases based ONLY on the given document section.

IMPORTANT INSTRUCTIONS:
- Do NOT use Markdown.
- Do NOT use ** or ### or bullet symbols.
- Do NOT use tables.
- Return only plain text.
- Keep the response neat and professional.

Use the following format for every test case:

Test Case 1

Test Case ID:
Title:
Objective:
Preconditions:
Test Steps:
1.
2.
3.
Expected Result:
Priority:

Repeat the same format for all 5 test cases.

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
            temperature=0.2
        )

        print("Groq Response Received Successfully")
        print("=" * 60)

        response = completion.choices[0].message.content

        # Extra cleanup (in case the model still returns markdown)
        response = (
            response.replace("**", "")
                    .replace("###", "")
                    .replace("```", "")
                    .replace("---", "")
                    .strip()
        )

        return response

    except Exception as e:
        print("=" * 60)
        print("GROQ ERROR")
        print(type(e))
        print(e)
        print("=" * 60)
        raise