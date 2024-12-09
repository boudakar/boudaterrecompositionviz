# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:32:52 2024

@author: pc
"""

import cv2
import t

# Charger le modèle YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Initialisation de la webcam
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    # Conversion de l'image pour YOLO
    results = model(frame)
    detections = results.pandas().xyxy[0]  # Résultats des détections

    for _, row in detections.iterrows():
        x1, y1, x2, y2, conf, cls, label = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax']), row['confidence'], int(row['class']), row['name']
        
        # Dessiner les boîtes de détection
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Détection d'objets en temps réel", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
