import sys
import time

def compare_string_with_equality(n):
    word1='a long string that is not interned'*200
    word2='a long string that is not interned'*200
    for i in range(n):
        if word1==word2:
            pass
def compare_string_with_interning(n):
    word1=sys.intern('a long string that is interned'*200)
    word2=sys.intern('a long string that is interned'*200)
    for i in range(n):
        if word1 is word2:
            pass

start=time.perf_counter()
compare_string_with_equality(10000000)
end=time.perf_counter()
print('equality: ',end-start)

start=time.perf_counter()
compare_string_with_interning(10000000)
end=time.perf_counter()
print('Interning with is:',(end-start))
