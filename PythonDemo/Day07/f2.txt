import os


def rwFile():
    with open("f1.txt", "r+", encoding="utf-8") as fr:
        # 读取文件内容
        txt = fr.read()
        print(txt)

        while 1:
            info = input("请输入文件内容:")
            if not info:
                break
            fr.write(info + "\n")

        txt = fr.read()
        print(f"txt={txt}")

        os.system("notepad f1.txt")


if __name__ == "__main__":
    rwFile()
