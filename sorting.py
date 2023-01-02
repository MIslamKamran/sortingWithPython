num = [3,5,2,8,3,2,8,2,"islam","kamran","khan","aaaaa"]
def mixs(num):
    try:
        ele = int(num)
        return (0, ele, '')
    except ValueError:
        return (1, num, '')
num.sort(key=mixs)

print(num)