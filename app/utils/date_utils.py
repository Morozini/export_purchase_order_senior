from datetime import datetime
from typing import Optional

def br_date_to_date(value: Optional[str]):

    if not value:
        return None

    return datetime.strptime(value, "%d/%m/%Y").date()
