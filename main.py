
from plugins.handler import handle_message

print("🤖 بوت الشاه يعمل...")

while True:
    msg = input("👤 اكتب أمر: ")
    print(handle_message(msg))
