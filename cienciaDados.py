import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# read the data base (as csv archive)
table = pd.read_csv('advertising.csv')
print(table)
graph = sns.heatmap(table.corr(), annot=True, cmap='Wistia')
plt.show()

# beginning of the machine learning process for data base analysis
y = table['Vendas']
x = table[['TV', 'Radio', 'Jornal']]
x_training, x_test, y_training, y_test = train_test_split(x, y, test_size = 0.3)

linear_regression = LinearRegression()
tree = RandomForestRegressor()

# trains the IA
linear_regression.fit(x_training, y_training)
tree.fit(x_training, y_training)

# tests the IA score
preview_linear_regression = linear_regression.predict(x_test)
preview_tree = tree.predict(x_test)
print(r2_score(y_test, preview_linear_regression))
print(r2_score(y_test, preview_tree))

# makes a new prediction
new = pd.read_csv('novos.csv')
preview = tree.predict(new)
print(preview)