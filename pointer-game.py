import cv2 as cv
import mediapipe as mp
import argparse
import random as rd

def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--device", type=int, default=0)
    parser.add_argument("--width", help='cap width', type=int, default=960)
    parser.add_argument("--height", help='cap height', type=int, default=540)

    parser.add_argument('--use_static_image_mode', action='store_true')
    parser.add_argument("--min_detection_confidence",
                        help='min_detection_confidence',
                        type=float,
                        default=0.7)
    parser.add_argument("--min_tracking_confidence",
                        help='min_tracking_confidence',
                        type=int,
                        default=0.5)

    args = parser.parse_args()

    return args

 
args = get_args()

cap_device = args.device
cap_width = args.width
cap_height = args.height

use_static_image_mode = args.use_static_image_mode
min_detection_confidence = args.min_detection_confidence
min_tracking_confidence = args.min_tracking_confidence

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, cap_width)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, cap_height)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
        static_image_mode=use_static_image_mode,
        max_num_hands=1,
        min_detection_confidence=min_detection_confidence,
        min_tracking_confidence=min_tracking_confidence,
    )


score = 0
previous_score = 0
box_x = 0
box_y = 0
big_size = 200

while True:
    # Process Key (ESC: end) #################################################
    key = cv.waitKey(10)
    if key == 27:  # ESC
        break

    ret, image = cap.read()

    image = cv.flip(image, 1)  # Mirror display
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    results = hands.process(image)

    image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
    image_height, image_width, _ = image.shape
    cv.putText(image, "Score : " + str(score), (int(image_width - 200), 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    if (score == 0):
        cv.rectangle(image, (0, 0), (big_size, big_size), (0, 255, 0), 3)
    if (score > 0):
        cv.rectangle(image, (box_x, box_y), (box_x + (big_size - (score * 2)), box_y + (big_size - (score * 2))), (0, 255, 0), 3)

    if results.multi_hand_landmarks is not None:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, connections=mp_hands.HAND_CONNECTIONS)
            pointer = hand_landmarks.landmark[8]
            x = int(pointer.x * image_width)
            y = int(pointer.y * image_height)
            if (x >= box_x and x <= box_x + (big_size - (score * 2)) and y >= box_y and y <= box_y + (big_size - (score * 2))):
                score = score + 1
                box_x = rd.randint(0, image_width - (big_size - (score * 2)))
                box_y = rd.randint(0, image_height - (big_size - (score * 2)))
                cv.rectangle(image, (box_x, box_y), (box_x + (big_size - (score * 2)), box_y + (big_size - (score * 2))), (0, 255, 0), 3)

            # for id, lm in enumerate(hand_landmarks.landmark):
            #     print(lm.x, lm.y)

    cv.imshow('Hand Gesture Recognition', image)

cap.release()
cv.destroyAllWindows()
       
