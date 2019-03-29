#coding:utf-8

def hamming_distance(n,m):
    xor_binary = format( n ^ m , 'b')
    print(xor_binary.count('1'))
    
hamming_distance(32473294, 85634985)
