#!/usr/bin/python3

import os,sys
import json

def read(addressProduct, addressList):
    dataProduct = []
    dataList = []
    listInfor = []
    listTemp = []
    with open(addressProduct) as f:  #read product into dict list
        for line in f:
            dataProduct.append(json.loads(line))
    with open(addressList) as f:  #read list into dict list
        for line in f:
            dataList.append(json.loads(line))
    """
    Go over the list of dict and sotre manufacturer,  model
    and family.
    """
    for index in range(len(dataProduct)):
        if dataProduct[index].get("manufacturer"):
            listInfor.append(dataProduct[index]["manufacturer"])
        else:
            listInfor.append("empty")
        if dataProduct[index].get("model"):
            listInfor.append(dataProduct[index]["model"])
        else:
            listInfor.append("empty")
        if dataProduct[index].get("family"):
            listInfor.append(dataProduct[index]["family"])
        else:
            listInfor.append("empty")
    index = 0
    indexIn = 0
    """
    Go over the listInfor, and only store non-empty infor among manufacturer,
    model and family into a new list.
    """
    productNum = 0 # product number in list
    while index < len(listInfor):
        if listInfor[index] != "empty":
            listTemp.append(listInfor[index])
        if listInfor[index+1] != "empty":
            listTemp.append(listInfor[index+1])
        if listInfor[index+2] != "empty":
            listTemp.append(listInfor[index+2])
        """
        Final match with listings.txt file
        """
        while indexIn < len(dataList):
            if (len(listTemp) == 3):
                if (listTemp[0] in dataList[indexIn]["title"] and listTemp[1]
                in dataList[indexIn]["title"] and listTemp[2] in
                dataList[indexIn]["title"]):
                    newString = ("{\"product_name\":" + "\"" +
                    dataProduct[productNum]["product_name"] + "\"," +
                    str(dataList[indexIn])[1:])
                    newString = newString.replace("\'","\"" )
                    dataList.pop(indexIn)
                    with open('../TestCases/result.txt', 'a') as the_file:
                        the_file.write(newString+"\n")
            # when there are only 2 conditions to search
            """
            elif (len(listTemp) == 2):
                if (listTemp[0] in dataList[indexIn]["title"] and
                listTemp[1] in dataList[indexIn]["title"]):
                    #print(dataList[indexIn])
                    newString = ("{\"product_name\":" + "\"" +
                    dataProduct[productNum]["product_name"] + "\"," +
                    str(dataList[indexIn])[1:])
                    newString = newString.replace("\'","\"" )
                    with open('../TestCases/result.txt', 'a') as the_file:
                            the_file.write(newString+"\n")
                    dataList.pop(indexIn)
            """
            indexIn = indexIn + 1
        listTemp = [] #reset listTemp for next loop
        indexIn = 0 #reset indexIn in order to loop from beginning
        index = index + 3 # jump to the next produce for listInfor
        productNum = productNum + 1 #set product number in order to find it

def main(argv):
    read(argv[1], argv[2])

if __name__=="__main__":
    main(sys.argv)
