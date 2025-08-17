# hellas.py
# ─────────────────────────────
#    جميع الحقوق محفوظة لمطوري سورس جـيبثون حصرياً
#    اذا تخمط الملف اذكر الحقوق وكاتبيه ومطوريه لا تحذف الحقوق
#    ─────────────────────────────

BOT_NAME = "HELLAS 𝘜𝘚𝘌𝘙𝘉𝘖𝘛"
SOURCE_VERSION = "1.23.0"
PYTHON_VERSION = "3.9.6"
OWNER_USER = "@F_Q_1"
SUPPORT_GROUP = "https://t.me/HELLASSupport"
SOURCE_CHANNEL = "https://t.me/HELLASUserBot"

HELLO_TEXT = f"""
**{BOT_NAME}**
-━═━═━═━═━━═━═━═━═━-
**- حالة البوت **: يعمل بنجاح ✅
**- اصدار السورس **: {SOURCE_VERSION}
**- اصدار البايثون **: {PYTHON_VERSION}
**- القناة **: {SOURCE_CHANNEL}
-━═━═━═━═━━═━═━═━═━-
"""

# دالة ترجع النصوص
def get_rights():
    return f"حقوق السورس لـ {BOT_NAME} | Dev : {OWNER_USER} "
