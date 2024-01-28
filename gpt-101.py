import os

import openai

# learn more: https://platform.openai.com/docs/api-reference/chat

# To set an environment variable, run this in your terminal: OPENAI_API_KEY=enter-your-api-key-here python gpt-101.py

openai.api_key = os.environ["OPENAI_API_KEY"]

# you can fine-tune the system prompt and create instructions for the ai chatbot to follow
system_prompt = "You are Paul Graham, also known as PG, the co-founder of Y Combinator. Use his analytical insights, calm demeanor, and deep startup wisdom to answer questions. Keep the answers casual and under 3 sentences, and include pauses like 'umm' between sentences."

messages = [{
    "role": "system",
    "content": system_prompt
}, {
    "role": "user",
    "content": input("ask me anything: ")
}]

response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                        messages=messages,
                                        temperature=0.8)

print(response.choices[0].message['content'])

