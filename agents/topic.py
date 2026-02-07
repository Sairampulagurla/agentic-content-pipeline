from groq import Groq

client = Groq(api_key="enter api")

def topic_agent(keyword):

    prompt = f"""
    Generate 5 blog topics related to {keyword}.
    Pick the best one and return ONLY that topic.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content.strip()
