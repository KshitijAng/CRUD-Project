from enum import Enum

class StatusEnum(str, Enum):
    """
    Represents lifecycle state of an item.
    """

    PENDING = "Pending"
    PROCESSING = "Processing"
    COMPLETED = "Completed"
    FAILED = "Failed"


class SourceEnum(str, Enum):
    """
    Represents where the item originated from.
    """

    CHAT = "CHAT"
    EMAIL = "EMAIL"
    API = "API"


class TenantEnum(str, Enum):
    """
    Represents where the item originated from.
    """

    GMAIL = "GMAIL"
    HIVERWEB = "HIVERWEB"
    OMNI = "OMNI"
