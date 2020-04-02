import signal
import sys

from flicr.motorcontroller import MotorController


def signal_handler(_sig, _frame):
    MotorController.get_instance().unload()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
