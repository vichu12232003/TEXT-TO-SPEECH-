import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        user_input = input("Enter the text you want to convert to speech (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        speak_text(user_input)

if __name__ == "__main__":
    main()
