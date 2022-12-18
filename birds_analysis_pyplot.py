import json
import pandas as pd
import matplotlib.pyplot as plt

jfile = "tmi.json"
data = json.load(open(jfile))
df = pd.json_normalize(data)
df = df.set_index('motif')
animals_df = df.filter(regex = 'B', axis = 0)

winged_creatures = [ 'bird', 'dragon', 'birds', 'eagle', 'owl', 'insect', 'parrot', 'bee', 'goose', 'peacock', 'swan', 'lark', 'crane', 'pigeon', 'sparrow', 'wasp', 'vulture', 'falcon', 'stork', 'hawk', 'duck', 'woodpecker', 'hornet', 'swift', 'cricket', 'dove', 'titmouse', 'gull']

def filterwinged(meep):
    return any(item in meep for item in winged_creatures)

def count_winged_creatures(lemmas):
  counts = {word: 0 for word in winged_creatures}
  for word in lemmas:
    if word in winged_creatures:
      counts[word] += 1
  return counts

filtercreatures = animals_df[animals_df['lemmas'].apply(filterwinged)] # https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
filtered = filtercreatures['lemmas'].apply(count_winged_creatures)
crittercounts = pd.DataFrame.from_records(filtered.tolist())

labels = list(crittercounts.columns)
frequencies = crittercounts.sum()


plt.bar(labels, frequencies, color='mediumpurple')
plt.title('Frequency of words relating to winged creatures in motif types')
plt.xlabel('Word')
plt.ylabel('# of Occurences')
plt.show()

