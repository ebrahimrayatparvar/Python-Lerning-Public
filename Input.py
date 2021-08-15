

# پیدا کردن بزرگترین عدد
#_num1 = int(input("adad num1 ra vared namayeid : "))
#_num2 = int(input("adad num2 ra vared namayeid : "))

#if _num1 > _num2 :
#    print("Num1 bozorgtar az Num2 mibashad")
#else:
#    print("Num2 bozorgtar az Num1 mibashad")



x = int(input("Enter X : "))
y = int(input("Enter Y : "))

print("\n--------------------------------------")
print("X =>" , x)
print("Y =>" , y)
print("--------------------------------------")
print("----------- Change Value -------------")
print("--------------------------------------")

#temp = x
#x = y
#y = temp

x = x + y
y = x - y
x = x - y

print("X =>" , x)
print("Y =>" , y)
print("--------------------------------------")

