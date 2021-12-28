from time import sleep

from datas import ContactInfo
# 실질적인 동작 관련 코드들을 함수로 갖고있는 파일(모듈)


# 메뉴 출력하고 / 입력값을 돌려받는 기능

def print_menu():
    print('====== 전화번호부 ======')
    print('1. 전화번호 등록')
    print('2. 전화번호 목록 조회')
    print('0. 프로그램 종료')
    print('=======================')
    input_num = int(input( '원하는 메뉴를 선택하세요 : '))
    
    # 입력한 결과를 함수의 결과로 return
    return input_num

# 이름/폰번/메모사항  세가지 데이터를 입력받아서 파일에 추가 저장하는 기능
def add_phone_num():
    # 세가지 데이터 입력 : 세 항목 모두 str으로 받자
    name = input('이름 : ')
    phone_num = input('전화번호 : ')
    memo = input('특이사항 : ')
    
    # 전화번호부 파일에 한 줄로 추가.   이름,폰번,메모 양식으로 추가해보자
    # with 구문 > 파일 열고 닫기 자동
    with open('phone_book.csv', 'a') as file:
        # .csv : 이름,폰번,메모처럼 , 를 이용해서 칸 구분 => 엑셀에서 표 형태로 표현이 가능하다
        
        input_line = f'{name}, {phone_num}, {memo}\n'   # 3개의 데이터를 한 줄로 ,로 붙여줌 + 다음줄로 내려주기
        file.write(input_line)
        
    # 안내 문구
    print('전화번호 등록이 완료되었습니다.')   # 2초 가량 대기 후 메뉴로
    sleep(2)
    
    
# 별도 기능 추가 - 저장된 목록 출력하기
def show_all_phone_num():
    # phone_book.csv 파일 로드하고, 한 줄씩 반복을 돌면서 ','로 분해해서 정보를 추출하기
    
    with open('phone_book.csv', 'r') as file:
        
        # 받아온 파일의 내용을 리스트로 (한줄씩) 담아두자
        line_list = file.readlines()
        
        # 임시 : 리스트를 하나하나 출력해보자(반복문)
        for line in line_list:
            line = line.strip()  # 마지막 줄바꿈 제거
            # print(line)   # 읽은 줄을 그대로 출력 X
            
            # ,로 붙여진 line을 split으로 분해해서 가공하자
            info_list = line.split(',')         
            
            # 연락처 정보를 표현하는 클래스 제작 => (가공해서 출력하는) 기능으로 구현
            # 연락처 객체 생성 => 생성자 활용
            contact = ContactInfo(info_list[0], info_list[1], info_list[2])
            
            # 가공해서 출력해주는 기능 활용 => 아직 x => 클래스에 메쏘드 추가하자