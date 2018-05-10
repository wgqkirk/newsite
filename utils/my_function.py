#!/user/bin/env.python
# _*_ coding;utf-8 _*_
def make_weight_list(userweight):
    my_func1 = lambda x: x != None
    userweight = list(filter(my_func1, userweight))
    print(userweight)
    return userweight

def make_bmi(userheight,userweight):

    def my_func2(x):
        value = (x / 2) / ((userheight / 100) * (userheight / 100))
        return round(value, 2)
    userbmi = list(map(my_func2, userweight))
    print(userbmi)
    return userbmi