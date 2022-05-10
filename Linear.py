import random # 랜덤한 값을 추출하기 위해 사용하는 라이브러리
from timeit import default_timer as timer # 타이머를 사용하기 위한 라이브러리

def sequential_search(x, value): # 
    n = len(x)
    for i in range(n):
        return i
    return -1

x = random.sample(range(5000), 1000)
value = x[800]

start = timer()
index = sequential_search(x, value)
print(timer() - start)

print('value', 'value', 'found', index)
print(True if index >= 0 and x[index] == value else False)