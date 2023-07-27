import os
import glob
import shutil
import yaml
from dotenv import load_dotenv
import logging
from logging.handlers import WatchedFileHandler
from datetime import datetime

#--------------- Prefixed Variables --------------#

JOB_TITLE_OF_INTEREST = ['Software Engineer', 'Machine Learning Engineer', 'Data Engineer', "Cloud Engineer", 'Data Analyst', "Quant"]

#----------- End of Prefixed Variables -----------#

#--------------- Logging utilities ---------------#
# Logger
logger = None

def create_log(path=None):
    '''Create a log file with default level at INFO.
    '''
    global logger

    if logger is not None:
        return logger

    if path is None:
        path = get_log_file_path()

    handler = WatchedFileHandler(os.environ.get("LOGFILE", path))
    formatter = logging.Formatter(logging.BASIC_FORMAT)
    handler.setFormatter(formatter)
    logger = logging.getLogger("PipelineLog")
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    return logger


def get_abs_root_path():
    '''Get absoulate root path.
    '''
    return os.path.abspath(os.path.dirname(__file__))


def get_log_file_path():
    '''Get log file path. Create one if not exist.
    '''
    current_date = datetime.now().strftime("%Y%m%d")
    logs_folder_path = os.path.join(get_abs_root_path(), r"../logs/")
    if not os.path.isdir(logs_folder_path):
        os.mkdir(logs_folder_path)  # create path if not found

    log_file_path = os.path.join(logs_folder_path, f"runtime_{current_date}.log")
    if not os.path.isfile(log_file_path):
        open(log_file_path, 'w').close()  # create file if not found

    return log_file_path


def get_logger():
    '''Create logger.
    '''
    global logger
    if logger is None:
        logger = create_log()
    return logger

#--------------- End of Logging utilities ---------------#

#---------------------------- Other utilities ----------------------------


def read_yaml() -> dict:
    """Read config.yml file.
    :return: a dictionary containing all configurations set in config.yml
    """
    with open(os.path.join(get_abs_root_path(), r'../config.yml'), 'r') as stream:
        try:
            get_logger().info(f"{get_current_datetime()}: Successfully read config.yml")
            return yaml.safe_load(stream)
        except yaml.YAMLError as e:
            get_logger().error(f"{get_current_datetime()}: Error while reading config.yml: {e}")


def read_sql_file(sql_path: str) -> str:
    """Read a SQL file into a string variable.
    :param sql_path: path to the SQL file.
    :return: a string variable containing content of the SQL file.
    """
    sql_code = ""
    try:
        with open(sql_path, 'r') as file:
            sql_code = file.read().upper()
    except Exception as e:
        get_logger().error(f"{get_current_datetime()}: Error while reading SQL file at path {sql_path}: {e}")
    return sql_code


def get_current_datetime():
    """Get current datetime in format of: Year-month-day hour-minute-second for logs.
    :return: current datetime.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


#---------------------------- End of Other utilities ----------------------------