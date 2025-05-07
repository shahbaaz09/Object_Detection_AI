
# Object Detection Using YOLO and OpenCV

This project demonstrates real-time object detection using the YOLOv3 model with OpenCV and Python. It can detect multiple objects in images or webcam video streams with high accuracy.

## Features
- Real-time object detection
- Pre-trained YOLOv3 model
- Easy to run on both images and live webcam
- Simple and clean code

## Requirements
- Python 3.x
- NumPy
- OpenCV
- OpenCV-Contrib

## Installation

Clone the repository and install the required Python packages:

```bash
git clone https://github.com/shahbaaz09/object-detection-ai.git
cd object-detection-ai
pip install -r requirements.txt
```

## Usage

To detect objects in an image:

```bash
python detect.py --image test_images/sample.jpg
```

To detect objects from your webcam:

```bash
python detect.py --webcam
```

> Ensure the following files are in the project folder:
> - `yolov3.cfg`
> - `yolov3.weights`
> - `coco.names`

## Sample Output

You can find example images and output in the `results/` folder.

## Project Structure

```
object-detection-ai/
├── detect.py
├── yolov3.cfg
├── yolov3.weights
├── coco.names
├── test_images/
├── results/
├── requirements.txt
└── README.md
```

## License
This project is for educational and non-commercial use only.

## Author
**Shahbaaz**
- GitHub: [shahbaaz09](https://github.com/shahbaaz09)
- LinkedIn: [Your LinkedIn Here]
