### 做科研立项用到的一个小工具，输入中文、英文回车生成列表
al = open('align.txt', 'w')

print('请按照提示输入，如果全部输入完成，请输入空格并连续敲击回车')

original = str(input('原文内容 '))
translation = str(input('英译 '))

print(original, '\n', translation, sep='')
print(original, '\n', translation, sep='', file=al)

while type(original) == str:
    original = str(input('原文内容 '))
    translation = str(input('英译 '))
    print(original, '\n', translation, sep='')
    print(original, '\n', translation, sep='', file=al)

    if original == ' ':
        break

print('输入完成！')

al.close()
