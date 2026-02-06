import cv2
from synthetic_field import generate_field
from vision_utils import detect_green, get_contours
from weed_detector import decide_action

USE_SYNTHETIC = True  # change to False when using camera

if USE_SYNTHETIC:
    frame = generate_field()
else:
    cap = cv2.VideoCapture(0)

while True:
    if not USE_SYNTHETIC:
        ret, frame = cap.read()
        if not ret:
            break

    frame = cv2.resize(frame, (640, 480))
    mask = detect_green(frame)
    contours = get_contours(mask)

    action = decide_action(frame, contours)

    cv2.putText(frame, f"ACTION: {action}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)

    cv2.imshow("Weed Robot Vision", frame)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
