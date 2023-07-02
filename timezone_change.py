import datetime
import pytz


def timezone_change(time_str, src_timezone, dst_timezone=None, time_format=None):
    """"""
    if not time_format:
        time_format = "%Y-%m-% %H:%M:%S"

    # 将字符串转datetime形式
    old_dt =datetime.datetime.strptime(time_str,time_format)

    # 将源时区datetime转成GMT时区（UTC+0）的 datetime形式
    dt =pytz.timezone(src_timezone).localize(old_dt)
    utc_dt = pytz.utc.normalize(dt.astimezone(pytz.utc))

    # 将GMT datetime 转成指定目的地时区的datetime形式
    if dst_timezone:
        _timezone = pytz.timezone(dst_timezone)
        new_dt = _timezone.normalize(utc_dt.astimezone(_timezone))
    else:
        new_dt = utc_dt.astimezone()
    # 转化成字符串格式
    return new_dt.strftime(time_format)

def timezone_change_Ymd(time_str, src_timezone, dst_timezone=None, time_format=None):
    if not time_format:
        time_format = "%Y-%m-%d %H:%M:%S"

    # 将字符串转datetime形式
    old_dt = datetime.datetime.strptime(time_str, time_format)

    # 将源时区datetime转成GMT时区（UTC+0）的 datetime形式
    dt = pytz.timezone(src_timezone).localize(old_dt)
    utc_dt = pytz.utc.normalize(dt.astimezone(pytz.utc))

    # 将GMT datetime 转成指定目的地时区的datetime形式
    if dst_timezone:
        _timezone = pytz.timezone(dst_timezone)
        new_dt = _timezone.normalize(utc_dt.astimezone(_timezone))
    else:
        new_dt = utc_dt.astimezone()
    # 转化成字符串格式
    return new_dt.strftime(time_format)


