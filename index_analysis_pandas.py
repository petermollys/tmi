# Molly Peters- LIS 487 Data Interoperability Use Case Project
# Index analysis with Pandas and HTML Transformation

import json
import pandas as pd
import codecs

# open tmi.json file as data
jfile = "tmi.json"
data = json.load(open(jfile))

# open output html file 
output = codecs.open('tmi_analysis.html', 'w', 'utf-8')

# create a pandas dataframe using the json_normalize method, with the motif column as the index 
# https://datagy.io/pandas-drop-index-column/ used to set motif column as index
df = pd.json_normalize(data)
df = df.set_index('motif')

# define function that flattens the series 
# meep is just a variable placeholder so any list can be used in its place
# https://stackoverflow.com/questions/30885005/pandas-series-of-lists-to-one-series 
def flatten_l(meep):
    return [x for y in meep for x in y]

# define function that gets the terms, adds them to a list, and counts their instances
# pass the name of the dataframe as arg
def all_motifs(dfname):

    # add them to lists
    alocations = dfname['locations'].apply(lambda x: x).tolist() # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html add the locations to a list
    alemmas = dfname['lemmas'].apply(lambda x: x).tolist()
    alocs = flatten_l(alocations) # flatten the dataframe
    alems = flatten_l(alemmas)

    # empty count dictionaries, key:value::word:count
    aloccount = {}
    alemcount = {}

    # counting loops
    # Locations
    for i in alocs:
        if i not in aloccount:
            aloccount[i] = 1
        else:
            aloccount[i] += 1
    # TODO look into this loop- is it working properly? should the aloccount and alemcount loops be in a separate function that is called after all_motifs()?
    for i in aloccount:
        if i == max(aloccount, key=aloccount.get):
            maxaloc = i

    # Lemmas
    for i in alems:
        if i not in alemcount:
            alemcount[i] = 1
        else:
            alemcount[i] += 1
    # TODO Look at this one too...
    for i in alemcount:
        if i == max(alemcount, key=alemcount.get):
            maxalem = i
   
    # sort the dict by highest value (most ocurrences) and return second most key because the name of the motif type was sometimes the highest value so thats not helpful
    sort_lemmas = sorted(alemcount.items(), key = lambda x: x[1], reverse = True) # https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/ sorting with lambda! cool
    next_lem = sort_lemmas[1][0]
    return maxaloc, maxalem, next_lem

# define function that prints the results from the all_motifs analysis function for the dataframe used
# results printed both in terminal and in the html output file
def index_analysis(df, motifs, output):
    maxaloc, maxalem, next_lem = all_motifs(df) # assign returned values from all_motifs function to variables for whichever dataframe is passed through
    print(f'Motifs of {motifs} feature most prominently in the folklore of {maxaloc}.\n')
    output.write(f'<p>Motifs of {motifs} feature most prominently in the folklore of {maxaloc}.</p>\n')
    print(f'The word "{maxalem}" is featured most commonly in the names of {motifs} motifs.\n' )
    output.write(f'<p>The word "{maxalem}" is featured most commonly in the names of {motifs} motifs.</p>\n' )
    print(f'The second most common word in the names of {motifs} motifs is "{next_lem}".\n' )
    output.write(f'<p>The second most common word in the names of {motifs} motifs is "{next_lem}".</p>\n' )

# Define function that acts similarly to the all_motifs function, except it finds and counts the instances of the word 'bird'
def birds_index_analysis(df,motifs, output):
    # try this if bird is in the motif type
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

        # if loop which prints different statement depending on the results 
        if next_value < 1:
            print(f'In motifs of {motifs}, birds are featured {birdfreq} times. There are not any other words that are repeated alongside "bird" in this motif type.\n')
            output.write(f'<p>In motifs of {motifs}, birds are featured {birdfreq} times. There are not any other words that are repeated alongside "bird" in this motif type.</p>\n')     
        elif next_value == 1:
            print(f'In motifs of {motifs}, birds are featured {birdfreq} time. There are not any other words that are repeated alongside "bird" in this motif type.\n')
            output.write(f'<p>In motifs of {motifs}, birds are featured {birdfreq} time. There are not any other words that are repeated alongside "bird" in this motif type.</p>\n')
        else:
            print(f'In motifs of {motifs}, birds are featured {birdfreq} times. They appear most frequently alongside the word "{next_lem}".\n')
            output.write(f'<p>In motifs of {motifs}, birds are featured {birdfreq} times. They appear most frequently alongside the word "{next_lem}".</p>\n')
    # except if bird does not appear in the index type
    except:
        print(f'The word "bird" does not appear in any of the motifs in the {motifs} type.')
        output.write(f'<p>The word "bird" does not appear in any of the motifs in the {motifs} type.</p>\n')

# make a new dataframe of all the motif types using their catalog # to organize them
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

# dictionary containing the names of the dataframes and the names of the motif types as regular strings
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

# Start printing the output both in terminal and in output file as html
print("\n ===== Analysis of Thompson's Motif Index ===== \n")

output.write('''<html>
    <body>
    <h1>Analysis of Thompson's Motif Index</h1>\n
''')
# loop through index dictionary and pass each dataframe into the program, print results
for df_name in index_dict:
    df = globals()[df_name] #https://www.geeksforgeeks.org/python-globals-function/
    df['typeletter'] = df.index.str.extract(r'^(\w){1}', expand = False) # https://re-thought.com/python-regex-example-for-pattern-2-digits-to-2-digits-26-to-40/
    amount_type = df['typeletter'].value_counts() # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Index.value_counts.html?highlight=value_counts#pandas.Index.value_counts
    for i in amount_type.index[0]:
        motif_letter = i

    motif_letter = amount_type.index[0][-1]

    amount_count = amount_type.max() # https://www.geeksforgeeks.org/select-row-with-maximum-and-minimum-value-in-pandas-dataframe/
    motifs = index_dict[df_name]
    capmotifs = motifs.upper()  # https://thehelloworldprogram.com/python/python-string-methods/#:~:text=Performing%20the%20.,of%20the%20characters%20to%20lowercase.
    print(f'\n==== TYPE {motif_letter}: {capmotifs} MOTIFS ====\n')
    output.write(f'<h3>TYPE {motif_letter}: {capmotifs} MOTIFS</h3>\n')
    print(f'There are {amount_count} motifs within this type classification.\n')
    output.write(f'<h4>There are {amount_count} motifs within this type classification.</h4>\n')
    index_analysis(df, motifs, output)
    birds_index_analysis(df, motifs, output)
    print('\n')

# close the output file
output.write('</body>\n</html>')
output.close()
