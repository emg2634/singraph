import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
# 함수 정의
def z(x, y, B, λ):
    return B * (np.cos(np.pi * 2 * x / λ) * np.cos(np.pi * 2 * y / λ))

# 초기 설정
atom_lattice = 2  # atom_lattice 값 수정
tip_lattice = 1.5 # tip_lattice 값 수정
atom_limit = 100  # radius_multiple와 tip_lattice 곱보다 큰 숫자
radius_multiple = np.linspace(1, 30, 30)  # 반지름을 1부터 n까지 변화시킬 예정, 원하는 반지름은 수정가능

max_min_potentials = []  # 각 반경에서의 최대-최소 잠재 에너지를 저장할 리스트

B = 0.01  # 적절한 B 값 설정
λ = atom_lattice

# tip 좌표 베이스 계산
tip_base = [(x, y) for x in np.arange(-atom_limit, atom_limit+1, tip_lattice) for y in np.arange(-atom_limit, atom_limit+1, tip_lattice)]
tip_base.insert(0, (0.0, 0.0))  # tip 중심 추가

# 반지름별 최대-최소 잠재 에너지 계산
for radius_multiplier in tqdm(radius_multiple, desc='Calculating max-min potentials'):
    radius = tip_lattice * radius_multiplier  # tip 원 반지름
    max_z_value_sum = float('-inf')  # 최대값 초기화
    min_z_value_sum = float('inf')  # 최소값 초기화

    # 각 반경에서의 함수값 합 계산
    z_values_sum=0
    z_values = []
    for x_start in np.arange(0, atom_lattice, 0.1):  # x가 0.1씩 변하도록 수정
        for y_start in np.arange(0,atom_lattice,0.1):
            for x, y in tip_base:
                if np.sqrt((x) ** 2 + (y) ** 2) <= radius:
                    z_values_sum += z(x_start + x, y_start + y, B, λ)
                    z_values.append(z_values_sum)

    # 최대값과 최소값을 계산합니다.
    max_z_value_sum = max(z_values)
    min_z_value_sum = min(z_values)

    # 최대-최소값을 리스트에 추가
    max_min_potentials.append(max_z_value_sum - min_z_value_sum)

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(radius_multiple * tip_lattice, max_min_potentials, marker='o')
plt.xlabel('Radius')
plt.ylabel('Max-Min Potential')
plt.title('Radius vs. Max-Min Potential')
plt.grid(True)
plt.show()












