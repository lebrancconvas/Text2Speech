import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

while True:
    s = input("Input Word: ")
    speaker.Speak(s)

