import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def extract_topics(review):
    prompt = f"""
Extract all user issues, complaints, feature requests or feedback
from the following app review.
Return short action-oriented topics (max 6 words).
Return Python list only.

Review:
{review}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    try:
        return eval(response.choices[0].message.content)
    except:
        return []
