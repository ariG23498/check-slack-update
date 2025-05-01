from dotenv import load_dotenv
import requests
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

load_dotenv()
slack_webhook_url = os.getenv("SLACK_WEBHOOK_URL")

def send_slack_message():
  payload = {"text": f"Hello World, I am Aritra"}
  try:
      response = requests.post(slack_webhook_url, json=payload)
      response.raise_for_status()
      logger.info("Slack message sent successfully")
  except requests.exceptions.RequestException as e:
      logger.error(f"Failed to send Slack message: {e}")

if __name__ == "__main__":
  send_slack_message()
