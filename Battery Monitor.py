import psutil
from random import choice
from time import sleep
from gtts import gTTS
import os
from playsound import playsound
from winsound import Beep


def get_username():
    '''This function will retrieve username from PC (Windows only).'''
    for user,name in os.environ.items():
        if user == "USERNAME":
            return name


def gtts_notify(cmd,name,flag):
    '''This funtion to alert user about battery status if it's optimally charged or running low.'''
    tts = gTTS(text=cmd, lang='en')
    try:
        os.chdir(r"C:\Users\\"+name+"\Documents")
        try:     
            os.mkdir("Battery Monitor")
        except:
            pass
        os.chdir(r"C:\Users\\"+name+"\Documents\Battery Monitor")
    except:
        os.chdir("/home/kartik/Documents")
        try:
            os.mkdir("Battery Monitor")
        except:
            pass
        os.chdir("/home/kartik/Documents/Battery Monitor")
    try:
        file_name = "Battery Monitor.mp3"
        tts.save(file_name)
        playsound(file_name)
        os.remove(file_name)
    except:
        if flag == "optimal":
            Beep(950,730)
        elif flag == "low":
            [Beep(800,750) for _ in range(2)]
    

def optimal_battery(percent,name):
    optimal_notify = [f"Battery has been charged to {int(percent)}%. You can unplug the device now", "Battery has been optimally charged. You can unplug the device now"]
    flag = "optimal"
    gtts_notify(choice(optimal_notify),name,flag)
    

def low_battery(percent,name):
    low_notify = [f"Current battery status is {int(percent)}%. Please charge your device", "Battery status is very low. You better start charging your device"]
    flag = "low"
    gtts_notify(choice(low_notify),name,flag)


def get_battery_status():
    '''This function will check the current battery status including percent and whether if it is charging or not.'''
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = int(battery.percent)
    return plugged, percent


def realtime(tpercent):
    '''This function will check the battery status continuously to let user know about battey status according to the setting.'''
    while True:
        sleep(0.1)
        plugged, percent = get_battery_status()
        if plugged and percent - tpercent < 1 and percent >= optimal_battery_cr:
            continue
        if not plugged and tpercent - percent < 1 and percent <= low_battery_cr: 
            continue
        else:
            break


def main(name):
    '''This is main function responsible for running all the battery monitoring services'''
    while True:
        plugged, percent = get_battery_status()
        if plugged and percent == 100:
            continue

        elif plugged and percent >= optimal_battery_cr:
            optimal_battery(percent,name)
            tpercent = percent 
            if plugged:
                realtime(tpercent)

        elif not plugged and percent <= low_battery_cr:
            low_battery(percent,name)
            tpercent = percent
            if not plugged:
                realtime(tpercent)
        sleep(0.1)


if __name__ == "__main__":
    '''On reaching low_battery_cr program will let the user know that the battery is running low and will continue to do so every 3% battery drop until user connect the device to
    AC. On reaching optimal_battery_cr program will let the user know that the battery is optimally charged and continue to do so for every 5% batery increment until it
    reaches 100% or user unplug the device from AC'''
    low_battery_cr = 40
    optimal_battery_cr = 80
    name = get_username()
    main(name)
 
