import json
import urllib
from urllib.request import urlretrieve
import csv

def getBseDataFromGoogle( row ):
    stock_keyword = "BOM:" + str(row[0])

    url_string = "https://finance.google.com/finance?output=json&q={0}".format(stock_keyword)

    filename = "./dumps/google/" + str(row[0]) + ".txt"
    filename1 = "./dumps/googleJson/" + str(row[0]) + ".json"

    try:
        urllib.request.urlretrieve( url_string, filename )
    except:
        print("Failed to retrieve stock data.")

    createGoogleStdJson( filename, filename1 )
    listedName = "Unknown"

    #firmName = jsonData[0]["financials"][1]["f_type"]  # firm name
    try:
        inFile = open(filename1)
        jsonData = json.load(inFile)

        try:
            listedName = jsonData[0]["name"]
        except:
            listedName = "Unknown"
        try:
            exchange_code = jsonData[0]["t"]  # exchange scrip name
        except:
            exchange_code = 111111

        exchange = "BSE"
        try:
            eps = jsonData[0]["eps"]  # earnings per share
        except:
            eps = 0.0

        try:
            hi52 = jsonData[0]["hi52"]  # 52-week hi
        except:
            hi52 = 0.0

        try:
            lo52 = jsonData[0]["lo52"]  # 52-week lo
        except:
            lo52 = 0.0

        try:
            pe = jsonData[0]["pe"]  # price-to-earnings
        except:
            pe = 0.0

        try:
            ltt = jsonData[0]["l"]
        except:
            ltt = 0.0

        try:
            hi = jsonData[0]["hi"]
        except:
            hi = 0.0

        try:
            lo = jsonData[0]["lo"]
        except:
            lo = 0.0

        try:
            divYield = jsonData[0]["dy"]
        except:
            divYield = 0.0

        try:
            lastDiv = jsonData[0]["ldiv"]
        except:
            lastDiv = 0.0

        try:
            netProfitMargin = jsonData[0]["keyratios"][0]["annual"]
        except:
            netProfitMargin = 0.0

        try:
            operatingMargin = jsonData[0]["keyratios"][1]["annual"]
        except:
            operatingMargin = 0.0

        try:
            ebitdMargin = jsonData[0]["keyratios"][2]["annual"]
        except:
            ebitdMargin = 0.0

        try:
            returnOnAverageAssets = jsonData[0]["keyratios"][3]["annual"]
        except:
            returnOnAverageAssets = 0.0

        try:
            returnOnAverageEquity = jsonData[0]["keyratios"][4]["annual"]
        except:
            returnOnAverageEquity = 0.0

        googleBseData = open("./dataset/googleBseData.csv", "a")
        googleBseWriter = csv.writer(googleBseData, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        stockData = [ listedName, ltt, hi, hi52, lo, lo52, eps, pe, divYield, lastDiv, netProfitMargin, operatingMargin, ebitdMargin, returnOnAverageAssets, returnOnAverageEquity, exchange_code, exchange ]
        googleBseWriter.writerow( stockData )
        googleBseData.close()
    except:
        print( stock_keyword )

    return listedName

# def getNseDataFromGoogle():
#     for row in india_se_data:
#         exchange = row[0]
#         if exchange == "BSE":
#             stock_keyword = "BOM:" + str(row[2])
#             filename = str(row[2])
#         elif exchange == "NSE":
#             stock_keyword = "NSE:" + row[3]
#             filename = row[3]
#         else:
#             print('Error @ 28')
#             continue
#         outFile.write(filename + "\n")
#         url_string = "http://www.google.com/finance/info?infotype=infoquoteall&q={0}".format(stock_keyword)
#         filename1 = "/share/18/dataset/" + filename
#         filename = "/share/18/dataset/googleDumps/" + filename
#         count += 1
#         urllib.urlretrieve(url_string, filename)
#         if count % 20 == 0:
#             time.sleep(5)
#         non_stdJson = open(filename, 'r')
#         stdJson = open(filename1, 'w')
#         data = non_stdJson.read()
#         data = data.replace("/", "")
#         data = data.replace("[", "")
#         data = data.replace("]", "")
#         stdJson.write(data)
#     print("GoogleFinance data download COMPLETE. THANK YOU, Google!!")
#     return

def createGoogleStdJson( filename, filename1):
    try:
        nonStdJson = open( filename, 'r' )
        stdJson = open( filename1, 'w' )
        data = nonStdJson.read()
        data = data.replace("/", "")
        stdJson.write( data )
        stdJson.close()
    except:
        print("Google dumped file missing.")
    return