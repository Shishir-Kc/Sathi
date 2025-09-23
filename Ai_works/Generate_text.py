from groq import Groq
from decouple import config
import asyncio

client = Groq(api_key=config('GROQ_API'))
async def generate_text(prompt) -> str:
    response = " "
    completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
      {
        "role": "user",
        "content": prompt
      }
    ],
    temperature=1,
    max_completion_tokens=8192,
    top_p=1,
    reasoning_effort="medium",
    stream=True,
    stop=None
    )

    for chunk in completion:
     data = chunk.choices[0].delta.content 
     if data:
        response += data
    return response


if __name__ == "__main__":
   prompt = input('=> ')
   response = asyncio.run(generate_text(prompt))
   print("==============================================")
   print(response)