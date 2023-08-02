from collections import Counter

"""
코드 구현
맨뒤에서 부터:

result = ""
len_a = len(a) -1
len_b = len(b) -1
counter = 0
carry_over = False

while counter >= len_a or counter >= len_b


if carry over = False:

    if both are 0:
    then 0:

    if both either is one:
    then 1:

    if both are one:
    then carry over:

if carry over = True:
    if both are 0:
    then 1

    if either is one:
    then 0 and another carry over

    if both are one:
    then 1 and another carry over

edge case:
when both are 0,0?
when both are 1?
    """


def addbinary(a,b):
    a=a[::-1]
    b=b[::-1]
    result = ''
    counter = 0
    carry_over = False
    

    if len(a) > len(b):
        longer_string = a
    else:
        longer_string = b

    shorter_length = min(len(a),len(b))
    longer_length = max(len(a),len(b))

    while counter < shorter_length:
        if carry_over == False:
            if a[counter] == '0' and b[counter] == '0':
                result += '0'
            elif a[counter] == '1' and b[counter] == '1':
                carry_over = True
                result += '0'
            else:# a[counter] == '1' or b[counter]=='1':
                result +='1'
        
        else: #if carry_over == True:
            if a[counter] == '0' and b[counter] == '0':
                carry_over = False
                result += '1'
            elif a[counter] == '1' and b[counter] == '1':
                result +='1'
            else:# a[counter] == '1' or b[counter]=='1':
                result +='0'

        counter += 1

    while counter < longer_length:
        if carry_over == True:
            if longer_string[counter]== '1':
                result += '0'
            else: # a[counter] or b[counter] == '0':
                carry_over = False
                result += '1'
        
        else:
            #carry_over == False:
            if longer_string[counter] == '1':
                result += '1'
            else:
                result += '0'
        counter += 1

    if carry_over == True:
        result += '1'

    return result[::-1]

if __name__=="__main__":
    print(addbinary('110010','11'))

    
        


