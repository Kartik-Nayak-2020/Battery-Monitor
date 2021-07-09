from time import sleep

import psutil

optimal_battery_percent = 80
low_battery_percent = 40


def get_battery_status():
    """Fetch battery percent and plugged in status"""
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = int(battery.percent)
    return plugged, percent


def watch_battery_status(temp_percent):
    """Calculate time interval to convey the message to user in specified time"""
    while True:
        sleep(0.1)
        plugged, percent = get_battery_status()
        if plugged and percent - temp_percent < 5 and percent >= optimal_battery_percent:
            continue
        if not plugged and temp_percent - percent < 3 and percent <= low_battery_percent:
            continue
        else:
            break
