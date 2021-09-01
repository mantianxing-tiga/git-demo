from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import numpy as np

def dictvec():
    """
    特征化字典数据
    """

    origin_data = [
        {
            'City': 'Beijing',
            'temperature': 30
        },
        {
            'City': "Xi'an",
            'temperature': 34
        },
        {
            'City': "Shanghai",
            'temperature': 29
        }
    ]
    dct = DictVectorizer(sparse=False)
    data = dct.fit_transform(origin_data)
    print(dct.get_feature_names())

    return data

def normalization():
    """
    归一化处理
    :return: ndarray
    """
    origin_data = np.array(
        [
            [90, 2, 10, 40],
            [60, 4, 15, 45],
            [75, 3, 13, 46]
        ]
    )
    normal = MinMaxScaler(feature_range=(0,1))
    data = normal.fit_transform(origin_data)

    return data

def std():
    """
    标准化处理
    :return: ndarray
    """

    origin_data = [
        [1, -1, 3],
        [2, 4, 2],
        [4, 6, -1]
    ]
    standard = StandardScaler()
    data = standard.fit_transform(origin_data)

    return data


if __name__ == "__main__":
    # data = dictvec()
    # print(data)

    # data = normalization()
    # print(data)

    data = std()
    print(data)