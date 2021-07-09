from time import sleep

from FetchBatteryDetail import (
    get_battery_status,
    watch_battery_status,
    optimal_battery_percent,
    low_battery_percent,
)
from FetchDirectory import create_target_directory
from NotifyUser import notify_message


def main():
    """Main executing function"""
    create_target_directory()
    while True:
        try:
            plugged, percent = get_battery_status()

            if plugged and percent == 100:
                continue

            elif plugged and percent >= optimal_battery_percent:
                message = f"Battery has been charged to {percent}%. You can unplug the device now"
                flag = "optimal"
                notify_message(message, flag)
                temp_percent = percent
                if plugged:
                    watch_battery_status(temp_percent)

            elif not plugged and percent <= low_battery_percent:
                message = f"Current battery status is {percent}%. Please charge your device"
                flag = "low"
                notify_message(message, flag)
                temp_percent = percent
                if not plugged:
                    watch_battery_status(temp_percent)
            sleep(0.1)
        except (OSError, RuntimeError):
            continue


main()
