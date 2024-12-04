# Index Finger Box Challenge

## :star2: Description
In this interactive Python game, the player is tasked with positioning their index finger precisely inside a moving box. The game uses computer vision to detect the tip of the player's index finger and determine if it's within the box's boundaries. The box is displayed on the screen, and the player must ensure that the tip of their index finger is placed inside it.

## :flight_departure:	Getting Started
### :bangbang: Prerequisites
- [cv2](https://opencv.org/)
- [mediapipe](https://ai.google.dev/edge/mediapipe/solutions/guide)

## :dart: Game Flow:

### Initialization:

- The game starts with the display of a box at the top left of the screen.
- The camera is activated to detect the player's movements in real-time.
- The game uses `OpenCV` to track the position of the index finger using `MediaPipe` for hand-tracking algorithms.

### Objective:

- The player must position their index finger's tip inside the box that appears on the screen.
- The game continuously monitors the position of the index finger and determines if it is within the defined area of the box.

### Random Box Movement:

- After each successful detection of the index finger tip inside the box, the box moves to a new random location on the screen.
- The size of the box is smaller every times that player succesfully points inside the box, increasing the challenge of keeping the index finger inside it.

### Key Features:

- Real-time Finger Detection: Uses computer vision to accurately track the tip of the player's index finger.
- Dynamic Movement: The box randomly moves to different areas of the screen after each success, keeping the game exciting and unpredictable.
- This game is ideal for practicing hand-eye coordination and precision, all while having fun with an interactive interface.
