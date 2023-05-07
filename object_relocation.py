import os

dir1 = 'C:\\Users\XLR8\\Documents'
key = ['PPTX', 'DOCX', 'PDF']

for keys in key: 
    newpath = f'{dir1}\{keys}' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    for files in os.listdir(dir1):
        if keys in files.upper() and files != keys:
            print(files)
            os.replace(f'{dir1}\{files}', f'{dir1}\{keys}\{files}')
