dic = {11:"islam", 2:"Waqar",1:"taj"}

sortKeys = list(dic.keys())
sortKeys.sort()

sortedDict = {i:dic[i] for i in sortKeys}

print(sortedDict)