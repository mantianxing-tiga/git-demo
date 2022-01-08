from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import jieba

def dictVec():
    """
    字典特征抽取: 将列表中每条字典数据特征值化
    """

    # 原始数据：列表里有多个字典
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

    # 实例化一个字典特征值工具类
    dctVec = DictVectorizer(sparse=False)   # sparse 默认为 True，以稀疏矩阵的形式存储，若要以完整矩阵格式存储，将其设为 False

    # 将原始数据转化为特征值
    output = dctVec.fit_transform(origin_data)
    
    print(output)


def countVec():
    """
    文本特征抽取: 对列表中每条文本数剧的单词数量进行统计
    """
    # 原始数据：列表里有多个文本
    origin_data = ['I love wang meng meng forever, she is my angle', 'I love physics and be good at quantum physics particularly']

    # 中文文本
    chinese_text_1 = ['我永远爱萌萌，他是我的天使', '我爱物理，而且尤其擅长于量子物理']

    # 手动空格分割的中文文本
    chinese_text_2 = ['我 永远 爱萌萌，他是我的 天使', '我爱 物理，而且尤其 擅长于 量子物理']

    # 实例化一个文本计数工具类
    cv = CountVectorizer()
    # 这个类没有设置 sparse 的选项，默认还是稀疏矩阵。
    # 如果要获取完整信息，因为数据是以 numpy 的数据形式存储的，可以利用 toarray 方法转化成矩阵


    # 文本数剧特征抽取
    output = cv.fit_transform(chinese_text_2)

    # 列索引
    print('列索引')
    print(cv.get_feature_names())

    print('矩阵值')
    print(output.toarray())


def chineseCountVec():
    """
    中文文本特征抽取: 对中文文本的词组进行计数
    """
    # 步骤概览：1.利用 jieba 进行文本分割 2.将分割好的文本作为输入数据 3.利用 CountVectorizer 进行特征抽取

    # 原始数据
    origin_data = [
        '我爱你，爱着你，就像老鼠爱大米',
        '我永远爱萌萌，他是我的天使',
        '我爱物理，而且尤其擅长于量子物理',
        '摆在西安人面前的最重要最主要的任务是团结一心众志成城共同支持抗疫实现早日解封是西安人的共同的最大利益需求'
    ]

    # 分割后的数据
    cutted_data = []

    for text in origin_data:
        content = list(jieba.cut(text)) # jieba 会输出一个生成器，我们可以将他直接转化为列表，列表的每个元素即为分割后的词语
        content_ = ' '.join(content)   # 将列表的元素拼接起来，以空格作为分隔符。所以这里我们生成了一个以空格作为词语分隔符的完整文本
        cutted_data.append(content_)

    print('*'*50)
    print('分割后的文本: ')
    print(cutted_data)
    
    # 实例化文本计数器
    cv = CountVectorizer()

    # 进行文本特征抽取
    output = cv.fit_transform(cutted_data)

    # 获取列索引
    print('列索引')
    print(cv.get_feature_names())

    print('矩阵值')
    print(output.toarray())




if __name__ == '__main__':
    # 调用字典特征抽取示例
    print('-'*50)
    print('字典特征抽取示例')
    dictVec()

    # 调用文本特征值抽取示例
    print('-'*50)
    print('文本特征抽取示例')
    countVec()

    # 调用中文文本特征抽取示例
    print('-'*50)
    print('中文文本特征抽取示例')
    chineseCountVec()