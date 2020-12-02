# 猜數字
import random  # 隨機輸入4位數字
list = ""  # 用來儲存生成的隨機數
for i in range(4):  # 正要產生4位數字
    j = random.randrange(0, 4)  # 先產生四種數字
    a = random.randrange(0, 10)  # 再寫入它的值
    list = list + str(a)
b = 0  # b的初始值是0
c = 0  # c的初始值是0
while 1:
    enterNum = input("請輸入您猜的四位數字:")
    if not enterNum.isdigit():      # 若輸入非數字，則要重新輸入
        continue
    if len(enterNum) != 4:          # 若輸入數字不是四個，則要重新輸入
        continue
    if enterNum == list:          # 若輸入數字與答案一樣，則輸出結果，結束迴圈
        print("恭喜您猜對了!")
        break
    for i in range(4):
        for j in range(4):
            if j == i and enterNum[j] == list[i]:
                b += 1              # 若數字與位置都正確，則a+1
            elif enterNum[j] == list[i]:
                c += 1              # 若數字正確、位置不正確，則b+1
    print(b, "A", c, "B")
    b = 0                           # a重置為0
    c = 0                           # b重置為0
