# Задание 1. Логирование с использованием нескольких файлов
# Напишите скрипт, который логирует разные типы сообщений в разные файлы.
# Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
# WARNING и выше — в warnings_errors.log.


import logging

logger_info = logging.getLogger('Logger info and debug')
formatter = "%(asctime)s — %(name)s — %(levelname)s — %(message)s"
logger_info.setLevel(logging.DEBUG)

logger_info_file = logging.FileHandler('warnings_errors.log')
logger_info.addHandler(logger_info_file)
logger_info_file.setFormatter(logging.Formatter(formatter))
logger_info_file.setLevel(logging.WARNING)


logger_info_file = logging.FileHandler('debug_info.log')
logger_info_file.setFormatter(logging.Formatter(formatter))
logger_info.addHandler(logger_info_file)
logger_info_file.setLevel(logging.DEBUG)


logger_info.debug('debug msg!!!')
logger_info.warning('warning')
logger_info.info('info')
logger_info.critical('critical')
logger_info.error('error')


# def log_all():
#
#     logger.debug('Detailed information,
#     typically only of interest to a developer trying to diagnose a problem.')
#     logging.info('Confirmation that things are working as expected.')
#     logger.warning('An indication that something unexpected happened, '
#                    'or that a problem might occur in the near future'
#                    ' (e.g. ‘disk space low’).
#                    The software is still working as expected.')
#
#     logging.error('Due to a more serious problem,
#     the software has not been able to perform some function.')
#     logging.critical('A serious error, indicating that the program
#     itself may be unable to continue running.')
#
# logging.basicConfig(filename='project.log',level=logging.INFO)
# logging.getLogger('Main project file')
# logger.warning('Attention. We are using new functions from another module')


