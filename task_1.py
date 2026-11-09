str1 = '1h 45m,360s,25m,30m 120s,2h 60s'

str2 = [i.replace(' ', '') for i in str1.split(',')]

summ_minutes = 0


for i in str2:
    if 'h' in i:
        hours = int(i.split('h')[0])
        summ_minutes += hours * 60
        i = i.split('h')[1]
    if 'm' in i:
        minutes = int(i.split('m')[0])
        summ_minutes += minutes
        i = i.split('m')[1]
    if 's' in i:
        sec = int(i.split('s')[0])
        summ_minutes += sec // 60
        i = i.split('s')[1]
print('str1',str1," summ_minutes = ",summ_minutes)
    