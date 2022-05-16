# pyconcd.py

from datetime import datetime

PYCON_DATE = datetime(year=2023, month=5, day=12, hour=8)
countdown = PYCON_DATE - datetime.now()
print(f"Countdown : {countdown}")