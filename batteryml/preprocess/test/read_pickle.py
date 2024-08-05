# read pkl file
import pickle
cache_file = '/Users/onesixx/my/git/BatteryML0/batteryml/data/MATR/preprocess/MATR_b1c0.pkl'
with open(cache_file, 'rb') as f:
    dataset = pickle.load(f)

type(dataset)
dataset.keys()
len(dataset.keys())
# 각 key 별 데이터 건수
for key in dataset.keys():
    print(key, len(dataset[key]))