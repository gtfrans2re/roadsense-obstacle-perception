"""Run the trained obstacle detector on an image, a folder, a video or a webcam.

Usage:
    python predict.py --source path/to/video.mp4
    python predict.py --source path/to/images/ --conf 0.4
    python predict.py --source 0            # webcam
"""
import argparse
from ultralytics import YOLO


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--weights", default="weights/best.pt")
    p.add_argument("--source", required=True)
    p.add_argument("--conf", type=float, default=0.25)
    p.add_argument("--imgsz", type=int, default=640)
    p.add_argument("--show", action="store_true", help="display results live")
    a = p.parse_args()

    src = int(a.source) if a.source.isdigit() else a.source
    model = YOLO(a.weights)
    model.predict(source=src, conf=a.conf, imgsz=a.imgsz, save=True,
                  show=a.show, project="runs", name="predict")
    print("Results saved under runs/predict*/")


if __name__ == "__main__":
    main()
