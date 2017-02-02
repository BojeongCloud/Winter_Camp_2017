# 조건문

C언어와 다르게 파이썬은 중괄호 `{}`를 사용하지 않기 때문에 들여쓰기에 민감하다. `:` 콜론(colon)을 잊지 않도록 주의한다.

## 기본
### 예제 1
수학 시간에 대소비교를 할 때 사용하는 `>`, `<`, `>=`, `<=`, `==` 연산자들을 사용한다.

```
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")
```

### 예제 2
리스트에 특정 자료(data)가 있는지 확인하고자 할 때는 다음과 같이 작성한다.
> 주머니(pocket)에 돈(money)가 있는지 확인

```
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
     print("택시를 타고 가라")
else:
     print("걸어가라")
```

## 심화
### 예제 3

- 여러 조건이 동시에 참인 경우에 대해서는 `and` 연산자로 묶어준다.
- 여러 조건 중 적어도 하나가 참인 경우는 `or` 연산자를 사용한다.
- 어떤 조건의 역을 의미할 때는 `not`을 붙여준다.

```
money = 2000
card = 1
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")
```

### 에제 4

`elif`는 `else if`의 축약된 형태로서 이전 if문에서 명시한 조건의 여집합과 현재 if문에서 명시한 조건의 교집합을 가리킬 때 사용한다.

```
pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket:
     print("택시를 타고가라")
elif card:
     print("버스를 타고가라")
else:
     print("걸어가라")
```

### 예제 5

![벤 다이어그램](http://www.mimedu.co.kr/MIM/ImgDir/584A6_0586_7C87.jpg)

```
if A: # a, b, c, d
    ...
if B: # e, b, c, f
    ...
if C: # g, d, c, f
    ...
```

```
if A:   # a, b, c, d
    ...
elif B: # 무엇이 될까?
    ...
elif C: # 무엇이 될까?
    ...
```

### 과제
다음은 두 수를 입력 받아서 덧셈을 수행하는 코드입니다.
```
operand1 = int(input("피연산자1을 입력하세요: "))
operand2 = int(input("피연산자2를 입력하세요: "))
result = operand1 + operand2

print(operand1, " + ",operand2," = ",result)
```

다음은 사칙연산을 수행하는 코드의 일부입니다. 위에서 제시한 소스코드를 참고하면서 다음 소스코드를 완성하세요.

```
operand1 = int(input("피연산자1을 입력하세요: "))
operand2 = int(input("피연산자2를 입력하세요: "))
operator = input("연산자를 입력하세요. (+, -, *, /): ")

if operator == "+":
    result = operand1 + operand2
elif # 코드를 완성하세요

elif # 코드를 완성하세요

elif # 코드를 완성하세요

print(operand1, operator, operand2," = ",result)
```
