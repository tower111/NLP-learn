txt=open("D:\\Project\\NLP_Course\\bbc.txt",'r').read()
biaodian='''#$%^&*()'_+-,./<‘>="@{}[]\~'''
for item in biaodian:
    txt = txt.replace(item,' ').lower()
    words_list=txt.split(' ')
# print(words_list)

dic = {}

for word in words_list:
    if word not in dic.keys():
        dic[word]=1
    else:
        dic[word]+=1
print(dic)

#         if key_word in line:
#

#
# if a in txt:
#     print(a)


# for item in txt:

# hamlettext = gettext()
# words = hamlettext.split()
# counts = {}
# for word in words:
#     counts[word]=counts.get(word,0)+1
# items = list(counts.items())
# items.sort(key = lambda x:x[1],reverse = True)
# for i in range (10000):
#     word,count = items[i]
#     print("{} {}".format(count,word))
#     # print("{0:<10}{1:>5}".format(word, count))
#
# txt_