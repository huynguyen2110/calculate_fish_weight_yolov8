from ultralytics import YOLO
import cv2
import numpy as np
from features.get_skeleton import get_skeleton
from features.calculate_weight import calculate_weight
from features.connect_database import connect_database
from features.get_number_and_total_weight import get_number_and_total_weight
from features.predict_on_images import predict_on_image, overlay, generate_number_fish_specific
from features.insert_into_database import insert_into_database


def predict(img):
    db = connect_database()
    img_path = img
    # Load a model
    model = YOLO('modules/best.pt')
    # load image by OpenCV like numpy.array
    img = cv2.imread(img)

    # predict by YOLOv8
    boxes, masks, cls, probs = predict_on_image(model, img_path, conf=0.55)

    image_copy = np.copy(img)

    image_with_contours = np.zeros_like(img, dtype=np.uint8)
    i = 0
    fish_array = []
    number_fish_specific = generate_number_fish_specific()
    total_weight = 0
    for mask_i in masks:
        class_name = model.names[cls[i]]
        i += 1
        image_with_masks = overlay(image_with_contours, mask_i, color=(255, 255, 255), alpha=1)

        # Saving the image
        cv2.imwrite(f'static/segment/object_{i}.jpg', image_with_masks)
        fish_length = get_skeleton(f'static/segment/object_{i}.jpg')
        fish_array.append(class_name)
        fish_array.append(fish_length)
        fish_weight = calculate_weight(fish_array)
        fish_array.append(fish_weight)
        total_weight += fish_weight
        number_fish_specific = get_number_and_total_weight(number_fish_specific, fish_array)
        fish_array.clear()

    insert_into_database(total_weight, number_fish_specific)
    cv2.imwrite(img_path, image_copy)
    return number_fish_specific
