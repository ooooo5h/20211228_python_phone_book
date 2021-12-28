# 다른 모듈에 -> 메뉴 출력, 전화번호 추가 등등의 기능을 함수로 만들자
# 해당 함수들을 import해서 사용하자
from phone_book import print_menu, add_phone_num    # 하나의 py파일에서, 여러 함수 import

from time import sleep

# 메뉴에서 0번을 입력할 때 까지 계속해서 입력을 받고 싶다.
# 언제 입력할지 몰라 => while True => 0번이 들어오면 반복 종료하게끔
while True:
    # 실행 결과로 어떤 숫자를 넣었는가? 받을 수 있다.
    num = print_menu()

    # num에 어떤 숫자가 담겼는가? 다른 행동(기능) 수행
    # 0번 : 프로그램 종료 => 우선 작업
    if num == 0:
        print('프로그램을 종료합니다.')
        break           # 무한반복 탈출해야 프로그램이 종료됨
    elif num == 1:
        # 전화번호부 기능 中 전화번호 데이터 추가 기록
        add_phone_num()        
        
    elif num == 2:
        # 전화번호부 기능 中 모든 목록 표시 
        pass
    else:
        # 0,1,2가 아니면 잘못된 숫자 들어왔다는 안내 메세지 띄우기
        print('잘못된 입력입니다. 다시 입력해주세요.')    # 참고 - 이 문장이 출력되고 나서, 2초정도 대기 후 다음 문장을 실행하고 싶다
        sleep(2)    # time모듈의 sleep 기능 활용
    