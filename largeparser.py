import sys, os
import csv

def writeToFile(fileName, data, isHeader=False):
    if isHeader:
        myFile = open(fileName, 'wb', encoding='utf-8')
    else:
        myFile = open(fileName, 'ab', encoding='utf-8')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerow(data)
    myFile.close()


file_name = sys.argv[1]
print "Start parsing {}".format(file_name)
csvHeaders = [
    'PC-ID_id',
    'PC_AssayDescription_name',
    'PC-AssayDescription_description_E'
]

## add header to csv file
x= file_name +".result1"
writeToFile(x, csvHeaders, True)
y= file_name +".result2"

cnt = 0
with open(file_name) as fp:
    PC_AssayDescription_description_E = ''
    PC_ID_id = ''
    PC_AssayDescription_name = ''
    for line in fp:
        if '<PC-ID_id>' in line:
            PC_ID_id = line.replace('<PC-ID_id>','').replace('</PC-ID_id>','').replace('\n','').strip()
            PC_AssayDescription_description_E = ''
            PC_AssayDescription_name = ''
            # print PC_ID_id
        elif '<PC-AssayDescription_name>' in line:
            PC_AssayDescription_name = line.eplace('<PC-AssayDescription_name>','').replace('</PC-AssayDescription_name>','').replace('\n','')
            # print PC_AssayDescription_name
        elif '<PC-AssayDescription_description_E>' in line:
            PC_AssayDescription_description_E += line.replace('<PC-AssayDescription_description_E>','').replace('</PC-AssayDescription_description_E>','').replace('\n','')
            # print PC_AssayDescription_description_E
        elif '</PC-AssayDescription>' in line:
            # output to csv file
            cnt += 1
            print cnt
            csvRow = [
                PC_ID_id,
                PC_AssayDescription_name,
                PC_AssayDescription_description_E
            ]
            writeToFile(y, csvRow, False)
print "Finish parsing, The result is {} and {}".format(x, y)
