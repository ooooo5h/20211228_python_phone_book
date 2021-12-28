from phone_book import print_menu, add_phone_num, show_all_phone_num 
from time import sleep

while True:
    num = print_menu()

    # 0 누르면 프로그램 종료
    if num == 0:
        print('프로그램을 종료합니다.')
        break           
    # 1 누르면 전화번호 추가
    elif num == 1:
        add_phone_num()        
        
    elif num == 2:
        show_all_phone_num()
        
    else:
        print('잘못된 입력입니다. 다시 입력해주세요.')    
        sleep(2)    
    