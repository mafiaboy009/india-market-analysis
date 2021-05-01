# Author: Mafiaboy
# date: 25-Nov-2017

import csv
import getGoogle
import datetime
import time
import getYahoo

def readBseList():
    __date__ = datetime.datetime.now()
    print ("Reading and Downloading stock info in progress...")

    print("Fetching and storing stock data from Google finance.")
    bseList = open( "./dataset/yahooBseData.csv", newline='' )
    bse_csv_data = csv.reader( bseList, delimiter=',', quotechar='"' )

    googleBseData = open("./dataset/googleBseData.csv", "w" )
    googleBseWriter = csv.writer( googleBseData, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    header = [ __date__ ]
    googleBseWriter.writerow( header )
    header = ["StockName", "LastTrade", "LastHi", "Hi52", "LastLo", "Lo52", "EPS", "PE", "DivYield", "LastDiv", "NetProfitMargin", "OperatingMargin", "EBITDMargin", "ReturnOnAverageAssets", "ReturnOnAverageEquity", "ExchangeCode", "Exchange"]
    googleBseWriter.writerow( header )
    googleBseData.close()

    for row in bse_csv_data:
        row.append("BSE")
        #print(row)
        getGoogle.getBseDataFromGoogle( row )
        time.sleep(1)

    print( "Imported and stored data from Google Finance." )
    bseList.close()

    print("Fetching and storing stock data from Yahoo! finance.")
    bseList = open("./dataset/yahooFinance_bse_equity.csv", newline='')
    bse_csv_data = csv.reader(bseList, delimiter=',', quotechar='"')

    yahooBseData = open("./dataset/yahooBseData.csv", "w")
    yahooBseWriter = csv.writer(yahooBseData, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    header = [ __date__ ]
    yahooBseWriter.writerow( header )
    header = ["StockName", "LastTrade", "LastHi", "Hi52", "LastLo", "Lo52", "EPS", "PE", "DivYield", "LastDiv",
              "NetProfitMargin", "OperatingMargin", "EBITDMargin", "ReturnOnAverageAssets", "ReturnOnAverageEquity",
              "ExchangeCode", "Exchange"]
    yahooBseWriter.writerow(header)
    yahooBseData.close()

    for row in bse_csv_data:
        row.append("BSE")
        # print(row)
        getYahoo.getBseDataFromYahoo(row)
        time.sleep(1)

    print("Imported and stored data from Yahoo! Finance.")
    bseList.close()


    return

def readNseList():
    __date__ = datetime.datetime.now()
    print("Reading and Downloading stock info in progress...")
    bse_csv_data = csv.reader(file('./dataset/bse_equity.csv'))
    for row in bse_csv_data:
        row.append("BSE")
        cursor.execute(
            "INSERT INTO INDIA_SE_SCRIPS(BSE_SCRIP_CODE, ISIN_CODE, PRIMARY_EXCHANGE) VALUES(convert(%s,unsigned), %s, %s)",
            row)
    nse_csv_data = csv.reader(file('./dataset/nse_equity.csv'))
    for row in nse_csv_data:
        row.append("NSE")
        cursor.execute("INSERT INTO INDIA_SE_SCRIPS(NSE_SCRIP_CODE, ISIN_CODE, PRIMARY_EXCHANGE) VALUES(%s, %s, %s)",
                       row)
    mydb.commit()
    cursor.close()
    print('INDIA_SE db created and populated')
    return


__author__ = "MafiaBoy"
__startdate__ = "25Nov2017"
__date__ = datetime.datetime.now()
print( __date__ )
readBseList()

#readNseList()
#getNseDataFromGoogle()
#getNseDataFromYahoo()
