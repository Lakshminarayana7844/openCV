import cv2

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
slow_motion_writer = cv2.VideoWriter('slow_motion_video.mp4', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))
fast_motion_writer = cv2.VideoWriter('fast_motion_video.mp4', cv2.VideoWriter_fourcc(*'XVID'), 60, (width, height))

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow('Slow Motion Video', frame)
    slow_motion_writer.write(frame)
    cv2.waitKey(100)

    cv2.imshow('Fast Motion Video', frame)
    fast_motion_writer.write(frame)
    cv2.waitKey(10)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
slow_motion_writer.release()
fast_motion_writer.release()
cv2.destroyAllWindows()
