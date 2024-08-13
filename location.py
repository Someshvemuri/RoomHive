import requests


def get_coordinates(place):
    url = f'https://api.tomtom.com/search/2/geocode/{place}.json'

    params = {
        'key': 'aGArnm6oXVRAGqBfiFCNpZaktp6OewMl',
        'query': place
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200 and data['summary']['numResults'] > 0:
        coordinates = data['results'][0]['position']
        return coordinates
    else:
        print('Error occurred:', data['status'])
        return None


#
# data = request.get_json()
# clgname = data['clgname']
# foodo = data['foodo']
# occ = data['occ']
# aco = data['aco']
# rangeo = data['rangeo']
# # clgname = request.args.get('clgname')
# # foodo = request.args.get('foodo')
# # occ = request.args.get('occ')
# # aco = request.args.get('aco')
# # rangeo = request.args.get('rangeo')
#
# api_key = 'aGArnm6oXVRAGqBfiFCNpZaktp6OewMl'
#
# coordinates = get_coordinates(api_key, clgname)
#
# if coordinates:
#     latitude = coordinates['lat']
#     longitude = coordinates['lon']
#
#
#     hotels = get_nearby_hotels(api_key, latitude, longitude)
#
#     hotel_list=[]
#     choices=['yes','no']
#     for hotel in hotels:
#         hotel_dict={}
#         hotel_dict['Name']=hotel['poi']['name']
#         hotel_dict['Address']=hotel['address']['freeformAddress']
#         hotel_dict['Price']=random.randint(1000,6000)
#         hotel_dict['AC']=random.choice(choices)
#         hotel_dict['Food']=random.choice(choices)
#         hotel_dict['Occupancy']=random.randint(1,3)
#         hotel_list.append(hotel_dict)
#         df = pd.DataFrame(hotel_list)
#         df.to_excel('hotels_list.xlsx', index=False)
#         df.to_csv('hotels_list.csv', index=False)
#
# df=pd.read_csv("hotels_list.csv")
# try:
#     if df.isna().sum().sum() != 0:
#         df = df.dropna()
# except:
#     print("Something went wrong when checking for null values")
#
# df['Occupancy'] = df['Occupancy'].astype(int)
#
# if foodo=="included":
#     f='yes'
# else:
#     f='no'
# if aco=="ac":
#     ac = 'yes'
# else:
#     ac = "no"
# o = int(occ)
# s1 = int(rangeo[0])*1000
# s2 = int(rangeo[-2])*1000
# condition = (df['Food'] == f) & (df['AC'] == ac) & (df['Occupancy'] >=o) & (df['Price'] <= s2) & (df['Price']>=s1)
# result = df[condition]
# not_result = df[~condition]
# condition1=(not_result['Price'] <= s2) & (not_result['Price'] >= s1)
# result1=not_result[condition1]
# not_result1=not_result[~condition1]
# List1=[]
# List2=[]
# List3=[]
# for i in range(0,len(result)):
#     s=result['Name'].values[i]
#     addrr=result['Address'].values[i].split(",")
#     addrr1=addrr[0:3]
#     straddrr1=",".join(addrr1)
#     wei=1
#     profit=result['Price'].values[i]
#     if result['Price'].values[i]>s1 and result['Price'].values[i]<s2:
#         wei+=1
#     if result['AC'].values[i]==ac:
#         wei+=1
#     if result['Food'].values[i]==f:
#         wei+=1
#     if result['Occupancy'].values[i]==o:
#         wei+=1
#     if result['AC'].values[i]=="yes":
#         profit+=1
#     if result['Food'].values[i]=="yes":
#         profit+=1
#     if result['Occupancy'].values[i]=="yes":
#         profit+=1
#     lis=[wei,profit,s,straddrr1,result['Price'].values[i],result['AC'].values[i],result['Food'].values[i],result['Occupancy'].values[i]]
#     List1.append(lis)
# print('loop completed')
# for i in range(0,len(result1)):
#     s=result1['Name'].values[i]
#     addrr=result1['Address'].values[i].split(",")
#     addrr1=addrr[0:3]
#     straddrr1=",".join(addrr1)
#     wei=1
#     profit=result1['Price'].values[i]
#     if result1['Price'].values[i]>s1 and result1['Price'].values[i]<s2:
#         wei+=1
#     if result1['AC'].values[i]==ac:
#         wei+=1
#     if result1['Food'].values[i]==f:
#         wei+=1
#     if result1['Occupancy'].values[i]==o:
#         wei+=1
#     if result1['AC'].values[i]=="yes":
#         profit+=1
#     if result1['Food'].values[i]=="yes":
#         profit+=1
#     if result1['Occupancy'].values[i]=="yes":
#         profit+=1
#     lis=[wei,profit,s,straddrr1,result1['Price'].values[i],result1['AC'].values[i],result1['Food'].values[i],result1['Occupancy'].values[i]]
#     List2.append(lis)
# for i in range(0,len(not_result1)):
#     s=not_result1['Name'].values[i]
#     addrr=not_result1['Address'].values[i].split(",")
#     addrr1=addrr[0:3]
#     straddrr1=",".join(addrr1)
#     wei=1
#     profit=not_result1['Price'].values[i]
#     if not_result1['Price'].values[i]>s1 and not_result1['Price'].values[i]<s2:
#         wei+=1
#     if not_result1['AC'].values[i]==ac:
#         wei+=1
#     if not_result1['Food'].values[i]==f:
#         wei+=1
#     if not_result1['Occupancy'].values[i]==o:
#         wei+=1
#     if not_result1['AC'].values[i]=="yes":
#         profit+=1
#     if not_result1['Food'].values[i]=="yes":
#         profit+=1
#     if not_result1['Occupancy'].values[i]=="yes":
#         profit+=1
#     lis=[wei,profit,s,straddrr1,not_result1['Price'].values[i],not_result1['AC'].values[i],not_result1['Food'].values[i],not_result1['Occupancy'].values[i]]
#     List3.append(lis)
#
# class Item:
#     def __init__(self, profit, weight, details):
#         self.profit = profit
#         self.weight = weight
#         self.details = details
#
# def Knapsack(W, arr):
#
#     arr.sort(key=lambda x: (x.profit/x.weight), reverse=True)
#
#     list_of_hotels=[]
#
#     for item in arr:
#
#         if item.weight <= W:
#             W -= item.weight
#             list_of_hotels.append(item.details)
#
#     return list_of_hotels
#
# cap=(s1+s2)/2
# if ac=="yes":
#     cap+=1
# if f=="yes":
#     cap+=1
# cap=cap+o
# cap1=5*cap
# def ArrFun(arr,l):
#     for i in l:
#         arr.append(Item(i[0],i[1],i[2:]))
#     return arr
# #print(List1,List2,List3)
# arr1=ArrFun([],List1)
# arr2=ArrFun([],List2)
# arr3=ArrFun([],List3)
# res=[]
# Suitable_result1 = Knapsack(cap1, arr1)
# res=res+Suitable_result1
# if len(Suitable_result1)<5:
#     cap2=(5-len(Suitable_result1))*cap
#     Suitable_result2 = Knapsack(cap2, arr2)
#     res = res + Suitable_result2
#     if len(Suitable_result1)+len(Suitable_result2)<5:
#         cap3=(5-len(Suitable_result1)+len(Suitable_result2))*cap
#         Suitable_result3 = Knapsack(cap3, arr3)
#         res=res+Suitable_result3
#         print(res)
# while len(res)>5:
#     res.pop(-1)
#     print(res)
# # res = []
# # df = pd.read_csv("hotels_list.csv")
# #
# # matching_rows = df[df.apply(lambda row: (row['Name']) in res, axis=1)]
# # df=pd.DataFrame(matching_rows)
# # print(matching_rows)
# #
# # df.to_csv('matching_hotels.csv', index=False)
# # # data = []
# # # with open('matching_hotels.csv', 'r') as csv_file:
# # #     csv_reader = csv.DictReader(csv_file)
# # #     for row in csv_reader:
# # #         data.append(row)
# # #     time.sleep(5)
# #
# #
# # return 'success'
