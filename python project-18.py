# Function to compute the angle between the hour and minute hand:
def findAngle(hh, mm):
    # handle 24-hour notation:
    hh = hh % 12

    # For finding the position of the hour's hand:
    h = (hh * 360) // 12 + (mm * 360) // (12 * 60)

    # For finding the position of the minute's hand:
    m = (mm * 360) // (60)

    # For calculating the angle difference:
    angle = abs(h - m)

    # consider the shorter angle and return it
    if angle > 180:
        angle = 360 - angle

    return angle
if __name__ == '__main__':
    hh = 5                          #input
    mm = 30                         #input
    print(findAngle(hh, mm))
if __name__ == '__main__':
    hh = 21                          #input
    mm = 00                          #input
    print(findAngle(hh, mm))
if __name__ == '__main__':
    hh = 12                          #input
    mm = 00                          #input
    print(findAngle(hh, mm))
if __name__ == '__main__':
    hh=22                           #input
    mm=36                           #input
    print(findAngle(hh, mm))