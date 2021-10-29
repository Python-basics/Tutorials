import requests
import pandas as pd
import pickle as pkl
import time, os, re
from keys import ameritrade



url = 'https://api.tdameritrade.com/v1/marketdata/quotes'

url = 'https://api.tdameritrade.com/v1/instruments'

symbols = 'AMD,F,GOOG'

df = pd.read_excel('company_list.xlsx')

symbols = df['Symbol'].values.tolist()

def look(file_name):
    file = open(file_name,'rb')
    info = pkl.load(file)
    file.close()
    return info

def load(f):
    points = ['symbol','Margin','PE','PEG','high52']
    
x = 5456
files = []
start = 0
end = 500
loop = 1
while start < x:
##    print(start, end)
    loop += 1
    tickers = ",".join(symbols[start:end])
##    print(tickers)
    payload = {'apikey':ameritrade,
           'symbol':tickers,
           'projection':'fundamental'}
    results = requests.get(url,params=payload)
    data = results.json()
    f_name = time.asctime() + '.pkl' 
    f_name = re.sub('[ :]','_',f_name)
    files.append(f_name)
    with open(f_name, 'wb') as file:
        pkl.dump(data,file)
##    file = open(f_name,'wb')
##    pkl.dump(data,file)
##    file.close()
##    print(f_name)
    time.sleep(1)
##    del data
    start = end
    end += 500
##start = end - 500
##end = x
##start = 2000
##end = x
##tickers = ",".join(symbols[start:end])
##payload = {'apikey':ameritrade,
##           'symbol':tickers,
##           'projection':'fundamental'}
##results = requests.get(url,params=payload)
##data = results.json()
##f_name = time.asctime().replace(' ','_') + '.pkl'
##f_name = f_name.replace(':','_')
##files.append(f_name)
##file = open(f_name,'wb')
##pkl.dump(data,file)
##file.close()

'''
symbol 'symbol'
price
Margin 'netProfitMarginMRQ'
pe 'peRatio'
peg 'pegRatio'
Name
Industary
52high 'high52'     
%of high 


'''

data = []
for file in files: # changed for new 
    with open(file,'rb') as f:
        info = pkl.load(f)

    tickers = list(info)
    points = ['symbol','netProfitMarginMRQ','peRatio','pegRatio','high52']
    for ticker in tickers:
##        print(ticker)
        tick = []
        for point in points:
            tick.append(info[ticker]['fundamental'][point])
##            print(point,tick)
        data.append(tick)
    os.remove(file)
points = ['symbol','Margin','PE','PEG','high52'] #  here
df_results = pd.DataFrame(data,columns=points) # here

file = time.asctime()[:10].replace(' ','_') + '.pkl'
df_results.to_pickle(file)
df_peg = df_results[(df_results['PEG'] < 1) & (df_results['PEG'] > 0) & (df_results['Margin'] > 20) & (df_results['PE'] > 10)]
df_peg['Growth'] = df_peg['PE']/df_peg['PEG']
order = [0,1,2,3,-1,-2]
df_peg = df_peg[df_peg.columns[order]]
##df_peg.set_index('symbol',inplace=True)
file = time.asctime()[:10].replace(' ','_') +'_peg.pkl'
df_peg.to_pickle(file)
##while True:
##    try:
##        df_peg.sort_values(['PEG'],inplace=True)
##        break
##    except:
##        pass

peg = df_peg.sort_values(['PEG'])
peg = peg.round(3)

def view(size,file=peg):
    start = 0
    stop = size
    while stop < len(file):
        print(file[start:stop])
        start = stop
        stop += size
    print(file[start:stop])

##view(40)

file = file[:-3]+'xlsx'

peg.to_excel(file,index=False)

##cur = pd.read_excel('peg-3-3-21.xlsx') # old with notes
cur = pd.read_excel('Current_Peg.xlsx') # new
cur = cur[['symbol','Action']]
new = pd.merge(peg,cur, on=['symbol'],how='left')
new.to_excel(file,index=False)
new.to_excel('Current_Peg.xlsx',index=False)
view(40,new)
##df_symbols = df_peg['symbol'].tolist()
##
##new = df['Symbol'].isin(df_symbols)
##
##companies = df[new]
##
##file = 'Jan_21_Picks.xlsx'
##
##companies.to_excel(file)



'''

df_symbols = df_peg['symbol'].tolist()

new = df['Symbol'].isin(df_symbols)

companies = df[new]

'''

##
##file = 'Sat_Oct_10_23_54_45_2020.pkl'
##stocks = look(file)
##
##start = 0
##end = 500
##symbols = ",".join(symbols[start:end])
##
##
##payload = {'apikey':key,
##           'symbol':symbols,
##           'projection':'fundamental'}
##
##results = requests.get(url,params=payload)
##
##data = results.json()
##print(data)
##for key in data["AA"]['fundamental']:
##    print(f"{key}: {data['AA']['fundamental']}")
'''

watch eminent possible purchase
watching close daily check
check  hasn't dropped enough weekly check

1) watch
2) watching
3) check

flat
weired
fund
gold
drug
volitile


too expensive
no options
'''

