coffee = 10

while True:
    money = int(input('돈을 넣어 주세요: '))
    if money == 300:
        print('돈 받았으니 커피 드림')
        coffee -= 1
    elif money > 300:
        print('거스름돈 %d를 주고 커피를 드림' % (money-300))
        coffee -= 1
    else:
        print('돈 다시 돌려주고 커피 ㄴㄴ')
        print('남은 커피: %d 개' %coffee)
    if not coffee:
        print('커피 떨어짐. 판매종료.')
        break
        
    if not coffee:
        print('커피 없음. ㄲㅈ')
        break