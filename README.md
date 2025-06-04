# 👁️ Real-Time Computer Vision Projects

A collection of fun and practical real-time **Computer Vision** projects built with **Python**, **OpenCV**, and **MediaPipe**. These mini-applications use your webcam to detect colors, track human poses, trigger alerts, and even simulate invisibility!

Each project demonstrates a unique concept in the field of computer vision and can serve as a great introduction or demo for students, hobbyists, and developers.

---

## 🔍 Projects Overview

### 🕵️ 1. Imposter Alarm — *Intruder Detection with Email Alerts*

**Core Idea:** Use pose detection to sense human presence and trigger security responses.

* Detects a human body using **MediaPipe Pose**.
* Sends an alert email with a captured image if someone is detected.
* Emits continuous beeping as an audible alarm while the person is present.
* Avoids multiple alerts using threading and email-locking mechanisms.

---

### 🧥 2. Invisible Cloak — *Camouflage with Background Replacement*

**Core Idea:** Mask a specific color (red cloak) and replace it with the pre-captured background, simulating invisibility.

* Captures the background before any subject enters the frame.
* Masks the red-colored cloak using **HSV color thresholding**.
* Overlays the masked area with the background, making the cloak disappear.
* A visual illusion technique often seen in sci-fi movies.

---

### 🔴 3. Object Detection (Red Color) — *Simple Color-Based Detection*

**Core Idea:** Detect and highlight red-colored objects in real time.

* Uses HSV color space to isolate red hues.
* Applies masking to highlight the red regions in the webcam feed.
* Displays both the original feed and the color-detected output side by side.
* Great for learning about basic **color segmentation**.

---

### 🧍 4. Pose Detection — *Full-Body Landmark Tracking*

**Core Idea:** Detect and visualize human pose landmarks (like head, arms, legs) in real time.

* Implements **MediaPipe Pose** to extract 33 human body keypoints.
* Draws a skeletal structure based on these keypoints.
* Useful for applications in fitness tracking, gesture recognition, and motion analysis.

---

## 📦 Installation & Dependencies

Install the required libraries using:

```bash
pip install -r requirements.txt
```

> Recommended packages include: `opencv-python`, `mediapipe`, `numpy`.

For the **Imposter Alarm**, you must also create a `config.env` file (details below).

---

## 🚀 How to Run the Projects

Use the following commands:

```bash
python imposter_alarm.py
python invisible_cloak.py
python obj_detection.py
python pose_detect.py
```

* Make sure your **webcam is connected**.
* Press **`q`** in any window to exit.

---

## 🔐 Email Configuration (`config.env`)

Required only for `imposter_alarm.py`. Create a file named `config.env` in the root directory with:

```
SENDER_EMAIL=youremail@gmail.com
EMAIL_PASSWORD=yourpassword_or_app_password
RECEIVER_EMAIL=receiveremail@gmail.com
```

> ⚠️ **Security Tip:** Use **app passwords** or environment variables. Avoid exposing personal credentials.

---

## 📁 Project Structure

```
ComputerVisionProjects/
├── imposter_alarm.py           # Pose-based intruder alarm system
├── invisible_cloak.py          # Red cloak invisibility effect
├── obj_detection.py            # Red object color detection
├── pose_detect.py              # Real-time pose landmark visualization
├── config.env                  # Email credentials (user must create this)
├── requirements.txt            # Python dependencies
└── README.md                   # Project guide
```

---

## ✅ Notes & Tips

* Works best in **bright lighting** conditions.
* The **beep** sound alert uses `winsound` (Windows-only).
* The **email feature** requires internet access and SMTP settings (e.g., Gmail).
* Excellent for **educational demos**, **security prototypes**, and **fun experiments**.

---

## 📚 Learning Outcomes

Through these projects, you’ll explore:

* **OpenCV fundamentals** (frame capture, color spaces, masking).
* **MediaPipe APIs** for pose estimation.
* **Threading and event-based programming** in Python.
* **Basic image processing concepts** (morphology, bitwise operations).
* **Automation tools** like email alerts and sound cues.
