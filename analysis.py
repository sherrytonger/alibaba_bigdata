 # -*- coding: utf-8 -*-

import codecs


filepath = 'dataset/'
usr_file = filepath+'user_profile_table.csv'
usr_balance = filepath+'user_balance_table.csv'
usr_share = filepath+'mfd_day_share_interest.csv'
bank_file = filepath+'mfd_bank_shibor.csv'


usr_info = []
balance_info = []
share_info = []
bank_info = []
#
# print 'loading file.....'
# cnt = 0
# with codecs.open(usr_file,encoding = 'utf-8') as U:
#     for u in U:
#         s = u.split(',')
#         usr_info.append(s)
#
# usr_info = usr_info[1:]
#
#
# print 'finish loading...'
#
# print '---------------------------analysis----------------------------------'
# print 'the total number of usr = ',len(usr_info)
#
#
# print 'analysis usr sex'
# male = 0
# female = 0
#
# city = {}
# xingzuo = {}
# for i in usr_info:
#     if i[1] == '1': male += 1
#     else: female += 1
#     if i[2] in city:
#         city[i[2]] += 1
#     else: city[i[2]] = 1
#     if i[3] in xingzuo:
#         xingzuo[i[3]] += 1
#     else: xingzuo[i[3]] = 1
#
# print 'male = ', male
# print 'female = ', female
#
# print 'the number of city = ',len(city)
# print city
# print
# for i in xingzuo:
#     print i,xingzuo[i]
#

print '-------------------------usr_balance----------------------------'
in_file = open('in.txt','w')
out_file = open('out.txt','w')

print 'loading file.............'
with codecs.open(usr_balance, encoding = 'utf-8') as B:
    for b in B:
        s = b.split(',')
        balance_info.append(s)

balance_info = balance_info[1:]
print 'finishing ..........'
print 'counting..........'
balance_in = {}
balance_out = {}
for i in balance_info:
    if i[1] in balance_in:
        balance_in[i[1]] = float(i[4]) + float(balance_in[i[1]])
        balance_out[i[1]] = float(i[8]) + float(balance_out[i[1]])
    else:
        balance_in[i[1]] = float(i[4])
        balance_out[i[1]] = float(i[8])
print 'counting done.........'
print 'writing into files.........'
for i in balance_in:
    in_file.write('%s\t%s\n'%(i, balance_in[i]))
for j in balance_out:
    out_file.write('%s\t%s\n'%(j, balance_out[j]))
print 'done!'

in_file.close()
out_file.close()

