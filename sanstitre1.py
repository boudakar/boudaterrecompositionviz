import cv2
import numpy as np

# Initialiser la vidéo
cap = cv2.VideoCapture(0)

# Lire la première image et initialiser le détecteur de coins
_, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, maxCorners=100, qualityLevel=0.3, minDistance=7)

# Définir les paramètres de Lucas-Kanade
lk_params = dict(winSize=(15, 15), maxLevel=2,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

while True:
    _, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    # Sélectionner les points pour lesquels le suivi a réussi
    if p1 is not None:
        good_new = p1[st == 1]
        good_old = p0[st == 1]

        # Dessiner les pistes
        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            c, d = old.ravel()

            # Assurez-vous que les coordonnées sont des entiers
            a, b = int(a), int(b)
            c, d = int(c), int(d)

            cv2.line(frame, (a, b), (c, d), (0, 255, 0), 2)
            cv2.circle(frame, (a, b), 5, (0, 0, 255), -1)

    cv2.imshow("Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Mettre à jour les anciennes images et points
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1, 1, 2)

cap.release()
cv2.destroyAllWindows()
