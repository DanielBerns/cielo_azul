from datetime import datetime, timezone, timedelta

CDR = -timedelta(hours=3)

def get_timestamp(separator: str = "", offset: timedelta = CDR) -> str:
    now = datetime.now(timezone(offset))
    timestamp = separator.join(
        [
            f"{now.year:4d}{now.month:02d}",
            f"{now.day:02d}{now.hour:02d}",
            f"{now.minute:02d}",
            f"{now.second:02d}",
        ]
    )
    return timestamp
 
