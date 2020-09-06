from googlesearch import search
query= "python"
for i in search(query,tld="co.in", num=10,stop=15,pause=2):
    print(i)