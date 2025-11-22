# modules/time_utils.py

from datetime import datetime, timedelta

def get_today_jst():
    """
    サーバーがUTCでも、JST（UTC+9）の「今日の日付」を返す。
    """
    return (datetime.utcnow() + timedelta(hours=9)).date()
