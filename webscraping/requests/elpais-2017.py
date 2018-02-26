# -*- coding: utf-8 -*-

import requests


#https://elpais.com/hemeroteca/elpais/2017/01/01/m/portada.html

list = []
for i in range(1, 13):
    if (i < 10):
        i = "0" + str(i)
    for j in range(1, 32):
        if (j < 10):
            j = "0" + str(j)
        url = "https://elpais.com/hemeroteca/elpais/2017/"+str(i)+"/"+str(j)+"/m/portada.html"
        list.append(url)
        res = requests.get(url)
        print("https://elpais.com/hemeroteca/elpais/2017/"+str(i)+"/"+str(j)+"/m/portada.html")
        file = open("elpais-2017-"+str(i)+"-"+str(j)+".html", "w")
        file.write(res.text) 

        
# url =  'http://www.gnu.org'
# page = requests.get(url)
# soup = BeatifulSoup(page.text, 'html.parser')
