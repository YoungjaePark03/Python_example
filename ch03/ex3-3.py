money = int(input("부모님으로부터 받은 용돈 : "))
change = money - 3550

print(f"용돈 : {money:,}원")
print(f"거스름돈 : {change:,}원")
print(f"500원짜리 거스름돈 : {change // 500}개")
print(f"100원짜리 거스름돈 : {(change%500)//100}개")
print(f"50원짜리 거스름돈 : {((change%500)%100)//50}개")
