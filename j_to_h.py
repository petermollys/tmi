# this program converts the json data into a dataframe using pandas, then writes an html file from that dataframe

import json
import pandas as pd
import os

# open and load the original json file
jfile = "tmi.json"
data = json.load(open(jfile))

# get a list of keys in the original json file 
# https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html#
keylist = []

df = pd.json_normalize(data)
print(df.axes)

# make a new dictionary, and add each motif number as an item so that there can be an index each item 
newdict = {}
for item in data:
    newdict[item["motif"]] = item

# dump the new dict into a new json file 
json.dump(newdict, open("new_tmi.json", "w"))
njfile = "new_tmi.json"
data_i = json.load(open(njfile))
# df = pd.json_normalize(data_i)
# print(df.axes)

# for key in df.keys():
#     keylist.append(key)
# print(keylist)

# if the html output file does not exist, create the file from the dataframe 
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_html.html
if not os.path.exists("tmi_output.html"):
    output = open("tmi_output.html", "w")
    output.write(df.to_html())
    print("tmi_output.html has been created. please check the local directory.")
else:
    print("the file tmi_output has already been created. please check the local directory")