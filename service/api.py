import argparse
import app
import service
from apscheduler.schedulers.background import BackgroundScheduler

def update_time():
    return 10

if __name__ == "__main__":
    deepface_app = app.create_app()
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=5000, help="Port of serving api")
    args = parser.parse_args()
    scheduler = BackgroundScheduler()
    scheduler.add_job(service.update_database, 'interval', seconds=update_time())
    scheduler.start()
    deepface_app.run(host="0.0.0.0", port=args.port)
