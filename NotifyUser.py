import os

from gtts import gTTS
from playsound import playsound

try:  # Beep module enables to produce beep sound in Windows systems
    from winsound import Beep
except OSError:
    pass


def notify_message(message, flag):
    """Notify user whether to start/stop charging the device based on battery percent using Google Text To Speech"""
    try:  # Google text to speech to convert message into audio
        tts = gTTS(text=message, lang="en")
        audio_file_name = "Battery Monitor.mp3"
        tts.save(audio_file_name)
        playsound(audio_file_name)
        os.remove(audio_file_name)
    except ConnectionError:  # In case of no internet connection
        try:  # Produce beep sound in Windows systems
            if flag == "optimal":
                Beep(950, 730)
            elif flag == "low":
                [Beep(800, 750) for _ in range(2)]
        except OSError:  # Produce beep sound in Linux systems
            if flag == "optimal":
                os.system(f"play -nq -t alsa synth {0.5} sine {320}")
            elif flag == "low":
                [
                    os.system(f"play -nq -t alsa synth {0.5} sine {250}")
                    for _ in range(2)
                ]
