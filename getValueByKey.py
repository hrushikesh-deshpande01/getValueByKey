#object = {"x":{"y":{"z":"a"}}}

object = {"a":{"b":{"c":"d"}}}
key="c"

flag=False

def function_1(obj,key,flag):

    for k,v in obj.items():
        if key in k:
            flag=True
        if type(v)==dict:
            return function_1(v,key,flag)
        else:
            if flag:
                return obj[k]
            else:
                return 'key not found'

if type(object)==dict:
    print(function_1(object,key,flag))
else:
    print("Please provide a valid input of type dict")