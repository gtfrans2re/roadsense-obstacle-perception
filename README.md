# Obstacle Detection and Classification with YOLOv11

Real-time detection and classification of road and urban obstacles for autonomous navigation (vehicles and mobile robots).
MSc course project, **INF8790 – Foundations of Artificial Intelligence**, UQAM, Fall 2024.

**Authors:** Francois Gonothi Toure, Aliou Barry · **Supervisor:** Prof. Hakim Lounis

<p align="center">
  <img src="assets/confusion_matrix_normalized.png" width="48%">
  <img src="assets/BoxPR_curve.png" width="48%">
</p>

## What it does
Classic proximity sensors (LiDAR, ultrasound) tell a robot that something is there, not what it is. This project trains a YOLOv11 detector that recognises 10 obstacle types, so a navigation layer can react differently to a pedestrian, a pole or an open manhole.

**Classes:** Bicycle, Bus, Car, Dog, Electric pole, Motorcycle, Person, Traffic signs, Tree, Uncovered manhole.

## Results (validation set)
| Class | mAP@0.5 |
|---|---|
| Dog | 0.975 |
| Bus | 0.957 |
| Motorcycle | 0.943 |
| Bicycle | 0.942 |
| Uncovered manhole | 0.797 |
| Car | 0.740 |
| Tree | 0.738 |
| Person | 0.721 |
| Traffic signs | 0.688 |
| Electric pole | 0.546 |
| **All classes** | **0.805** |

- Pre-trained on COCO, fine-tuned for 200 epochs.
- Dataset: 8,251 original images, 21,546 after augmentation, annotated with bounding boxes.
- Qualitative test: a previously unseen 4-minute dashcam video from YouTube (not redistributed here, see disclaimer). Pedestrians, cars, electric poles, traffic signs and trees were detected reliably.

Training curves and settings are in `docs/results.csv` and `docs/args.yaml`.

## Quick start
```bash
git clone https://github.com/gtfrans2re/obstacle-detection-yolov11.git
cd obstacle-detection-yolov11
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python predict.py --source path/to/video.mp4
```
Annotated output is saved under `runs/predict*/`.

## Dataset
Not stored in the repo. Download link and details: [`data/README.md`](data/README.md).

## Limitations
- Weakest classes are electric poles (thin, often occluded), traffic signs and people.
- No dedicated truck class, so large vehicles can be confused with buses.
- Evaluation covers detection only; real-time navigation performance on a physical robot was not measured.
- The report also describes a decision layer (reinforcement learning with Prolog/JRules rules) and ROS simulation. This repository contains the **vision component only**. Targets in the report such as ">90% navigation success" are design goals, not measured results.

## Documentation
Full course report (French): [`docs/INF8790_report_FR.pdf`](docs/INF8790_report_FR.pdf).

## Disclaimer
The test video used for the qualitative evaluation comes from YouTube and is used for academic demonstration only. We hold no rights to it and do not redistribute it. Original: LINK_FROM_YOUR_POST.

## Acknowledgements
UQAM Département d'informatique, Prof. Hakim Lounis, and the Ultralytics YOLO project.

## License
MIT, see [LICENSE](LICENSE). Dataset terms: see `data/README.md`.
