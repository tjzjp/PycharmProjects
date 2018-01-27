import pandas as pd
from datetime import timedelta

# 使不换行
pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# def number_to16(number):
#     if int(number) != 551:
#         return 0
#     else:
#         return 1


# def t2s(t):
#     h, m, s = str(t).strip().split(":")
#     return int(h) * 3600 + int(m) * 60 + int(s)

# 判断是短中长
def number_to17(number):
    if number <= timedelta(seconds=60):
        return 0
    elif number <= timedelta(minutes=10):
        return 1
    else:
        return 2


if __name__ == "__main__":
    data = pd.read_table('C:/Users/13511/Desktop/test.txt', sep='\t', header=None, delim_whitespace=True)

    start = pd.to_datetime(data[9])
    end = pd.to_datetime(data[10])
    data[14] = pd.to_timedelta(end - start, unit='s')

    data[15] = data[9].str.split(':', expand=True)[0]

    print("每小时通话次数：")
    print(data[15].groupby(data[15]).count())

    # data[16] = data[6].map(number_to16)
    data[17] = data[14].map(number_to17)

    # print(data[17])

    print("每小时市话次数(1)、长途次数(2)和漫游次数(3)：")
    print(data[15].groupby([data[4]]).count())

    print("每小时短通话次数(0)、中通话次数(1)和长通话次数(2)：")
    print(data[15].groupby([data[15], data[17]]).count())

    # print(data)
