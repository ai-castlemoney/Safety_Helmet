import os
import pandas as pd

files = os.listdir('C:/Users/김민주/project/Safety_Helmet/add_MS_Column/google_sheet')


for i in range(len(files)):
    file_name = files[i].split('.')[0]
    xlsx = pd.read_excel('C:/Users/김민주/project/Safety_Helmet/add_MS_Column/google_sheet/' + file_name + '.xlsx')
    xlsx.to_csv('C:/Users/김민주/project/Safety_Helmet/add_MS_Column/csv/' + file_name + '.csv')

print("Done!!")