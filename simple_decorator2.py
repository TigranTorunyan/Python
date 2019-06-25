from datetime import datetime
from decorators import repeat, timer

def not_during_the_night(func):
    def wrapper():
        print("Smth before func")
        if 7 <= datetime.now().hour <= 22:
            func()
        else:
            pass
        print("Smth after func")
    return wrapper

@not_during_the_night
def say_whee():
    print('Whee!')

#say_whee = not_during_the_night(say_whee)
'''
say_whee()
'''

'''Reusing decorators'''
#@do_twice
def say_whee():
    print('Whee!')

#say_whee()	


'''Decorating functions with arguments'''
@repeat(num_times = 2)
def greet(name):
   print("Hello, %s" % name)
   # return "Hello, %s" % name


greet("Maria")
greet('Vazgen')
'''
@timer
def waste_some_time(num_times):
    l = [x **2 for x in list(range(num_times))]
    return l

print(waste_some_time(6))
print(waste_some_time(1000))'''
