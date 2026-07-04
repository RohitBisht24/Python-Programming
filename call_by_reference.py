def test(x):
    x.append(10)
    print("Function  value : ",x)


a = [1, 2, 3, 4]
print("original : ",a)
b = a.copy()
test(b)

print("next value : ",a )
