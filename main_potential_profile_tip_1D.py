import numpy as np
import matplotlib.pyplot as plt


# 함수 정의
def z(x, y, B, λ):
    return B * (np.cos(np.pi * 2 * x / λ) + np.cos(np.pi * 2 * y / λ))


# 초기 설정
atom_lattice = 2  # atom_lattice 값 수정
tip_lattice = 1.5 # tip_lattice 값 수정

atom_number = np.linspace(1, 50, 50, dtype=int)  # 원자 개수를 1부터 30까지 변화시킬 예정입니다.

max_min_potentials = []  # 각 원자 수에서의 최대-최소 잠재 에너지를 저장할 리스트

B = 0.1  # 적절한 B 값 설정
λ = atom_lattice

for num_atoms in atom_number:
    max_z_value_sum = float('-inf')  # 최대값 초기화
    min_z_value_sum = float('inf')  # 최소값 초기화

    tip_base = [(x, 0) for x in np.arange(0, tip_lattice * num_atoms, tip_lattice)]  # tip_base 초기화

    for x_start in np.arange(0, atom_lattice, 0.1):
        for y_start in np.arange(0, atom_lattice, 0.1):
            z_values_sum = 0  # Initialize z_values_sum for each combination of x and y

            # Iterate over tip_base and calculate the z-value for each atom
            for x_tip, y_tip in tip_base:
                z_value = z(x_tip + x_start, y_tip + y_start, B, λ)  # Calculate the z-value for the current atom
                z_values_sum += z_value  # Add the z-value to the sum

            max_z_value_sum = max(max_z_value_sum, z_values_sum)  # Update the maximum potential energy
            min_z_value_sum = min(min_z_value_sum, z_values_sum)  # Update the minimum potential energy

    max_min_potentials.append(max_z_value_sum - min_z_value_sum)  # 현재 원자 수에 대한 최대-최소 잠재 에너지 저장

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(atom_number, max_min_potentials, marker='o', color='b')
plt.xlabel('Number of Atoms')  # x 축 라벨을 원자 수로 변경합니다.
plt.ylabel('Max-Min Potential')
plt.title('Number of Atoms vs. Max-Min Potential')  # 그래프 제목을 변경합니다.
plt.grid(True)
plt.show()
