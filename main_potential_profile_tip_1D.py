import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# 함수 정의
def z(x, y, B, λ):
    return B * (np.cos(np.pi * 2 * x / λ) * np.cos(np.pi * 2 * y / λ))

# 초기 설정
atom_lattice = 1  # atom_lattice 값 수정
tip_lattice = 1
atom_limit = 1000  # 그냥 radius보다 충분히 큰 숫자
atom_number = np.linspace(1, 30, 30)  # 반지름을 1부터 n까지 변화시킬 예정입니다.

max_min_potentials = []  # 각 반경에서의 최대-최소 잠재 에너지를 저장할 리스트

B = 0.01  # 적절한 B 값 설정
λ = atom_lattice

# tip 좌표 베이스 계산
tip_base = [(x, 0) for x in np.arange(tip_lattice, atom_limit, tip_lattice)]  # y 좌표는 0으로 고정하여 1차원 모델을 만듭니다.
tip_base.insert(0, (0.0, 0.0))  # tip 중심 추가

# 반지름별 최대-최소 잠재 에너지 계산
for radius_multiplier in tqdm(atom_number, desc='Calculating max-min potentials'):
    radius = tip_lattice * radius_multiplier  # tip 원 반지름
    max_z_value_sum = float('-inf')  # 최대값 초기화
    min_z_value_sum = float('inf')  # 최소값 초기화

    # 각 원자들 에서의 함수값 합 계산
    z_values = []
    for x_start in np.arange(0, atom_lattice, 0.1):  # x가 0.1씩 변하도록 수정
        for x, y in tip_base:
            if np.sqrt((x_start + x) ** 2 + y ** 2) <= radius:  # y 좌표는 고정되어 있으므로 y_start를 제거합니다.
                z_values_sum = sum([z(x_start + x, y, B, λ) for x, y in tip_base if np.sqrt((x_start + x) ** 2 + y ** 2) <= radius])
                z_values.append(z_values_sum)

    # 최대값과 최소값을 계산합니다.
    max_z_value_sum = max(z_values)
    min_z_value_sum = min(z_values)

    # 최대-최소값을 리스트에 추가
    max_min_potentials.append(max_z_value_sum - min_z_value_sum)

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(atom_number, max_min_potentials, marker='o')  # x 축을 atom_number로 변경합니다.
plt.xlabel('Atom Number')  # x 축 라벨을 반경이 아닌 원자 수로 변경합니다.
plt.ylabel('Max-Min Potential')
plt.title('Atom Number vs. Max-Min Potential')  # 그래프 제목을 변경합니다.
plt.grid(True)
plt.show()
