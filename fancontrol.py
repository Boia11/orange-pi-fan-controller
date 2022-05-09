#!/usr/bin/env python3

import os
import sys
import time

ON_THRESHOLD = 60  #(°C) Fan kicks on at this temperature.
OFF_THRESHOLD = 50  #(°C) Fan shuts off at this temperature.
SLEEP_INTERVAL = 5  #[seconds] How often we check the core temperature.

# GPIO PIN is 9 using to control the fan. [Physical PIN 16 on board]

def get_temp():
    """Get the core temperature.

    Read file from /sys to get CPU temp in temp in C *1000

    Returns:
        int: The core temperature in thousanths of degrees Celsius.
    """
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        temp_str = f.read()

    try:
        return int(temp_str) / 1000
    except (IndexError, ValueError,) as e:
        raise RuntimeError('Could not parse temperature output.') from e

if __name__ == '__main__':
    # Validate the on and off thresholds
    if OFF_THRESHOLD >= ON_THRESHOLD:
        raise RuntimeError('OFF_THRESHOLD must be less than ON_THRESHOLD')

    os.system('gpio mode 9 out')
    os.system('gpio write 9 0')
    

    while True:
        fan = os.system('gpio read 9')
        temp = get_temp()
        print(temp)

        # Start the fan if the temperature has reached the limit and the fan
        # isn't already running.
        # NOTE: `fan` returns 1 for "on" and 0 for "off"
        if temp > ON_THRESHOLD and fan==0:
            os.system('gpio write 9 1')
        # Stop the fan if the fan is running and the temperature has dropped
        # to 10 degrees below the limit.
        if temp <= OFF_THRESHOLD:
            os.system('gpio write 9 0')

        time.sleep(SLEEP_INTERVAL)