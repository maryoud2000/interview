# for n is an input in range 1 - 10 and n is an integer, the output result shoud be as string (ONE, TWO, THREE, ...).. 
# if out of this range the output = OTHER

def numberToWord(num):
    converted_num ={0:"ZERO",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten"}
    if num in converted_num.keys():
        result = converted_num[num]
        # result = num2words(num)
    else:
        result = "OTHER"
    return result

print(numberToWord(11))
