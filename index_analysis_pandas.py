# This program loads the new json file into a dataframe and does some analysis of the data

import json
import pandas as pd
import re
import matplotlib.pyplot as plt

jfile = "tmi.json"
data = json.load(open(jfile))

# https://datagy.io/pandas-drop-index-column/ used to set motif column as index
df = pd.json_normalize(data)
df = df.set_index('motif')

# define function that flattens lists 
def flatten_l(meep):
    return [x for y in meep for x in y]

def all_motifs(dfname):

    alocations = dfname['locations'].apply(lambda x: x).tolist() # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html add the locations to a list
    alemmas = dfname['lemmas'].apply(lambda x: x).tolist()
    alocs = flatten_l(alocations) # flatten the list
    alems = flatten_l(alemmas)

    aloccount = {}
    alemcount = {}
    for i in alocs:
        if i not in aloccount:
            aloccount[i] = 1
        else:
            aloccount[i] += 1

    for i in aloccount:
        if i == max(aloccount, key=aloccount.get):
            maxaloc = i

    for i in alems:
        if i not in alemcount:
            alemcount[i] = 1
        else:
            alemcount[i] += 1
    for i in alemcount:
        if i == max(alemcount, key=alemcount.get):
            maxalem = i

    sort_lemmas = sorted(alemcount.items(), key = lambda x: x[1], reverse = True) # https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/ sorting 
    next_lem = sort_lemmas[1][0]
    return maxaloc, maxalem, next_lem

def index_analysis(df, motifs):
    maxaloc, maxalem, next_lem = all_motifs(df)
    print(f'Motifs of {motifs} feature most prominently in the folklore of {maxaloc}.\n')
    print(f'The word "{maxalem}" is featured most commonly in the names of {motifs} motifs.\n' )
    print(f'The second most common word in the names of {motifs} motifs is "{next_lem}".\n' )

def birds_index_analysis(df,motifs):
    try:
        findbird = df['lemmas'].apply(lambda x: 'bird' in x)
        birdies = df.loc[findbird]
        birdlist = birdies['lemmas'].apply(lambda x: x).tolist()
        blist = flatten_l(birdlist)
        
        birdcount = {}
        for i in blist:
            if i not in birdcount:
                birdcount[i] = 1
            else:
                birdcount[i] += 1
        for i in blist:
            if i == max(birdcount, key=birdcount.get):
                birdfreq = birdcount[i] 
        sort_lemmas = sorted(birdcount.items(), key = lambda x: x[1], reverse = True)
        next_lem = sort_lemmas[1][0]
        next_value = sort_lemmas[1][1]
        maxaloc, maxalem, next_lem = all_motifs(birdies)
        if next_value < 1:
            print(f'In motifs of {motifs}, birds are featured {birdfreq} times. There are not any other words that are repeated alongside "bird" in this motif type.\n')
        elif next_value == 1:
            print(f'In motifs of {motifs}, birds are featured {birdfreq} time. There are not any other words that are repeated alongside "bird" in this motif type.\n')
        else:
            print(f'In motifs of {motifs}, birds are featured {birdfreq} times. They appear most frequently alongside the word "{next_lem}".\n')
    except:
        print(f'The word "bird" does not appear in any of the motifs in the {motifs} type.')

# make a new dataframe of all the animal motifs (their numbers start with B)

mythological_df = df.filter(regex = 'A', axis = 0)
animals_df = df.filter(regex = 'B', axis = 0)
taboo_df = df.filter(regex = 'C', axis = 0)
magic_df = df.filter(regex = 'D', axis = 0)
dead_df = df.filter(regex = 'E', axis = 0)
marvels_df = df.filter(regex = 'F', axis = 0)
ogres_df = df.filter(regex = 'G', axis = 0)
tests_df = df.filter(regex = 'H', axis = 0)
wisefoolish_df = df.filter(regex = 'J', axis = 0)
deceptions_df = df.filter(regex = 'K', axis = 0)
fortunereversal_df = df.filter(regex = 'L', axis = 0)
ordainingfuture_df = df.filter(regex = 'M', axis = 0)
chancefate_df = df.filter(regex = 'N', axis = 0)
society_df = df.filter(regex = 'P', axis = 0)
rewardpunishment_df = df.filter(regex = 'Q', axis = 0)
captivefugitive_df = df.filter(regex = 'R', axis = 0)
unnaturalcruelty_df = df.filter(regex = 'S', axis = 0)
sex_df = df.filter(regex = 'T', axis = 0)
natureoflife_df = df.filter(regex = 'U', axis = 0)
religion_df = df.filter(regex = 'V', axis = 0)
charactertraits_df = df.filter(regex = 'W', axis = 0)
humor_df = df.filter(regex = 'X', axis = 0)

index_dict = {
    'mythological_df' : 'mythological',
    'animals_df' : 'animals',
    'taboo_df': 'taboo',
    'magic_df': 'magic',
    'dead_df': 'the dead',
    'marvels_df': 'marvels',
    'ogres_df': 'ogres',
    'tests_df': 'tests',
    'wisefoolish_df': 'the wise and the foolish',
    'deceptions_df': 'deceptions',
    'fortunereversal_df': 'reversals of fortune',
    'ordainingfuture_df': 'ordaining the future', 
    'chancefate_df': 'chance and fate',
    'society_df': 'society',
    'rewardpunishment_df': 'rewards and punishements',
    'captivefugitive_df': 'captives and fugitives',
    'unnaturalcruelty_df': 'unnatural cruelty',
    'sex_df': 'sex',
    'natureoflife_df': 'the nature of life',
    'religion_df': 'religion',
    'charactertraits_df': 'traits of character',
    'humor_df': 'humor'
}

print("\n ===== Analysis of Thompson's Motif Index ===== \n")
for df_name in index_dict:
    df = globals()[df_name] #https://www.geeksforgeeks.org/python-globals-function/
    df['typeletter'] = df.index.str.extract(r'^(\w){1}', expand = False) # https://re-thought.com/python-regex-example-for-pattern-2-digits-to-2-digits-26-to-40/
    amount_type = df['typeletter'].value_counts() # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Index.value_counts.html?highlight=value_counts#pandas.Index.value_counts
    for i in amount_type.index[0]:
        motif_letter = i
    amount_count = amount_type.max() # https://www.geeksforgeeks.org/select-row-with-maximum-and-minimum-value-in-pandas-dataframe/
    motifs = index_dict[df_name]
    capmotifs = motifs.upper()  # https://thehelloworldprogram.com/python/python-string-methods/#:~:text=Performing%20the%20.,of%20the%20characters%20to%20lowercase.
    print(f'\n==== TYPE {motif_letter}: {capmotifs} MOTIFS ====\n')
    print(f'There are {amount_count} motifs within this type classification.\n')
    index_analysis(df, motifs)
    birds_index_analysis(df, motifs)
    print('\n')
