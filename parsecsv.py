import csv
import gzip
import os, sys

from itertools import dropwhile, takewhile

"""
def getstuff(filename, criterion):
    with open(filename, "rb") as csvfile:
        datareader = csv.reader(csvfile)
        yield next(datareader)  # yield the header row
        # first row, plus any subsequent rows that match, then stop
        # reading altogether
        # Python 2: use `for row in takewhile(...): yield row` instead
        # instead of `yield from takewhile(...)`.
        for row in takewhile(dropwhile(datareader)):
            yield row
        return
def getdata(filename, criteria):
    for criterion in criteria:
        for row in getstuff(filename, criterion):
            yield row
"""

# read content of zip file ".gz" file
def readZipfile(fileName):
    with gzip.open(fileName, 'rb') as f:
        file_content = f.read()
        return file_content

# read content of csv file
def readCSVfile(filename):
    file = open(filename, "r")
    file_content = file.read()
    file.close()
    return file_content

# out data to csv file
def writeToCSV(filename, data, isHeader=False):
    if isHeader == True:
        file = open(filename, 'w')
    else:
        file = open(filename, 'a')
    file.write(data)
    file.close()

# add # column to row
def process(fileContent, firstCol='', saveDir=''):
    if not os.path.isdir(saveDir):
        os.mkdir(saveDir)

    fileName = saveDir + "/" + firstCol + ".csvdata.csv"
    header ="Assay_Id,PUBCHEM_SID,PUBCHEM_CID,PUBCHEM_ACTIVITY_OUTCOME,PUBCHEM_ACTIVITY_SCORE,PUBCHEM_ACTIVITY_URL,PUBCHEM_ASSAYDATA_COMMENT,Assay_Value,Assay_Value_Label\n"
    writeToCSV(fileName, header, True)
    data = fileContent.split('\n')
    csvdata = ''

    #Assay_Value_Label
    headerValues = data[0].split(',')
    Assy_Value_Label = ''
    if len(headerValues)>7:
        Assy_Value_Label = headerValues[7]
    print Assy_Value_Label
    for i in range(1,len(data)):
        if data[i] != '' and data[i].split(',')[1] != '':
            values = data[i].split(',')
            dataline = ','.join(values[1:]) + ',' + Assy_Value_Label
            # csvdata += firstCol + ',' + dataline + '\n'
            writeToCSV(fileName, firstCol + ',' + dataline + '\n')
    # writeToCSV(fileName, csvdata)

"""
def process1(fileContent, firstCol='', saveDir=''):
    if not os.path.isdir(saveDir):
        os.mkdir(saveDir)
    fileName = saveDir + "/" + firstCol + ".csvdata.csv"
    header ="#,PUBCHEM_SID,PUBCHEM_CID,PUBCHEM_ACTIVITY_OUTCOME,PUBCHEM_ACTIVITY_SCORE,PUBCHEM_ACTIVITY_URL,PUBCHEM_ASSAYDATA_COMMENT,EC50\n"
    writeToCSV(fileName, header, True)
    # data = fileContent.split('\n')
    data = ''
    for i in range(6,len(fileContent)):
        data += firstCol + ',' + fileContent[i]
    writeToCSV(fileName ,data)
    # writeToCSV(fileName ,firstCol + ',' + fileContent[i] + '\n')
"""


if __name__ == '__main__':
    resourceDir = sys.argv[1] #"csvs"
    saveDir = sys.argv[2] #"savecsvs"
    # get all files of directory
    csvFileList = os.listdir(resourceDir)
    for name in csvFileList:
        print name
        firstCol = name.split('.')[0]
        # fileContent = readZipfile("/".join([resourceDir, name]))
        fileContent = readCSVfile("/".join([resourceDir, name]))
        process(fileContent=fileContent, firstCol=firstCol, saveDir=saveDir)
    print "convert finish"