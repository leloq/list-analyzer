import pandas as pd
import numpy as np 
from prettytable import PrettyTable

noResults = 10 # Number of desired results in tables
html = True # If representation is HTML or regular string

def excelInputRequested():
	try: 
		listname = input("Please type in Excel name: ")
		df = pd.read_excel(listname)
		return df
	except: 
		print("Error: No correct list name input.")

### Function to display column names - user chooses afterwards to-be-analyzed columns###
def listColumnNames(df):
	try:
		print("### COLUMNS IN LIST ###")
		columnNamesList = list(df)
		index = 0
		columnNames = ""
		for i in columnNamesList:
			strAdd = "Index: "+str(index)+" Column Name: "+i+"\n"
			columnNames = columnNames + strAdd
			#print("Index: ",index," Column Name:",i)
			index = index +1
		return(columnNames)
	except Exception as e: 
		print("Error: Listing column names failed.",e)

### Function to request to-be-analyzed columns by user ###
def enterColumnNames(): 
	try: 
		desiredColumnsStr = input("Please enter index numbers of to-be-analyzed columns (comma seperated):")
		strippedStr = desiredColumnsStr.replace(" ", "") ## Remove whitespaces
		columnList = strippedStr.split(",")
		columnListInt = [] ### convert strings to ints
		for i in columnList:
			try: 
				iInt = int(i) ## Convert element to int
				columnListInt.append(iInt) ## Append it to int list
			except:
				pass
		return columnListInt

	except:
		print("Error: Please insert desired columns in right format (if columns with index 0, 1, 5 desired, enter --> 0,1,5")

### Function to calculate the column counts ###
def getColumnCounts(dataframe, columns):
	try:
		dictList = [] ### List of key value dicts
		for i in columns:
			counts = dataframe[dataframe.columns[i]].value_counts().to_dict() ### Get value counts in dict
			dictList.append(counts) ### Append value counts to dict list
		return dictList
	except:
		print("Error: Getting frequency of values in columns failed.")

### Function to return string of. Amount determines how many entries, html if return string is in html format or regular string
def getFinalResults(dictList, dataframe, amount, html):
	try:
		counter = 0 
		tables = [] #table to store strings of tables

		for i in dictList:
			tables.append(dataframe.columns[columnListInt[counter]])
			#print(counter+1, ": counts and frequency of column ", dataframe.columns[columnListInt[counter]]) ### Print column title
			totalEntries = sum(i.values()) # Get total number of entries to calculate percentages
			x = PrettyTable() # Create Pretty Table
			x.field_names = ["Value", "Count", "Percentage in %"]
			### Iterate over values and respective counts
			entries = list(i.items()) ### Convert dict items to 
			for k, v in entries[:amount]:
				percentage = round((v/totalEntries)*100,2)
				x.add_row([k,v, percentage])

			if(html):
				tables.append(x.get_html_string()) ### Transform to html
			else:
				tables.append(x.get_string()) ### Transform to html
			counter = counter + 1

		tableString = ' '.join(tables)
		return(tableString)
	except Exception as e:
		print("Error: Returning final results failed.")
		logger.error(print(str(e)))


df = excelInputRequested() ### Create dataframe from input
print(listColumnNames(df))
columnListInt = enterColumnNames()
countsDict = getColumnCounts(df, columnListInt)
print(getFinalResults (countsDict, df, noResults, html))