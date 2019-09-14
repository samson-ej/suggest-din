# imports
import pandas as pd
from collections import Counter, OrderedDict

# populate dataframe parsing csv; data starts as strings
with open('/home/esamson/Desktop/projects/suggest-din/dummy.csv') as meals:
    # fullCSV = csv.reader(meals, delimiter=',')
    mealdata = pd.read_csv(meals, delimiter=',', header=0, skiprows=0)
    df = pd.DataFrame(mealdata)

# process new text file lists of each food type
# code abbreviates protein -> meat, etc.
with open('/home/esamson/Desktop/projects/suggest-din/carb-list.txt','r') as carbs:
    carb_list = carbs.read().split(',')

with open('/home/esamson/Desktop/projects/suggest-din/meat-list.txt','r') as meats:
    meat_list = meats.read().split(',')

with open('/home/esamson/Desktop/projects/suggest-din/vege-list.txt','r') as veggies:
    vege_list = veggies.read().split(',')

# initialize dictionaries for each 
meat_dict, carb_dict, vege_dict = {},{},{}

# initialize rank arrays
rank_meat, rank_carb, rank_vege = [],[],[]

# parse DataFrame into processing arrays
for row in df:
    tempM = df['meat']
    tempC = df['carb']
    tempV = df['vege']

# use Counter to tally counts of each
m_count = Counter(tempM)
c_count = Counter(tempC)
v_count = Counter(tempV)

# populate dictionaries with collected counts
for each in tempM:
    meat_dict[meat_list[each]] = m_count[each]
for each in tempC:
    carb_dict[carb_list[each]] = c_count[each]
for each in tempV:
    vege_dict[vege_list[each]] = v_count[each]

# create ordered dictionaries of each using OrderedDict sorted() function 
ord_meat = OrderedDict(sorted(meat_dict.items(), key=lambda meat: meat[1]))
ord_carb = OrderedDict(sorted(carb_dict.items(), key=lambda carb: carb[1]))
ord_vege = OrderedDict(sorted(vege_dict.items(), key=lambda vege: vege[1]))

# populate ranked list of each
for key in ord_meat:
    rank_meat.append(key)
for key in ord_carb:
    rank_carb.append(key)
for key in ord_vege:
    rank_vege.append(key)

# analysis - TBD

# returns top 3 suggestions for each based on rank
print('For your protein, you should have ' + rank_meat[0] + ', ' + rank_meat[1] + ', or ' + rank_meat[2])
print('For your carb, you should have ' + rank_carb[0] + ', ' + rank_carb[1] + ', or ' + rank_carb[2])
print('For your vegetable, you should have ' + rank_vege[0] + ', ' + rank_vege[1] + ', or ' + rank_vege[2])