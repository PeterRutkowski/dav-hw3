# MIMUW_2019S_DAV_HW3
MIMUW 2019/20 Data Analysis and Visualisation Homework 3

Exercise 4

We use again the same file from the World Bank:
https://data.worldbank.org/indicator/SP.POP.TOTL?end=2018&start=1960&view=chart

In the previous exercise, we selected the data for:
a) 5 most populated countries
b) 5 randomly picked 
c) 5 with Poland as the centroid

=====================================================================================

IMPORTANT: For animation plots use as much as possible "matplotlib.animation"
https://matplotlib.org/3.2.0/api/animation_api.html

Remember, we use English. All text used in the plots should be English.

=====================================================================================

I) Playing with colors and labels:
For all plots from exercise 3 (a-c) do bar plots:
a) color version (most likely you already have a good starting point)
b) black & white version

Requirements:
- on top of each bar put three letter "Country Code" e.g. CHN for China
- "Country Code" position is updated with respect to the bar size
- for black and white version use shapes and/or textures to indicate the classification
- the axis indicating the population should be fixed 
  (the bar should show the increase, not the lidership)
- there is year counter inside of the plot (make it big enough)
- the font for all elements should be visible (from a large distance)
- increase the readiness of the plot as much as possible 
(e.g. do not use 150.000.000 on the scale; 150M is much shorter and easy to read)

Expected result: 6 animated bar plots (gif; 3 b&w and 3 color)

=====================================================================================

II) Play with a different representation of the data:

All of the plots so far had been "bar plots". Now, the task is to present 
the data using different plot representation. For each a-c from previous lab do similar animated plots, but as:
A) line plot (so the plots start as a dot and the line moves while the time progress)
B) bubble plot (x is time, y is the population, z (bubble) is a population density) 
C) any other representation

- find the data about the area related to the countries of interest and calculate population density (population/area).

Requirements:
- on top of each bar, line or bubble put three-letter "Country Code" e.g. CHN for China
- "Country Code" position is updated with the respect to the line or bubble location
- there is year counter inside of the plot (make it big enough)
- the font for all elements should be visible (from a large distance)

Expected result: 3 animated, color plots (gif)

=====================================================================================

Exercise 5

We use again the same file from the World Bank:
https://data.worldbank.org/indicator/SP.POP.TOTL?end=2018&start=1960&view=chart

In the previous exercise, we selected the data for:
a) 5 most populated countries
b) 5 randomly picked 
c) 5 with Poland as the centroid

=====================================================================================

IMPORTANT: For animation plots use as much as possible "matplotlib.animation"
https://matplotlib.org/3.2.0/api/animation_api.html

Remember, we use English. All text used in the plots should be English.

=====================================================================================

III) Exploration of the data. Select a group of 4-8 countries that:
- at least one shows some strange behavior e.g. strong increase, decrease or 
stability of the population size in some particular period of time
(thus it is up to you to find those in the data)
- mark this event on the plot

For instance, you could pick one or a few countries in some war zone and few 
other outside of it (e.g. Balkans in '90s) and show how the population changed 
(to highlight the difference try to use neighbors or/and countries with similar 
population size). To mark the event stop/freeze (or decrease speed) 
the animation for ~4s in order to allow people to read the information 
(imagine that you are having speech and you want to emphasize the fact) 
- thus you need to put some additional text for those ~4s in some part 
of the plot ('e.g. "WAR") explaining the observed fact. If the selected 
event is related to a given period e.g. 5 years, than you show the text
on all related years (e.g. 1992-1995).  

Expected result: 2 animated, bar plots (gif) 

SUMMARY OF POINTS I-III: Embed plots from I-III in a single HTML page 
(describe the plots).

IV) Generate Gantt plot from the data presented on the second page of 
https://www.mimuw.edu.pl/sites/default/files/dwmim.2019.34.zd_.13.pdf

Requirements:
- the labels must be in English
- the labels should be placed inside of the bar or next to it, but
  cannot overlap
- do color and black&white version (2 plots)
- if needed, introduce abbreviations and explain them below the plot
- each plot should be presented as a separate pdf file of A4 size
(the plot should take the whole A4 page and be as much readable as
possible - think about printing it and putting on the wall)

Expected result: 2 static, Gantt plots (2 separate single page A4 pdf files). Additionally, convert the plots into images for report purposes.

========================================================================================

Homework:

Prepare the homework as project directory with lab4 & lab5 exercises. It should contain:
- the main report file in HTML (with all the plots embedded) 
- the plots (both GIFs from I-III and PDFs from IV thus lab4 & lab5 together) 
as separate files
- the python scripts generating plots
- the data for each plot (csv format) - each time you need to filter out relevant data

All files should be organized as the project folder and send until 29.03.2020
via email to lukaskoz@mimuw.edu.pl with the email subject:
'lab5_hw_Name_Surname' without email text body and with 
'lab5_hw_Name_Surname.7z' (ASCII letters only) attachment.

(thus no 'lab5_Małgorzata_Łóżyńska', should be 'lab5_Malgorzata_Luzynska')

All emails with a different structure (the one that will not go through email filter to the proper email folder dedicated for home works) will be scored -10% 

Using non-English labels, legends, descriptions, etc. will be scored -10%

Additionally, all problems with the structure of the plot e.g. the plot size,  
labels font size, etc. will also affect the grading. You need to follow advice included
in the lectures (e.g. correct bars spacing). 
