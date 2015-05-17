#!/usr/bin/env python
# coding=utf-8
import codecs

in_file = 'in.txt'
out_file = 'out.txt'

new_in = open('sorted_in.txt', 'w')
new_out = open('sorted_out.txt', 'w')
total_in = {}
total_out = {}
print 'loading in file............'
with codecs.open(in_file,encoding = 'utf-8') as I:
    for i in I:
        s = i.split('\t')
        total_in[s[0]] = s[1]
print 'finishing in file.......'

print 'loading out file..........'
with codecs.open(out_file, encoding = 'utf-8') as O:
    for o in O:
        s = o.split('\t')
        total_out[s[0]] = s[1]
print 'finishing out file........'

total_in = sorted(total_in.iteritems(),key = lambda d:d[0])
total_out = sorted(total_out.iteritems(), key = lambda d:d[0])

print 'writing files...........'
for i in total_in:
    new_in.write('%s\t%s'%(i[0], i[1]))


for j in total_out:
    new_out.write('%s\t%s'%(j[0], j[1]))
print 'finishing writing......'


