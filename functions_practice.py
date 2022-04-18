def hello():
    print("Hello, user!")


def pack(maria, jose, teresa):
    return[maria, jose, teresa]

def eat_lunch(my_list):
    if len(my_list) == 0:
        print("my lunchbox is empty!")
    else:
        for i in range(len(my_list)):
            item = "I eat {}".format(my_list[i])
            if i==0:
                print("First {}".format(item))
            else:
                 print("Next {}".format(item))


hello()
print(pack(1, 2, 3))
eat_lunch(["apple", "carrot", "tomato"])
eat_lunch([])
