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