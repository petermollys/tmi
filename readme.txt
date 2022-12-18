LIS487 Data Interoperability- Catherine Dumas, Fall 2022
Final Project- Thompson's Motif Index 
Molly Peters 

Thompson's Motif-Index of Folk Literature: A Classification of Narrative Elements in Folktales, Ballads, Myths, Fables, Mediaeval Romances, Exempla, Fabliaux, Jestbooks, and Local Legends.

Using the data file found here: https://github.com/fbkarsdorp/tmi/blob/master/data/tmi.json 
I am not sure what source exactly this person used to extract the data from Thompson's Motif indef, but this other project (tmi_csv) cites Thompson's original index, as well as some other sources: https://osf.io/zs7p2
I think this resource will be helpful too: https://sites.ualberta.ca/~urban/Projects/English/Content/Motif_Help.htm

Transform the JSON data from tmi.json into XML, using a schema
I think it seems like it will be easier to analyze the data if its in JSON, so I probably will not do the analysis using the XML file. I might use the XML to turn it into HTML if I have extra time at the end.

Analyze JSON data using Pandas
find: which motifs appear most frequently (in the most locations)
      which locations have the most motifs 
      which motif types contain the most instances of certain terms/descriptors (i.e. clever, fool, justice, witch), and the location they appear from the most

visualize:
      which motifs within a letter type appear in the most geographic locations
      comparing 2 locations in 1 chart; value of each motif letter type


