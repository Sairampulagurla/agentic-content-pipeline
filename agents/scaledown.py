from groq import Groq

client = Groq(api_key="enter api")

def scaledown_agent(drafts):

    combined = "\n---\n".join(drafts)

    prompt = f"""
    Compress aggressively to 40% size.
    Preserve meaning, structure, and key points.

    Drafts:
    {combined}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
