from phone_book import print_menu, add_phone_num, show_all_phone_num, remove_all, search_and_view_contact
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
        remove_all() 
        
    elif num == 4:
        search_and_view_contact()  
    else:
        print('잘못된 입력입니다. 다시 입력해주세요.')    
        sleep(2)    
    