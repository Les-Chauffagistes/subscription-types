from datetime import datetime
from typing import Any
from typing import Literal
from dataclasses import dataclass

SubscriptionStatus = Literal["inactive", "active", "expired"]


@dataclass(frozen=True, slots=True)
class Subscription:
    pool_address: str
    started_at: datetime | None
    expires_at: datetime | None
    status: SubscriptionStatus
    created_at: datetime
    updated_at: datetime

    def to_dict(self) -> dict[str, Any]:
        return {
            "pool_address": self.pool_address,
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "expires_at": self.expires_at.isoformat() if self.expires_at else None,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
