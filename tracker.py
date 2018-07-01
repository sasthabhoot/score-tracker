import bs4 as bs
import urllib.request
import time
import matplotlib.pyplot as plt

crickbuzz = input('Copy and paste the crickbuzz score page url here: ')
print("")
max_limit = str(input('Limit the over (eg. 16.2): '))
print("")
temp = 'start'

ovs = []
runs = []
wicks = []

over = 0
while over != max_limit :
	sauce = urllib.request.urlopen(crickbuzz)
	soup = bs.BeautifulSoup(sauce,'lxml')

	rawscore = soup.find_all('span', class_='cb-font-20')
	score = rawscore[0].text
	if score != temp:
		print(score)
		split_score = score.split()
		over = split_score[2].replace("(","")
		ovs.append(over)
		run = split_score[1].split('/')
		runs.append(int(run[0]))
		wicks.append(run[1])
		temp = score

	time.sleep(15)

plt.plot(ovs, runs)
plt.xlabel('Overs')
plt.ylabel('Runs')
plt.title('Progress of run with overs')
plt.show()