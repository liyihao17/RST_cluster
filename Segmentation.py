import re
import PCAPReader
import copy
#分割单词
def SplitCluster(message_list,seq_bytes):
    """
    将单词按照分隔符进行分割
    :param result:聚类结果
    :return: 单词分割后的聚类结果
    """
    result_split = []
    for i in range(len(message_list)):
        tmp = re.split(' |\:|\;|\=', str(message_list[i]).strip('[').strip(']'))
        if len(tmp) < seq_bytes + 1:
            continue
        if tmp[seq_bytes] != '' and tmp[seq_bytes] != "'" and tmp[seq_bytes] not in result_split:
            result_split.append(tmp[seq_bytes])
    return result_split

def GetSplitMaxLen(message_list):
    """
    获取最大的分词长度
    :param message_list:报文列表
    :return:最大分词长度
    """
    max_lenth = 0
    for i in range(len(message_list)):
        tmp = re.split(' |\:|\;|\=', str(message_list[i]).strip('[').strip(']'))
        if len(tmp) > max_lenth:
            max_lenth = len(tmp)
    return max_lenth


def AllSplitList(message_list,max_lenth):
    """
    将所有分词进行组合
    :param message_list: 报文列表
    :param max_lenth: 分词最大长度
    :return: 所有分词的列表
    """
    split_list = []
    for i in range(max_lenth):
        result_split = SplitCluster(message_list,i)
        if result_split == []:
            continue
        split_list.append(result_split)
    return split_list

if __name__ == '__main__':
    message_list = PCAPReader.ImportMessage()
    # result_split = SplitCluster(message_list,15)
    max_lenth = GetSplitMaxLen(message_list)
    split_list = AllSplitList(message_list,max_lenth)
    for i in range(len(split_list)):
        print(split_list[i])