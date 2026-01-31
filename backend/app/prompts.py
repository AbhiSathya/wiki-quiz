QUIZ_PROMPT = """
You are an expert quiz creator.

Using ONLY the information from the Wikipedia article below,
generate 5 to 10 multiple-choice questions.

Rules:
- Each question must have exactly 4 options
- Only ONE correct answer
- Difficulty must be one of: easy, medium, hard
- Explanation must reference the article content
- DO NOT hallucinate facts
- Output MUST be valid JSON
- Do not include any text outside the JSON (no comments, no markdown, no explanations)

Wikipedia Article:
{article_text}

Return JSON strictly in this format:
[
  {{
    "question": "",
    "options": ["", "", "", ""],
    "answer": "",
    "difficulty": "",
    "explanation": ""
  }}
]
"""



RELATED_TOPICS_PROMPT = """
Based ONLY on the Wikipedia article below,
suggest 5 related Wikipedia topics for further reading.

Rules:
- Topics must be relevant
- No explanations
- Output ONLY a JSON array of strings

Wikipedia Article:
{article_text}
"""
