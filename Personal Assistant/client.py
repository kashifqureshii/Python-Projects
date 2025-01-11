from openai import OpenAI

client=OpenAI(
    api_key= os.environ.get("custom_ENV_Name"),

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant name jarvis assistant skilled in general task like alexa and google"},
        {
            "role": "user",
            "content": "what is coding."
        }
    ]
)

print(completion.choices[0].message.content)
)
