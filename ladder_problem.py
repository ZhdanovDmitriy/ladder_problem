import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

a = 6.0
b = 8.0
Eps = 0.000001
exp_coef = 1.001
rude_exp_coef = 1.1
compr_coef = 0.999
rude_compr_coef = 0.9
step_coef = 0.1

if a > b: a, b = b, a
L = (a*a + b*b)**0.5
delta = step_coef * min(a,b)
max_iterations = 100000
x_prev = b * 1.1

def find_point_C(A, B, L):
    a, b = A
    c, d = B
    dx = c - a
    dy = d - b
    dist_AB = math.hypot(dx, dy)

    k = L / dist_AB
    x = a + k * dx
    y = b + k * dy
    return (x, y)

fig, ax = plt.subplots()
x_center = b
y_center = -1.25 * a
width = 3*b
height = 4*a
ax.set_xlim(x_center - width/2, x_center + width/2)
ax.set_ylim(y_center - height/2, y_center + height/2)
ax.set_aspect('equal')
point_A, = ax.plot([], [], 'ro', label='A')
point_B, = ax.plot([], [], 'bo', label='B')
point_C, = ax.plot([], [], 'go', label='C')
line_AC, = ax.plot([], [], 'k-', lw=1)
line_AB, = ax.plot([], [], 'gray', lw=1)
# y = 0, x > 0
ax.plot([0, b + delta * max_iterations + 2], [0, 0], 'r-', lw=2)
# y = -a, x > b
ax.plot([b, b + delta * max_iterations + 2], [-a, -a], 'r-', lw=2)
# x = 0, y < 0
ax.plot([0, 0], [-4 * a, 0], 'g-', lw=2)
# x = b, y < -a
ax.plot([b, b], [-4 * a - 3, -a], 'r-', lw=2)
ax.legend(loc='upper right')


cur_frame = 0
rude_approx = True
def update(frame):
    global cur_frame, L, x_prev, delta, rude_approx
    cur_frame += 1
    A = (b + delta * cur_frame, 0)
    B = (b, -a)
    C = find_point_C(A, B, L)


    if(x_prev - C[0] < 0):
        if(rude_approx):
            L = L * rude_exp_coef
        else:
            L = L * exp_coef
        if(x_prev <= Eps):
            anim.event_source.stop()
            ans = (a**(2/3) + b**(2/3))**(3/2)
            print("======================================================================================")
            print(f"Максимальная длина лестницы для a = {a}, b = {b} составляет {L}\nПотребовалось {frame} итераций")
            print(f"Аналитический ответ: L = {ans}")
            print(f"Относительная погрешность: {abs(1 - L/ans) * 100} %")
            print("======================================================================================")
            return ()
        x_prev = b * 1.1
        cur_frame = 0
    else:
        x_prev = C[0]

    if(C[0] < 0):
        if(rude_approx):
            rude_approx = False
            L = L * rude_compr_coef
        else:
            L = L * compr_coef
            if(x_prev <= Eps):
                anim.event_source.stop()
                ans = (a**(2/3) + b**(2/3))**(3/2)
                print("======================================================================================")
                print(f"Максимальная длина лестницы для a = {a}, b = {b} составляет {L}\nПотребовалось {frame} итераций")
                print(f"Аналитический ответ: L = {ans}")
                print(f"Относительная погрешность: {abs(1 - L/ans) * 100} %")
                print("======================================================================================")
                return ()
        x_prev = b * 1.1
        cur_frame = 0

    point_A.set_data([A[0]], [A[1]])
    point_B.set_data([B[0]], [B[1]])
    point_C.set_data([C[0]], [C[1]])

    line_AC.set_data([A[0], C[0]], [A[1], C[1]])

    info_text = ax.text(
        0.02, 0.95, f"Текущее значение L = {L}", 
        transform=ax.transAxes,
        fontsize=10,
        verticalalignment='top',
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.7)
    )
    
    return point_A, point_B, point_C, line_AB, line_AC, info_text

anim = FuncAnimation(fig, update, frames=max_iterations, interval=0, blit=True, cache_frame_data=False)
plt.show()
