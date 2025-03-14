# License Plate Recognition using YOLO and OCR

## 📌 Overview
This project implements an **Automatic License Plate Recognition (ALPR)** system using **YOLO (You Only Look Once)** for object detection and **OCR (Optical Character Recognition)** for text extraction. The system detects vehicle license plates in images or video streams and extracts the plate numbers.

## 🚀 Features
- Detects license plates in real-time using **YOLO**.
- Extracts plate numbers using **OCR (Tesseract/ EasyOCR)**.
- Supports video and image input.
- Exports results in a structured format (JSON, CSV).
- Can be integrated with security and traffic monitoring systems.



## 📂 Project Structure
```
📦 license-plate-recognition
├── 📂 models          # Pre-trained YOLO models
├── 📂 datasets        # Sample images/videos for testing
├── 📂 output          # Detected results and logs
├── detect.py         # Main script for license plate detection
├── ocr.py            # OCR processing script
├── requirements.txt  # Required dependencies
└── README.md         # Project documentation
```

## 🛠️ Model Details
- **YOLOv5/YOLOv8** is used for license plate detection.
- **Tesseract OCR/EasyOCR** is used for text extraction.
- Pretrained models are included in the `models/` directory or can be downloaded from external sources.

## 🎯 Applications
- Automatic Toll Collection 🚗
- Parking Lot Management 🅿️
- Traffic Law Enforcement 🚦
- Smart City Surveillance 🏙️

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing
Feel free to submit issues, fork the repository, and create pull requests!

## 📧 Contact
For questions or collaboration opportunities, contact: **tuanthanh2kk4@gmail.com**

