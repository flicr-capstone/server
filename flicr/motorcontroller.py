import struct
from SGVHAK_Rover.lewansoul_wrapper import lewansoul_wrapper as LewanSoulWrapper

KEY_UP = "keyup"
KEY_DOWN = "keydown"

KEY_W = "KeyW"
KEY_S = "KeyS"
KEY_A = "KeyA"
KEY_D = "KeyD"

DRIVE_IDS = [20, 21, 22]
TURN_FRONT_ID = 23
TURN_BACK_ID = 24


class MotorController:
    _instance = None

    def __init__(self):
        self.axial = 0
        self.lateral = 0
        self.lsw = LewanSoulWrapper()
        self.lsw.connect()
        self.lsw.send(TURN_FRONT_ID, 29, (0, 0, 0, 0))
        self.lsw.send(TURN_BACK_ID, 29, (0, 0, 0, 0))

    @staticmethod
    def get_instance():
        if MotorController._instance is None:
            MotorController._instance = MotorController()
        return MotorController._instance

    def triage_key_event(self, key_event):
        axial_movement = 0
        lateral_movement = 0

        if key_event["code"] == KEY_W:
            axial_movement = 1
        elif key_event["code"] == KEY_S:
            axial_movement = -1
        elif key_event["code"] == KEY_A:
            lateral_movement = -1
        elif key_event["code"] == KEY_D:
            lateral_movement = 1

        if key_event["type"] == KEY_UP:
            axial_movement *= -1
            lateral_movement *= -1

        self.axial += axial_movement
        self.lateral += lateral_movement
        print(f"Axial {axial_movement}, Lateral {lateral_movement}")
        self.send_commands()

    def send_commands(self):
        for i in DRIVE_IDS:
            self.lsw.send(i, 29, bytearray(struct.pack("hh", 1, 500 * self.axial)))
        self.lsw.send(
            TURN_FRONT_ID,
            1,
            bytearray(struct.pack("hh", 500 + 100 * self.lateral, 500)),
        )
        self.lsw.send(
            TURN_BACK_ID,
            1,
            bytearray(struct.pack("hh", 500 + 100 * -self.lateral, 500)),
        )

    def unload(self):
        for i in DRIVE_IDS:
            self.lsw.send(i, 31, (0,))
        self.lsw.send(TURN_FRONT_ID, 31, (0,))
        self.lsw.send(TURN_BACK_ID, 31, (0,))
