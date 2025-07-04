import asyncio
from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("remind"))
async def cmd_remind(message: types.Message):
   
    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        await message.reply("❗ Используй: /remind <секунд> <текст>")
        return

    try:
        delay = int(args[1])
    except ValueError:
        await message.reply("⏱ Время должно быть числом.")
        return

    reminder_text = args[2].strip()
    if not reminder_text:
        await message.reply("❗ Текст напоминания пустой.")
        return

    await message.answer(f"⏰ Напоминание установлено! Я напомню через {delay} сек.")

    async def send_reminder():
        await asyncio.sleep(delay)
        await message.bot.send_message(message.chat.id, f"🔔 Напоминание: {reminder_text}")

    asyncio.create_task(send_reminder())
