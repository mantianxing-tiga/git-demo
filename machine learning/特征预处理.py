from sklearn.preprocessing import MinMaxScaler,StandardScaler

def normalization():
    """
    将特征数据进行归一化处理
    """

    # 原始特征数据：随便给一个矩阵
    ori_vec = [
        [90, 80, 50, 30],
        [80, 200, 60, 50],
        [150, 60, 33, 59]
    ]

    print('原始数据')
    print(ori_vec)

    # 实例化一个缩放工具类
    mm = MinMaxScaler(feature_range=(0,1)) # feature_range 默认是 (0,1)，表示要将原始数据映射的目标区间

    # 进行数据转化
    output = mm.fit_transform(ori_vec)

    # 输出数据
    print('归一化数据')
    print(output)


def standardization():
    """
    标准化处理
    """

    # 原始特征数据：随便给一个矩阵
    ori_vec = [
        [90, 80, 50, 30],
        [80, 200, 60, 50],
        [150, 60, 33, 59],
        [600, 1, 52, 43]
    ]

    print('原始数据')
    print(ori_vec)

    # 实例化一个标准化工具类
    std = StandardScaler() # feature_range 默认是 (0,1)，表示要将原始数据映射的目标区间

    # 进行数据转化
    output = std.fit_transform(ori_vec)

    # 输出数据
    print('标准化数据')
    print(output)




if __name__ == '__main__':
    # 调用归一化示例
    normalization()

    # 调用标准化示例
    standardization()