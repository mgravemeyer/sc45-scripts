import json

filename = ["data.json"]

exportText = []

for file in filename:

	with open(file) as jsonFile:
		jsonObject = json.load(jsonFile)
		jsonFile.close()
	
	for jOb in jsonObject:
		print('-----------------------------------')
		print("INHALT: " + jOb[list(jOb.keys())[0]]['inhalt'])
		print("QUELLE: " + jOb[list(jOb.keys())[0]]['quelle'])
		print('-----------------------------------')