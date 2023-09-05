import random

# if 문의 숫자 및 문자가 있으면 True
if 0:
    print("Hello")
else:
    print("0")

# all & any
all([True, False, True])
any([True, False, True])

# 연습 문제
current_year = datetime.date.today().year
birth_year = int(input("당신이 태어난 년도를 입력하세요"))

age = (current_year - birth_year + 1)

if 26 >= age >= 20:
    print("대학생")
elif 20 > age >= 17:
    print("고등학생")
elif 17 > age >= 14:
    print("중학생")
elif 14 > age >= 8:
    print("초등학생")
else:
    print("학생이 아닙니다")

# Loop end condition
for i in range(5):
    print(i,)  # 쉼표 뒤에 쉼표 사용 가능

i = 0
while i < 10:
    if i > 5: break

    print(i, )
    i += 1

else:
    print("EOP")


# 연습 문제2
times_table = int(input("구구단 몇단을 계산할까요? \n"))
print(f"구구단 {times_table}단을 계산합니다.")
for i in range(1, 10):
    print(f"{times_table} X {i} = {times_table * i}")

# 십진수 --> 이진수
decimal = int(input("십진수 입력 : "))
results = ""

while decimal > 0:
    remainder = decimal % 2
    decimal = decimal // 2
    results = str(remainder) + results  # 역 순으로 값을 받음

print(results)

# 십진수 --> 이진수 (Debugging)
print("input decimal number: ", )
decimal = int(input())
result = ""
loop_counter = 0  # 루프 횟수

while decimal > 0:
    temp_decimal_input = decimal
    temp_result_input = result

    remainder = decimal % 2
    decimal = decimal // 2
    result = str(remainder) + result

    print("-----------", loop_counter, "loop value check -------- ")
    print("Initial decimal:", temp_decimal_input,  # 기존 값 출력
          ", Remainder:", remainder,  # 나머지 출력
          ", Initial result", temp_result_input)  # 기존 결과 값 출력

    print("Output decimal:", decimal,  # 나눈 몫 출력
          "Output result:", result)  # 결과 값 출력

    print("------------------------------------------------------")
    print("")

    loop_counter += 1

print("Binary number is", result)

# 숫자 찾기 게임
# 1 ~ 100 임의의 숫자를 맞추시오

answer = random.randint(1, 101)
guess = -100

print("숫자를 맞춰보세요 (1 ~ 100)")
while guess != answer:
    guess = int(input())

    if guess > answer:
        print("숫자가 너무 큽니다")
    elif guess < answer:
        print("숫자가 너무 작습니다")
    else:
        print(f"정답 입니다. 입력한 숫자는 {guess}입니다.")

#연습 문제3

while 1:
    print("구구단 몇 단을 계산할까요 (1~9)")
    dan = int(input())

    # 0 입력 시 죵료
    if dan == 0:
        print("구구단 게임을 종료합니다")
        break

    # 1 ~ 9 이외의 숫자 라면 다시 입력
    if 9 < dan or dan < 1:
        print("1 ~ 9 사이의 숫자를 입력해주세요!")
        continue

    print(f"구구단 {dan}단을 계산합니다.")
    for i in range(1,10):
        print(f"{dan} X {i} = {dan * i}")

