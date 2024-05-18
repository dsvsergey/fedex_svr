from .celery_app import celery_app
import requests


@celery_app.task
def fetch_tracking_info(tracking_number):
    url = f"https://api.fedex.com/track/v1/trackingnumbers/{tracking_number}"
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers)
    return response.json()
