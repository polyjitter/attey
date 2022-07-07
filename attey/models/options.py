from enum import Enum

class Mic(Enum):
    DISABLED = 1
    AVAILABLE = 2
    REQUIRED = 3

class NSFW(Enum):
    NO = 1
    YES = 2

class Visibility(Enum):
    PRIVATE = 1
    ASK_TO_JOIN = 2
    LOOKING_FOR_GAME = 3