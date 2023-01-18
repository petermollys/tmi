# tmi
# 
Thompson's Motif-Index of Folk Literature: A Classification of Narrative Elements in Folktales, Ballads, Myths, Fables, Mediaeval Romances, Exempla, Fabliaux, Jestbooks, and Local Legends.

LIS487 Data Interoperability- Catherine Dumas, Fall 2022
Final Project- Thompson's Motif Index 
Molly Peters 

Sources of data:
Using the data file found here: https://github.com/fbkarsdorp/tmi/blob/master/data/tmi.json 
I am not sure what source exactly this person used to extract the data from Thompson's Motif indef, but this other project (tmi_csv) cites Thompson's original index, as well as some other sources: https://osf.io/zs7p2
This website proved to be very helpful for getting the names of the motif types: https://sites.ualberta.ca/~urban/Projects/English/Content/Motif_Help.htm

Overview of my process:
Initially I intended to transform the JSON data from tmi.json into XML, using a schema. I struggled with this early on in the project, and decided to move on to the data analysis and figure out the transformation later.
I decided to transform the data into HTML instead, since it was something that could be done quickly and would be helpful to use for reference while doing the analysis. 
I plugged the original JSON file into dataframes using pandas to do the analysis. From there, I defined separate dataframes for each motif index type and analyzed them 1 at a time using a for loop. 
The analysis file goes through the data and prints information about the data in each tale type, and also creates a new html file with the same analyses. 

Files:
tmi.json -- Original JSON file containing Thompson's Motif Index data. From this project: https://github.com/fbkarsdorp/tmi

j_to_h.py -- Import original JSON file, outputs the same data in HTML form as tmi_output.html and a further nested new JSON file called new_tmi.json

tmi_output.html -- Output from j_to_h.py. Contains tmi data in the form of a table.

new_tmi.json -- Output from j_to_h.py. Thought I would need the more nested data structure for some things, ended up not using it elsewhere. 

index_analysis.py -- Takes the data from tmi.json and makes a dataframe with pandas. Creates separate dataframes for each motif type, and adds a column for the motif class letter using regex.
                  Analyzes the data for each motif type in the index by counting the frequency of words. Also counts for the frequency of the word 'bird' across types. 
                  This analysis is printed by the program, and also output into an HTML file called tmi_analysis.html

tmi_analysis.html -- Analyzed data output from index_analysis.py

birds_analysis_pyplot.py -- Using the dataframe for the animals index type, counts occurrences of winged-creature related words against a list of these words, and plots the data in a bar chart.
