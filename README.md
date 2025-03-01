# 🎯 Laser Pointer Gesture Control

🚀 A Python-based hand gesture recognition project that allows users to control PowerPoint slides and activate a laser pointer using a webcam. This project uses **OpenCV**, **MediaPipe**, and **PyAutoGUI** for real-time hand tracking and gesture-based interactions.

---

## ✨ Features
✅ **Hand gesture detection** for swiping slides left/right  
✅ **Laser pointer mode** activation using a button  
✅ **Automatic PowerPoint control** integration  
✅ **Uses OpenCV & MediaPipe for real-time hand tracking**  

---

## 📌 How It Works
This project uses a **webcam** to track **hand gestures** and translates them into **PowerPoint navigation commands**.

- 🖐 **Swipe Right (Right Hand)** → Move to the **next** PowerPoint slide  
- 🖐 **Swipe Left (Left Hand)** → Move to the **previous** PowerPoint slide  
- 🔴 **Press 'T' Button** → Toggle **Laser Pointer Mode**  

Once laser mode is activated, the **cursor follows the fingertip**, mimicking a real laser pointer.

---

## 🚀 Installation & Setup

### **1️⃣ Install Dependencies**
Before running the project, install the required libraries:
```bash
pip install opencv-python mediapipe pyautogui keyboard pygetwindow
If you want to use a requirements.txt file:

bash
Copy
Edit
pip install -r requirements.txt
2️⃣ Run the Program
bash
Copy
Edit
python mainproject.py
3️⃣ Use Gestures to Control PowerPoint
Make sure PowerPoint is open before running the script.
Press 'T' to switch between swipe and laser pointer mode.
Press 'Q' to quit the application.
🔧 Tech Stack
Python 🐍
OpenCV (for image processing) 📷
MediaPipe (for real-time hand tracking) ✋
PyAutoGUI (for simulating keyboard/mouse actions) ⌨️
PyGetWindow (for controlling active PowerPoint windows) 📊
🛠 Troubleshooting
⚠️ Common Issues & Fixes
❌ Error: No active PowerPoint window found
✅ Solution: Open PowerPoint before running the script.

❌ Camera is not opening
✅ Solution: Ensure no other application is using your webcam.

❌ Gestures not detected properly
✅ Solution: Make sure your hands are visible and well-lit.

🤝 Contributing
Feel free to fork this repository and submit a pull request if you want to improve the project! 🚀

📜 License
This project is open-source and available under the MIT License.
