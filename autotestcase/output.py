info={}
outfile = open('D:\hahaha\ky I nam 4\kiem thu va dam bao chat luong phan mem\AutoTestCase\output.txt','w') 
with open('D:\hahaha\ky I nam 4\kiem thu va dam bao chat luong phan mem\AutoTestCase\input.txt','r') as infile:
    for line in infile:
        player, outcome, date = (item.strip() for item in line.split(';', 2))
        #date = tuple(map(int, date.split('/')))
        info[player] = outcome,date

print 'info:'
for player in info.items():
    print player
a:[0; 10][11;20]