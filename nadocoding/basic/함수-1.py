# 함수 정하기 = def
def open_account():
    print("새로운 계좌가 생성되었습니다.") # open_account()라는 함수 생성

open_account() # 새로운 계좌가 생성되었습니다.

# 전달값과 반환값
def deposit(balance, money):       # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance+money    # return을 통해 balance+money값을 반환해 balance에 저장

balance = 0    # 잔액
balance = deposit(balance, 1000)   # 입금이 완료되었습니다. 잔액은 1000원입니다.
# print(balance) # 1000
balance = deposit(balance, 2000)   # 입금이 완료되었습니다. 잔액은 3000원입니다.
# print(balance) # 3000

def withdraw(balance,money):       # 출금
    if balance >= money:           # 잔액이 출금액보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

balance = withdraw(balance,5000)   # 출금이 완료되지 않았습니다. 잔액은 3000원입니다.
balance = withdraw(balance,1500)   # 출금이 완료되었습니다. 잔액은 1500원입니다.

def withdraw_night(balance,money): # 저녁 출금엔 수수료 발생
    commission = 100   # 수수료
    if balance >= money+commission:
        print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission,balance-money-commission))
        return commission, balance-money-commission  # 한번에 여러개의 값 반환 가능
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return commission, balance # commission을 반환하지 않으면 아래 함수가 작동은 하지만 TypeError가 발생


commission, balance = withdraw_night(balance,1000)  # 수수료는 100원이며, 잔액은 400원입니다.
commission, balance = withdraw_night(balance,1000)  # 출금이 완료되지 않았습니다. 잔액은 400원입니다.