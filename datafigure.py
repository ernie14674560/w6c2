#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import pandas as pd
from matplotlib import pyplot as plt


def data_plot(file):
    df1 = pd.read_json(file, orient='value').groupby(by='user_id').sum()
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)  # 设置子图对象 ax
    x = df1.index.values
    y = df1['minutes'].values
    # 按要求绘制图像
    ax.set_title("StudyData")
    ax.set_xlabel("User ID")
    ax.set_ylabel("Study Time")
    ax.plot(x, y)

    # fig, axes = plt.subplots()  # nrows=0, ncols=0
    # ax = df1.reset_index().plot(x='user_id', y='minutes')  # ax=axes[0,0]
    plt.show()
    # 务必返回子图对象 ax
    return ax


if __name__ == '__main__':
    data_plot('user_study.json')
