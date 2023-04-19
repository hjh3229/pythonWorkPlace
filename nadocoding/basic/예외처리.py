# try/ except 를 통해 에러가 발생시 출력할 문장을 정할 수 있다.

try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:   # 위에서 input에 문자를 입력시 ValueError가 발생하므로
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err: # 에러 메시지를 그대로 출력할 경우
    print(err)                   # division by zero
# except:                        # 그 외 에러 발생시 출력메시지
#     print("알 수 없는 에러가 발생하였습니다.")
except Exception as err:         # 그 외 에러 발생시 에러 메시지 그대로 출력
    print(err)