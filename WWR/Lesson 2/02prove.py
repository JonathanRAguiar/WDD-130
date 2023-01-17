from datetime import datetime
import math
w = round(float(input("Enter the width of the tire in mm (ex. 205):")))
a = round(float(input("Enter the aspect ratio of the tire (ex. 60):")))
d = round(float(input("Enter the diameter of the wheel in inches (ex. 15):")))
wl = round(float(input("Enter the length of the window in inches (ex. 60):")))
cl = round(float(input("Enter the length of the car in feet (ex. 14):")))
cw = round(float(input("Enter the width of the car in meters (ex. 5):")))

v = (math.pi * w**2 * a *(w * a + 2540 * d) ) / 10000000000
ca = cl * cw
wa = wl * wl
current_date_and_time = datetime.now()

with open('volumes.txt', 'at') as volumes_file:
    
    print(f"current date: {current_date_and_time:%Y-%m-%d}, Wheel width: {w}, wheel ratio: {a}, wheel diameter: {d}, wheel volume: {v:.2f}, window length: {wl}, window area: {wa}, car length: {cl}, car width: {cw}, car area: {ca}", file=volumes_file)
pi * tire**2 * ratio (tire*ratio+2540*diameter) / 10000000000