# StockData
Sym = "ATHN"
#create time bound variables
StartDate = '2017-11-28'
EndDate = '2017-12-05'
# write a class that contstructs the hyperlink below
from datetime import datetime
StartDate = datetime.strptime(StartDate,'%Y-%m-%d')
EndDate = datetime.strptime(EndDate,'%Y-%m-%d')

def APICallLInk (StartDate,EndDate,Sym)
    link = ('https://www.investopedia.com/markets/api/partial/historical/?Symbol='+Sym+'%Type=Historical+Prices&Timeframe=Daily&StartDate='
            +str(StartDate.month)+'+'+str(StartDate.day)+'%2C+'+str(StartDate.year)+'&EndDate='+str(EndDate.month)+'+'+str(EndDate.day)+'%2C+'+str(EndDate.year))
    return link;