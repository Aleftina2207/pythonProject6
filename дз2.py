# задание1
li = (60, 60.5, 'orange', 'melon')
print(type(li))

# задание2
li = [10, 11, 12, 13]
l1 = len(li)
for el in range(0,l1,2):
    if el != l1-1:
        li[el], li[el+1] = li[el+1], li[el]

print(li)

# задание3
dic = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
n = int(input('месяц:'))
for elem in dic:
    if n in dic[elem]:
        print(elem)


# задание 4
s1 = 'Children'
s2 = 'likes'
s3 = 'a'
s4 = 'melon'
print(s1)
print(s2)
print(s3)
print(s4)
for ind, el in enumerate (['Children', 'likes', 'a', 'melon']):
    print(ind,el)


