# read pkl file
import pickle
import numpy as np
cache_file = '/Users/onesixx/my/git/BatteryML0/batteryml/data/processed0/MATR/MATR_b1c0.pkl'




with open(cache_file, 'rb') as f:
    dataset = pickle.load(f)

type(dataset)
dataset.keys()
len(dataset.keys())
# 각 key 별 데이터 건수
for key in dataset.keys():
    print(key, len(dataset[key]))


import pickle
import numpy as np

# 예제 데이터 생성
data = {
    'array1': np.random.rand(100),
    'array2': np.random.rand(200),
    'array3': np.random.rand(300)
}

# pickle 파일 경로
output_file = '/Users/onesixx/my/git/BatteryML0/batteryml/data/test.pkl'

# 데이터를 pickle 파일로 저장
with open(output_file, 'wb') as f:
    pickle.dump(data, f)

print(f"Data has been successfully saved to {output_file}")

with open(output_file, 'rb') as f:
    dataset = pickle.load(f)