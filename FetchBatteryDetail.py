import psutil
from time import sleep

optimalBatteryPercent = 80
lowBatteryPercent = 40


def getBatteryStatus():
    """Fetch battery percent and plugged in status"""
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = int(battery.percent)
    return plugged, percent


def realtimeBatteryStatus(tpercent):
    """Calculate time interval to convey the message to user in specified time"""
    while True:
        sleep(0.1)
        plugged, percent = getBatteryStatus()
        if plugged and percent - tpercent < 5 and percent >= optimalBatteryPercent:
            continue
        if not plugged and tpercent - percent < 3 and percent <= lowBatteryPercent:
            continue
        else:
            break
