from picamzero import Camera
from time_calc import get_time_diff
import features
import distance

cam = Camera()

def take_photos():
    for i in range(10):
        cam.take_photo(f"image{i}.jpg")

time_diff = get_time_diff("image1.jpg", "image2.jpg")
kp1, kp2, desc1, desc2 = features.calculate_features("image1.jpg", "image2.jpg", 1000)
matches = features.calculate_matches(desc1, desc2)
coords1, coords2 = distance.find_matching_coordinates(kp1, kp2, matches)
average_feature_dist = distance.calculate_mean_distance(coords1, coords2)
speed = distance.calculate_speed(average_feature_dist, 12648, time_diff)

with open ("result.txt", "w") as f:
    f.write("{:.4f}".format(speed))
