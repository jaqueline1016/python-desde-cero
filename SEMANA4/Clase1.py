# variable scope 
# scopoe resolution

def func1():
    x = 10
    print("Inside func1, a =", x)

def func2():
    x = 20
    print("Inside func2, b =", x)

func1()
func2()

