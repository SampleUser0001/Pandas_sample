# -*- coding: utf-8 -*-
from logging import getLogger, config, DEBUG
import os

# import sys
from logutil import LogUtil

from importenv import ImportEnvKeyEnum
import unittest

from controller import ReadCSVController, ReadTSVController

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
LOG_CONFIG_FILE = ['config', 'log_config.json']

logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(os.path.join(PYTHON_APP_HOME, *LOG_CONFIG_FILE))
config.dictConfig(log_conf)
logger.setLevel(DEBUG)
logger.propagate = False

class TestReadCSVController(unittest.TestCase):
    def test_has_header(self):
        """CSVヘッダあり"""
        acctual = ReadCSVController.has_header(os.path.join(PYTHON_APP_HOME, 'datas', 'has_header.csv'))
        self.assertEqual(acctual, [['value1','value2']])
    
    def test_not_has_header(self):
        """CSVヘッダなし"""
        acctual = ReadCSVController.not_has_header(os.path.join(PYTHON_APP_HOME, 'datas', 'not_has_header.csv'))
        self.assertEqual(acctual, [['value1','value2']])

    def test_has_header_crlf(self):
        """CSVヘッダあり, CRLF"""
        acctual = ReadCSVController.has_header_crlf(os.path.join(PYTHON_APP_HOME, 'datas', 'has_header_crlf.csv'))
        self.assertEqual(acctual, [['value1','value2']])


class TestReadTSVController(unittest.TestCase):
    def test_has_header(self):
        """TSVヘッダあり"""
        acctual = ReadTSVController.has_header(os.path.join(PYTHON_APP_HOME, 'datas', 'has_header.tsv'))
        self.assertEqual(acctual, [['value1','value2']])
    
    def test_not_has_header(self):
        """CSVヘッダなし"""
        acctual = ReadTSVController.not_has_header(os.path.join(PYTHON_APP_HOME, 'datas', 'not_has_header.tsv'))
        self.assertEqual(acctual, [['value1','value2']])

    def test_has_header_crlf(self):
        """CSVヘッダあり, CRLF"""
        acctual = ReadTSVController.has_header_crlf(os.path.join(PYTHON_APP_HOME, 'datas', 'has_header_crlf.tsv'))
        self.assertEqual(acctual, [['value1','value2']])
