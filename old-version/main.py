# Author: Mafiaboy
# date: 25-Nov-2017

import csv

import datetime
import time

import getYahoo
import getGoogle

#import methods


def readBseList():
    today = datetime.datetime.now()
    print ("Reading and downloading stock info in progress and storing stock data from Google finance and Yahoo! Finance.")
    bseList = open( "./dataset/yahooFinance_bse_equity.csv", newline='' )
    bse_csv_data = csv.reader( bseList, delimiter=',', quotechar='"' )

    googleBseData = open("./dataset/googleBseData.csv", "w" )
    googleBseWriter = csv.writer( googleBseData, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    header = [ today ]
    googleBseWriter.writerow( header )
    header = ["StockName", "LastTrade", "LastHi", "Hi52", "LastLo", "Lo52", "EPS", "PE", "DivYield", "LastDiv", "NetProfitMargin", "OperatingMargin", "EBITDMargin", "ReturnOnAverageAssets", "ReturnOnAverageEquity", "ExchangeCode", "Exchange"]
    googleBseWriter.writerow( header )
    googleBseData.close()

    yahooBseData = open("./dataset/yahooBseData.csv", "w")
    yahooBseWriter = csv.writer(yahooBseData, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    header = [ today ]
    yahooBseWriter.writerow(header)
    # header = ["StockName", "LastTrade", "LastHi", "Hi52", "LastLo", "Lo52", "EPS", "PE", "DivYield", "LastDiv",
    #           "NetProfitMargin", "OperatingMargin", "EBITDMargin", "ReturnOnAverageAssets", "ReturnOnAverageEquity",
    #           "ExchangeCode", "Exchange"]
    header = ["StockName", "LastTrade", "LastHi", "Hi52", "LastLo", "Lo52", "BookValue", "EPS", "PE", "DivYield",
              "LastDiv", "NetProfitMargin", "OperatingMargin", "EBITDMargin", "ReturnOnAverageAssets", "ReturnOnAverageEquity",
              "ExchangeCode", "Exchange"]
    yahooBseWriter.writerow(header)
    yahooBseData.close()

    for row in bse_csv_data:
        row.append("BSE")
        print(row)
        stockName = getGoogle.getBseDataFromGoogle( row )
        getYahoo.getBseDataFromYahoo( row, stockName )
        time.sleep(0.5)

    print( "Imported and stored data from Google Finance." )
    bseList.close()

    return

def readNseList():
    today = datetime.datetime.now()
    print ("Reading and downloading stock info in progress and storing stock data from Google finance and Yahoo! Finance.")
    nseList = open( "./dataset/yahooFinance_nse_equity.csv", newline='' )
    nse_csv_data = csv.reader( nseList, delimiter=',', quotechar='"' )

    googleNseData = open("./dataset/googleNseData.csv", "w" )
    googleNseWriter = csv.writer( googleNseData, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    header = [ today ]
    googleNseWriter.writerow( header )
    header = ["StockName", "LastTrade", "LastHi", "Hi52", "LastLo", "Lo52", "EPS", "PE", "DivYield", "LastDiv", "NetProfitMargin", "OperatingMargin", "EBITDMargin", "ReturnOnAverageAssets", "ReturnOnAverageEquity", "ExchangeCode", "Exchange"]
    googleNseWriter.writerow( header )
    googleNseData.close()

    yahooNseData = open("./dataset/yahooNseData.csv", "w")
    yahooNseWriter = csv.writer(yahooNseData, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    header = [ today ]
    yahooNseWriter.writerow(header)
    # header = ["StockName", "LastTrade", "LastHi", "Hi52", "LastLo", "Lo52", "EPS", "PE", "DivYield", "LastDiv",
    #           "NetProfitMargin", "OperatingMargin", "EBITDMargin", "ReturnOnAverageAssets", "ReturnOnAverageEquity",
    #           "ExchangeCode", "Exchange"]
    header = ["StockName", "LastTrade", "LastHi", "Hi52", "LastLo", "Lo52", "BookValue", "EPS", "PE", "DivYield",
              "LastDiv", "NetProfitMargin", "OperatingMargin", "EBITDMargin", "ReturnOnAverageAssets", "ReturnOnAverageEquity",
              "ExchangeCode", "Exchange"]
    yahooNseWriter.writerow(header)
    yahooNseData.close()

    for row in nse_csv_data:
        row.append("NSE")
        print(row)
        stockName = getGoogle.getNseDataFromGoogle( row )
        getYahoo.getNseDataFromYahoo( row, stockName )
        time.sleep(0.25)

    print( "Imported and stored data from Google Finance." )
    nseList.close()

    return
# def readNseList():
#     __date__ = datetime.datetime.now()
#     print("Reading and Downloading stock info in progress...")
#     bse_csv_data = csv.reader(file('./dataset/bse_equity.csv'))
#     for row in bse_csv_data:
#         row.append("BSE")
#         cursor.execute( "INSERT INTO INDIA_SE_SCRIPS(BSE_SCRIP_CODE, ISIN_CODE, PRIMARY_EXCHANGE) VALUES(convert(%s,unsigned), %s, %s)",
#             row)
#     nse_csv_data = csv.reader(file('./dataset/nse_equity.csv'))
#     for row in nse_csv_data:
#         row.append("NSE")
#         cursor.execute("INSERT INTO INDIA_SE_SCRIPS(NSE_SCRIP_CODE, ISIN_CODE, PRIMARY_EXCHANGE) VALUES(%s, %s, %s)",
#                        row)
#     mydb.commit()
#     cursor.close()
#     print('INDIA_SE db created and populated')
#     return


__author__ = "MafiaBoy"
__startdate__ = "25Nov2017"
__date__ = datetime.datetime.now()
print( __date__ )
readBseList()
#readNseList()
#methods.convertYahooJsonToYahooCSV()

