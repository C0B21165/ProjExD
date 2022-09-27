import random

tai = 7
kes = 2

zennbu = [
    "A","B","C","D","E","F","G","H","I","J","K","L","M",\
    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
    ]

taisyou = (random.sample(zennbu, tai))#26文字からsampleでとる
(random.shuffle(taisyou))
print("対象文字:", end = "")
for i in taisyou:
    print(i + " ", end = "")
print("")

a = (random.sample(taisyou, kes))
b = a[0]
c = a[1]



result = list(set(taisyou) - set(a))

print("表示文字:", end = "")
for j in result:
    print(j + " ", end = "")

print("")
count = 0
while count < 11:
    ans1 = int(input("欠損した文字数は？"))
    if ans1 == kes:
        print("正解です！では欠損文字は何でしょうか？一文字ずつ答えてください。")
        break
    else:
        print("不正解") 
        count += 1
        continue
count = 0
while count < 11:
    ans2 = input("一つ目")
    if ans2 == b:
        print("正解")
        break
    else:
        print("不正解。もう一回。")
count = 0
while count < 11:
    ans3 = input("二つ目")
    if ans3 == c:
        print("正解")
        break
    else:
        print("不正解。もう一回。")