from pathlib import Path
import requests

# string method test
title = "TEAMLAB X Upstage"
print(title.find("TEAMLAB"))  # 0

# YesterDay

# 파일 다운로드
file_path = Path() / "yesterday.txt"

if not file_path.exists():
    response = requests.get("https://raw.githubusercontent.com/TeamLab"
                            + "/introduction_to_python_TEAMLAB_MOOC/master/code/6/yesterday.txt")

    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)

        print(f'파일이 다운로드 되었습니다: {file_path}')
    else:
        print(f'파일 다운로드 실패. 응답 코드: {response.status_code}')

f = open("yesterday.txt", 'r')
yesterday_lyric = ""

while True:
    line = f.readline()
    if not line:
        break

    yesterday_lyric = yesterday_lyric + line.strip() + "\n"

f.close()

print(yesterday_lyric)

# n_of_yesterday = yesterday_lyric.upper().count("YESTERDAY")  # 대소문자 구분 제거
n_of_Yesterday = yesterday_lyric.count("Yesterday")
n_of_yesterday = yesterday_lyric.count("yesterday")
print("Number of a Word 'Yesterday'", n_of_Yesterday)
print("Number of a Word 'yesterday'", n_of_yesterday)

# factorial - for 문 구현
base_num = int(input("factorial input : "))
factorial_num = 1
for i in range(base_num,0,-1):
    factorial_num = factorial_num * i

print(factorial_num)
