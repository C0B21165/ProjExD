import random



if __name__== "__main__":

    quizlst = {
        "サザエの旦那の名前は？":{"まずお","マスオ"},
        "カツオの妹の名前は？":{"わかめ","ワカメ"},
        "タラオはカツオから見てどんな関係？":{"甥っ子","甥"}
        }


z = random.choice(quizlst)
print(z)

