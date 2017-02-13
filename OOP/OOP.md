# 객체 지향 프로그래밍
영어를 직역해서 처음에는 다소 어색한 이름이다. 영어로는 Object Oriented Programming이라고 한다. 조금 풀어서 설명하면 객체를 지향하는 프로그래밍이라는 말이다.

객체 지향적으로 프로그래밍한다는 말이 정확히 어떤 것을 의미하는지 이해하려면 절차 지향적 프로그래밍 이라는 것이 있다는 것을 알아야 한다.

사실 초급 프로그래머들은 일반적으로 절차 지향적으로 프로그래밍을 배우기 시작한다. 다음 그림이 절차 지향적 프로그래밍을 한 눈에 설명해준다고 할 수 있곘다. 즉, 프로그램이 시작해서 끝나기까지 어떤 절차 또는 **흐름**이 존재하는데, 절차 지향적 프로그래밍은 이 **흐름**에 주안점을 두고 프로그래밍을 한다는 것이다.

반면 객체 지향적 프로그래밍이란 객체(Object)에 주안점을 두고 프로그래밍을 하는 것이다. 한 객체가 가진 정적인 특성(ex. 무게, 크기)과 한 객체가 가진 동적인 특성(ex. 용도, 능력)을 정의하는 것이 객체 지향적 프로그래밍이라고 할 수 있다. 프로그램의 시작과 끝을 염두에 두고 프로그래밍하는 것이 아니라, 프로그램을 구성하는 것들을 정의하는 것에 주안점을 두는 프로그래밍 방식이라고 하면 이해하면 쉬울 것이다.

객체 지향 프로그래밍이라는 것은 사실은 프로그래밍 언어 차원의 이야기라기 보다는 프로그래밍 패러다임에 가깝다. 이게 무슨 말이냐면, 같은 프로그래밍 문제를 절차 지향적으로 풀거나 또는 객체 지향적으로 풀어낼 수 있다는 것이다. 둘 중에 어떤 것이 정답이다라고는 할 수 없다는 것이다.

하지만 상황에 따라서는 어떤 것이 다른 것보다 효율적일 수 있고, 여러 개발자들 간의 협업을 요구하는 상황에서 어떤 것이 다른 것보다 한 눈에 이해하기 쉬운 코드가 될 수 있다는 것이다. 그리고 물론 여러분이 객체 지향적 프로그래밍을 배우는 이유는 절차 지향적 프로그래밍이 갖지 못한 여러 장점이 객체 지향 프로그래밍에 있기 때문이다.

## 예제 1

파이썬 3.5 버전의 `math` 패키지에 대해서 자세히 알고 싶다면 [공식 홈페이지의 설명](https://docs.python.org/3.5/library/math.html)을 참고한다. 

```
import math

class Circle:
    def __init__(self, radius = 1):
        self.set_radius(radius)

    def set_radius(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def get_area(self):
        return math.pow(self.get_radius(), 2) * math.pi

circle = Circle()
print("원의 반지름은", circle.get_radius(), "입니다.")
print("원의 넓이는", circle.get_area(), "입니다.\n")

circle.set_radius(3)
print("원의 반지름을 3 으로 수정!\n")
print("원의 반지름은", circle.get_radius(), "입니다.")
print("원의 넓이는", circle.get_area(), "입니다.")
```

## 과제

```
import math

class Rectangle:
    def __init__(self, width = 1, height = 1):
        self.set_width(width)
        self.set_height(height)

    def set_width(self, width):
        # 적당한 명령어를 입력하세요

    def get_width(self):
        # 적당한 명령어를 입력하세요

    def set_height(self, height):
        # 적당한 명령어를 입력하세요

    def get_height(self):
        # 적당한 명령어를 입력하세요

    def get_area(self):
        # 적당한 명령어를 입력하세요

rectangle = Rectangle()
print("사각형의 너비는", rectangle.get_width(), "입니다.")
print("사각형의 높이는", rectangle.get_height(), "입니다.")
print("사각형의 넓이는", rectangle.get_area(), "입니다.\n")

rectangle.set_width(2)
rectangle.set_height(3)
print("사각형의 너비와 높이를 각각 2 와 3 으로 수정!\n")
print("사각형의 너비는", rectangle.get_width(), "입니다.")
print("사각형의 높이는", rectangle.get_height(), "입니다.")
print("사각형의 넓이는", rectangle.get_area(), "입니다.")
```

실행결과:

```
사각형의 너비는 1 입니다.
사각형의 높이는 1 입니다.
사각형의 넓이는 1 입니다.

사각형의 너비와 높이를 각각 2 와 3 으로 수정!

사각형의 너비는 2 입니다.
사각형의 높이는 3 입니다.
사각형의 넓이는 6 입니다.
```
