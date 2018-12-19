"""
파이썬 dictionary 활용 기초!
"""

# 1. 평균을 구하세요.
iu_score = {
    "수학": 80,
    "국어": 90,
    "음악": 100
}

# 답변 코드는 아래에 작성해주세요.

# 1. iu_score라 하는 dic 변수에서 key, value 순으로 저장될 때, value 값만 뽑아내보자. / 영어로검색 python get values in dict
total_score = 0
count = 0

for score in iu_score:
    
# 미리 프린트 해본다. python app3.py -> print(iu_score[score]) / 숫자로 바뀜.
    total_score = total_score + iu_score[score]
    count = count+1
print(total_score/count)

# 2. 뽑아낸 값의 총합을 구한다.

# 3. 총합을 갯수로 나눈다.


scores = list(iu_score.values())

print(sum(scores)/len(iu_score))

# 2. 반 평균을 구하세요.
scores = {
    "iu": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "ui": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    }
}
# 답변 코드는 아래에 작성해주세요.

# 1. 각 반을 순회하는 반복문을 작성한다.
for cl in scores:
    print(cl)
    print(scores[cl])
    tmp = list(scores[cl].values())
    print("{}:{}".format(cl, sum(tmp)/len(tmp)))

# 2. 한 번 순회를 할 때 1번에서 작성한 코드를 활요한다. / for문을 두번 쓸수도 있다.

# 3. 출력한다.

print("")


# 3. 도시별 최근 3일의 온도 평균은?
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
# 3-1. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
cities = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9],
}

# 답변 코드는 아래에 작성해주세요.
print("=====Q3=====")
for city in cities:
    temp=cities[city]
    print("{}의 평균기온:{}".format(city, sum(temp)/len(temp)))
# 소숫점 2번째 자리
    print("{}의 평균기온:{}".format(city, round(sum(temp)/len(temp),1)))
    print("{}의 평균기온:{:0.1f}".format(city, sum(temp)/len(temp)))
    
    # 답변 코드는 아래에 작성해주세요.
    print("=====Q3-1=====")

# 0. 최저기온, 최고기온을 저장할 수 있는 변수를 선언한다
minimum = {"도시명": 1000}
maximum = {"도시명": -1000}

# 1. 각 도시를 순회하는 반복문을 만든다.
for city in cities:
      for temp in cities[city]:
        
        if(maximum[1]<temp):
            maximum[0]= city
            maximum[1]= temp
            
        if(minimum[1]>temp):
            manimum[0]= city
            manimum[1]= temp       
        
print("최고 기온은 {}시의 {}도이며, 최저 기온은 {}의 {}도입니다.".format(maximum[0], maximum[1], minimum[0], minimum[1])
        
# 2. 각 도시의 기온 정보를 순회하는 반복문을 만든다.

# 3. 순회하다가 최저기온의 경우에는 현재 저장된 값보다 작은 값이, 최고 기온의 경우에는 현재 저장된 값보다 큰 값이 있는 경우 현재 저장되어 있는 값을 바꾼다.


# 4. 위에서 서울은 영상 2도였던 적이 있나요?
# 답변 코드는 아래에 작성해주세요.

    # 1. cities 변수에서 서울 부분만 추출한다.
    
    # 1-1. flag 라고 하는 변수에 false 저장한다.
    
    # 2. seoul 변수(list)를 순회하며 2와 같았던 적이 있는지 찾는다.

    # 3. 온도가 2도였던 적이 있다면 flag 변수를 true로 바꿔준다.
    
    # 4. flag 변수에 따라 출력문을 작성한다.
    
    