from time import sleep
from datas import ContactInfo

def print_menu():
    print('====== 전화번호부 ======')
    print('1. 전화번호 등록')
    print('2. 전화번호 목록 조회')
    print('3. 모든 연락처 삭제')
    print('4. 연락처 상세 조회')
    print('0. 프로그램 종료')
    print('=======================')
    input_num = int(input( '원하는 메뉴를 선택하세요 : '))
    
    return input_num

def add_phone_num():
    name = input('이름 : ')
    phone_num = input('전화번호 : ')
    memo = input('특이사항 : ')
    
    with open('phone_book.csv', 'a') as file:
             
        input_line = f'{name}, {phone_num}, {memo}\n'  
        file.write(input_line)
        
    print('전화번호 등록이 완료되었습니다.')   
    sleep(2)
    

def show_all_phone_num():

    with open('phone_book.csv', 'r') as file:
        
        line_list = file.readlines()
        
        for line in line_list:
            line = line.strip()            
            info_list = line.split(',')            
            contact = ContactInfo(info_list[0], info_list[1], info_list[2])
            contact.print_contact_info()
            
        sleep(2)
        

# phone_book.csv 파일의 모든 내용을 삭제해주는 함수
def remove_all():
    # 기존 파일을 불러내서 => 내용물 전부 삭제
    # 파일을 새로 만들어주자 w모드로 불러내보자
    with open('phone_book.csv', 'w') as f:
        pass   # w모드로 불러내면, 기존 내용 삭제처리되니까!!  그 뒤의 일은 없어도 됨
    
    # 삭제 완료되었다는 안내메세지 2초간 출력
    print('모든 기록이 삭제되었습니다.')
    sleep(2)
    
# 상세보기 -> 이름을 기반으로 검색(전체 연락처 목록에서 )
def search_and_view_contact():
    print('----- 사용자 검색 -----')
    search_name = input('조회할 사용자 이름 : ')
    
    # 모든 연락처 목록을 불러내야함 => 파일 다시 조회
    with open('phone_book.csv', 'r') as file:
        line_list = file.readlines()
        
        for line in line_list:
            line = line.strip()
            
            # 실제로 해야할 것 : 사용자 이름이 정말 들어있는가? 검색 구현하자
            print(line)