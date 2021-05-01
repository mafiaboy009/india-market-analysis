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
        time.sleep(0.5)

    print( "Imported and stored data from Google Finance." )
    nseList.close()

    return