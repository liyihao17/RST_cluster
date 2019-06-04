import Segmentation
import PCAPReader
import re
import copy
import pickle

def MessageCluster(message_list,split_list):
    """
    按照每个分词进行聚类
    :param message_list: 报文列表
    :param split_list: 分词列表
    :return: 聚类结果
    """
    cluster_result = []
    for i in range(len(split_list)):
        cluster_tmp_1 = []
        for j in range(len(split_list[i])):
            cluster_tmp_2 = []
            for k in range(len(message_list)):
                tmp = re.split(' |\:|\;|\=', str(message_list[k]).strip('[').strip(']'))
                if len(tmp) < i + 1:
                    continue
                if tmp[i] == split_list[i][j]:
                    cluster_tmp_2.append(message_list[k])
            cluster_tmp_1.append(cluster_tmp_2)
        cluster_result.append(cluster_tmp_1)
    return cluster_result

def DeleteRedun(cluster_result):
    """
    将聚类结果的冗余进行去除
    :param cluster_result:聚类结果
    :return: 聚类结果
    """
    cluster_result_tmp = copy.deepcopy(cluster_result)
    for i in range(len(cluster_result_tmp)):
        for j in range(len(cluster_result_tmp[i])):
            if len(cluster_result_tmp[i][j]) <= 9:
                cluster_result[i].remove(cluster_result_tmp[i][j])

    cluster_result_tmp = copy.deepcopy(cluster_result)
    for i in range(len(cluster_result_tmp)):
        if len(cluster_result_tmp[i]) == 0:
            cluster_result.remove(cluster_result_tmp[i])
    return cluster_result

def WriteBin(cluster_result):
    """
    将聚类结果写入二进制文件以便提取协议关键词使用
    :param cluster_result:聚类结果
    """
    for i in range(len(cluster_result)):
        filename = "result" + str(i) + ".bin"
        f = open(filename,"wb")
        pickle.dump(cluster_result[i], f)
        f.close()


if __name__ == '__main__':
    message_list = PCAPReader.ImportMessage()
    # result_split = SplitCluster(message_list,15)
    max_lenth = Segmentation.GetSplitMaxLen(message_list)
    split_list = Segmentation.AllSplitList(message_list,max_lenth)
    cluster_result = MessageCluster(message_list,split_list)
    cluster_result = DeleteRedun(cluster_result)
    WriteBin(cluster_result)
    for i in range(len(cluster_result)):
        print("")
        print("number " + str(i) + " cluster:")
        for j in range(len(cluster_result[i])):
            print("\n")
            for k in range(len(cluster_result[i][j])):
                print(cluster_result[i][j][k])
    # for i in range(len(cluster_result[0])):
    #     print("")
    #     for j in range(len(cluster_result[0][i])):
    #         print(cluster_result[0][i][j])