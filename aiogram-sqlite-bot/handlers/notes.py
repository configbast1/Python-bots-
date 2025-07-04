from aiogram import Router, types
from aiogram.filters import Command, CommandObject

from db import add_note, get_notes

router = Router()

@router.message(Command("note"))
async def cmd_add_note(message: types.Message, command: CommandObject):
   
    note_text = command.args
    if not note_text:
        await message.reply("❗ Используй: /note <текст>")
        return

    await add_note(message.from_user.id, note_text)
    await message.answer("🗒 Заметка сохранена!")

@router.message(Command("notes"))
async def cmd_list_notes(message: types.Message):
 
    notes = await get_notes(message.from_user.id)
    if not notes:
        await message.answer("😕 У тебя пока нет заметок.")
    else:
        text = "📋 Твои заметки:\n" + "\n".join(f"{i+1}. {n}" for i, n in enumerate(notes))
        await message.answer(text)
