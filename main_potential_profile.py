import numpy as np
import matplotlib.pyplot as plt


# 초기 설정
atom_lattice = 2  # atom_lattice 값 수정
tip_lattice = 1.5  # tip_lattice 값 수정
atom_limit = 20  # radius_multiple와 tip_lattice 곱보다 큰 숫자
radiuses = np.arange(0, atom_limit, 0.1)  # 반지름을 1부터 n까지 변화시킬 예정, 원하는 반지름은 수정가능

# 함수 정의
def potential_at_xy(x, y, B, λ):
    return B * (np.cos(np.pi * 2 * x / λ) + np.cos(np.pi * 2 * y / λ))

B = 1 / 4  # 적절한 B 값 설정
λ = atom_lattice

potential_barrier = []  # 각 반경에서의 최대-최소 잠재 에너지를 저장할 리스트

# tip 좌표 베이스 계산
base = [x * s for x in np.arange(tip_lattice, atom_limit, tip_lattice) for s in (1, -1)]
base.insert(0, 0.0)  # tip 중심 추가
tip_base = [(x, y) for x in base for y in base]

# 반지름별 최대-최소 잠재 에너지 계산
for radius in radiuses :
    max_potential = float('-inf')  # 최대 잠재 에너지 초기화
    min_potential = float('inf')   # 최소 잠재 에너지 초기화

    # 각 반경에서 x_move와 y_move를 변화시키며 잠재 에너지를 계산합니다.
    potential_values = {}  # 각 위치에서의 잠재 에너지 값을 저장하기 위한 딕셔너리
    for x_move in np.arange(0, atom_lattice, 0.1):
        for y_move in np.arange(0, atom_lattice, 0.1):
            potential_sum = 0.0
            for x, y in tip_base:
                if np.sqrt((x) ** 2 + (y) ** 2) <= radius + 0.001:
                    potential = potential_at_xy(x + x_move, y + y_move, B, λ)
                    potential_sum += potential

                    # 각 위치에서의 잠재 에너지 값을 저장합니다.
                    potential_values[(x_move, y_move)] = potential_sum

    # 최대값과 최소값을 찾습니다.
    max_potential = max(potential_values.values())
    min_potential = min(potential_values.values())

    # 최대값과 최소값을 가지는 위치의 x_move와 y_move를 찾습니다.
    best_max_x_move, best_max_y_move = [move for move, potential in potential_values.items() if potential == max_potential][0]
    best_min_x_move, best_min_y_move = [move for move, potential in potential_values.items() if potential == min_potential][0]

    # 각 반경에서 최대값일 때와 최소값일 때의 x_move와 y_move를 출력합니다.
    print(f"radius: {radius}, (max x_move: {best_max_x_move}, max y_move: {best_max_y_move}), max potential: {max_potential}")
    print(f"radius: {radius}, (min x_move: {best_min_x_move}, min y_move: {best_min_y_move}), min potential: {min_potential}")

    # 최대-최소 잠재 에너지의 차이를 계산하여 리스트에 추가합니다.
    potential_barrier.append(max_potential - min_potential)

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(radiuses, potential_barrier, marker='o')
plt.xlabel('Radius')
plt.ylabel('Max-Min Potential')
plt.title('Radius vs. Max-Min Potential')
plt.grid(True)
plt.show()




