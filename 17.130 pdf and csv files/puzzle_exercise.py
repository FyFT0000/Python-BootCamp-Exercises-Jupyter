""" PDFs and Spreadsheets Puzzle Exercise

Let's test your skills, the files needed for this puzzle exercise

You will need to work with two files for this exercise and solve the following tasks:

    Task One: Use Python to extract the Google Drive link from the .csv file. (Hint: Its along the diagonal from top left to bottom right).
    Task Two: Download the PDF from the Google Drive link (we already downloaded it for you just in case you can't download from Google Drive) and find the phone number that is in the document. Note: There are different ways of formatting a phone number!

 """

import os
import csv
import re
import requests
import bs4
import PyPDF2

cwd = os.getcwd()
walk = list(os.walk(cwd))
#print(cwd)
csv_files = []
pdf_files = []
for folder,sub_folder,files in walk:
    #print('---')
    #print(f'Folder: {folder}')
    #print(f'Sub-Folders: {sub_folder}')
    #print(f'Files: {files}')
    for f in files:
        if '.csv' in f:
            csv_files.append(folder+'\\'+f)
        if '.pdf' in f:
            pdf_files.append(folder+'\\'+f)
#print(f'The CSV files are:\n{csv_files}')
#print(f'The PDF files are:\n{pdf_files}')

f_csv = open(csv_files[2],encoding='utf-8')
csv_data = csv.reader(f_csv)
print(type(csv_data))
csv_lines = list(csv_data)
f_csv.close()
#print(csv_lines)
web_pages = ''
#match_d = re.findall(r'\w\w+',str(data))
""" i = 0
for line in csv_lines:
    if i < len(line):
        web_pages += str(line[i])
    i += 1 """
for num,line in enumerate(csv_lines):
    web_pages += line[num]
print(web_pages)

#res = requests.get(web_pages)
#soup = bs4.BeautifulSoup(res.text,'lxml')
#print(soup)

f_pdf = open(pdf_files[3],'rb')
pdf_reader = PyPDF2.PdfReader(f_pdf)
print(len(pdf_reader.pages))
#print(type(pdf_reader))
pdf_text = []
for num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[num]
    pdf_text.append(page.extract_text())
f_pdf.close()
match_pdf = re.findall(r'\s\d\d\d+|\W\d\d\d+',str(pdf_text))
match_pdf2 = re.findall(r'\d\d\d\W\d\d\d\W\d\d\d\d|\d\d\d\s\d\d\d\s\d\d\d\d',str(pdf_text))
print('--------------')
print(match_pdf)
print(match_pdf2)



