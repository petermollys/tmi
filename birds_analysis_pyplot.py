# Molly Peters- LIS 487 Data Interoperability Use Case Project
# Plotting the data. 

import json
import pandas as pd
import matplotlib.pyplot as plt

# open the data file and load it into a dataframe
jfile = "tmi.json"
data = json.load(open(jfile))
df = pd.json_normalize(data)
df = df.set_index('motif')
animals_df = df.filter(regex = 'B', axis = 0) # make a dataframe for just the animals motifs (begin with b)

# List of winged creatures that appear in the motif index type, pulled from the dataset 
winged_creatures = [ 'bird', 'dragon', 'birds', 'eagle', 'owl', 'insect', 'parrot', 'bee', 'goose', 'peacock', 'swan', 'lark', 'crane', 'pigeon', 'sparrow', 'wasp', 'vulture', 'falcon', 'stork', 'hawk', 'duck', 'woodpecker', 'hornet', 'swift', 'cricket', 'dove', 'titmouse', 'gull']

# filter dataframe to include only motifs which match a value in the winged creatures list
def filterwinged(meep):
    return any(item in meep for item in winged_creatures)

# count the instances of winged creature words in the dataset 
def count_winged_creatures(lemmas):
  counts = {word: 0 for word in winged_creatures}
  for word in lemmas:
    if word in winged_creatures:
      counts[word] += 1
  return counts

# create a filtered dataframe using the filterwinged function
filtercreatures = animals_df[animals_df['lemmas'].apply(filterwinged)] # https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
# create a series that includes the counts
filtered = filtercreatures['lemmas'].apply(count_winged_creatures)
# Create a dataframe from the series including the counts using from_records
crittercounts = pd.DataFrame.from_records(filtered.tolist())

# define labels and frequencies variables for the plot
labels = list(crittercounts.columns)
frequencies = crittercounts.sum()

# create a bar plot using the data
plt.bar(labels, frequencies, color='mediumpurple')
plt.title('Frequency of words relating to winged creatures in the animal motif type')
plt.xlabel('Word')
plt.ylabel('# of Occurences')
plt.show()


