import openai
import os

api_key = os.environ["api_key"]

def generate_response(context,content,model="gpt-4"):
  response = openai.ChatCompletion.create(model=model,
    messages=[
      {"role": "system", "content": content},
      {"role": "user", "content": content}
      ]
  )
  return response['choices'][0]['message']['content']