import logging
import azure.functions as func
import datetime

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
    logging.info(f'Timer trigger function ran at {utc_timestamp}')
