import sys


class Camp(object):
    """ Logging class help to predefine logs information. It's also place to
    store global logs strings
    """

    # global logs tags
    INFO_TAG = '[INFO]'
    WARNING_TAG = '[WARN]'
    TEST_TAG = '[TEST]'
    TAG_DELIMITER = '-------------------------------------------------------------------------'

    # specific messages
    PROCESS_COMPLETED = 'Process completed at'
    START_CREATING_PARTITIONS = 'Start creating partitions at '
    FINISH_CREATING_PARTITIONS = 'Finish creating partitions at '
    START_DROPPING_PARTITIONS = 'Start dropping partitions at '
    FINISH_DROPPING_PARTITIONS = 'Finish dropping partitions at '
    START_PROCESSING_OMNITURE = 'Start processing omniture requests at '
    FINISH_PROCESSING_OMNITURE = 'Finish processing omniture requests at '

    # technical and visual tags
    PYTHON_VERSION = sys.version
    PYTHON_LOGO = '                       ____        _   _                                        \n' \
                  '                      |  _ \ _   _| |_| |__   ___  _ __                         \n' \
                  '                      | |_) | | | | __|  _ \ / _ \|  _ \                        \n' \
                  '                      |  __/| |_| | |_| | | | (_) | | | |                       \n' \
                  '                      |_|    \__  |\__|_| |_|\___/|_| |_|                       \n' \
                  '              ===============|___/================================              '

    @staticmethod
    def welcome_message():
        print Camp.PYTHON_LOGO
        print Camp.INFO_TAG + ' ' + Camp.TAG_DELIMITER
        print Camp.PYTHON_VERSION
        print "Welcome to lumberjack! Thank's for using!"
        print Camp.INFO_TAG + ' ' + Camp.TAG_DELIMITER

    @staticmethod
    def display_python_logo():
        print Camp.PYTHON_LOGO

    @staticmethod
    def display_script_info():
        print Camp.INFO_TAG + ' ' + Camp.TAG_DELIMITER
        print Camp.PYTHON_VERSION
        print Camp.INFO_TAG + ' ' + Camp.TAG_DELIMITER

    @staticmethod
    def display_info_delimiter():
        print Camp.INFO_TAG + ' ' + Camp.TAG_DELIMITER

    @staticmethod
    def display_info_arg(info_arg, info_tag=INFO_TAG):
        print info_tag + ' ' + info_arg

    @staticmethod
    def display_info_args(info_message, info_value, info_tag=INFO_TAG):
        print info_tag + ' ' + info_message + ' ' + info_value
