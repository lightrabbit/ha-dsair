from enum import Enum, IntEnum


class EnumCmdType(IntEnum):
    AIR_CAPABILITY_QUERY = 6
    AIR_RECOMMENDED_INDOOR_TEMP = 4
    AIR_SCENARIO_CONTROL = 32
    CONTROL = 1
    QUERY_SCENARIO_SETTING = 34
    QUERY_STATUS = 3
    SCENARIO_SETTING = 33
    STATUS_CHANGED = 2
    SYS_ACK = 1
    SYS_CHANGE_PW = 17
    SYS_CMD_RSP = 2
    SYS_CMD_TRANSFER = 40961
    SYS_CMD_TRANSFER_TARGET_QUIT = 40962
    SYS_ERR_CODE = 6
    SYS_GET_ROOM_INFO = 48
    SYS_GET_WEATHER = 7
    SYS_HAND_SHAKE = 40960
    SYS_LOGIN = 16
    SYS_QUERY_SCHEDULE_FINISH = 68
    SYS_QUERY_SCHEDULE_ID = 66
    SYS_QUERY_SCHEDULE_SETTING = 65
    SYS_SCENARIO_CONTROL = 67
    SYS_SCHEDULE_SETTING = 64
    SYS_SET_BASIC_ROOM_INFO = 49
    SYS_TIME_SYNC = 5


class EnumDevice(Enum):
    AIRCON = (8, 18)
    BATHROOM = (8, 24)
    GEOTHERMIC = (8, 19)
    HD = (8, 22)
    NEWAIRCON = (8, 23)
    SYSTEM = (0, 0)
    VENTILATION = (8, 20)


class FanDirection(IntEnum):
    FIX = 0
    STEP_1 = 1
    STEP_2 = 2
    STEP_3 = 3
    STEP_4 = 4
    STEP_5 = 5


class FanVolume(IntEnum):
    NO = 0
    FIX = 1
    STEP_2 = 2
    STEP_3 = 3
    STEP_4 = 4
    STEP_5 = 5
    STEPLESS = 7


class OutDoorRunCond(IntEnum):
    COLD = 2
    HEAT = 1
    VENT = 0
