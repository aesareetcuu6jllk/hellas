# WRITE  BY JoKeRUB
# PLUGIN FOR JoKeRUB 
# @HELLASUserBot


from telethon import events
import random, re
from ..Config import Config

from JoKeRUB.utils import admin_cmd

import asyncio
from JoKeRUB import l313l
from random import choice
from hellas import NAME, CH
from ..core.managers import edit_or_reply
from ..sql_helper.globals import gvarstatus
plugin_category = "extra"

rehu = [
    "اللهم صلِ على محمد و على آله محمد",
]
@l313l.ar_cmd(pattern="الاوامر(?:\s|$)([\s\S]*)")
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        F_O_1 = random.choice(rehu)
        await event.edit(
        f": **⦑ قائمة اوامر {NAME}"  ⦒**\n★•┉ ┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n( `.م1` )  ⦙ **اوامر الادمن**\n( `.م2` )  ⦙ **اوامر المجموعة**\n( `.م3` )  ⦙ **اوامر الترحيب والردود**\n( `.م4` )  ⦙ **حماية خاص والتلكراف**\n( `.م5` )  ⦙ **اوامر المنشن والانتحال**\n( `.م6` )  ⦙ **اوامر التحميل والترجمة**\n( `.م7` )  ⦙ **اوامر المنع و القفل**\n( `.م8` )  ⦙ **اوامر التنظيف والتكرار**\n( `.م9` )  ⦙ **اوامر التخصيص والفارات**\n( `.م10` ) ⦙ **اوامر الوقتي و التشغيل**\n( `.م11` ) ⦙ **اوامر الكشف و الروابط**\n( `.م12` ) ⦙ **اوامر المساعدة والإذاعة** \n( `.م13` ) ⦙ **اوامر الارسال والاذكار**\n( `.م14` ) ⦙ **اوامر المـلصقات وكوكل**\n( `.م15` ) ⦙ **اوامر التسلية والميمز والتحشيش** \n( `.م16` ) ⦙ **اوامر الصيغ والجهات**\n( `.م17` ) ⦙ **اوامر التمبلر والزغرفة والمتحركة**\n( `.م18` ) ⦙ **اوامر الحساب والترفيه**\n( `.م19` ) ⦙ **اوامر اضافيه للسورس**\n( `.م20` ) ⦙ **اوامر بصمات الميمز**\n( `.م21` ) ⦙ **اوامر تجميع النقاط وبوت وعد**\n★•┉ ┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n **᯽︙ {F_O_1} **"
)


@l313l.ar_cmd(
    pattern="م1$",
    command=("م1", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            f"** قائمة اوامر الادمن لسورس {NAME}  **:\n"
            f" ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f" ᯽︙ اختر احدى هذه القوائم\n\n"
            f"- ( `.اوامر الحظر` )\n"
            f"- ( `.اوامر الكتم` )\n"
            f"- ( `.اوامر التثبيت` )\n"
            f"- ( `.اوامر الاشراف` )\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"⌔︙CH : {CH}"
        )

@l313l.ar_cmd(
    pattern="م2$",
    command=("م2", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            f"** قائمة اوامر المجـموعه لسورس {NAME} **:\n"
            f" ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f" ᯽︙ اختر احدى هذه القوائم\n\n"
            f"- ( `.اوامر التفليش` )\n"
            f"- ( `.اوامر المحذوفين` )\n"
            f"- ( `.اوامر الكروب` )\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"⌔︙CH : {CH}"
        )


from hellas import NAME, CH

@l313l.ar_cmd(
    pattern="م3$",
    command=("م3", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            f"** قائمة اوامر الـترحيب والـردود لسورس {NAME} **:\n"
            f" ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f" ᯽︙ اختر احدى هذه القوائم\n\n"
            f"- ( `.اوامر الترحيب` )\n"
            f"- ( `.اوامر الردود` )\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"⌔︙CH : {CH}"
        )

from hellas import NAME, CH

@l313l.ar_cmd(
    pattern="م4$",
    command=("م4", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            f"** قائمة اوامر حـماية الخاص والتلكراف لسورس {NAME} **:\n"
            f" ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f" ᯽︙ اختر احدى هذه القوائم\n\n"
            f"- ( `.اوامر الحماية` )\n"
            f"- ( `.اوامر التلكراف` )\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"⌔︙CH : {CH}"
        )

@l313l.ar_cmd(
    pattern="م5$",
    command=("م5", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            f"** قائمة اوامر الـمنشن والانتحال لسورس {NAME} **:\n"
            f" ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f" ᯽︙ اختر احدى هذه القوائم\n\n"
            f"- ( `.اوامر الانتحال` )\n"
            f"- ( `.اوامر التقليد` )\n"
            f"- ( `.اوامر المنشن` )\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"⌔︙CH : {CH}"
        )

@l313l.ar_cmd(
    pattern="م6$",
    command=("م6", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            f"** قائمة اوامر التحميل والترجمه لسورس {NAME} **:\n"
            f" ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f" ᯽︙ اختر احدى هذه القوائم\n\n"
            f"- ( `.اوامر النطق` )\n"
            f"- ( `.اوامر التحميل` )\n"
            f"- ( `.اوامر الترجمة` )\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"⌔︙CH : {CH}"
        )

@l313l.ar_cmd(
    pattern="م7$",
    command=("م7", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            f"** قائمة اوامر القفل والمنع لسورس {NAME} **:\n"
            f" ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f" ᯽︙ اختر احدى هذه القوائم\n\n"
            f"- ( `.اوامر القفل` )\n"
            f"- ( `.اوامر الفتح` )\n"
            f"- ( `.اوامر المنع` )\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"⌔︙CH : {CH}"
        )


@l313l.ar_cmd(
    pattern="م8$",
    command=("م8", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            f"** قائمة اوامر التكرار والتنظيف لسورس {NAME} **:\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"᯽︙ اختر احدى هذه القوائم\n\n"
            f"- ( `.اوامر التكرار` )\n"
            f"- ( `.اوامر السبام` )\n"
            f"- ( `.اوامر التنظيف` )\n"
            f"- ( `.اوامر المسح` )\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"⌔︙CH : {CH}"
        )

@l313l.ar_cmd(
    pattern="م9$",
    command=("م9", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            f"** قائمة التخصيص والفارات لسورس {NAME} **:\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"᯽︙ اختر احدى هذه القوائم\n\n"
            f"- ( `.اوامر التخصيص` )\n لتغير الصور والكلايش كل من الحماية والفحص والبنك\n"
            f"- ( `.اوامر الفارات` )\n - لتغير الاسم وزخرفة الوقت والصورة الوقتية والمنطقة الزمنية ورمز الاسم والبايو الوقتي وغيرها\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"⌔︙CH : {CH}"
        )

@l313l.ar_cmd(
    pattern="م10$",
    command=("م10", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            f"** قائمة اوامر الوقتي والتشغيل لسورس {NAME} **:\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"᯽︙ اختر احدى هذه القوائم\n\n"
            f"- ( `.اوامر الاسم` )\n"
            f"- ( `.اوامر البايو` )\n"
            f"- ( `.اوامر الكروب الوقتي` )\n"
            f"- ( `.اوامر التشغيل` )\n"
            f"- ( `.اوامر الاطفاء` )\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"⌔︙CH : {CH}"
        )

@l313l.ar_cmd(
    pattern="م11$",
    command=("م11", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            f"** قائمة اوامر الكـشف و الروابط لسورس {NAME} **:\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"᯽︙ اختر احدى هذه القوائم\n\n"
            f"- ( `.اوامر الكشف` )\n"
            f"- ( `.اوامر الروابط` )\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"⌔︙CH : {CH}"
        )

@l313l.ar_cmd(
    pattern="م12$",
    command=("م12", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            f"** قائمة اوامر المساعدة لسورس {NAME} **:\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"᯽︙ اختر احدى هذه القوائم\n\n"
            f"- ( `.اوامر الوقت والتاريخ` )\n"
            f"- ( `.اوامر كورونا` )\n"
            f"- ( `.اوامر الصلاة` )\n"
            f"- ( `.اوامر مساعدة` )\n"
            f"- ( `.اوامر الاذاعه` )\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"⌔︙CH : {CH}"
        )


@l313l.ar_cmd(
    pattern="م13$",
    command=("م13", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            f"** قائمة اوامر الارسال لسورس {NAME} **:\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"᯽︙ اختر احدى هذه القوائم\n\n"
            f"- ( `.امر الصورة الذاتية` )\n"
            f"- ( `.اوامر التحذيرات` )\n"
            f"- ( `.اوامر اللستة` )\n"
            f"- ( `.اوامر الملكية` )\n"
            f"- ( `.اوامر السليب` )\n"
            f"- ( `.اوامر الاذكار` )\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"⌔︙CH : {CH}"
        )

@l313l.ar_cmd(
    pattern="م14$",
    command=("م14", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            f"** قائمة اوامر الملصقات وكوكل لسورس {NAME} **:\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"᯽︙ اختر احدى هذه القوائم\n\n"
            f"- ( `.اوامر الملصقات` )\n"
            f"- ( `.اوامر كوكل` )\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"⌔︙CH : {CH}"
        )

@l313l.ar_cmd(
    pattern="م15$",
    command=("م15", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            f"** قائمة اوامر التسلية والتحشيش لسورس {NAME} **:\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"᯽︙ اختر احدى هذه القوائم\n\n"
            f"- ( `.اوامر التسلية` )\n"
            f"- ( `.اوامر التحشيش` )\n"
            f"- ( `.اوامر الميمز` )\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"⌔︙CH : {CH}"
        )

@l313l.ar_cmd(
    pattern="م16$",
    command=("م16", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            f"** قائمة اوامر تحويل الصيغ و الجهات لسورس {NAME} **:\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"᯽︙ اختر احدى هذه القوائم\n\n"
            f"- ( `.اوامر التحويل` )\n"
            f"- ( `.اوامر الجهات` )\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"⌔︙CH : {CH}"
        )

@l313l.ar_cmd(
    pattern="م18$",
    command=("م18", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            f"** قائمة اوامر الحساب و الترفيه لسورس {NAME} **:\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"᯽︙ اختر احدى هذه القوائم\n\n"
            f"- ( `.اوامر الترفيه` )\n"
            f"- ( `.اوامر الحساب` )\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"⌔︙CH : {CH}"
        )

@l313l.ar_cmd(
    pattern="م19$",
    command=("م19", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            f"**⦑ قائمة الأوامر الجديدة لسورس {NAME} ⦒**\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n"
            f"⥾ `.اوامر البصمات`\n"
            f"⥾ `.اوامر النقل`\n"
            f"⥾ `.اوامر الرصيد`\n"
            f"⥾ `.اوامر النشر`\n"
            f"⥾ `.اوامر التنزيل`\n"
            f"⥾ `.اوامر الذكاء`\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n"
            f"⌔︙CH : {CH}"
        )

@l313l.ar_cmd(
    pattern="م20$",
    command=("م20", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            f"** قائمة اوامر بصمات الميمز لسورس {NAME} **:\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"᯽︙ اختر احدى هذه القوائم\n\n"
            f"- ( `.بصمات ميمز` )\n"
            f"- ( `.بصمات ميمز2` )\n"
            f"- ( `.بصمات ميمز3` )\n"
            f"- ( `.بصمات ميمز4` )\n"
            f"- ( `.بصمات ميمز5` )\n"
            f"- ( `.بصمات انمي` )\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"⌔︙CH : {CH}"
        )

@l313l.ar_cmd(
    pattern="م21$",
    command=("م21", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            f"** قائمة اوامر تجميع النقاط و بوت وعد لسورس {NAME} **:\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"᯽︙ اختر احدى هذه القوائم\n\n"
            f"- ( `.اوامر التجميع` )\n"
            f"- ( `.اوامر وعد` )\n"
            f"★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n"
            f"⌔︙CH : {CH}"
        )

