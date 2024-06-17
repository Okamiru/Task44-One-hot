# import pandas  as pd
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

# print(data.head(20))

# data = pd.get_dummies(data, columns=['whoAmI'])

# print(data.head())


import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})


data['robot'] = 0
data['human'] = 0

# print(data.head())


for i in range(len(data)):
  if data['whoAmI'][i] == 'robot':
    data['robot'][i] = 1
  else:
    data['human'][i] = 1


data = data.drop('whoAmI', axis=1)

print(data.head(20))