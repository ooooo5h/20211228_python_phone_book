from time import sleep
from datas import ContactInfo

def print_menu():
    print('====== 전화번호부 ======')
    print('1. 전화번호 등록')
    print('2. 전화번호 목록 조회')
    print('3. 모든 연락처 삭제')
    print('4. 연락처 상세 조회')
    print('5. 특정 연락처 삭제')
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
        
        
def remove_all():
    with open('phone_book.csv', 'w') as f:
        pass   
    
    print('모든 기록이 삭제되었습니다.')
    sleep(2)
    

def search_and_view_contact():
    print('----- 사용자 검색 -----')
    search_name = input('조회할 사용자 이름 : ')
    
    with open('phone_book.csv', 'r') as file:
        line_list = file.readlines()
        
        for line in line_list:
            line = line.strip()
            
            if f'{search_name},' in line:
                
                infos = line.split(',')
                
                contacnt = ContactInfo(infos[0], infos[1], infos[2])
                
                contacnt.print_contact_info_deteail()
                sleep(2)
                
                
# 특정 연락처 삭제 : 몇번째 연락처를 지울건지 입력을 받고, 그 위치에 맞는 연락처를 삭제해보자
def remove_contact_by_position():
    # 지우고 싶은 위치를 입력받자
    position = int(input('몇번째 연락처를 삭제하겠습니까? (1부터 입력하세요.) : '))
    
    # 그 위치의 연락처가 누구인지? 이름을 꺼내고, 이 사람이 맞는 지 확인을 받자
    
    # 입력값 보정 - 실제 파일의 목록에서는 0번부터 시작하니까, -1 해줘야 같음
    position-= 1
    
    with open('phone_book.csv', 'r') as f:
        # readlines활용해서 한 줄씩 목록으로 받아오자
        contact_list = f.readlines()
        
        # 특정 위치의 연락처만 다루자 => 인덱스 활용
        target_contact = contact_list[position].strip()       
        infos = target_contact.split(',')
        
        # 연락처 객체로 변환..? 이 작업을 왜하는건지 이해못함
        remove_contact = ContactInfo(infos[0], infos[1], infos[2])
        
        # 이 사람을 삭제하고 싶은 게 맞는지 확인받기