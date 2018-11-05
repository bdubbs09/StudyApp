n = 1
count = 0
while(n>0):
    remainder = n%10
    count = count + remainder
    n = n/10

print count
string = "racecar "






reverse = ''.join(reversed(string))
palindrome = filter(str.isalnum,string)

print palindrome, reverse

# print reverse
# if string.lower() == string[::-1]:
#     print True
# else:
#     print False


def reverse(x):
    if x < 0:
        x = abs(x)
        x = -1*int(str(x)[::-1])

    else:
        x = int(str(x)[::-1])

    return x

x = -12325
print reverse(x)

