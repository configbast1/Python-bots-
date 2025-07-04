from aiogram import Router, types
from aiogram.filters import Command

from db import add_user

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    """
    Обработчик команды /start:
    - регистрирует пользователя в базе, если ещё нет
    - отправляет приветственное сообщение
    """
    user_id = message.from_user.id
    name = message.from_user.full_name  # Имя пользователя из Telegram

    await add_user(user_id, name)

    await message.answer(
        f"👋 Привет, {name}!\n"
        f"Ты успешно зарегистрирован. "
        f"Можешь использовать /poll, /note, /notes и /remind."
    )
