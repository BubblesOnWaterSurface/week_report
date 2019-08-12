import datetime


# 获得当月周数
def get_week():
    week_mon_begin = datetime.datetime(y, m, 1).strftime("%w")
    # 当某月第一日是周六或者周日时，3号计算该月第一周数
    if week_mon_begin != 6 and week_mon_begin != 0:
        begin_day = 1
    else:
        begin_day = 3
    begin = int(datetime.datetime(y, m, begin_day).strftime("%W"))
    now_week = int(datetime.datetime.now().strftime("%W"))   # 40
    return int(now_week) - int(begin)


y = int(datetime.datetime.now().strftime("%Y"))
m = int(datetime.datetime.now().strftime("%m"))
y_l = int(datetime.datetime.now().strftime("%y"))
w = get_week()

