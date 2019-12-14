#import requests
#import json
import pandas as pd
import numpy as np 
#import traceback
#import sys

def excelInputRequested():
	try: 
		listname = input("Please type in Excel name: ")
		df = pd.read_excel(listname)
		return df
	except: 
		print("Error: No correct list name input.")

excelInputRequested()