from pathlib import Path
import logging
from datetime import datetime

def setup_logging():
    try:
        # Create logs directory in current working directory
        log_dir = Path.cwd() / "logs"
        log_dir.mkdir(exist_ok=True)
        
        # Configure log file path
        log_file = log_dir / f"{datetime.now().strftime('%Y-%m-%d')}.log"
        
        # Setup logging configuration
        logging.basicConfig(
            filename=str(log_file),
            format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO,
            filemode='w'
        )
        logging.info("Logging has been set up successfully.")
    except PermissionError:
        # Fallback to current directory if logs folder is not writable
        fallback_log = Path.cwd() / f"app_{datetime.now().strftime('%Y-%m-%d')}.log"
        logging.basicConfig(
            filename=str(fallback_log),
            format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO,
            filemode='w'
        )
        logging.warning(f"Could not write to {log_dir}, falling back to {fallback_log}")

