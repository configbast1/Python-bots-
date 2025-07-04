from aiogram import Router, types
from aiogram.filters import Command

from db import save_poll_answer

router = Router()

POLL_QUESTION = "Какой твой любимый цвет?"
POLL_OPTIONS = ["🔴 Красный", "🟢 Зелёный", "🔵 Синий"]

@router.message(Command("poll"))
async def cmd_poll(message: types.Message):
    """
    Команда /poll: отправляет опрос.
    """
    await message.answer_poll(
        question=POLL_QUESTION,
        options=POLL_OPTIONS,
        is_anonymous=False,
        allows_multiple_answers=False
    )

@router.poll_answer()
async def handle_poll_answer(poll_answer: types.PollAnswer):
    """
    Обработчик ответа на опрос.
    """
    user_id = poll_answer.user.id
    poll_id = poll_answer.poll_id

    option_index = poll_answer.option_ids[0] if poll_answer.option_ids else -1
    answer_text = POLL_OPTIONS[option_index] if 0 <= option_index < len(POLL_OPTIONS) else "Неизвестно"

    await save_poll_answer(user_id, poll_id, answer_text)

    try:
        await router.bot.send_message(user_id, f"✅ Твой ответ «{answer_text}» сохранён!")
    except:
        pass
