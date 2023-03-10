import pandas as pd
import logging
from logging.handlers import SysLogHandler

logging_destination_df = pd.read_csv(".\papertrail_log\logging_destination.txt", header=None)

PAPERTRAIL_HOST = "logs.papertrailapp.com" #str(logging_destination_df.iloc[0, 0])

PAPERTRAIL_PORT = 54829 #int(logging_destination_df.iloc[1, 0])


class LoggingToPapertrail(object):
    def __init__(self) -> None:
        self.logger = logging.getLogger("SnuistersLog")
        self.logger.setLevel(logging.DEBUG)
        handler = SysLogHandler(address=(PAPERTRAIL_HOST, PAPERTRAIL_PORT))
        self.logger.addHandler(handler)

    def critical(self, message: str) -> None:
        """Write log to Papertrail with 'critical-level"""
        self.logger.critical(message)

    def error(self, message: str) -> None:
        """Write log to Papertrail with 'error-level"""
        self.logger.error(message)

    def warning(self, message: str) -> None:
        """Write log to Papertrail with 'warning-level"""
        self.logger.warning(message)

    def info(self, message: str) -> None:
        """Write log to Papertrail with 'info-level"""
        self.logger.info(message)

    def debug(self, message: str) -> None:
        """Write log to Papertrail with 'debug-level"""
        self.logger.debug(message)


if __name__ == "__main__":
    log = LoggingToPapertrail()
    log.warning("warning")
