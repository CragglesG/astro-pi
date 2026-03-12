from picamzero import Camera
from time_calc import get_time_diff
import features
import distance

cam = Camera()

def take_photos():
    for i in range(10):
        cam.take_photo(f"image{i}.jpg")

def calculate(image1, image2):
    time_diff = get_time_diff(image1, image2)
    kp1, kp2, desc1, desc2 = features.calculate_features(image1, image2, 1000)
    matches = features.calculate_matches(desc1, desc2)
    coords1, coords2 = distance.find_matching_coordinates(kp1, kp2, matches)
    feature_dist = distance.calculate_distance(coords1, coords2)
    speed = distance.calculate_speed(feature_dist, 12648, time_diff)
    return speed

take_photos()

# speeds = []
# for i in range(9):
#     speeds.append(calculate(f"image{i}.jpg", f"image{i+1}.jpg"))

# speed = sum(speeds)/10

speed = calculate("image0.jpg", "image1.jpg")

with open ("result.txt", "w") as f:
    f.write("{:.4f}".format(speed))
