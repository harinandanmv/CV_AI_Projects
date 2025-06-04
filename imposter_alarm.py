import mediapipe as mp
import cv2
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import winsound
import threading
import time

def load_env_file(filename):
    env_vars = {}
    with open(filename) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                env_vars[key] = value
    return env_vars

env = load_env_file("config.env")

sender_email = env["SENDER_EMAIL"]
password = env["EMAIL_PASSWORD"]
receiver_email = env["RECEIVER_EMAIL"]

# MediaPipe Pose setup
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

# OpenCV video capture
cap = cv2.VideoCapture(0)

# Thread control variables for beep
beep_thread = None
stop_beep = False

# Lock for sending email to avoid multiple sends at once
email_lock = threading.Lock()

def send_email_with_attachment(filename):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Human Detected - Intruder ALERT!!!"

    body = "An intruder was detected. See attached frame."
    message.attach(MIMEText(body, "plain"))

    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename={os.path.basename(filename)}",
    )
    message.attach(part)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
        winsound.Beep(1500, 500)  # Single beep after sending email
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        server.quit()

def email_sender_thread(frame):
    # Save frame to disk
    cv2.imwrite('saved_frame.jpg', frame)
    # Acquire lock to prevent multiple concurrent sends
    with email_lock:
        send_email_with_attachment('saved_frame.jpg')

def loop_beep():
    global stop_beep
    while not stop_beep:
        winsound.Beep(1000, 500)  # beep 500ms
        time.sleep(1)             # wait 1 second before next beep

sent_email = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)

    if results.pose_landmarks:
        mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        if not sent_email:
            # Start email sending in a separate thread to avoid freezing
            threading.Thread(target=email_sender_thread, args=(frame.copy(),), daemon=True).start()
            sent_email = True

        # Start beep thread if not running
        if beep_thread is None or not beep_thread.is_alive():
            stop_beep = False
            beep_thread = threading.Thread(target=loop_beep, daemon=True)
            beep_thread.start()

    else:
        # Stop beep thread if running
        stop_beep = True
        if beep_thread is not None and beep_thread.is_alive():
            beep_thread.join()
            beep_thread = None
        # Reset email flag to send again next time human appears
        sent_email = False

    cv2.imshow('Pose Estimation', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        stop_beep = True
        if beep_thread is not None and beep_thread.is_alive():
            beep_thread.join()
        break

cap.release()
cv2.destroyAllWindows()