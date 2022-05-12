import pandas as pd
import plotly.express as px

# read the csv archive
table = pd.read_csv('telecom_users.csv')
#print(table)

# delete useless information
newTable = table.drop('Unnamed: 0', axis=1) # axis = 0 row axis= 1 column
#print(newTable)

# data handling (empty rowns and cloumns)
# adjusting values in the wrong format
#print(newTable.info())
newTable['TotalGasto'] = pd.to_numeric(newTable['TotalGasto'], errors='coerce')
newTable['Churn'] = pd.to_numeric(newTable['Churn'], errors='coerce')
#print(newTable.info())
newTable = table.dropna(how='any', axis=0)
newTable = table.dropna(how='all', axis=1)
print(newTable.info())

# simple analysis
print(newTable['Churn'].value_counts())
print(newTable['Churn'].value_counts(normalize=True))

# complete analysis
#! using this method to plot the graph isn't working in VSCode editor, I couldn't find the problem, neither some fixes, it might work in Juyter Notebooks
#graph = px.histogram(newTable, x='TotalGasto', color='Churn')
#graph.show()
#for column in newTable.columns:
#    graph = px.histogram(newTable, x=column, color='Churn')
#    graph.show()