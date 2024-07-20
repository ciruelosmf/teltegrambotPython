import os
from openai import OpenAI
client = OpenAI()
from aiogram import Bot, Dispatcher, executor, types
from keep_alive import keep_alive

bot = Bot(token = os.getenv("tg_token"))
dp = Dispatcher(bot)

client.api_key = os.getenv("OPENAI_API_KEY")

keep_alive()

@dp.message_handler(commands = ['start', 'help'])
async def welcome(message: types.Message):
  await message.reply('Hi. Ask  ')


@dp.message_handler()
async def gpt(message: types.Message):
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f" {message.text}"},
    ],
    temperature=0.5,
    max_tokens=424,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )
  await message.reply(response.choices[0].message.content)


if __name__ == "__main__":
  executor.start_polling(dp)