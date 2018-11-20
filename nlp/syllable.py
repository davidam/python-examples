import pyphen
dic = pyphen.Pyphen(lang='en')
print(dic.inserted('Rohit'))
print(dic.inserted('xxxx'))
dic = pyphen.Pyphen(lang='es')
print(dic.inserted('Gema'))
print(dic.inserted('David'))
