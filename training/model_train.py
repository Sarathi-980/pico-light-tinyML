import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text

data=pd.read_csv("dataset/light_dataset.csv")

x = data[["raw_adc"]]
y = data[["label"]]

model = DecisionTreeClassifier(max_depth=2)

model.fit(x, y)

print(export_text(model, feature_names=["raw_adc"]))