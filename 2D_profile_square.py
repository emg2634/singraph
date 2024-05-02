import numpy as np
import matplotlib.pyplot as plt


# 함수 정의
def z(x, y, B, λ):
    return B * (np.cos(np.pi * 2 * x / λ) + np.cos(np.pi * 2 * y / λ))


# 초기 설정
atom_lattice = 2  # atom_lattice 값 수정
tip_lattice = 1.5  # tip_lattice 값 수정

atom_number = np.linspace(1, 65, 65, dtype=int)  # 원자 개수를 1부터 65까지 변화시킬 예정입니다.

max_min_potentials = []  # 각 원자 수에서의 최대-최소 잠재 에너지를 저장할 리스트
max_min_positions = []  # 각 원자 수에서의 최대-최소 잠재 에너지를 갖는 위치를 저장할 리스트

B = 0.5  # 적절한 B 값 설정
λ = atom_lattice

for num_atoms in atom_number:
    max_z_value_sum = float('-inf')  # 최대값 초기화
    min_z_value_sum = float('inf')  # 최소값 초기화
    best_max_x_start = None  # 최대값을 가지는 x_start
    best_max_y_start = None  # 최대값을 가지는 y_start
    best_min_x_start = None  # 최소값을 가지는 x_start
    best_min_y_start = None  # 최소값을 가지는 y_start
    tip_base = [(x, y) for x in np.arange(0, tip_lattice * num_atoms, tip_lattice) for y in
                np.arange(0, tip_lattice * num_atoms, tip_lattice)]  # tip_base 초기화

    for x_start in np.arange(0, atom_lattice, 0.1):
        z_values_sum = 0
        for y_start in np.arange(0, atom_lattice, 0.1):

            for x_tip, y_tip in tip_base:
                z_value = z(x_tip + x_start, y_tip + y_start, B, λ)  # Calculate the z-value for the current atom
                z_values_sum += z_value  # Add the z-value to the sum

            if z_values_sum > max_z_value_sum:  # Update the maximum potential energy if necessary
                max_z_value_sum = z_values_sum
                best_max_x_start, best_max_y_start = x_start, y_start

            if z_values_sum < min_z_value_sum:  # Update the minimum potential energy if necessary
                min_z_value_sum = z_values_sum
                best_min_x_start, best_min_y_start = x_start, y_start

    max_min_potentials.append(max_z_value_sum - min_z_value_sum)  # 현재 원자 수에 대한 최대-최소 잠재 에너지 저장
    max_min_positions.append(((best_max_x_start, best_max_y_start), (best_min_x_start, best_min_y_start)))  # 최대-최소 잠재 에너지를 갖는 위치 저장

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(atom_number, max_min_potentials, marker='o', color='b')
plt.xlabel('Number of Atoms')  # x 축 라벨을 원자 수로 변경합니다.
plt.ylabel('Max-Min Potential')
plt.title('Number of Atoms vs. Max-Min Potential')  # 그래프 제목을 변경합니다.
plt.grid(True)


# 각 원자 수에 대한 최대-최소 잠재 에너지를 갖는 위치 출력
for i, num_atoms in enumerate(atom_number):
    max_pos, min_pos = max_min_positions[i]
    print(f"For {num_atoms} atoms:")
    print(f"Maximum potential position: {max_pos}")
    print(f"Minimum potential position: {min_pos}")
plt.show()