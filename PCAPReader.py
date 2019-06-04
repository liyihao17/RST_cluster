from netzob.all import *
import copy

def ImportMessage():
    """
    将报文包导入,并输出原始报文包以及用-1补齐后的报文包
    :return: 原始报文包,用-1补齐后的报文包
    """
    message_session1 = PCAPImporter.readFile('ftp1.pcap').values()
    message_session2 = PCAPImporter.readFile('ftp2.pcap').values()
    message_session3 = PCAPImporter.readFile('ftp3.pcap').values()
    message_session4 = PCAPImporter.readFile('ftp4.pcap').values()
    message = message_session1 + message_session2 + message_session3 + message_session4

    message_session5 = PCAPImporter.readFile('http.pcap').values()
    message = message_session5
    symbol = Symbol(messages=message)

    #将pcap包中的内容转换为二维列表
    message_list_original = symbol.getValues()
    message_list_original_removelong = copy.deepcopy(message_list_original)

    for i in range(len(message_list_original_removelong)):
        if len(message_list_original_removelong[i]) > 1000:
            message_list_original.remove(message_list_original_removelong[i])

    # print('There is tottal ' + repr(len(message_list_original)) + ' messages')

    message_list_tmp = copy.deepcopy(message_list_original)
    for i in range(len(message_list_tmp)):
        if b'\r' in message_list_tmp[i]:
            message_list_tmp[i] = message_list_tmp[i].replace(b'\r',b' ')
        if b'\n' in message_list_tmp[i]:
            message_list_tmp[i] = message_list_tmp[i].replace(b'\n',b' ')
        if b'\r\n' in message_list_tmp[i]:
            message_list_tmp[i] = message_list_tmp[i].replace(b'\r\n',b' ')
        if b'\t' in message_list_tmp[i]:
            message_list_tmp[i] = message_list_tmp[i].replace(b'\t',b' ')
    message_list_tmp,message_list_original = message_list_original,message_list_tmp

    print("总共有" + str(len(message_list_original)) + "条报文")


    return message_list_original

if __name__ == '__main__':
    message_list= ImportMessage()
    print('original message is:')
    for i in range(len(message_list)):
        print(message_list[i])