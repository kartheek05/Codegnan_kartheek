import pyttsx3
engine = pyttsx3.init()

def text_speech(n):
        engine.say(user_text)
user_text = input("Enter the message: ").lower()
if "name" in user_text:
        name = user_text.split("name is")[-1].strip()
elif "this is" in user_text:
        name = user_text.split("this is")[-1].strip()
elif "i am " in user_text:
        name = user_text.split("i am")[-1].strip()

if user_text in ["hi","hello","hey"]:
        response = "Hello,how can i help you"
elif name in user_text:
        response = f"Hello! {name} how can i help you?"
else:
        response = "I didn't Understand"

print(response)
text_speech(user_text)
engine.runAndWait()

