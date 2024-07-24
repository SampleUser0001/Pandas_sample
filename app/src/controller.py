# -*- coding: utf-8 -*-
from logging import getLogger, config, DEBUG
import os

# import sys
from logutil import LogUtil

import pandas as pd

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
LOG_CONFIG_FILE = ['config', 'log_config.json']

logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(os.path.join(PYTHON_APP_HOME, *LOG_CONFIG_FILE))
config.dictConfig(log_conf)
logger.setLevel(DEBUG)
logger.propagate = False

class ReadCSVController():
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def has_header(filepath) -> list:
        """CSVヘッダあり"""
        return pd.read_csv(filepath).values.tolist()
    
    @staticmethod
    def not_has_header(filepath) -> list:
        """CSVヘッダなし"""
        return pd.read_csv(filepath,header=None).values.tolist()

    @staticmethod
    def has_header_crlf(filepath) -> list:
        """CSVヘッダあり, CRLF"""
        return pd.read_csv(filepath).values.tolist()


class ReadTSVController():
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def has_header(filepath) -> list:
        """TSVヘッダあり"""
        return pd.read_csv(filepath, sep='\t').values.tolist()
    
    @staticmethod
    def not_has_header(filepath) -> list:
        """TSVヘッダなし"""
        return pd.read_csv(filepath, header=None, sep='\t').values.tolist()

    @staticmethod
    def has_header_crlf(filepath) -> list:
        """TSVヘッダあり, CRLF"""
        return pd.read_csv(filepath,  sep='\t').values.tolist()
