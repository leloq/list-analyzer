import pandas as pd
import numpy as np 
from prettytable import PrettyTable

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
		for i in columnNamesList:
			print("Index: ",index," Column Name:",i)
			index = index +1

	except: 
		print("Error: Listing column names failed.")

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

### Function to convert column counts in readable results ###
def getFinalResults(dictList, dataframe):
	try:
		counter = 0 
		for i in dictList:
			print(counter+1, ": counts and frequency of column ", dataframe.columns[counter]) ### Print column title
			totalEntries = sum(i.values()) # Get total number of entries to calculate percentages
			x = PrettyTable() # Create Pretty Table
			x.field_names = ["Value", "Count", "Percentage in %"]
			### Iterate over values and respective counts
			for k, v in i.items():
				percentage = (v/totalEntries)*100
				x.add_row([k,v, percentage])
			print(x)
			counter = counter + 1
	except Exception as e:
		print("Error: Returning final results failed.")
		logger.error(print(str(e)))


df = excelInputRequested() ### Create dataframe from input
listColumnNames(df)
columnListInt = enterColumnNames()
countsDict = getColumnCounts(df, columnListInt)
getFinalResults (countsDict, df)