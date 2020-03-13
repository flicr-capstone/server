from enum import Enum


class PayloadType(str, Enum):
    GREET = "GREET"
    KEY_EVENT = "KEY_EVENT"
