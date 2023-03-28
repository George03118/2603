def result (x, y):
    return (x+2)*(y-3)

def func(result):
    if result<0:
        s1 = "negative"
    else:
        s1 = "positive"
        return s1

    if __name__ =='__main__':
        print_hi('George')
        number = result(4,4)
        print (number)
        print(func(number))


