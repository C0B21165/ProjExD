import random

tai = 7
kes = 2

zennbu = [
    "A","B","C","D","E","F","G","H","I","J","K","L","M",\
    "N","O","P","Q","R","S","T","U","V","v","W","X","Y","Z"
    ]

taisyou = ["A", "F", "D", "G", "H", "S","W"]#26文字からsampleでとる
(random.shuffle(taisyou))
print("対象文字:", end = "")
for i in taisyou:
    print(i + " ", end = "")
print("")

a = (random.sample(taisyou, kes))

result = list(set(taisyou) - set(a))

print("欠損文字:", end = "")
for j in result:
    print(j + " ", end = "")

