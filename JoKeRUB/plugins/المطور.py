from JoKeRUB import l313l
from ..core.managers import edit_or_reply
from .hellas import get_rights  # استيراد الحقوق من ملف hellas.py

plugin_category = "البحث"

@l313l.ar_cmd(
    pattern="(مطور|المطور)$",
    command=("مطور", plugin_category),
    info={
        "header": "لعرض معلومات المطور",
        "الاستـخـدام": "{tr}المطور - لعرض معلومات مطور البوت",
    },
)
async def _(event):
    await edit_or_reply(event, get_rights())
