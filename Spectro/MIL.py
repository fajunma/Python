print('Hlw')
print('HLOX')
print('Matrox , Hello,paichusuo')
print('HLOO')

with open('temp.txt','w') as f:
    f.writelines('google')
    f.writelines('sina.com')
    f.write('www.baidu.com')

txtName = "codingWord.txt"
f=open(txtName, "a+")
for i in range(1,100):
    if i % 2 == 0:
        new_context = "C++" + '\n'
        f.write(new_context)
    else:
        new_context = "Python" + '\n'
        f.write(new_context)
f.close()


with open(txtName, 'r') as f:
    r = f.readlines()

for x in r:
    print(x)

