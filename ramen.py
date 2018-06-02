#%%
#import相關library，並放入金鑰
import googlemaps 
import pandas as pd
import numpy as np

gmaps = googlemaps.Client(key="你的金鑰")

#建立一個包含台北市行政區的list
districts=["中正區","大同區","中山區","松山區","大安區","萬華區","信義區","士林區","北投區","內湖區","南港區","文山區"]

#以for loop，使用gmaps.geocode取得每個行政區的GPS位位址，搜尋以其為中心半徑2500m中符合的拉麵店家id，
#並append到變數ids中

ids=[]
for district in districts:
    geocode_result=gmaps.geocode(district)
    #以loc儲存該行政區座標
    loc = geocode_result[0]['geometry']['location']
    
       #將符合之拉麵店append進ids list之中
    for place in gmaps.places_radar(keyword="拉麵", location=loc, radius=2500)['results']:
        ids.append(place['place_id'])
#%%
ids
#%%
stores_info = []
# 去除重複的店家
ids = list(set(ids))
for id in ids:
    stores_info.append
    stores_info.append(gmaps.place(place_id=id, language='zh-TW')['result'])
np.array(stores_info)

#%%
output= pd.DataFrame.from_dict(stores_info)
output
#水平合併所需要的資訊
df_1 = output.loc[:, "formatted_address"]
df_2 = output.loc[:, "formatted_phone_number"]
df_3 = output.loc[:, "name"]
df_4 = output.loc[:, "rating"]

df = pd.concat([df_1, df_2, df_3, df_4], axis=1)
#取得店名
#%%

#選取rating>4之拉麵店
rating_df=df[df.loc[:,"rating"]>4]
#整理需要之資訊（地址、電話、國際電話、店名、評價），存入fixed_list中
fixed_df = rating_df[["formatted_address",
                      "name", "formatted_phone_number", "rating"]]

#將fixed_df中formatted_address，以.str.contains() function方式，以行政區的郵遞區號，選擇該行政區的拉麵店，在此以114內湖區為例
rating_df[fixed_df.formatted_address.str.contains("114")]
