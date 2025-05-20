import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.speak("Hello, i don't want to say anything to you😁")