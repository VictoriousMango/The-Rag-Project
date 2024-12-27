# Imports Libraries
import logging

'''
!Docstring
- This modules contains helper functions.
- Functionality includes:
    - File I/O operations (eg., loading PDFs, saving responses)
    - Logging and debugging utilities.
    - Timer functions for performances analysis.
'''

def Logger(logLevel, log) -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s: %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S',
        filename='Logs/Logs.log'
        )
    log_functions = {
      'debug': logging.debug,
      'info': logging.info,
      'warning': logging.warning,
      'error': logging.error,
      'critical': logging.critical,
      }
    if logLevel not in log_functions:
        log_functions["error"](f"Invalid log level: {logLevel}")
    else:
        log_functions[logLevel](log)

if __name__ == "__main__":
    Logger(log="Test", logLevel="debug")
    Logger(log="Test", logLevel="info")
    Logger(log="Test", logLevel="warning")
    Logger(log="Test", logLevel="error")
    Logger(log="Test", logLevel="critical")