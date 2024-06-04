from openai import OpenAI
import os

MODEL="gpt-3.5-turbo"
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

completion = client.chat.completions.create(
  model=MODEL,
  messages=[
    {"role": "system", "content": "あなたは英語と日本語のエキスパート猫です。語尾は「ニャン」です。私の翻訳を手伝ってくれます！"},
    {"role": "user", "content": "ねこがこたつでねころんだ！"}
  ]
)

print("🐱: " + completion.choices[0].message.content)