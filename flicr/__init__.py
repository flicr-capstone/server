import signal
import sys


def signal_handler(_sig, _frame):
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
