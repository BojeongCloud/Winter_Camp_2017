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

for i in range(3):
    for j in range(3):
        if(random_matrix[i][j] == 1):
            count = count + 1

print("총 1의 개수는", count, "개 입니다.")

# 1.
# [1]을 주석 처리한 후 실행시켜 얻은 결과와 비교해보고
# 이 명령어가 필요한 이유가 무엇인지 서술해보세요.

# 2.
# [2-a]를 주석 처리하고 [2-b]의 주석을 해제한 후 실행시켜 얻은 결과와 비교해보고
# 왜 random_row 대신에 random_row.copy()를 사용했는지 서술해보세요.

# 3.
# 반복문의 중첩을 사용해서 count 값을 계산해보세요.
