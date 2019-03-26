from bs4 import BeautifulSoup
import threading
import pandas as pd
from itertools import chain
from collections import defaultdict
import time
import multiprocessing
import sys

sem = threading.Semaphore()


def createMap(dic, tag):
    if not bool(dic):
        dic[str(tag.string)] = 1
    else:
        if dic.get(tag.string, 0):
            dic[str(tag.string)] = dic[str(tag.string)] + 1
        else:
            dic[str(tag.string)] = 1


def printToXml(dec, type):
    i = 1
    sem.acquire()
    column = []
    dic = {}
    for key, value in dec.iteritems():
        column.append(key)
    df = pd.DataFrame(dec, columns=column, index=[0])
    filename = type + ".csv"
    df.to_csv(filename)
    sem.release()


def count_direction(soup, type):
    dic = {}
    for tag in soup.findAll(type):
        createMap(dic, tag)
    printToXml(dic, type)


def CreateDataFrame(reason, list_rawData, i):
    rawData = {'mdn': 0, 'deviceID': 0, 'dialedNumber': 0, 'userAgent': 0, 'direction': 0, 'callType': 0,
               'failureTrigger': 0}
    for tag in reason[i].findAll():
        rawData[tag.name] = tag.string
    list_rawData.append(rawData)


def creatThreadToFillDataFrame(i, thread_list, reason, list_rawData):
    thread_list.append(threading.Thread(target=CreateDataFrame, args=(reason, list_rawData, i)))


def count_direction_service(soup, type):
    dicservice = {}
    for i in type:
        count = 0
        for tag in soup.findAll(i):
            count = count + 1
        dicservice[i] = count

    column = []
    dic = {}
    for key, value in dicservice.iteritems():
        column.append(key)
    df = pd.DataFrame(dicservice, columns=column, index=[0])
    filename = "service.csv"
    df.to_csv(filename)


if __name__ == "__main__":

    xmlformat = open(r"/home/erasunn/log.txt", "r").read()
    soup = BeautifulSoup(xmlformat, "xml")
    process_list = []
    service = ['FCD', 'DEFLECTION', 'CDIV', 'BARRING', 'DBL', 'MCID', 'CONF', 'COMWAIT', 'STOD', 'OIP', 'OIR', 'TIP',
               'TIR', 'CNIP', 'FIP', 'OCNIP', 'SSC', 'MCID', 'ABDIAL', 'CAC', 'CARRIER_SELECTvCARRIER_PRE_SELECT', 'CC',
               'FSFS', 'CUG',
               'UCD', 'IDPRES', '3PTY', 'SND', 'ANN', 'POLICING', 'ECT', 'CPC', 'PX', 'CAT', 'CR', 'HOTLINE', 'DNM',
               'MSN', 'DR', 'OCT']

    for i in range(0, len(sys.argv)):
        argList = sys.argv[i]
        process_list.append(multiprocessing.Process(target=count_direction, args=(soup, argList)))
        if (sys.argv[i] == "service"):
            process_list.append(multiprocessing.Process(target=count_direction_service, args=(soup, service)))
    for t in process_list:
        t.start()
    for t in process_list:
        t.join()