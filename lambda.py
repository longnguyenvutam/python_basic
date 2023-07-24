"""
Ham an danh nho 
1 ham lambda co the nhan nhieu doi so nhung chi co 1 bieu thuc

"""

#Cu phap: lambda arguments : expression

#Vi du
kiemTraSoChan = lambda a : (a%2==0)
print(kiemTraSoChan(5))

#Lambda trong function

def hamMu(n):
    return lambda x : x**n

hamMu2 = hamMu(2)
hamMu3 = hamMu(3)
hamMu4 = hamMu(4)

print(hamMu2(3))
print(hamMu3(3))
print(hamMu4(3))