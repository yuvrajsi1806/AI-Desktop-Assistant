import cv2
import os

def AuthenticateFace():
    flag = 0

    # Load trained model
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('engine\\auth\\trainer\\trainer.yml')

    # Haar Cascade for face detection
    cascadePath = "engine\\auth\\haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)
    font = cv2.FONT_HERSHEY_SIMPLEX

    # --- Load registered user names dynamically ---
    # You can edit this list manually if needed
    names = ["Yuvraj"]  
    names_dir = "engine\\auth\\samples"
    if os.path.exists(names_dir):
        for file in os.listdir(names_dir):
            try:
                # filename format: face.<id>.<count>.jpg
                id_str = file.split(".")[1]
                id_int = int(id_str)
                while len(names) <= id_int:
                    names.append("User" + str(len(names)))
            except:
                pass

    # Start camera
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640)  # width
    cam.set(4, 480)  # height

    # Minimum window size for face detection
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

            # ✅ Confidence check (lower = better)
            if confidence < 50:
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
