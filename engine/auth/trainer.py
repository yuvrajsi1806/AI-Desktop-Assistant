import cv2

def AuthenticateFace():
    flag = 0

    # Load trained LBPH model
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('engine\\auth\\trainer\\trainer.yml')

    # Haar Cascade for face detection
    faceCascade = cv2.CascadeClassifier("engine\\auth\\haarcascade_frontalface_default.xml")
    font = cv2.FONT_HERSHEY_SIMPLEX

    # --- Registered users (IDs must match those used in sample.py) ---
    # Example: if you used face_id=1 → names[1] = "Yuvraj"
    names = ["Unknown", "Yuvraj"]

    # Start webcam
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640)  # width
    cam.set(4, 480)  # height

    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:
        ret, img = cam.read()
        if not ret:
            print("❌ Camera not available")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

            id_, confidence = recognizer.predict(gray[y:y+h, x:x+w])

            # Debug print
            print(f"DEBUG → ID={id_}, Confidence={confidence}")

            # ✅ Confidence threshold
            if confidence < 70:   # adjust if needed (try 60–75)
                name = names[id_] if id_ < len(names) else f"User{id_}"
                label = f"{name} ({round(confidence,2)})"
                flag = 1
            else:
                name = "Unknown"
                label = f"{name} ({round(confidence,2)})"
                flag = 0

            cv2.putText(img, label, (x+5, y-5), font, 1, (255,255,255), 2)

        cv2.imshow('Face Recognition', img)

        k = cv2.waitKey(10) & 0xff
        if k == 27 or flag == 1:  # ESC or recognized
            break

    cam.release()
    cv2.destroyAllWindows()
    return flag


if __name__ == "__main__":
    result = AuthenticateFace()
    if result == 1:
        print("✅ Access Granted")
    else:
        print("⛔ Access Denied")
