import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

class LPConfig:
    N_CLASSES = 1

class ModelConfig:
    ROOT_DIR = Path(__file__).parent.parent
    MODEL_NAME = 'yolo and ocr'
    MODEL_WEIGHT_DETECTOR = ROOT_DIR / 'app' / 'models' / 'weights' / 'LP_detector.pt'
    MODEL_WEIGHT_OCR = ROOT_DIR / 'app' / 'models' / 'weights' / 'LP_ocr.pt'
    DEVICE = 'cpu'