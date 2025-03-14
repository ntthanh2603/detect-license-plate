from pathlib import Path

class LoggingConfig:
    
    ROOT_DIR = Path(__file__).parent.parent

    LOG_DIR = ROOT_DIR / 'logs'

LoggingConfig.LOG_DIR.mkdir(parents=True, exist_ok=True)
