import numpy as np
import matplotlib.pyplot as plt

# 함수 정의
def z(x, y, B, λ):
    return B * (np.cos(np.pi*2*x/λ) * np.cos(np.pi*2*y/λ))

# 초기 설정
atom_lattice = 1
tip_lattice = 1
atom_limit = 1000  # 그냥 radius보다 충분히 큰 숫자
radius_multiple = np.linspace(1, 30, 30)  # 반지름을 1부터 n까지 변화시킬 예정입니다.

total_z_sum = []  # 각 반경 내의 함수값의 총 합을 저장할 리스트
atom_counts = []  # 각 반경에 대한 tip 원자의 총 수

B = 0.01  # 적절한 B 값 설정
λ = atom_lattice

# tip 좌표 베이스 계산
tip_base = [x * s for s in (1, -1) for x in np.arange(tip_lattice, atom_limit, tip_lattice)]
tip_base.insert(0, 0.0)  # tip 중심 추가

# 반지름과 함수값의 총합 계산
for radius_multiplier in radius_multiple:
    radius = tip_lattice * radius_multiplier  # tip 원 반지름
    tip_xy_list_unduplicate = []  # 원 안의 tip 좌표 리스트 초기화

    # tip 원 안의 좌표만 선택
    for x in tip_base:
        for y in tip_base:
            if np.sqrt(x**2 + y**2) <= radius:
                tip_xy_list_unduplicate.append((x, y))

    # 함수값 계산
    z_values_sum = sum(z(x, y, B, λ) for x, y in tip_xy_list_unduplicate)
    total_z_sum.append(z_values_sum)
    atom_counts.append(len(tip_xy_list_unduplicate))  # tip 원자의 총 수 추가

# 그래프 그리기
fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:red'
ax1.set_xlabel('Radius')
ax1.set_ylabel('Total Z Sum', color=color)
ax1.plot(radius_multiple * tip_lattice, total_z_sum, color=color, marker='o', label='Total Z Sum')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # y축 공유 그래프 생성
color = 'tab:blue'
ax2.set_ylabel('Atom Count', color=color)  # 두 번째 y축 레이블
ax2.plot(radius_multiple * tip_lattice, atom_counts, color=color, marker='x', linestyle='--', label='Atom Count')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # 레이아웃 조정
plt.title('Radius vs. Total Z Sum and Atom Count')
plt.show()







