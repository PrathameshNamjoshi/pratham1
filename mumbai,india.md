# Wrangle-OpenStreetMap-Data

On the particular project, I am using data mungling techniques to assess the quality of OpenStreetMap’s (OSM) data for the mumbai city regarding their consistency and uniformity. The data wrangling takes place programmatically, using Python for the most of the process and SQL for items that need further attention.

The dataset describes the city of mumbai.Mumbai,India is the closest thing I have to a hometown in the India as I lived there for a good chunk of my childhood, so I was keen to take a look at it in this new, OpenStreetMap-based lens. The size of the dataset is 66 MB and can can be downloaded from here: https://mapzen.com/data/metro-extracts/metro/mumbai_india/

# About the project

# Scope

OpenStreetMap (OSM) is a collaborative project to create a free editable map of the world. The creation and growth of OSM have been motivated by restrictions on use or availability of map information across much of the world, and the advent of inexpensive portable satellite navigation devices.

On the specific project, I am using data from https://www.openstreetmap.org/node/16173235 and data mungling techniques, to assess the quality of their validity, accuracy, completeness, consistency and uniformity. The biggest part of the wrangling takes place programmatically using Python and then the dataset is entered into a SQL database for further examination of any remaining elements that need attention. Finally, I perform some basic exploration and express some ideas for additional improvements.

# Skills demonstrated

Assessment of the quality of data for validity, accuracy, completeness, consistency and uniformity. Parsing and gathering data from popular file formats such as .xml and .csv. Processing data from very large files that cannot be cleaned with spreadsheet programs. Storing, querying, and aggregating data using SQL. Mumbai, India

https://www.openstreetmap.org/node/16173235 https://mapzen.com/data/metro-extracts/metro/mumbai_india/

Problems Encountered in the Map

Problems Encountered in the Map Once the location was decided, I downloaded the full extract of the region and ran Python code to investigate any issues with the data. The following problems were discovered:

Street Names: Incomplete ('hanuman raod ___') or incorrect names ('Zhopadpatti'), along with street abbreviations ('rd.' instead of 'Road')

Postal Codes: Inconsistent postal code formats ('500023' and '120045') and incorrect post codes ('123')

To tackle these issues, I had to create python scripts to clean each respective category of data. Auditing part is explained in Openstreetmap.ipynb notebook
