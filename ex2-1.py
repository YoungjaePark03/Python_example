kor = int(input("국어 : "))
eng = int(input("영어 : "))
math = int(input("수학 : "))
tot = kor + eng + math
avg = tot / 3

print(f"총점 : {tot}")
print(f"평균 : {avg:.2f}")
