# imports
import numpy as np
import pandas as pd
import csv
import json
import math
from collections import Counter, OrderedDict

# print("ZA WORULDO!")

# populate dataframe

# csv parsing, data starts as strings
with open('/home/esamson/Desktop/projects/what4dinner/dummy.csv') as meals:
    # fullCSV = csv.reader(meals, delimiter=',')
    mealdata = pd.read_csv(meals, delimiter=',', header=0, skiprows=0)
    df = pd.DataFrame(mealdata)
    # print(df)

    # add column for meal-name?

# need dictionary to define each meat,carb,veg 
meat_list = ['chicken', 'steak','ground-beef', 'pork', 'roast-beef', 'salmon', 'white-fish',
            'tofu']
carb_list = ['rice', 'pasta', 'spaghetti', 'macncheese', 'potato', 'risotto', 'lasagna', 'dumplings',
            'gnocchi', 'legumes', 'cauliflower', 'zucchini', 'parsnip', 'beets', 'squash', 'corn',
            'eggplant']
vege_list = ['cabbage', 'brocolli', 'asparagus', 'spinach', 'brussels-sprouts', 'collards', 'celery',
            'bell-peppers', 'okra']             
meat_dict, carb_dict, vege_dict = {},{},{}
# carb_dict = {}
# vege_dict = {}
rank_meat, rank_carb, rank_vege = [],[],[]
# rank_carb = []
# rank_vege = []

for row in df:
    tempM = df['meat']
    tempC = df['carb']
    tempV = df['vege']

m_count = Counter(tempM)
c_count = Counter(tempC)
v_count = Counter(tempV)
for each in tempM:
    meat_dict[meat_list[each]] = m_count[each]
for each in tempC:
    carb_dict[carb_list[each]] = c_count[each]
for each in tempV:
    vege_dict[vege_list[each]] = v_count[each]

# print(tempC)

# prints out ascending rank of meat dictionary
ord_meat = OrderedDict(sorted(meat_dict.items(), key=lambda meat: meat[1]))
ord_carb = OrderedDict(sorted(carb_dict.items(), key=lambda carb: carb[1]))
ord_vege = OrderedDict(sorted(vege_dict.items(), key=lambda vege: vege[1]))
# print(ord_vege)

for key in ord_meat:
    rank_meat.append(key)
for key in ord_carb:
    rank_carb.append(key)
for key in ord_vege:
    rank_vege.append(key)


# print(rank_carb[2])
# print(rank_vege)

# analysis


# return suggestion based on rank
print('For your protein, you should have ' + rank_meat[0] + ', ' + rank_meat[1] + ', or ' + rank_meat[2])
print('For your carb, you should have ' + rank_carb[0] + ', ' + rank_carb[1] + ', or ' + rank_carb[2])
print('For your vegetable, you should have ' + rank_vege[0] + ', ' + rank_vege[1] + ', or ' + rank_vege[2])
