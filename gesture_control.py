
import cv2
import mediapipe as mp

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
RunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path="hand_landmarker.task"),
    running_mode=RunningMode.IMAGE,
    num_hands=1
)

cap = cv2.VideoCapture(0)

with HandLandmarker.create_from_options(options) as landmarker:
    while True:
        success, frame = cap.read()

        if not success:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb
        )

        result = landmarker.detect(image)
        gesture = "No gesture"

        for hand in result.hand_landmarks:
            height, width = frame.shape[:2]

            for point in hand:
                x = int(point.x * width)
                y = int(point.y * height)
                cv2.circle(frame, (x, y), 4, (0, 255, 0), -1)

            index_up = hand[8].y < hand[6].y
            middle_up = hand[12].y < hand[10].y
            ring_up = hand[16].y < hand[14].y
            pinky_up = hand[20].y < hand[18].y

            if index_up and middle_up and not ring_up and not pinky_up:
                gesture = "Next Slide"

            elif index_up and not middle_up and not ring_up and not pinky_up:
                gesture = "Previous Slide"

        cv2.putText(
            frame,
            gesture,
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow("Gesture Control", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()

