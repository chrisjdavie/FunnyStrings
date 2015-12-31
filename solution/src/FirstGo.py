'''
Solving the hackerrank Funny String puzzle

https://www.hackerrank.com/challenges/funny-string

------------------------

Problem Statement

Suppose you have a string S that has the length N. It is indexed from 0 to N-1. String R is the reverse of string S. The string S is funny if the condition |Si-Si-1|=|Ri-Ri-1| is true for every i from 1 to N-1.

Note: Given a string str, stri denotes the ascii value of the ith character (0-indexed) of str. Here, |x| denotes the absolute value of an integer x.

Input Format

The first line of input will contain an integer T, the number of test cases. Each of the next T lines contains one string S.

Constraints

1<=T<=10
2<=length of S<=10000
Output Format

For each string, print Funny or Not Funny on separate lines.

------------------------

Could be made a little tighter by not copying the string in reverse
and using the indicies, but I think this is clearer 

Created on 31 Dec 2015

@author: chris
'''

for _ in range(input()):
    inputString = raw_input().strip()
    reverse = inputString[::-1]
    funny = True
    for i in range(1,len(inputString)):
        lhs = abs(ord(inputString[i])-ord(inputString[i-1]))
        rhs = abs(ord(reverse[i])    -ord(reverse[i-1]))
        if lhs != rhs:
            funny = False
    if funny:
        print "Funny"
    else:
        print "Not Funny"