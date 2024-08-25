import os

def speak_text(text):
    text_escaped = text.replace('"', '""')
    command = f"Add-Type -AssemblyName System.speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{text_escaped}')"
    os.system(f'powershell -Command "{command}"')

if __name__ == '__main__':
    print("Welcome to RoboSpeaker")
    sentence = ""
    while True:
        user_input = input("Enter what you want to speak (or 'q' to quit): ")
        if user_input.lower() == "q":
            print("Exiting RoboSpeaker. Goodbye!")
            break
        sentence += user_input
        speak_text(sentence)
