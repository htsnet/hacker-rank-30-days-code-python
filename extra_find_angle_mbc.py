# Find Angle MBC


# call the library math
import math

segmentAB = int(input())
segmentBC = int(input())

# calculate the hypotenuse
segmentCA = math.hypot(segmentAB, segmentBC)

# calculate the angle
angle = math.degrees(math.acos(segmentBC/segmentCA))

print('{}{}'.format(round(angle), chr(176)))
