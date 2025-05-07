import cv2
import numpy as np

# Load the image
image_path = 'sample.jpg'  # Make sure this file is in the same directory
image = cv2.imread(image_path)

# Check if the image is loaded successfully
if image is None:
    print("Error: Image not found! Check the file path.")
    exit()

# Load YOLO model
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# Load class names
with open("coco.names", "r") as f:
    classes = f.read().strip().split("\n")

# Get image dimensions
height, width = image.shape[:2]

# Convert image to YOLO format
blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
net.setInput(blob)

# Get output layer names
layer_names = net.getUnconnectedOutLayersNames()
detections = net.forward(layer_names)

# Initialize lists for bounding boxes, confidences, and class IDs
boxes = []
confidences = []
class_ids = []

# Process detections
for detection in detections:
    for obj in detection:
        scores = obj[5:]  # Get confidence scores for all classes
        class_id = np.argmax(scores)  # Get the class with the highest confidence
        confidence = scores[class_id]

        if confidence > 0.5:  # Confidence threshold
            # Scale detection box back to image size
            center_x, center_y, w, h = (obj[0:4] * [width, height, width, height]).astype(int)
            x, y = int(center_x - w / 2), int(center_y - h / 2)
            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# Apply non-max suppression to remove duplicate boxes
indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

# Draw bounding boxes and labels if detections exist
if len(indices) > 0:
    for i in indices.flatten():
        x, y, w, h = boxes[i]
        label = f"{classes[class_ids[i]]}: {confidences[i]:.2f}"
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Display the final result
cv2.imshow('YOLO Object Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
