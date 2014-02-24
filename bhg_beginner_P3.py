# -*- coding: utf-8 -*- #
""" #
Given a file containing a list of dictionaries implement a sorting algorithm (of your choosing) #
that will sort the list based on the dictionary keys. #
The dictionary keys will contain alphabetic characters while the values will be integers #
""" #

def read_dicts(file_path): #
    result = [] #
    with open(file_path,'r') as f: #
        for line in f: #
            d = {} #
            vals = line.strip().split(' ') #
            for i in range(0,len(vals),2): #
                d[vals[i]] = vals[i+1] #
            result.append(d) #
            #result.append(collections.OrderedDict(sorted(d.iteritems()))) #
    return result #


def sort_dicts(dicts): #
    def _compare(d1, d2): #
       for k1 in sorted(d1.iterkeys()): #
           if k1 in d2: #
               return int(d1[k1]) - int(d2[k1]) #
       return 0 #


    return sorted(dicts, cmp=_compare) #

print '#'*40 #
dicts = read_dicts('dicts_file.txt') #
print dicts #
print '-'*40 #
print sort_dicts(dicts) #
print '#'*40 #