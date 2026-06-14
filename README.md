# ♻️ End-to-End Waste Detection System using YOLOv11

## 📌 Overview

This project is an end-to-end waste detection system built using **YOLOv11**, **PyTorch**, **OpenCV**, and **Streamlit**. The model is trained on a custom waste dataset and deployed as a web application that allows users to upload images and automatically detect waste objects.

The project demonstrates the complete machine learning lifecycle including data ingestion, preprocessing, model training, evaluation, deployment, and inference.

---

## 🚀 Live Demo

🔗 **Deployed Application:**  
https://end-to-end-waste-detection-using-yolo-f4zpitwbadgblxxzfyc5ah.streamlit.app/

---

## ✨ Features

- Custom Waste Detection using YOLOv11
- Object Detection with Bounding Boxes
- Real-time Image Inference
- Streamlit Web Application
- Custom Dataset Training
- Model Evaluation
- Cloud Deployment

---

## 🛠️ Tech Stack

### Machine Learning
- Python
- PyTorch
- YOLOv11 (Ultralytics)

### Computer Vision
- OpenCV
- Pillow

### Deployment
- Streamlit
- GitHub

---

## 📂 Project Structure

```bash
End-To-End-Waste-Detection-Using-YOLO/
│
├── WasteDetection/
│   ├── components/
│   ├── constant/
│   ├── entity/
│   ├── exception/
│   ├── logger/
│   ├── pipeline/
│   └── utils/
│
├── templates/
├── models/
│   └── best.pt
│
├── streamlit_app.py
├── app.py
├── requirements.txt
├── setup.py
├── Dockerfile
└── README.md
```

---

## 📊 Dataset

The model was trained on a custom waste detection dataset containing multiple waste categories including:

- Organic Waste
- Plastic Waste
- Paper Waste
- Metal Waste
- Glass Waste
- Other Recyclable Materials

All annotations were prepared in YOLO format.

---

## 🧠 Model Training

### Training Configuration

| Parameter | Value |
|------------|------------|
| Model | YOLOv11 |
| Epochs | 50 |
| Image Size | 640 |
| Framework | Ultralytics |

---

## 📈 Performance Metrics

| Metric | Score |
|----------|----------|
| Precision | 59.5% |
| Recall | 34.7% |
| mAP@50 | 40.1% |
| mAP@50-95 | 29.4% |

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Karan2915/End-To-End-Waste-Detection-Using-YOLO.git

cd End-To-End-Waste-Detection-Using-YOLO
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Locally

```bash
streamlit run streamlit_app.py
```

Application will be available at:

```bash
http://localhost:8501
```

---

## 🔍 How It Works

1. Upload an image.
2. YOLOv11 processes the image.
3. Waste objects are detected.
4. Bounding boxes are drawn.
5. Predicted class labels and confidence scores are displayed.
6. Result image is returned to the user.

---

## 🎯 Sample Output

- Original Image
- Detected Waste Objects
- Bounding Boxes
- Confidence Scores

---

## 🔮 Future Improvements

- Webcam Detection
- Video Waste Detection
- Improved Dataset Quality
- Hyperparameter Tuning
- Docker Deployment
- AWS Deployment
- CI/CD Integration

---

## 👨‍💻 Author

**Karan Kumar**

- Data Scientist Intern at Sabudh Foundation
- Autonomous Systems Engineer – Team NIDAR
- AI, Computer Vision, Robotics & UAV Enthusiast

---

## ⭐ If you found this project useful

Please consider giving the repository a star.
