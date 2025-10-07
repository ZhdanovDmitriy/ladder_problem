# ladder_problem
Given: a, b are the width of two corridors (non-negative numbers)

It is necessary: to find the length of an infinitely narrow (without width) staircase that can be carried through an absolutely straight (90 degrees) angle formed by two converging corridors with widths a and b.

<img width="825" height="811" alt="image" src="https://github.com/user-attachments/assets/153e36f2-8695-49d3-afe5-527f75dc69f0" />
<img width="832" height="789" alt="image" src="https://github.com/user-attachments/assets/f617c620-6b6b-479f-9b17-f359acbce8ca" />
<img width="793" height="106" alt="image" src="https://github.com/user-attachments/assets/30bbb9a5-c112-42f4-a8a1-297ae843787c" />

The repository contains an animation of the numerical method for solving this problem. If you are interested in the analytical solution, you can find it online. I was interested in constructing a numerical scheme for this problem.

The main parameters affecting the convergence rate are:
step_coef - a coefficient governing the size of the shift of point A at each iteration (the smaller the better, but the more iterations are required)
exp_coef - the expansion coefficient of the segment AC
compr_coef - the compression coefficient of the segment AC
Eps - the stopping parameter (the point x_prev should be closer than Eps to the green (left) wall)

The main idea of ​​the solution:
Fix a corner point B. Choose L such that the staircase necessarily passes through the corridor. Take point A above point B and begin moving it along the wall. The coordinates of point C are calculated at each step. The process continues until:
1) x_prev - x <= 0 - this means that point C has passed the extreme point of its trajectory (the trajectory resembles a golden ratio loop from 0 to 2Pi), meaning it can easily move on. Therefore, this L is satisfactory. We reset all variables to their initial values ​​and lengthen L by exp_coef times. A small step allows us to capture the extreme point as accurately as possible, which is why step_coef is so important. If step_coef is not large enough, we will undershoot or overshoot the extreme point.
2) x < 0. This means that our staircase does not extend into the corridor and must be shortened by compr_coef times.

In both cases, the stopping condition is checked: x_prev < Eps. x_prev is the point closest to the extreme point. This condition does not guarantee the order of accuracy of Eps, but merely states that we are reasonably close to the given answer. Achieving the specified accuracy requires a more rigorous mathematical evaluation or the selection of a different stopping criterion.

The constructed iterative numerical scheme is guaranteed to converge to the maximum possible ladder length due to the choice of the exp_coef and compr_coef coefficients. The convergence of the process is non-uniform.

On average, obtaining an answer with 0.1% accuracy requires approximately 6000 iterations, which is a very poor indicator for an iterative process. However, considering that this problem is being solved with enthusiasm for educational purposes, this is a good result. The number of iterations can be reduced by a factor of 10 by initially increasing the interval by exp_coef = 1.1 until it hits a wall. Then, reduce exp_coef = 1.001 for a more accurate solution search.

Note: The absolute error increases significantly if a<<b, i.e., if a and b are large. The first problem (a<<b) is caused by the fact that the intervals AB<<BC, so a small shift in point A significantly shifts point C, increasing its step and reducing the probability of capturing an exact extremum. The second problem (large a and b) arises because the method essentially only controls the relative error, not the absolute error. The relative error always stays around 0.1% with these settings. It could be improved by reducing step_coef and increasing the number of iterations proportionally.

If you're interested in my solution, I'd love to hear your feedback. Please give me a star if you've read this far. If this topic proves relevant, I'll propose a more rigorous numerical approach for this problem!

# Задача о лестнице в углу
Дано: a, b - ширина двух коридоров (неотрицательные числа) 
Необходимо: найти длину бесконечно узкой (не имеющей ширины) лестницы, которую можно пронести через абсолютно прямой (90 градусов) угол, образованный двумя сходящимися коридорами с шириной a и b.

В репозитории представлена анимация численного метода решения данной задачи. Если вас интересует аналитическое решение - вы можете найти его в интернете. Мне было интересно построить численную схему для данной задачи.

Основными параметрами влияющими на скорость сходимости являются:
step_coef - коэфициент, отвечающий за размер сдвига точки A на каждой итерации(чем меньше, тем лучше, но тем больше итераций требуется)
exp_coef - коэфициент растяжения отрезка AC
compr_coef - коэфициент сжатия отрезка AC
Eps - парaметр остановки(точка x_prev должна находится у зеленой(левой) стены ближе чем на Eps)

Основная идея решения:
Фиксируем угловую точку B. Берем L такое, что лестница обязательно проходит через коридор. Точку А берем над точкой B и начинаем двигать вдоль стены. Координаты точки C считаем на каждом шаге. Процесс продолжается до тех пор, пока:
1)x_prev - x  <= 0 - это означает, что точка C прошла экстримальную точку своей траектории(троектория напоминает петлю золотого сечения от 0 до 2Pi), а значит легко сможет пройти дальше. Следовательно, данная длина L нас устраивает. Мы сбрасываем все переменные на начальные значения, а L удлиняем в exp_coef раз. Маленький шаг позволяет максимально точно уловить экстремум, поэтому step_coef так важен. Если step_coef недостаточно большой, то мы будем недоходить или перепрыгивать экстремум.
2)x < 0. Это означает, что наша лестница не проходит в коридор и её нужно укоротить в compr_coef раз.

В обоих случаях проверяется условие остановки: x_prev < Eps. x_prev - точка наиболее близкая к экстремуму. Данное условие не гарантирует порядок точности Eps, а лишь констатирует факт, что мы достаточно близки к данному ответу. Для достижения заданной точности требуется более строгая математическая оценка или выбор другого критерия остановки.

Построенная итерационная численная схема гарантированно сходится к максимально возможной величине длины лестницы за счет выбора коэфициентов exp_coef, compr_coef. Сходимость процесса неоднородная. 

В среднем для получения ответа с точностью 0,1% требуется около 6000 итераций, что является очень плохим показателем для итерационного процесса. Однако, учитывая что данная задача решается на интузиазме в образовательных целях, - это неплохой результат. Количество итераций можно сократить в 10 раз, если изначально увеличивать отрезок в exp_coef = 1.1 раз до тех пор, пока он не упрется в стену. А потом сократить exp_coef = 1.001 для более аккуратного поиска решения.

Замечание: Абсолютная погрешность сильно возрастает, если a<<b, если a и b большие. Первая проблема (a<<b) вызвана тем, что отрезов AB<<BC, поэтому небольшой сдвиг точки A сильно сдвигает точку C - увеличивая её шаг и снижая вероятность поймать точный экстремум. Вторая проблема(a и b большие) возникает из-за того, что метод по сути контролирует только относительную погрешность, а не абсолютную. Относительная погрешность всегда держиться в районе 0.1% при данных настройках. Можно лучше, если уменьшить step_coef, увеличив пропорционально число итераций.

Если вас заинтересовало моё решение, буду рад услышать обратную связь. Не жалейте звезд, если дочитали до сюда. Если данная тема будет актуальна, я предложу более строгую численную схему для данной задачи!
