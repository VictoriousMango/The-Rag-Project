# File imports
from core import preprocessor
from utils.utils import Logger

'''
!Docstring
- Tests for Preprocessor functions.
'''

def QueryPreprocessor():
    testCases = {
        "Hello World" : "hello world",
        "Python Programming " : "python programming",
        "TESTING CASES" : "testing cases",
        " Mixed CASE Input" : "mixed case input",
        "" : ""
    }
    count = 1
    for query, expected in testCases.items():
        if expected == preprocessor.QueryPreprocessor(query):
            Logger(
                log=f"Test Case {count} : PASS",
                logLevel="debug"
            )
        else:
            Logger(
                log=f"Test Case {count} : FAIL. Expected {expected} but got {QueryPreprocessor(query)}",
                logLevel="warning"
            )
        count += 1

if __name__ == "__main__":
    QueryPreprocessor()