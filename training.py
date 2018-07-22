import pandas as pd
import numpy as np
from sklearn import preprocessing
import csv


def fixText(text):
    row = []
    z = text.find(',')
    if z == 0:  row.append('')
    else:   row.append(text[:z])
    for x in range(len(text)):
        if text[x] != ',':  pass
        else:
            if x == (len(text)-1):  row.append('')
            else:
                if ',' in text[(x+1):]:
                    y = text.find(',', (x+1))
                    c = text[(x+1):y]
                else:   c = text[(x+1):]
                row.append(c)
    return row

def createTuple(oldFile):
    f1 = open(oldFile, "r")
    tup = []
    first_row_processed = False
    while 1:
        text = f1.readline()
        if text == "":  break
        else:   pass
        if text[-1] == '\n':
            text = text[:-1]
        else:   pass
        row = fixText(text)
        if first_row_processed == True:
            tup.append(row)
        first_row_processed = True
    # print (type(tup))
    # print (tup)
    return tup



def addMetadata(csv_array, fileName):
    rows=len(csv_array)
    atts=len(csv_array[0])-1
    metadata=[]
    metadata.extend((rows,atts,0,1))
    print([metadata])
    print(type(csv_array))
    csv_array=[metadata]+csv_array

    with open('./' + fileName + '.csv' ,"w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(csv_array)


# Load data
FILE_PATH = "./bank-full.csv"
data = pd.read_csv(FILE_PATH)
# Variables names
var_names = data.columns.tolist() #stores the values of the top row (the headings as you might call them)

#Removing the variables (there will be 2 types- 1. Categorical-those having non number values 2. Quantitative-Numerical Values)
# Categorical vars
categs = ['job','marital','education','housing', 'loan']
# Quantitative vars
quantit = [i for i in var_names if i not in categs]
print ("quantit")
print (quantit)

job = pd.get_dummies(data['job'])
marital = pd.get_dummies(data['marital'])
education = pd.get_dummies(data['education'])
housing = pd.get_dummies(data['housing'])
loan = pd.get_dummies(data['loan'])



# Map variable to predict
dict_map = dict()
y_map = {'yes':1,'no':0}


# dict_map['y'] = y_map
# print (dict_map)
# data['y'].map(dict_map)
# data.replace(dict_map)
data.y = [y_map[item] for item in data.y]
label = data['y']
# print ("*****")
# print (label)

df1 = data[quantit]
df1_names = df1.keys().tolist()
# print (df1_names)

# Scale quantitative variables
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(df1)
df1 = pd.DataFrame(x_scaled)
df1.columns = df1_names

# Get final df
final_df = pd.concat([df1, job, marital, education, housing, loan, label], axis=1)

print (type(final_df))
final_df[:-5].to_csv('./NormalizedTrainingData.csv', index = False)
final_df.tail(5).to_csv('./NormalizedTestData.csv', index = False)

addMetadata(createTuple('./NormalizedTrainingData.csv'), 'Training')
addMetadata(createTuple('./NormalizedTestData.csv'), 'Testing')