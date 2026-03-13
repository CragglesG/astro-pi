from picamzero import Camera
from logzero import logger, logfile
from time_calc import get_time_diff
from time import sleep
import features
import distance

cam = Camera()
logfile("main.log")

def take_photos():
    for i in range(25):
        cam.take_photo(f"image{i}.jpg")
        sleep(15)

def calculate(image1, image2):
    time_diff = get_time_diff(image1, image2)
    kp1, kp2, desc1, desc2 = features.calculate_features(image1, image2, 1000)
    matches = features.calculate_matches(desc1, desc2)
    coords1, coords2 = distance.find_matching_coordinates(kp1, kp2, matches)
    feature_dist = distance.calculate_distance(coords1, coords2)
    speed = distance.calculate_speed(feature_dist, 12648, time_diff)
    return speed

take_photos()

speeds = []
for i in range(24):
    s = calculate(f"image{i}.jpg", f"image{i+1}.jpg")
    logger.info(f"Speed estimate {i}: {s}")
    speeds.append(s)

speed = sum(speeds)/24

with open ("result.txt", "w") as f:
    f.write("{:.4f}".format(speed))
