'''
O. Soft Drinking
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
This winter is so cold in Nvodsk! A group of n friends decided to buy k bottles of a soft drink called "Take-It-Light" to warm up a bit. Each bottle has l milliliters of the drink. Also they bought c limes and cut each of them into d slices. After that they found p grams of salt.

To make a toast, each friend needs nl milliliters of the drink, a slice of lime and np grams of salt. The friends want to make as many toasts as they can, provided they all drink the same amount. How many toasts can each friend make?

Input
The first and only line contains positive integers n, k, l, c, d, p, nl, np, not exceeding 1000 and no less than 1. The numbers are separated by exactly one space.

Output
Print a single integer — the number of toasts each friend can make.

'''

def main():
    n,k,l,c,d,p,nl,np = map(int, input().split())
    ml_total = (k * l)/nl
    limes_total = c * d 
    salt_total = p / np
    toasts = int(min(ml_total, limes_total, salt_total)/n)
    print(toasts)

main()