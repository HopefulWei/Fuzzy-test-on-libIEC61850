#!/usr/bin/python
# coding=utf-8
from __future__ import print_function
import datetime
import argparse
import logging
import socket
import struct
from copy import deepcopy

logging.basicConfig(filename='./fuzzer.log', filemode='w', level=logging.DEBUG, format='[%(asctime)s][%(levelname)s] %(message)s')
# logging模块用于打印日志，logging.basicConfig()函数实现打印日志的基础配置，其中filemode和file函数意义相同，指定日志文件的打开模式，'w'或'a' ，'a'表示不清空文件，并在指定位置添加日志记录语句；
#level表示设置日志级别；format表示输出格式
fp = open('RECEIVE.txt','wb+')  #  wb+  以二进制写方式打开,可以读、写文件

TIMEOUT = 5
PORT = 102

initate_request_1 = b'\x03\x00\x00\xbb\x02\xf0\x80\x0d\xb2\x05\x06\x13\x01\x00\x16\x01\x02\x14\x02\x00\x02\x33\x02\x00\x01\x34\x02\x00\x01\xc1\x9c'
initate_request_2 = b'\x31\x81\x99\xa0\x03\x80\x01\x01\xa2\x81\x91\x81\x04\x00\x00\x00\x01\x82\x04\x00\x00\x00\x01\xa4\x23\x30\x0f\x02\x01\x01\x06\x04\x52\x01\x00\x01\x30\x04\x06\x02\x51\x01\x30\x10\x02\x01\x03\x06\x05\x28\xca\x22\x02\x01\x30\x04\x06\x02\x51\x01\x61\x5e\x30\x5c\x02\x01\x01\xa0\x57'
initate_request_3 = b'\x60\x55\xa1\x07\x06\x05\x28\xca\x22\x02\x03\xa2\x07\x06\x05\x29\x01\x87\67\x01\xa3\x03\x02\x01\x0c\xa6\x06\x06\x04\x29\x01\x87\x67\xa7\x03\x02\x01\x0c\xbe\x2f\x28\x2d\x02\x01\x03\xa0\x28'
initate_request_4 = b'\xa8\x26\x80\x03\x00\xfd\xe8\x81\x01\x05\x82\x01\x05\x83\x01\x0a\xa4\x16\x80\x01\x01\x81\x03\x05\xf1\x00\x82\x0c\x03\xee\x1c\x00\x00\x04\x08\x00\x00\x79\xef\x18'
initate_request = initate_request_1 + initate_request_2 + initate_request_3 + initate_request_4

class MMS:

    def  __init__(self, TPKT, COTP, IEC_Presentation, SPDU, MMS_PDU):
        self.TPKT = TPKT
        self.COTP = COTP
        self.IEC_Presentation = IEC_Presentation
        self.SPDU = SPDU
        self.MMS_PDU = MMS_PDU

    def pack(self):
        A = []
        return self.TPKT+self.COTP+self.IEC_Presentation+self.SPDU+self.MMS_PDU


class TPKT:

    def  __init__(self, TPKT_version, TPKT_reserved, TPKT_length):
        self.TPKT_version = TPKT_version
        self.TPKT_reserved = TPKT_reserved
        self.TPKT_length = TPKT_length

    def pack(self):
        return self.TPKT_version + self.TPKT_reserved + self.TPKT_length


class COTP:

    def __init__(self, COTP_len, COTP_PDU_type):
        self.COTP_len = COTP_len
        self.COTP_PDU_type = COTP_PDU_type

    def pack(self):
        return self.COTP_len + self.COTP_PDU_type


class IEC_Presentation:

    def __init__(self, IEC_Presentation_1, IEC_Presentation_2):
        self.IEC_Presentation_1 =  IEC_Presentation_1
        self.IEC_Presentation_2 =  IEC_Presentation_2

    def pack(self):
        return self.IEC_Presentation_1 + self.IEC_Presentation_2

class SPDU:

    def __init__(self, SPDU_CPC, SPDU_length_1, SPDU_PDV, SPDU_length_2, SPDU_context_1, SPDU_context_2, SPDU_ASN, SPDU_length_3):
        self.SPDU_CPC =  SPDU_CPC
        self.SPDU_length_1 = SPDU_length_1
        self.SPDU_PDV = SPDU_PDV
        self.SPDU_length_2 = SPDU_length_2
        self.SPDU_context_1 = SPDU_context_1
        self.SPDU_context_2 = SPDU_context_2
        self.SPDU_ASN = SPDU_ASN
        self.SPDU_length_3 = SPDU_length_3

    def pack(self):
        return  self.SPDU_CPC+ self.SPDU_length_1 + self.SPDU_PDV + self.SPDU_length_2 + self.SPDU_context + self.SPDU_ASN + self.SPDU_length_3


class MMS_PDU:

    def __init__(self, MMS_ITAG, MMS_ITAG_length,invoke_ID_1,invoke_ID_2, MMS_LTAG, MMS_LTAG_length, MMS_LTAG_PDU):
        self.MMS_ITAG = MMS_ITAG
        self.MMS_ITAG_length = MMS_ITAG_length
        self.invoke_ID_1 = invoke_ID_1
        self.invoke_ID_2 = invoke_ID_2
        self.MMS_LTAG = MMS_LTAG
        self.MMS_LTAG_length = MMS_LTAG_length
        self.MMS_LTAG_PDU = MMS_LTAG_PDU

    def pack(self):
        return self.MMS_ITAG + self.MMS_ITAG_length + self.invoke_ID_1 + self.invoke_ID_2 + self.MMS_LTAG + self.MMS_LTAG_length + self.MMS_LTAG_PDU


def get_args():  # 该函数表示，返回从命令行输入的IP地址
    parser = argparse.ArgumentParser()  # python中的命令行解析模块 argparse
    parser.add_argument('-ip', metavar='<ip addr>', help='IP address', required=True)  # add_argument()方法，用来指定程序需要接受的命令参数 ；其中help表示参数命令的介绍
    args = parser.parse_args()
    return args

def hexstr(s):
    return '-'.join('%02x' % ord(c) for c in s) # '-'.join()表示对括号内的每一字符之间都加一个'-' ； ord（）函数以一个字符（长度为1的字符串）作为参数，返回对应的ASCII数值
#  % 表示输出格式化字符 %02x表示两位无符号整数(十六进制)；'%02x' % ord(c) for c in s表示对s 数组中的元素c均转化为ASCII数值并以两位无符号整数(十六进制)的形式进行输出；

def connect(ip, port, timeout):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket 起连接作用的库，和对象之间建立连接
        s.settimeout(timeout)
        s.connect((ip, port))
        return s
    except Exception as e:
        print("[--][%s] No connection with %s:%d. Exception: %s" % (datetime.datetime.now().strftime('%Y%m%d %H:%M:%S.%f'),ip, PORT, e))
        return s

def mutation(i):
    MMS_Mutation = []
    MMS_LTAG_PDU = b'\xa0\x03\x80\x01\x09\xa1\x02\x80\x00'

    MMS_LTAG_length = b'\x09'
    MMS_LTAG = b'\xa1'
    invoke_ID_2 = b'x\01\x01'
    invoke_ID_1 = b'\x02'
    MMS_ITAG_length = 14
    MMS_ITAG = b'\xa0'
    SPDU_length_3 = MMS_ITAG_length + 2
    SPDU_ASN = b'\xa0'
    SPDU_context_2 = b'\x01\x03'
    SPDU_context_1 = b'\x02'
    SPDU_length_2 = MMS_ITAG_length + 7
    SPDU_PDV = b'\x30'
    SPDU_length_1 = MMS_ITAG_length + 9
    SPDU_CPC = b'\x61'
    IEC_Presentation_2 = b'\x01\x00'
    IEC_Presentation_1 = b'\x01\x00'
    COTP_PDU_type = b'\xf0\x80'
    COTP_len = b'\x02'
    TPKT_length = SPDU_length_1 + 13
    TPKT_reserved = b'\x00'
    TPKT_version = b'\x03'

    MMS_Mutation.append(TPKT_version), MMS_Mutation.append(TPKT_reserved), MMS_Mutation.append(struct.pack(">H", TPKT_length)), MMS_Mutation.append(COTP_len)
    MMS_Mutation.append(COTP_PDU_type), MMS_Mutation.append(IEC_Presentation_1), MMS_Mutation.append(IEC_Presentation_2), MMS_Mutation.append(SPDU_CPC)
    MMS_Mutation.append(struct.pack(">B", SPDU_length_1)), MMS_Mutation.append(SPDU_PDV), MMS_Mutation.append(struct.pack(">B", SPDU_length_2))
    MMS_Mutation.append(SPDU_context_1), MMS_Mutation.append(SPDU_context_2), MMS_Mutation.append(SPDU_ASN), MMS_Mutation.append(struct.pack(">B", SPDU_length_3))
    MMS_Mutation.append(MMS_ITAG), MMS_Mutation.append(struct.pack(">B",MMS_ITAG_length)), MMS_Mutation.append(invoke_ID_1), MMS_Mutation.append(invoke_ID_2)
    MMS_Mutation.append(MMS_LTAG), MMS_Mutation.append(MMS_LTAG_length)

    if len(MMS_Mutation[i]) == 1:
        MMS_copy = []
        for j in range(255):
            MMS = MMS_LTAG_PDU
            MMS_Mutation[i] = struct.pack(">B", j)
            for k in range(len(MMS_Mutation)):
                k1 = len(MMS_Mutation) - k - 1
                MMS = MMS_Mutation[k1] + MMS
            MMS_copy.append(MMS)
        return MMS_copy

    elif len(MMS_Mutation[i]) == 2:
        MMS_copy = []
        for j in range(255*255):
            MMS = MMS_LTAG_PDU
            MMS_Mutation[i] = struct.pack(">H", j)
            for k in range(len(MMS_Mutation)):
                k1 = len(MMS_Mutation) - k - 1
                MMS = MMS_Mutation[k1] + MMS
            MMS_copy.append(MMS)
        return MMS_copy




def fuzz(ip):
    #if not s: return    # return之后，后面的代码就不会执行了
    mutation_bytes = ['TPKT_version', 'TPKT_reserved', 'TPKT_length', 'COTP_len', 'COTP_PDU_type', 'IEC_Presentation_1',
                      'IEC_Presentation_2', 'SPDU_CPC', 'SPDU_length_1', 'SPDU_PDV', 'SPDU_length_2',
                      'SPDU_context_1', 'SPDU_context_2', 'SPDU_ASN', 'SPDU_length_3', 'MMS_ITAG', 'MMS_ITAG_length',
                      'invoke_ID_1', 'invoke_ID_2', 'MMS_LTAG', 'MMS_LTAG_length']
    for count1 in range(2,len(mutation_bytes)) :
        mutations = mutation(count1)
        fp.write('[' + mutation_bytes[count1] + ']:' +  '\r\n')
        s = connect(ip, PORT, TIMEOUT)
        s.send(initate_request)
        rec = s.recv(1024)
        fp.write('initate_response' + ' ： ' + rec + '\r\n')
        for count2 in range(len(mutations)):
            try:
                print(mutation_bytes[count1],count2)
                s.send(mutations[count2])
                rec = s.recv(2048)  # socket.recv(bufsize[, flags])，从socket接收数据，注意是byte类型，bufsize指定一次最多接收的数据大小，单位是byte；
                if len(rec) == 0:
                    logging.exception("[--][%s]No Receive in application layer with %s:%d,send_data:[%s]" % (datetime.datetime.now().strftime('%Y%m%d %H:%M:%S.%f'),ip, PORT,hexstr(mutation_bytes[count1])))
                else:
                    rec = hexstr(rec)
                s_count2 = str(count2)
                fp.write(s_count2 +' ： '+ rec + '\r\n')
            except Exception as e:
                s.close()
                logging.exception("[--][%s]Receive was error with %s:%d. Exception: %s,send_data:[%s]" % (datetime.datetime.now().strftime('%Y%m%d %H:%M:%S.%f'),ip, PORT, e,hexstr(mutation_bytes[count1])))
                s = connect(ip, PORT, TIMEOUT)
        s.close()

def test():
    args = get_args()
    s = connect(args.ip, PORT, TIMEOUT)

    MMS_pdu = MMS_PDU(MMS_ITAG=b'\xa0', MMS_ITAG_length=b'\x0e', invoke_ID_1=b'\x02', invoke_ID_2=b'x\01\x01',MMS_LTAG=b'\xa1', MMS_LTAG_length=b'\x09', MMS_LTAG_PDU=b'\xa0\x03\x80\x01\x09\xa1\x02\x80\x00')
    MMS_pdu_packet = MMS_pdu.pack()
    MMS_ITAG_length = 0x0e

    Spdu = SPDU(SPDU_CPC=b'\x61', SPDU_length_1=struct.pack(">B",MMS_ITAG_length + 9), SPDU_PDV=b'\x30', SPDU_length_2=struct.pack(">B",MMS_ITAG_length + 7), SPDU_context_1=b'\x02', SPDU_context_2=b'\x01\x03', SPDU_ASN=b'\xa0', SPDU_length_3=struct.pack(">B",MMS_ITAG_length + 2))
    Spdu_packet =Spdu.pack()
    SPDU_length_1 = MMS_ITAG_length + 9

    IEC_presentation = IEC_Presentation(IEC_Presentation_1 = b'\x01\x00', IEC_Presentation_2 = b'\x01\x00')
    IEC_presentation_packet = IEC_presentation.pack()

    cotp = COTP(COTP_len = b'\x02', COTP_PDU_type = b'\xf0\x80')  #b'\xf0\x80'
    cotp_packet = cotp.pack()

    tpkt = TPKT(TPKT_version = b'\x03', TPKT_reserved = b'\x00\x00', TPKT_length = struct.pack(">B",SPDU_length_1 + 13))  #b'\x9D\x7F')
    tpkt_packet = tpkt.pack()

    mms = MMS(TPKT = tpkt_packet,COTP = cotp_packet, IEC_Presentation = IEC_presentation_packet, SPDU = Spdu_packet, MMS_PDU = MMS_pdu_packet)
    mms_packet = mms.pack()
    #print(hexstr(initate_request))
    for i in range(1):
        try:
            s.send(initate_request)
            rec1 = s.recv(1024)  # socket.recv(bufsize[, flags])，从socket接收数据，注意是byte类型，bufsize指定一次最多接收的数据大小，
            print(hexstr(rec1))
            s.send(mms_packet)
            rec2 = s.recv(1024)
            print(hexstr(rec2))
        except Exception as e:
            print("================================")
            print("[-] ]Receive was error with %s:%d. Exception: %s" % (args.ip, PORT, e))
        #finally:
            #s.close()
    s.close()
    print("fuzzer finished===========")

def main():
    args = get_args()
    fuzz(args.ip)
    print("fuzzer finished===========")


if __name__ == '__main__':
    main()
    #test()
    fp.close()
