import string
import time
def my_func():
    a=a*b
    b=(1,5)*5
    c='abc'*3
    d='ab'*11
    e='the quick brown fox'*5
    f=['a','b']*3
    g=60*40

print(my_func.__code__.co_consts)

print('using string libarary to print ascii letters: ')

print(string.ascii_letters)
char_list=list(string.ascii_letters)
char_tuple=tuple(string.ascii_letters)
char_set=set(string.ascii_letters)

print('Character\'s List: \n',char_list)
print('tuple\'s character\'s \n',char_tuple)
print('set\'s character\'s \n',char_set)

def membership_check(n,container):
    for i in range(n):
        if 'z' in container:
            pass

start=time.perf_counter()
membership_check(10000000,char_set)
end=time.perf_counter()
print('time taken for set:',end-start)
