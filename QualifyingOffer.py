import requests
import heapq
from bs4 import BeautifulSoup

URL = 'https://questionnaire-148920.appspot.com/swe/data.html'
r = requests.get(URL)
# Used this resource as an intro to beautiful soup, I'd heard of it before but never used it. This was so fun!
# https://stackabuse.com/guide-to-parsing-html-with-beautifulsoup-in-python/

soup = BeautifulSoup(r.content, 'html5lib')
salaries = (soup.findAll('td', {'class': 'player-salary'}))
# Used this YouTube video to learn how to use findAll()
# https://www.youtube.com/watch?v=Fin_f2uqmK4

salaryInt = []
for salary in salaries:
    s = ""
    string = str(salary)
    for x in range(26, len(string)):
        if (string[x] == '0' or string[x] == '1' or string[x] == '2' or string[x] == '3' or string[x] == '4' or
        string[x] == '5' or string[x] == '6' or string[x] == '7' or string[x] == '8' or string[x] == '9'):
            s = s + string[x]

    if s == "":
        continue
    else:
        salaryInt.append(float(s))


qoPlayers = heapq.nlargest(125, salaryInt)
# Used this resource to learn how to get the top 125, I would've used a for loop if I didn't have this
# https://stackoverflow.com/questions/16878715/how-to-find-the-index-of-n-largest-elements-in-a-list-or-np-array-python

sum = 0
for i in qoPlayers:
    sum += i

totalSalary = "{:,.2f}".format(sum)
offer = "{:,.2f}".format(sum/125)
# Used this resource to learn how to add comments between each three digits
# https://stackoverflow.com/questions/36626017/format-a-number-with-comma-separators-and-round-to-2-decimal-places-in-python-2


print('The qualifying offer for this season is: $%s' %offer)
print('The 125 highest paid players in the MLB made $%s last season' %totalSalary)