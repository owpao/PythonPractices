d1 = {'python':10, 'java':3 , 'c#':8, 'javascript':15}
d2 = {'java':10 , 'c++':10, 'c#':4, 'go':9, 'python':6}
d3 = {'erlang':5, 'haskell':2 , 'python':1, 'pascal':1}

result = {}
alldicts = [d1,d2,d3]
for dic in alldicts:
    for item in dic.keys():
        if item not in result:
            result[item] = dic[item]
        else:
            result[item] += dic[item]

print(result)



