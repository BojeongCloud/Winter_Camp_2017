# 반복문

반복문에서 수행하는 작업은 크게 다음 세 가지로 구분할 수 있다.
- 변수 초기화
- 조건 검사
- 명령어 수행

while문의 경우, 변수 초기화는 while문을 마주하기 전에 이루어지기 때문에 논외로 간주한다. while문과 for문 모두 내부 명령어들을 수행하기 전에 반복 조건을 검사한다. 반복 조건을 만족하지 않을 때까지, 내부 명령어를 모두 수행한 후에는 반복문 상단으로 이동하여 다시 반복 조건을 검사하는 작업을 반복하게 된다.

![](http://soen.kr/lecture/ccpp/cpp1/4-3-2.files/image002.gif)

## while문
조건을 만족하는 한, 반복문 안에 있는 명령어들을 실행한다.

### 예제 1
```
treeHit = 0

while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)

if treeHit == 10:
    print("나무 넘어갑니다.")
```

### 예제 2
break문을 사용하면 반복문에서 강제로 나갈 수 있다. for문에도 사용가능하다.
```
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
```

### 예제 3
continue문을 사용하면 이하 명령어를 수행하지 않고 반복문 상단으로 이동하여 반복문 조건을 검사한다.

```
a = 0
while a < 10:
    a = a+1
    if a % 2 == 0: continue
    print(a)
```

### 예제 4
반복문 수행 조건이 항상 참(True)이 되도록 하면 무한 루프를 만들 수 있다. 게임 제작시에 많이 사용된다.

```
while True:
    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")
```

## for문
반복문을 일상 생활에서 ~~전혀~~ 사용하~~지않~~는 표현처럼 서술할 수 있다. 리스트, 튜블 또는 문자열 안에 있는 항목(item)들에 대하여 차례대로 명령어를 수행한다.

### 예제 5
```
test_list = ['one', 'two', 'three']

for i in test_list:
    print(i)
```

### 예제 6
```
a = [(1,2), (3,4), (5,6)]

for (first, last) in a:
    print(first + last)
```

### 예제 7
반복문 안에 조건문을 같이 사용할 수 있다.

```
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number +1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)
```

## 과제

```
import random

random_matrix = []
random_row = []
count = 0

def build_random_matrix():
    for i in range(3):
        random_row.clear()                          # --- [1]
        for j in range(3):
            random_row.append(random.randint(0, 1))
        random_matrix.append(random_row.copy())     # --- [2-a]
        # random_matrix.append(random_row)            # --- [2-b]
build_random_matrix()
print(random_matrix)

# 다음 중첩된 반복문을 완성하세요.
for :
    for :

print("총 1의 개수는", count, "개 입니다.")

# 1.
# [1]을 주석 처리한 후 실행시켜 얻은 결과와 비교해보고
# 이 명령어가 필요한 이유가 무엇인지 서술해보세요.

# 2.
# [2-a]를 주석 처리하고 [2-b]의 주석을 해제한 후 실행시켜 얻은 결과와 비교해보고
# 왜 random_row 대신에 random_row.copy()를 사용했는지 서술해보세요.

# 3.
# 반복문의 중첩을 사용해서 count 값을 계산해보세요.
```
