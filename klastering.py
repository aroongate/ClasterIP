import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import parse

raw_data = pd.read_csv("hackathon.csv", delimiter=";")
print(len(raw_data))

arr = np.array(raw_data)

date = arr[:,1]
okvd = arr[:,3]
region = arr[:,2]
region = np.array([x.lower() if isinstance(x, str) else x for x in region])
regionU = np.unique(region)
industry = arr[:,4]
industry = np.array([x.lower() if isinstance(x, str) else x for x in industry])
industryU = np.unique(industry)
selection = arr[:,5]
selection = np.array([x.lower() if isinstance(x, str) else x for x in selection])
selectionU = np.unique(selection)
for i in range(0, len(date)):
    date[i] = date[i].replace('-', '')
    okvd[i] = okvd[i].replace('.', '')
print(date, okvd)
arr[:,1] = date
del date

for i in range(0, len(regionU)):
    for elem in np.where(region == regionU[i].lower()):
        region[elem] = i
print(region)
arr[:,2] = region
del region

for i in range(0, len(industryU)):
    for elem in np.where(industry == industryU[i].lower()):
        industry[elem] = i
print(industry)
arr[:,4] = industry
del industry

for i in range(0, len(selectionU)):
    for elem in np.where(selection == selectionU[i].lower()):
        selection[elem] = i
print(selection)
arr[:,5] = selection
del selection


print(arr)

true_k = 5
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=1000, n_init=5)

arr = np.delete(arr, -1, axis=1)
model.fit(pd.DataFrame(arr))
labels = model.labels_
print(len(model.labels_))

raw_data.insert(6, "", model.labels_)
raw_data.to_csv('export.csv', index=False, sep = ";", encoding="windows-1251")