#Pyhotn  抓美股

#查詢美股線圖用

import datetime
import yfinance  as yf
import matplotlib.pyplot as plt


print("4隻被動收入推薦 KO,JNJ,MMM,PG")
print("科技，物流類推薦 COST,AMZN,AAPL,TSLA ")
print("月配息推薦O\n收月費公司DIS\nETF推薦 NOBL,VIG,VYMNOBL,VIG,VYM")
print("賣大麻的公司 PLNHF \n10隻被動收入推薦 XOM,MO,ENB,T,UVV,CVX,WEYS,PBCT,IBM,NNN")
print("--------------------")
print("請輸入美股英文代號，會顯示2018年1月1日到  今天  的線圖,若要結束請直接按 Enter ")
print("--------------------")
list1 = []
while input1 := input("請輸入美股代號,結束按 Enter"):
    list1.append(input1)
print(list1)
start = datetime.date(2020,1,1)
end = datetime.date.today()
codelist = list1
#・データの取得
# 抓美股的  data2 = yf.download(codelist, start=start, end=end)["Adj Close"]
data2 = yf.download(codelist, start=start, end=end)["Adj Close"]
print(data2.head().append(data2.tail()))
#・データをパーセント表記に変換
df_all = (1+ data2.pct_change()).cumprod()
print(df_all.head().append(df_all.tail()))
#・プロット
#倍率表記したい場合は
# df_all.plot(figsize=(10,6),fontsize = 10)
#株価で表示したい場合は
data2.plot(figsize=(7,5),fontsize=10)
plt.legend(bbox_to_anchor=(0,1) ,loc = "upper right", borderaxespad = 1, fontsize=13)
plt.grid(True)
plt.tight_layout()
plt.show()

