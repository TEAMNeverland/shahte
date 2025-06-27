
def handle_message(msg):
    if msg.startswith("/قفل"):
        return "✅ تم قفل العنصر المطلوب"
    elif msg.startswith("/فتح"):
        return "✅ تم فتح العنصر المطلوب"
    elif msg.startswith("/تفعيل الالعاب"):
        return "🎮 الألعاب مفعلة"
    elif msg.startswith("/زخرفه"):
        return "🌟 تم زخرفة الاسم!"
    elif msg.startswith("/يوت "):
        q = msg.split("/يوت ",1)[1]
        return f"🔊 جاري البحث عن: {q}"
    elif msg.startswith("/رفع ملك"):
        return "👑 تم رفعه ملك!"
    else:
        return "❓ أمر غير معروف"
