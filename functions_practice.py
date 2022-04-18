def hello():
print("Hello, user!")

def pack(maria, jose, teresa):
    return[maria, jose, teresa]

def eat_lunch(my_list):
    if len(my_list) == 0:
        print("my lunchbox is empty!")
    else:
        for i in range(len(my_list)):
            if i==0:
                print(f"First i eat {my_list[0]})
            else:
                 print(f"Next I eat {my_list[i]}")


