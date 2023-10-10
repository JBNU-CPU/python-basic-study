# 단어 횟수 세기 : 텍스트 파일에서 각 단어가 얼마나 자주 나오는지 세는 프로그램 작성
#
# 파일 : 함께 올려둔 a.txt 참조
#
#
# 작성자 : 김지훈 (xxxjjhhh@naver.com)
# 일시 : 2023.10.10

def openFile():

    file = open("a.txt", 'r')

    return file

def closeFile(file):

    file.close()

def countWord(wordList):

    dic = dict()
    for word in wordList:

        try: dic[word] = dic[word] + 1
        except: dic[word] = 1

    return dic

def main():
    
    file = openFile()

    context = file.read()
    wordList = context.split()

    dic = countWord(wordList)

    print(dic)

    closeFile(file)


if __name__ == "__main__":
    main()
