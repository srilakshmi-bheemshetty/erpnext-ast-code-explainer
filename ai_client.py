import os
from groq import Groq

def explain_with_ai(function_name, fallback_explanation):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return fallback_explanation 

    try:
        client = Groq(api_key=api_key)

        prompt = f"""
You are an ERPNext expert.
Explain this function in simple business terms.

Function name: {function_name}
Technical summary: {fallback_explanation}
"""

        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        return response.choices[0].message.content.strip()

    except Exception:
        return fallback_explanation 
