import speech_recognition as sr
import os
import json
import pyautogui
import ctypes
import threading

def recognize_speech_from_mic(recognizer, microphone):
    with microphone as source:
        print("Listening...")
        audio = recognizer.listen(source)

    response = {"success": True, "error": None, "transcription": None}

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response

def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:
        response = recognize_speech_from_mic(recognizer, microphone)

        if response["transcription"]:
            print(f"You said: {response['transcription']}")
            with open("./data.json") as e:
                lowered_speech = response["transcription"].lower()
                data = json.load(e)
                voice_cmds = data["voice_cmds"]
                for info in voice_cmds:
                    if info[0].lower() in lowered_speech or info[0].lower().replace(" ", "") in lowered_speech:
                        if info[1] == "cmd":
                            cmd = threading.Thread(target=lambda: os.system(info[2]))
                            cmd.start()
                        elif info[1] == "shortcut":
                            if ["WIN", "L"] == info[2]:
                                ctypes.windll.user32.LockWorkStation()
                                continue
                            pyautogui.hotkey(*info[2])

        elif response["error"]:
            print(f"ERROR: {response['error']}")
