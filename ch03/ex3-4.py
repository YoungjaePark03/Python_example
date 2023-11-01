userSec = int(input("초를 입력하세요 : "))
hour = userSec // 3600
minute = (userSec % 3600) // 60
second = (userSec % 3600) % 60

print(f"입력받은 {userSec}초는 {hour}시간 {minute}분 {second}초 이다.")
