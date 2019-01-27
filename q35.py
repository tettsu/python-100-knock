#coding:utf-8

short_list = [1,2,3]
while True:
    value = input("Position [q to qui]? ")
    if value == "q":
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print("Bad index:", position)
    except Exception as other:
        print("something else broke:", other)