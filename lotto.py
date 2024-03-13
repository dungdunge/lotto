import requests, random
from datetime import datetime
import streamlit as st
import pandas as pd

# 확률은 1개 같을확률 42, 2개 같을확률 17 3개 같을확률 2 다 다를확률 38.6 
# 2번째 전회차와 1개 같을확률 45, 2개 같을확률 15 3개 같을확률 3 다 다를확률 36
# -> 1개같은거 2개 2개같은거 1개 다 다른거 2개
def get_lotto_numbers(drawing_no):
    url = f'http://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={drawing_no}'
    response = requests.get(url)
    data = response.json()
    winning_numbers = (
        data['drwtNo1'],
        data['drwtNo2'],
        data['drwtNo3'],
        data['drwtNo4'],
        data['drwtNo5'],
        data['drwtNo6']
    )
    return winning_numbers
def possibility_formernumber(list): #이전 회차 번호가 다음 회차에 나올 확률 계산함수
    same=0
    same1=0
    same2=0
    same3=0
    for i in range(1,len(list)-1):
        former = list[i]
        current = list[i+1]
        count = 0
        for num1 in former:
            for num2 in current:
                if num1 == num2:
                    count += 1
        if count == 1:
            same1 += 1
        elif count == 2:
            same2 += 1
        elif count == 3:
            same3 += 1
        elif count == 0:
            same += 1
    pos1 = same1/len(list)*100
    pos2 = same2/len(list)*100
    pos3 = same3/len(list)*100
    pos4 = same/len(list)*100
    # print(f"pos1 : {pos1}\npos2 : {pos2}\npos3 : {pos3}\npos4 : {pos4}")
    print(f"1개가 같을 확률 : {pos1} %\n2개가 같을 확률 : {pos2} %\n3개가 같을 확률 : {pos3} %\n다 다를 확률 : {pos4} %")

def possibility_former2number(list): #2번째 이전 회차 번호가 다음 회차에 나올 확률 계산함수
    same=0
    same1=0
    same2=0
    same3=0
    for i in range(2,len(list)-1):
        former = list[i-1]
        current = list[i+1]
        count = 0
        for num1 in former:
            for num2 in current:
                if num1 == num2:
                    count += 1
        if count == 1:
            same1 += 1
        elif count == 2:
            same2 += 1
        elif count == 3:
            same3 += 1
        elif count == 0:
            same += 1
    pos1 = same1/len(list)*100
    pos2 = same2/len(list)*100
    pos3 = same3/len(list)*100
    pos4 = same/len(list)*100
    # print(f"pos1 : {pos1}\npos2 : {pos2}\npos3 : {pos3}\npos4 : {pos4}")
    print(f"1개가 같을 확률 : {pos1} %\n2개가 같을 확률 : {pos2} %\n3개가 같을 확률 : {pos3} %\n다 다를 확률 : {pos4} %")

#이전 회차와 1개 같은 lucky_list 출력
def lucky_extraction1(array): 
    #이전 거에서 숫자 1개 뽑기
    random_element = random.choice(array[len(array)-1]) 
    #이전 거 리스트
    exception_list = list(array[len(array)-1])
    # 1부터 45까지의 숫자로 이루어진 리스트 생성
    to45 = list(range(1, 46))
    # to45에서 exception_list의 요소들을 제거
    yebi_list = [item for item in to45 if item not in exception_list]
    #이전 거에서 뽑은 1개랑 5개뽑은거 합쳐서 오름차순 정렬
    lucky_list = random.sample(yebi_list, 5)
    lucky_list.append(random_element)
    lucky_list.sort()
    return(lucky_list)

#이전 회차와 2개 같은 lucky_list 출력
def lucky_extraction2(array): 
    #이전 거에서 숫자 2개 뽑기
    random_element = random.choice(array[len(array)-1]) 
        # 첫 번째 숫자와 같지 않은 두 번째 무작위 숫자 뽑기
    while True:
        random_element2 = random.choice(array[len(array)-1]) 
        if random_element != random_element2:
            break
    #이전 거 리스트
    exception_list = list(array[len(array)-1])
    # 1부터 45까지의 숫자로 이루어진 리스트 생성
    to45 = list(range(1, 46))
    # to45에서 exception_list의 요소들을 제거
    yebi_list = [item for item in to45 if item not in exception_list]
    #이전 거에서 뽑은 1개랑 5개뽑은거 합쳐서 오름차순 정렬
    lucky_list = random.sample(yebi_list, 4)
    lucky_list.append(random_element)
    lucky_list.append(random_element2)
    lucky_list.sort()
    return(lucky_list)

#이전 회차와 다 다른 lucky_list 출력
def lucky_extraction_all_different(array): 
    #이전 거 리스트
    exception_list = list(array[len(array)-1])
    # 1부터 45까지의 숫자로 이루어진 리스트 생성
    to45 = list(range(1, 46))
    # to45에서 exception_list의 요소들을 제거
    yebi_list = [item for item in to45 if item not in exception_list]
    #이전 거 뺀 yebi_list에서 lucky_list 뽑고 오름차순 정렬
    lucky_list = random.sample(yebi_list, 6)
    lucky_list.sort()
    return(lucky_list)

# lucky_list 생성기
def lucky_list_maker(lotto_results):
    print(f"첫번째 행운의 숫자는   {lucky_extraction1(lotto_results)}")
    print(f"두번째 행운의 숫자는   {lucky_extraction1(lotto_results)}")
    print(f"세번째 행운의 숫자는   {lucky_extraction2(lotto_results)}")
    print(f"네번째 행운의 숫자는   {lucky_extraction_all_different(lotto_results)}")
    print(f"다섯번째 행운의 숫자는 {lucky_extraction_all_different(lotto_results)}")
    return
# streamlit에 맞게 5개의 리스트를 return하는 함수
def five_list(array):
    # 다섯 개의 함수를 호출하여 반환된 리스트를 하나의 배열로 만듦
    result = []
    # 다섯 개의 함수를 호출하여 반환된 리스트를 요소로 가지는 배열 생성
    result = [lucky_extraction1(array), lucky_extraction1(array), lucky_extraction2(array), lucky_extraction_all_different(array), lucky_extraction_all_different(array)]
    print(result)
    return result

#현재 날짜에 따라 start,end 초기화
start=1109
end=1110
def set_date():
    # 현재 날짜와 시간 가져오기
    current_date = datetime.now()
    # 년, 월, 일 정보 가져오기
    year = str(current_date.year)
    month = str(current_date.month)
    day = str(current_date.day)
    # 만약 월이 1자리라면 앞에 0을 추가
    if len(month) == 1:
        month = "0" + month
    # 통합
    date = int(year+month+day)
    # 20240316을 기준으로 start = 1109 end = 1110
    
    if (date > 20240316):
        tmp = (date - 20240316)//7 + 1
        start += tmp
        end += tmp
lotto_results = []
def main():    
    set_date()
    global lotto_results # 각 회차의 당첨번호를 담을 배열
    for drawing_no in range(start, end+1):
        lotto_numbers = get_lotto_numbers(drawing_no)
        lotto_results.append(lotto_numbers)
    five_list(lotto_results)
    # print(f"start = {start}, end = {end}")
if __name__ == "__main__":
    main()
st.markdown("""
<style>

</style>
""", unsafe_allow_html=True)
# 버튼을 만들고 클릭시 로또 번호 호출
if st.button('로또 번호 호출'):
    lotto_lists = five_list(lotto_results)
    
    # 가로로 정렬된 로또 번호를 담을 div 컨테이너 생성
    st.write('<div>', unsafe_allow_html=True)
    
    for i, lotto_numbers in enumerate(lotto_lists):
        st.subheader(f'행운의 조합 {i+1}')
        
        st.markdown('<div style="display:flex; flex-direction: row;>', unsafe_allow_html=True)
        for number in lotto_numbers:
            # 각 로또 번호들을 가로로 정렬하기 위한 div 컨테이너 생성
            # 숫자 범위에 따라 색이 다른 동그란 공 출력
            if number <= 10:
                st.markdown(f'<div style="width: 70px; height: 70px; border-radius: 50%; background-color: #FBC400; color: white; text-align: center; line-height: 70px; margin-right: 10px;">{number}</div>', unsafe_allow_html=True)
            elif number <= 20:
                st.markdown(f'<div style="width: 70px; height: 70px; border-radius: 50%; background-color: #69C8F2; color: white; text-align: center; line-height: 70px; margin-right: 10px;">{number}</div>', unsafe_allow_html=True)
            elif number <= 30:
                st.markdown(f'<div style="width: 70px; height: 70px; border-radius: 50%; background-color: #FF7272; color: white; text-align: center; line-height: 70px; margin-right: 10px;">{number}</div>', unsafe_allow_html=True)
            elif number <= 40:
                st.markdown(f'<div style="width: 70px; height: 70px; border-radius: 50%; background-color: #AAAAAA; color: black; text-align: center; line-height: 70px; margin-right: 10px;">{number}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div style="width: 70px; height: 70px; border-radius: 50%; background-color: #B0D840; color: black; text-align: center; line-height: 70px; margin-right: 10px;">{number}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)  # 각 로또 번호들을 가로로 정렬하는 div 컨테이너 종료
        
    st.write('</div>', unsafe_allow_html=True)  # 전체 로또 번호 div 컨테이너 종료
