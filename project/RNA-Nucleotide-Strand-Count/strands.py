#!/usr/bin/env python3

def rna_strand_count(test_string,sub_string):
    test_string = test_string.replace(' ','').upper()    
    sub_string = sub_string.replace(' ','').upper()    
    first = sub_string[0]
    second = sub_string[1:]
    return {sub_string:len(re.findall(r'{0}(?={1})'.format(first,second),test_string))}


print rna_strand_count('AAAA', ['AA']) {'AA': 3}
