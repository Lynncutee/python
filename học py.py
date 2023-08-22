n = input(" hãy nhập mật khẩu ")
x = bool
y = bool # kiểu true hoặc false 
for i in n:
    if i.isdigit():
        x =True 
        break # nó sẽ thoát luôn 
    else: 
        x =False
for i in n: 
    if i.isalpha():
        y = True 
        break 
    else:
        y = False # True và False phân biệt chữ hoa và chữ thường
print(x,y)
while len(n) <= 6 or x ==False or y ==False:
    n = input(" hãy nhập lại mật khẩu phải bao gồm 1 số hoặc 1 ký tự: ")
else: 
    print(" mật khẩu hợp lệ") 

# mở rộng 
s = input(" mời nhập mật khẩu dăng nhập lại hệ thống ")
dem = 0
while s != n:
    dem += 1
    s = input(f" nhập lại mật khẩu, nhập sai {dem}/5 lần: ")
    if dem == 5:
        print(" bạn nhập sai mật khẩu quá 5 lần, khóa đăng nhập ")
else: 
    print(" đăng nhập thành công")