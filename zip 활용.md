```python
lst = [[1,2,3],[4,5,6],[7,8,9]] 
for i in lst:
    print(i)
print('\n-----\n')
lst2 = zip(*lst) # transpose / 전치
for i in lst2:
    print(i)
print('\n-----\n')
lst3 = list(zip(*lst))[::-1] # 90도 회전 시계 반대 방향
for i in lst3:
    print(i)
print('\n-----\n')
lst4 = zip(*lst[::-1]) # 90도 회전 시계 반대방향
for i in lst4:
    print(i)
```

