#movies=["movie1", 1985, 4, "cast", ["pankaj", "thakur", "subcast", ["this", "is", "nice", ["I", "am", "amazing", ["and", "that", "is", "correct"]]]]]
movies=["1", 2, 3, "4", ["5", "6", "7", ["8", "9", "10", ["11", "12", "13", ["14", "15", "16", "17"]]]]]
print(movies)

for each_item in movies:
    print(each_item)

for each_item in movies:
    if isinstance(each_item,list):
        for sub_each_item in each_item:
            print(sub_each_item)
    else:
        print(each_item)

print("--------------------------")

def _loop_solver(obj):
    if isinstance(obj,list):
        for loop_list_item in obj:
            _loop_solver(loop_list_item)
    else:
        print(obj)

_loop_solver(movies)

"""comment"""
#comment
'comment'
        
