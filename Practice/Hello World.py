from scipy.optimize import linprog

# 계수 행렬
A = [[6, 4, 2], [7, 13, 5]]
# 제한 조건
b = [31, 40]
# 이익 계수
c = [-5, -4, -2]

# 최적화 함수를 사용하여 최대 이익을 찾습니다.
res = linprog(c, A_ub=A, b_ub=b)
# 소수점 이하 3번째 자리에 반올림합니다.
x1_optimal, x2_optimal, x3_optimal = map(lambda x: round(x, 3), res.x)

print(f"서비스 1의 제공량: {x1_optimal}")
print(f"서비스 2의 제공량: {x2_optimal}")
print(f"서비스 3의 제공량: {x3_optimal}")
