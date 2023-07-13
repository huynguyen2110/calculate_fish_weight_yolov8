import cv2
import numpy as np
from PIL import Image
from .get_longest_distance import get_longest_distance


def get_skeleton(img):
    # read image and invert so blob is white on black background
    img = cv2.imread(img, 0)

    kernel = np.ones((25, 25), np.uint8)
    img = cv2.erode(img, kernel, iterations=2)
    # cv2.imshow('White Image', img)
    # cv2.waitKey(0)
    # threshold img
    ret, thresh = cv2.threshold(img, 127, 255, 0)

    # do distance transform
    dist = cv2.distanceTransform(thresh, distanceType=cv2.DIST_L2, maskSize=5)

    # set up cross for tophat skeletonization
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    skeleton = cv2.morphologyEx(dist, cv2.MORPH_TOPHAT, kernel)

    # threshold skeleton
    ret, skeleton = cv2.threshold(skeleton, 0, 255, 0)

    skel = np.uint8(skeleton)
    skeleton_contours, _ = cv2.findContours(skel, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    largest_skeleton_contour = max(skeleton_contours, key=cv2.contourArea)

    image_with_contours = np.zeros_like(img, dtype=np.uint8)
    cv2.drawContours(image_with_contours, [largest_skeleton_contour], -1, (255, 255, 0), 2)

    cv2.imwrite('static/segment/fish_segment.jpg', image_with_contours)

    length_object = get_longest_distance('static/segment/fish_segment.jpg')

    return int(round(length_object.value, 0))
