from pandas_datareader import data as wb

tickers=['TSLA']
start_date='2021-1-1'
end_date='2021-6-1'

data=wb.DataReader(tickers, 'yahoo',start_date,end_date)  #.to_csv("Datos.csv")  #se puede definir la fecha de inicio y la fecha de fin separada por comas en el datareader [o solo una columna]
returns = data.pct_change() 
print(returns)

