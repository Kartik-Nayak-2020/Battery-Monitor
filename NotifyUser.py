import os
from gtts import gTTS
from playsound import playsound

try:  # Beep module enables to produce beep sound in Windows systems
    from winsound import Beep
except:
    pass


def speakToNotify(message, flag):
    """Notify user whether to start/stop charging the device based on battery percent using Google Text To Speech"""
    try:  # Google text to speech to convert message into audio
        tts = gTTS(text=message, lang="en")
        audioFileName = "Battery Monitor.mp3"
        tts.save(audioFileName)
        playsound(audioFileName)
        os.remove(audioFileName)
    except:  # In case of no internet connection
        try:  # Produce beep sound in Windows systems
            if flag == "optimal":
                Beep(950, 730)
            elif flag == "low":
                [Beep(800, 750) for _ in range(2)]
        except:  # Produce beep sound in Linux systems
            if flag == "optimal":
                os.system(f"play -nq -t alsa synth {0.5} sine {320}")
            elif flag == "low":
                [
                    os.system(f"play -nq -t alsa synth {0.5} sine {250}")
                    for _ in range(2)
                ]
