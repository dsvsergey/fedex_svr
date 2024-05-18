from celery import Celery

celery_app = Celery(
    "tasks", broker="redis://redis:6379/0", backend="redis://redis:6379/0"
)

celery_app.conf.update(
    result_expires=3600,
)

if __name__ == "__main__":
    celery_app.start()
