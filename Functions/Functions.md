# 함수

- 어떤 작업을 수행하는 명령어 뭉치
- `def`를 사용해서 함수를 정의한다.
- 들여쓰기를 반드시 하도록 한다.
-
## 예제 1

```
def sum(a, b):
    return a + b
```

## 예제 2
![함수](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Function_machine2.svg/191px-Function_machine2.svg.png)

일반적으로 함수는 위와 같은 그림으로 설명된다. 함수는 어떤 **입력**을 받아서, 입력된 정보를 토대로 정보를 **처리**하여 **출력**을 내보낸다.

입력과 출력의 유무에 따라서 함수의 종류를 크게 네 가지로 구분할 수 있다.

- 입력 O, 출력 O
- 입력 O, 출력 X
- 입력 X, 출력 O
- 입력 X, 출력 X

### 입력값이 없는 함수
```
>>> def say():
...     return 'Hi'
...
>>>
```

### 출력값이 없는 함수
```
>>> def sum(a, b):
...     print("%d, %d의 합은 %d입니다." % (a, b, a+b))
...
>>>
```

### 입력값과 출력값 모두 없는 함수
```
>>> def say():
...     print('Hi')
...
>>>
```

## 예제 3
함수가 전달받는 입력의 초기값은 다음과 같이 설정할 수 있다.

```
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
```

## 예제 4
변수의 범위(scope)

```
a = 1           # --- [1]
def vartest(a):
    a = a +1    # --- [2]

vartest(a)
print(a)
```

- 결과값은 어떻게 나올까?
- [1]에서의 a와 [2]에서의 a는 같은 변수일까?

## 과제
다음은 재귀(recursive) 함수를 사용해서 팩토리얼(!)의 값을 구하는 프로그램입니다.

![](http://web.mit.edu/6.005/www/fa15/classes/10-recursion/figures/factorial-recurrence.png)

```
def factorial(k):
    if(k == 1):
        return 1
    else:
        return k * factorial(k - 1)
print(factorial(7))
```

ex)
factorial(5) = 120
factorial(7) = 5040

위 코드를 참고하여 n번째 피보나치 수열의 값을 구하는 함수를 작성하세요.

![](http://www.cs.utsa.edu/~wagner/CS3343/recursion/fib.gif)

```
def fibonacci(n):
    # 함수를 완성하세요
```

ex)
fibonacci(5) = 5
fibonacci(20) = 6765
