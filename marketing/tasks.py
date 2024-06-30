import time
from celery import shared_task
import logging
# Configure logging
logger = logging.getLogger(__name__)
@shared_task(bind=True)
def send_emails(self):
    try:
        logger.info(f"Task {self.request.id} started")
        for x in range(5):
            logger.info(f"Sending email {x}")
            print(f"Sending email {x}")
            time.sleep(1)
        logger.info(f"Task {self.request.id} completed")
    except Exception as e:
        logger.error(f"Error in task {self.request.id}: {str(e)}")
        print(f"Error in task {self.request.id}: {str(e)}")