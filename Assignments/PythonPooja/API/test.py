import requests

BASE='http://127.0.0.1:5000/'

# response=requests.get(BASE+'hello')
# print(response.json())

# response=requests.post(BASE+'world')
# print(response.json())


# response=requests.get(BASE+'helloworld/bill')

data=[
    {'name':'hello','likes':10,'views':30},
    {'name':'title2','likes':20,'views':60},
    {'name':'title3','likes':30,'views':90},
]

# for i in range(len(data)):
#     response=requests.put(BASE+'video/'+str(i),data[i])
#     print(response.json())

# input()
# response=requests.delete(BASE+'video/1')
# print(response)
# input()

response=requests.get(BASE+'video/1')
print(response.json())
