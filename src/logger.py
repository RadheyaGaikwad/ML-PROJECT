import logging
import os
from datetime import datetime

# Only create the 'logs' directory
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Build the full log file path
log_file = os.path.join(logs_dir, f"{datetime.now().strftime('%Y-%m-%d')}.log")

# Set up logging
logging.basicConfig(
    filename=log_file,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filemode='a'  # append mode
)

if __name__ == "__main__":
    logging.info("Logging has been set up successfully.")
    print(f"Log file created at: {log_file}")


