import math

def find_matching_coordinates(kp1, kp2, matches):
    coords1 = []
    coords2 = []
    for match in matches:
        image_1_idx = match.queryIdx
        image_2_idx = match.trainIdx
        (x1,y1) = kp1[image_1_idx].pt
        (x2,y2) = kp2[image_2_idx].pt
        coords1.append((x1,y1))
        coords2.append((x2,y2))
    return coords1, coords2

def calculate_distance(coords1, coords2):
    all_distances = 0
    merged_coords = list(zip(coords1, coords2))
    for coord in merged_coords:
        x_diff = coord[0][0] - coord[1][0]
        y_diff = coord[0][1] - coord[1][1]
        distance = math.hypot(x_diff, y_diff)
        all_distances = all_distances + distance
    return all_distances / len(merged_coords)

def calculate_speed(feature_dist, GSD, time_diff):
    distance = feature_dist * GSD / 10000
    speed = distance / time_diff
    return speed
