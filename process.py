import json

test="""{
    "ret": 0,
    "info": "",
    "data": [
        {
            "date": "01.28",
            "city": "海口",
            "confirm": 7,
            "dead": 0,
            "heal": 0,
            "suspect": 0,
            "confirm_add": ""
        },
        {
            "date": "01.29",
            "city": "海口",
            "confirm": 9,
            "dead": 0,
            "heal": 0,
            "suspect": 0,
            "confirm_add": ""
        },
        {
            "date": "01.30",
            "city": "海口",
            "confirm": 9,
            "dead": 0,
            "heal": 0,
            "suspect": 0,
            "confirm_add": ""
        },
        {
            "date": "01.31",
            "city": "海口",
            "confirm": 9,
            "dead": 0,
            "heal": 0,
            "suspect": 0,
            "confirm_add": ""
        },
        {
            "date": "02.01",
            "city": "海口",
            "confirm": 11,
            "dead": 0,
            "heal": 0,
            "suspect": 0,
            "confirm_add": ""
        },
        {
            "date": "02.02",
            "city": "海口",
            "confirm": 11,
            "dead": 0,
            "heal": 0,
            "suspect": 0,
            "confirm_add": ""
        },
        {
            "date": "02.03",
            "city": "海口",
            "confirm": 13,
            "dead": 0,
            "heal": 0,
            "suspect": 0,
            "confirm_add": ""
        },
        {
            "date": "02.04",
            "city": "海口",
            "confirm": 14,
            "dead": 0,
            "heal": 0,
            "suspect": 0,
            "confirm_add": ""
        },
        {
            "date": "02.05",
            "city": "海口",
            "confirm": 16,
            "dead": 0,
            "heal": 0,
            "suspect": 0,
            "confirm_add": ""
        },
        {
            "date": "02.06",
            "city": "海口",
            "confirm": 18,
            "dead": 0,
            "heal": 2,
            "suspect": 0,
            "confirm_add": "2"
        },
        {
            "date": "02.07",
            "city": "海口",
            "confirm": 21,
            "dead": 0,
            "heal": 1,
            "suspect": 0,
            "confirm_add": "3"
        },
        {
            "date": "02.08",
            "city": "海口",
            "confirm": 24,
            "dead": 0,
            "heal": 2,
            "suspect": 0,
            "confirm_add": "3"
        },
        {
            "date": "02.09",
            "city": "海口",
            "confirm": 23,
            "dead": 0,
            "heal": 5,
            "suspect": 0,
            "confirm_add": "0"
        },
        {
            "date": "02.10",
            "city": "海口",
            "confirm": 28,
            "dead": 0,
            "heal": 4,
            "suspect": 0,
            "confirm_add": "5"
        },
        {
            "date": "02.11",
            "city": "海口",
            "confirm": 29,
            "dead": 0,
            "heal": 5,
            "suspect": 0,
            "confirm_add": "1"
        },
        {
            "date": "02.12",
            "city": "海口",
            "confirm": 29,
            "dead": 0,
            "heal": 6,
            "suspect": 0,
            "confirm_add": "0"
        },
        {
            "date": "02.13",
            "city": "海口",
            "confirm": 29,
            "dead": 0,
            "heal": 6,
            "suspect": 0,
            "confirm_add": "0"
        },
        {
            "date": "02.14",
            "city": "海口",
            "confirm": 31,
            "dead": 0,
            "heal": 9,
            "suspect": 0,
            "confirm_add": "2"
        },
        {
            "date": "02.15",
            "city": "海口",
            "confirm": 33,
            "dead": 0,
            "heal": 9,
            "suspect": 0,
            "confirm_add": "3"
        },
        {
            "date": "02.16",
            "city": "海口",
            "confirm": 33,
            "dead": 0,
            "heal": 9,
            "suspect": 0,
            "confirm_add": "3"
        },
        {
            "date": "02.17",
            "city": "海口",
            "confirm": 34,
            "dead": 0,
            "heal": 12,
            "suspect": 0,
            "confirm_add": "1"
        },
        {
            "date": "02.18",
            "city": "海口",
            "confirm": 34,
            "dead": 0,
            "heal": 16,
            "suspect": 0,
            "confirm_add": "0"
        },
        {
            "date": "02.19",
            "city": "海口",
            "confirm": 34,
            "dead": 0,
            "heal": 17,
            "suspect": 0,
            "confirm_add": "0"
        },
        {
            "date": "02.20",
            "city": "海口",
            "confirm": 39,
            "dead": 0,
            "heal": 18,
            "suspect": 0,
            "confirm_add": "5"
        },
        {
            "date": "02.21",
            "city": "海口",
            "confirm": 39,
            "dead": 0,
            "heal": 18,
            "suspect": 0,
            "confirm_add": "5"
        },
        {
            "date": "02.22",
            "city": "海口",
            "confirm": 39,
            "dead": 0,
            "heal": 19,
            "suspect": 0,
            "confirm_add": "0"
        },
        {
            "date": "02.23",
            "city": "海口",
            "confirm": 39,
            "dead": 0,
            "heal": 19,
            "suspect": 0,
            "confirm_add": "0"
        },
        {
            "date": "02.24",
            "city": "海口",
            "confirm": 39,
            "dead": 0,
            "heal": 20,
            "suspect": 0,
            "confirm_add": ""
        },
        {
            "date": "02.25",
            "city": "海口",
            "confirm": 39,
            "dead": 0,
            "heal": 28,
            "suspect": 0,
            "confirm_add": "0"
        },
        {
            "date": "02.26",
            "city": "海口",
            "confirm": 39,
            "dead": 0,
            "heal": 28,
            "suspect": 0,
            "confirm_add": "0"
        },
        {
            "date": "02.27",
            "city": "海口",
            "confirm": 39,
            "dead": 0,
            "heal": 31,
            "suspect": 0,
            "confirm_add": "0"
        },
        {
            "date": "02.28",
            "city": "海口",
            "confirm": 39,
            "dead": 0,
            "heal": 31,
            "suspect": 0,
            "confirm_add": "0"
        },
        {
            "date": "02.29",
            "city": "海口",
            "confirm": 39,
            "dead": 0,
            "heal": 31,
            "suspect": 0,
            "confirm_add": "0"
        },
        {
            "date": "03.01",
            "city": "海口",
            "confirm": 39,
            "dead": 0,
            "heal": 33,
            "suspect": 0,
            "confirm_add": "0"
        },
        {
            "date": "03.02",
            "city": "海口",
            "confirm": 39,
            "dead": 0,
            "heal": 35,
            "suspect": 0,
            "confirm_add": "0"
        },
        {
            "date": "03.03",
            "city": "海口",
            "confirm": 39,
            "dead": 0,
            "heal": 35,
            "suspect": 0,
            "confirm_add": "0"
        },
        {
            "date": "03.04",
            "city": "海口",
            "confirm": 39,
            "dead": 0,
            "heal": 37,
            "suspect": 0,
            "confirm_add": "0"
        },
        {
            "date": "03.05",
            "city": "海口",
            "confirm": 39,
            "dead": 0,
            "heal": 38,
            "suspect": 0,
            "confirm_add": ""
        }
    ]
}
"""
num=[]
content=json.loads(test)
# print(type(content))
for day in content['data']:
    now=int(day['confirm'])-int(day['heal'])-int(day['dead'])
    date=day['date']
    print((date,now))
