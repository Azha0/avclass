"""
    根据AVClass2生成的文件得出对应的4段式病毒名
"""

import sys
import time
import re
import csv


def GenerateVirusName(filepath):
    f = open('result.csv', 'w', newline="")
    f_csv = csv.writer(f)
    with open(filepath, "r") as inputFile:
        for line in inputFile.readlines():
            splitlist = line.split("\t")
            md5 = splitlist[0]
            engineCount = splitlist[1]
            if len(splitlist) > 2:
                virusInfo = splitlist[2]
                virusTypelist = re.findall(
                    re.compile(r"CLASS:[a-z]+\|[0-9]+,?"), virusInfo)
                if len(virusTypelist) >= 1:
                    virusFirstType = virusTypelist[0].split(":")[1].split("|")[0]
                else:
                    virusFirstType = "NULL"
                virusTypeStr = ""
                for virusType in virusTypelist:
                    virusTypeStr += virusType + ":"
                virusTypeStr = virusTypeStr[:-1]
                fileTypeList = re.findall(re.compile(r"FILE:os:[a-z]+\|[0-9]+,?"), virusInfo)
                if len(fileTypeList) >= 1:
                    fileType = fileTypeList[0].split(":")[2].split("|")[0]
                else:
                    fileType = "NULL"
                virusFamilyList = re.findall(re.compile(r"FAM:[a-z]+\|[0-9]+,?"), virusInfo)
                if len(virusFamilyList) >= 1:
                    virusFamily = virusFamilyList[0].split(":")[1].split("|")[0]
                else:
                    virusFamily = "NULL"
            else:
                virusFirstType = "NULL"
                virusTypeStr = "NULL"
                fileType = "NULL"
                virusFamily = "NULL"
            f_csv.writerow([md5, engineCount, virusFirstType, fileType, virusFamily, virusTypeStr])
    pass


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("请输入生成的labels的路径")
        sys.exit(1)
    else:
        startTime = time.time()
        filePath = sys.argv[1]
        print("输入文件: %s" % filePath)
        GenerateVirusName(filePath)
        endTime = time.time()
        print("执行时间: %s s" % (round(endTime - startTime, 2)))
    pass
