from re import A


def hello():
    print("hello there")

#hello()

def pack(arg1, arg2, arg3):
    my_pack = [arg1, arg2, arg3]
    return my_pack

#pack("CPU", "GPU", "RAM")

def eat_lunch(list):
    if not list:
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {list[0]}")
        print(f"Next I eat {list[1]}")

my_lunch = ["ham", "bacon"]
not_my_lunch = []
#eat_lunch(my_lunch)
