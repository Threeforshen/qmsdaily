import pandas as pd
import numpy as np


def opendata(path, number):
    df = pd.read_csv(path, usecols=[0, 1, number])
    list_test=df.values.tolist()

    print(list_test[16])
    print(list_test[17])
    print(list_test[38])
    print(list_test[39])
    print(list_test[40])
    print(list_test[41])
    print(list_test[42])
    print(list_test[43])
    print(list_test[45])
    print(list_test[46])
    print(list_test[47])
    print(list_test[50])


if __name__ == '__main__':
    path = r'D:/completed.csv'
    number = int(input('请输入列数：'))
    opendata(path, number)
    i = input('看完了吗？')
