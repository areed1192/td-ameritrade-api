from enum import Enum


class OrderStatus(Enum):
    """Represents the different order status types
    when querying the `Orders` service.

    ### Usage
    ----
        >>> from td.utils.enums import OrderStatus
        >>> OrderStatus.Working.value
    """

    AwaitingParentOrder = 'AWAITING_PARENT_ORDER'
    AwaitingCondition = 'AWAITING_CONDITION'
    AwaitingManualReview = 'AWAITING_MANUAL_REVIEW'
    Accepted = 'ACCEPTED'
    AwaitingUrOut = 'AWAITING_UR_OUT'
    PendingActivation = 'PENDING_ACTIVATION'
    Queued = 'QUEUED'
    Working = 'WORKING'
    Rejected = 'REJECTED'
    PendingCancel = 'PENDING_CANCEL'
    Canceled = 'CANCELED'
    PendingReplace = 'PENDING_REPLACE'
    Replaced = 'REPLACED'
    Filled = 'FILLED'
    Expired = 'EXPIRED'
