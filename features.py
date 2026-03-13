import cv2
from logzero import logger

def convert_to_cv(*images):
    return [cv2.imread(img, 0) for img in images]

def calculate_features(image_1, image_2, feature_number):
    orb = cv2.ORB_create(nfeatures = feature_number)
    image_1_cv, image_2_cv = convert_to_cv(image_1, image_2)
    kp1, desc1 = orb.detectAndCompute(image_1_cv, None)
    kp2, desc2 = orb.detectAndCompute(image_2_cv, None)
    return kp1, kp2, desc1, desc2

def calculate_matches(desc1, desc2):
    brute_force = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = brute_force.match(desc1, desc2)
    matches = sorted(matches, key=lambda x: x.distance)
    return matches
