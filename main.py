from phone_book import print_menu, add_phone_num, show_all_phone_num, remove_all
from time import sleep

while True:
    num = print_menu()

    if num == 0:
        print('프로그램을 종료합니다.')
        break           
    elif num == 1:
        add_phone_num()        
        
    elif num == 2:
        show_all_phone_num()
    
    elif num == 3:
        # 새로 추가된 remove_al 함수 실행
        remove_all()  # 3번 누르면 모든 번호 삭제하는 기능    
        
    elif num == 4:
        pass  # 이름을 입력하면, 그런 사용자가 있는 지 검색해서 있으면 상세 정보 표기
    else:
        print('잘못된 입력입니다. 다시 입력해주세요.')    
        sleep(2)    
    