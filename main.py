import cv2
import pyvirtualcam

# Path to your video file
video_path = r''

# Open the video file
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Open virtual camera
with pyvirtualcam.Camera(width, height, fps, print_fps=True) as cam:
    print(f'Using virtual camera: {cam.device}')
    while True:
        ret, frame = cap.read()
        if not ret:
            # Restart video if it reaches the end
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = cap.read()
        # Convert frame to RGB (pyvirtualcam expects RGB)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Send frame to virtual camera
        cam.send(frame_rgb)
        cam.sleep_until_next_frame()
