import os
import shutil
import re

file_directory = os.getcwd()
print(file_directory)
print(os.listdir())

file_read = open(file_directory+'\\puzzle.txt','r')
file_read.seek(0)
print('\n')
print(file_read.read())
file_read.close()

#Executed just once:
shutil.unpack_archive('unzip_me_for_instructions.zip',file_directory+'\\unziped_instructions')

walk = (tuple(os.walk(file_directory,True)))
#print(walk)
for folders,sub_folders,files in walk:
    print(f'---{folders}')
    print(f'\t{sub_folders}')
    serch = re.search('ins',str(files).lower())
    if serch != None:
        print(f'\t{files}')

file_read = open(file_directory+'\\unziped_instructions\\extracted_content\\Instructions.txt','r')
file_read.seek(0)
print('\n')
print(file_read.read())
file_read.close()

directory = os.getcwd()
phones = []
pattern = r'\d{3}-\d{3}-\d{4}'
for folders,sub_folders,files in walk:
    #print(type(files))
    #print(type(str(files)))
    #print(files)
    #print(str(files))
    for file1 in files:
        if '.txt' in str(file1):
            file_direc = (str(folders))+'\\'+(str(file1))
            open_files = open(file_direc,'r')
            open_files.seek(0)
            read_file = open_files.read()
            open_files.close()
            #print(read_file)
            matches = re.findall(pattern,read_file)
            phones.extend(matches)
            if matches != []:
                for match in matches:
                    print(f'\nThe phone {match} are in the directory:')
                    print(file_direc)
print('\nThe serched phones with format ###-###-#### are:')
print(phones)