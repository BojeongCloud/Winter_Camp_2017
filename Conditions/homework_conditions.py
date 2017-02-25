operand1 = int(input("피연산자1을 입력하세요: "))
operand2 = int(input("피연산자2를 입력하세요: "))
operator = input("연산자를 입력하세요. (+, -, *, /): ")

if operator == "+":
    result = operand1 + operand2
elif operator == "-":
    result = operand1 - operand2
elif operator == "*":
    result = operand1 * operand2
elif operator == "/":
    result = operand1 / operand2

print(operand1, operator, operand2," = ",result)
