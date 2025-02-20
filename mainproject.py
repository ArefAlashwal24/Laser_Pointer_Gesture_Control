import cv2
import mediapipe as mp
import pyautogui
import pygetwindow as gw
import keyboard
import time

# Initialize Mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(model_complexity=1, max_num_hands=2)  # Track up to 2 hands
mp_draw = mp.solutions.drawing_utils

# Screen size for mouse pointer mapping
screen_width, screen_height = pyautogui.size()

# Initialize variables
current_mode = "laser"  # Start in laser mode
previous_hand_positions = {"Left": None, "Right": None}
swipe_cooldown = {"Left": time.time(), "Right": time.time()}  # Cooldown timer for each hand
laser_pointer_activated = False

def detect_hand_type(hand_landmarks):
    """Determine if the detected hand is Left or Right."""
    handedness = results.multi_handedness
    if handedness:
        return handedness[0].classification[0].label  # 'Left' or 'Right'
    return None

def detect_swipe(hand, previous_position, current_position, threshold=50):
    """Detect swipe gestures based on horizontal movement."""
    if not previous_position or not current_position:
        return None

    delta_x = current_position[0] - previous_position[0]

    if hand == "Right" and delta_x > threshold:  # Swipe right with the right hand
        return "swipe_right"
    elif hand == "Left" and delta_x < -threshold:  # Swipe left with the left hand
        return "swipe_left"
    return None

def activate_laser_pointer_in_powerpoint():
    """Activate the PowerPoint window and enable laser pointer mode."""
    powerpoint_windows = [window for window in gw.getWindowsWithTitle("PowerPoint") if window.isActive]

    if powerpoint_windows:
        window = powerpoint_windows[0]
        window.activate()
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'l')
        print("Laser pointer mode activated in PowerPoint.")
    else:
        print("No active PowerPoint window found.")

# Start video capture
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("App started! Press 't' to toggle between laser and swipe modes.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    frame = cv2.flip(frame, 1)  # Flip for a mirrored view
    h, w, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)

    if keyboard.is_pressed('t'):
        if current_mode == "laser":
            current_mode = "swipe"
            laser_pointer_activated = False
        else:
            current_mode = "laser"
        print(f"Switched to {current_mode} mode")
        time.sleep(0.3)

    if current_mode == "laser" and not laser_pointer_activated:
        activate_laser_pointer_in_powerpoint()
        laser_pointer_activated = True

    if results.multi_hand_landmarks and results.multi_handedness:
        for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
            hand_type = results.multi_handedness[i].classification[0].label  # 'Left' or 'Right'
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get fingertip position
            fingertip_x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
            fingertip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y

            # Map fingertip position to screen size
            screen_x = int(fingertip_x * screen_width)
            screen_y = int(fingertip_y * screen_height)
            current_position = (screen_x, screen_y)

            if current_mode == "laser":
                # Laser pointer functionality
                pyautogui.moveTo(screen_x, screen_y)  # Move mouse pointer
                cv2.circle(frame, (int(fingertip_x * w), int(fingertip_y * h)), 10, (0, 0, 255), -1)  # Laser pointer
            elif current_mode == "swipe":
                # Swipe gesture functionality
                swipe_direction = detect_swipe(hand_type, previous_hand_positions[hand_type], current_position)
                if swipe_direction and time.time() - swipe_cooldown[hand_type] > 0.65:
                    if swipe_direction == "swipe_right":
                        pyautogui.hotkey("right")
                        print("Swiped right!")
                    elif swipe_direction == "swipe_left":
                        pyautogui.hotkey("left")
                        print("Swiped left!")
                    swipe_cooldown[hand_type] = time.time()  # Reset cooldown timer

            # Update previous hand position
            previous_hand_positions[hand_type] = current_position

    cv2.putText(frame, f"Mode: {current_mode.capitalize()}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("Laser and Swipe App", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()