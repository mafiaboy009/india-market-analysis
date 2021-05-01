import urllib
import json
import csv
from urllib.request import urlretrieve

def getBseDataFromYahoo( row, stockName ):
    filename = row[1]
    url_string = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/{0}?formatted=true&lang=en-IN&region=IN&modules=summaryProfile%2CfinancialData%2Cearnings%2CdefaultKeyStatistics&corsDomain=in.finance.yahoo.com".format(
        row[1])
    filename = "./dumps/yahoo/" + filename
    #filename1 = "./dumps/yahooJson/" + filename
    try:
        urllib.request.urlretrieve(url_string, filename)
        makeYahooJson( row )
        filename1 = "./dumps/yahooJson/" + str(row[0]).strip() + ".json"

        try:
            jsonFile = open(filename1, "r")
            jsonData = json.load(jsonFile)

            listedName = stockName
            exchange = "BSE"
            exchange_code = row[0]  # exchange scrip name

            try:
                bv = jsonData["quoteSummary"]["result"][0]["defaultKeyStatistics"]["bookValue"]["raw"]
            except:
                bv = 0.0

            try:
                priceToBook = jsonData["quoteSummary"]["result"][0]["defaultKeyStatistics"]["priceToBook"]["raw"]
            except:
                priceToBook = 0.0

            try:
                lastDiv = jsonData["quoteSummary"]["result"][0]["defaultKeyStatistics"]["lastDividendValue"]["raw"]
            except:
                lastDiv = 0.0

            try:
                ltt = jsonData["quoteSummary"]["result"][0]["financialData"]["currentPrice"]["raw"]
            except:
                ltt = 0.0

            try:
                totalCashPerShare = jsonData["quoteSummary"]["result"][0]["financialData"]["totalCashPerShare"]["raw"]
            except:
                totalCashPerShare = 0.0

            try:
                eps = jsonData["quoteSummary"]["result"][0]["financialData"]["revenuePerShare"]["raw"]
                # eps = jsonData["quoteSummary"]["result"][0]["defaultKeyStatistics"]["trailingEps"]["raw"]
            except:
                eps = 0.0

            try:
                ebitdMargin = jsonData["quoteSummary"]["result"][0]["financialData"]["ebitdaMargins"]["raw"]
            except:
                ebitdMargin = 0.0

            try:
                ebitda = jsonData["quoteSummary"]["result"][0]["financialData"]["ebitda"]["raw"]
            except:
                ebitda = 0.0

            try:
                returnOnAverageAssets = jsonData["quoteSummary"]["result"][0]["financialData"]["returnOnAssets"]["raw"]
            except:
                returnOnAverageAssets = 0.0

            try:
                returnOnAverageEquity = jsonData["quoteSummary"]["result"][0]["financialData"]["returnOnEquity"]["raw"]
            except:
                returnOnAverageEquity = 0.0

            try:
                netProfitMargin = jsonData["quoteSummary"]["result"][0]["financialData"]["profitMargins"]["fmt"]
            except:
                netProfitMargin = "0%"

            try:
                operatingMargin = jsonData["quoteSummary"]["result"][0]["financialData"]["operatingMargins"]["fmt"]
            except:
                operatingMargin = "0%"

            hi = 0
            hi52 = 0
            lo = 0
            lo52 = 0
            pe = 0
            divYield = 0

            #    print( row[0], bv, priceToBook, eps )#     print( listedName )
            #     print( exchange_code )
            #     print( exchange )
            #     print( eps )
            #     print( hi52 )
            #     print( lo52 )
            #     print( pe )
            #     print( netProfitMargin )
            #     print( operatingMargin )
            #     print( ebitdMargin)
            #     print( returnOnAverageAssets )
            #     print( returnOnAverageEquity )
            #

            stockData = [listedName, ltt, hi, hi52, lo, lo52, bv, eps, pe, divYield, lastDiv, netProfitMargin,
                         operatingMargin, ebitdMargin, returnOnAverageAssets, returnOnAverageEquity, exchange_code,
                         exchange]
            yahooBseData = open("./dataset/yahooBseData.csv", "a")
            yahooBseWriter = csv.writer(yahooBseData, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            yahooBseWriter.writerow(stockData)
            print(stockData)

            jsonFile.close()
        except:
            print( filename, "Not Found in Yahoo! Finance.")
    except:
        print(row[0],"does NOT exist in Yahoo! Finance.")
    return

def getNseDataFromYahoo():
    return

def makeYahooJson(row):
    print(row)
    try:
        filename1 = "./dumps/yahoo/" + str(row[1])
        inFile = open(filename1)
        jsonData = json.load(inFile)
        filename2 = "./dumps/yahooJson/" + str(row[0]).strip() + ".json"
        jsonFile = open(filename2, 'w')
        json.dump(jsonData, jsonFile, indent=2)
        jsonFile.close()
    except:
        print("Failed to convert.")
    return