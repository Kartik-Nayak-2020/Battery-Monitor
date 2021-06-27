from time import sleep

from FetchBatteryDetail import (
    getBatteryStatus,
    realtimeBatteryStatus,
    optimalBatteryPercent,
    lowBatteryPercent,
)
from NotifyUser import speakToNotify
from FetchDirectory import createTargetDirectory


def main():
    """Main executing function"""
    createTargetDirectory()
    while True:
        try:
            plugged, percent = getBatteryStatus()

            if plugged and percent == 100:
                continue

            elif plugged and percent >= optimalBatteryPercent:
                message = f"Battery has been charged to {percent}%. You can unplug the device now"
                flag = "optimal"
                speakToNotify(message, flag)
                tpercent = percent
                if plugged:
                    realtimeBatteryStatus(tpercent)

            elif not plugged and percent <= lowBatteryPercent:
                message = f"Current battery status is {percent}%. Please charge your device now"
                flag = "low"
                speakToNotify(message, flag)
                tpercent = percent
                if not plugged:
                    realtimeBatteryStatus(tpercent)
            sleep(0.1)
        except:
            continue


main()
