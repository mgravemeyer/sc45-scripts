import re
import json
import io
import codecs

filename = ["enscheidungUtf8.txt"]

exportJSON = []

searchRadius = 150
skip = 7

for file in filename:

	kategorien = []

	selectedFile = open(file, 'r')
	selectedFileContent = selectedFile.read()
	selectedFile.close()

	for i in range(skip, searchRadius):
		inhaltStart, inhaltEnd = selectedFileContent.find('<<<inhalt=' + str(i) + '>>>'), selectedFileContent.find('<<<inhaltEnde=' + str(i) + '>>>')
		quelleStart, quelleEnd = selectedFileContent.find('<<<quelle=' + str(i) + '>>>'), selectedFileContent.find('<<<quelleEnde=' + str(i) + '>>>')
		inhalt = str(selectedFileContent[inhaltStart:inhaltEnd]).replace('<<<inhalt=' + str(i) + '>>>', '')

		kategorie = ""

		for c in inhalt:
			if not c.isupper():
				if not kategorie in kategorie:
					kategorien.append(kategorie)
				break;
			else:
				kategorie = kategorie + c

		quelle = str(selectedFileContent[quelleStart:quelleEnd]).replace('<<<quelle=' + str(i) + '>>>', '')

		autor = quelle.replace(" ", "")
		autor = ''.join([o for o in autor if not o.isdigit()])

		jahr = filter(str.isdigit, quelle)

		exportJSON.append({str(i) : {"inhalt": str(inhalt), "kategorie" : str(kategorie), "jahr" : str(jahr), "autor": str(autor)}})

with open('data.json', 'w') as f:
	json.dump(exportJSON, f, ensure_ascii=False)