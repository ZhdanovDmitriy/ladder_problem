# ladder_problem
Given: a, b are the width of two corridors (non-negative numbers)

It is necessary: to find the length of an infinitely narrow (without width) staircase that can be carried through an absolutely straight (90 degrees) angle formed by two converging corridors with widths a and b.

<img width="825" height="811" alt="image" src="https://github.com/user-attachments/assets/153e36f2-8695-49d3-afe5-527f75dc69f0" />
<img width="832" height="789" alt="image" src="https://github.com/user-attachments/assets/f617c620-6b6b-479f-9b17-f359acbce8ca" />
<img width="793" height="106" alt="image" src="https://github.com/user-attachments/assets/30bbb9a5-c112-42f4-a8a1-297ae843787c" />

The repository contains an animation of a numerical method for solving this problem. If you are interested in an analytical solution, you can find it on the Internet. I was interested in constructing a numerical scheme for this problem.

The main parameters affecting the convergence rate are:

step_coef is the coefficient responsible for the size of the shift of point A at each iteration (the smaller the better, but the more iterations are required)
exp_coef is the coefficient of stretching the AC segment (subtle search for a solution)
rude_exp_coef is the coefficient of stretching the AC segment until it collides with the wall
compr_coef is the coefficient of compression of the AC segment (subtle search for a solution)
rude_compr_coef is the coefficient of compression of the AC segment after the first collision with the wall
Eps is the stop parameter (the x_prev point should be located at the green (left) wall closer than Eps)

The basic idea of the solution:

We fix the corner point B. We take L such that the staircase necessarily passes through the corridor. We take point A above point B and start moving along the wall. The coordinates of point C are calculated at each step. The process continues until:

1)x_prev - x <= 0 - this means that point C has passed the extreme point of its trajectory (the trajectory resembles a loop of the golden ratio from 0 to 2Pi), which means it can easily pass further. Therefore, this length L suits us. We reset all variables to their initial values, and lengthen L by exp_coef times (Until the first collision with the wall by rude_exp_coef times). A small step after a collision allows you to capture the extreme as accurately as possible, which is why step_coef is so important. If step_coef is not big enough, then we will undershoot or overshoot the extreme.

2)x < 0. This means that our staircase does not go into the corridor and it needs to be shortened by a factor of compr_coef.(the first decrease occurs in rude_compr_coef times)

In both cases, the stop condition is checked: x_prev < Eps. x_prev is the point closest to the extreme. This condition does not guarantee the order of accuracy of Eps, but only states the fact that we are close enough to this answer. To achieve the specified accuracy, a more rigorous mathematical assessment or the choice of another stopping criterion is required.

The constructed iterative numerical scheme is guaranteed to converge to the maximum possible length of the ladder by selecting the coefficients exp_coef, compr_coef, rude_exp_coef, rude_compr_coef. The convergence of the process is heterogeneous. 

On average, it takes about 350 iterations to get an answer with an accuracy of 0.1%, which is an acceptable indicator for an iterative process.

Note: The absolute error increases greatly if a<<b, if a and b are large. The first problem (a<<b) is caused by the fact that the segments are AB<<BC, so a small shift of point A strongly shifts point C, increasing its pitch and reducing the probability of catching the exact extreme. The second problem (a and b are large) arises from the fact that the method essentially controls only the relative error, not the absolute one. The relative margin of error is always around 0.1% at these settings. You can do better if you reduce step_coef by increasing the number of iterations proportionally.

If you are interested in my solution, I will be glad to hear your feedback. 
Don't spare the stars if you've read this far.

# Задача о лестнице в углу
Дано: a, b - ширина двух коридоров (неотрицательные числа) 

Необходимо: найти длину бесконечно узкой (не имеющей ширины) лестницы, которую можно пронести через абсолютно прямой (90 градусов) угол, образованный двумя сходящимися коридорами с шириной a и b.

В репозитории представлена анимация численного метода решения данной задачи. Если вас интересует аналитическое решение - вы можете найти его в интернете. Мне было интересно построить численную схему для данной задачи.

Основными параметрами влияющими на скорость сходимости являются:

step_coef - коэфициент, отвечающий за размер сдвига точки A на каждой итерации(чем меньше, тем лучше, но тем больше итераций требуется)
exp_coef - коэфициент растяжения отрезка AC (тонкий поиск решения)
rude_exp_coef - коэфициент растяжения отрезка AC до столкновения со стеной
compr_coef - коэфициент сжатия отрезка AC (тонкий поиск решения)
rude_compr_coef - коэфициент сжатия отрезка AC после первого столкновения со стеной
Eps - парaметр остановки(точка x_prev должна находится у зеленой(левой) стены ближе чем на Eps)

Основная идея решения:

Фиксируем угловую точку B. Берем L такое, что лестница обязательно проходит через коридор. Точку А берем над точкой B и начинаем двигать вдоль стены. Координаты точки C считаем на каждом шаге. Процесс продолжается до тех пор, пока:

1)x_prev - x  <= 0 - это означает, что точка C прошла экстримальную точку своей траектории(троектория напоминает петлю золотого сечения от 0 до 2Pi), а значит легко сможет пройти дальше. Следовательно, данная длина L нас устраивает. Мы сбрасываем все переменные на начальные значения, а L удлиняем в exp_coef раз(До первого столкновения со стеной в rude_exp_coef раз). Маленький шаг после столкновения позволяет максимально точно уловить экстремум, поэтому step_coef так важен. Если step_coef недостаточно большой, то мы будем недоходить или перепрыгивать экстремум.

2)x < 0. Это означает, что наша лестница не проходит в коридор и её нужно укоротить в compr_coef раз.(первое уменьшение происходит в rude_compr_coef раз)

В обоих случаях проверяется условие остановки: x_prev < Eps. x_prev - точка наиболее близкая к экстремуму. Данное условие не гарантирует порядок точности Eps, а лишь констатирует факт, что мы достаточно близки к данному ответу. Для достижения заданной точности требуется более строгая математическая оценка или выбор другого критерия остановки.

Построенная итерационная численная схема гарантированно сходится к максимально возможной величине длины лестницы за счет выбора коэфициентов exp_coef, compr_coef, rude_exp_coef, rude_compr_coef. Сходимость процесса неоднородная. 

В среднем для получения ответа с точностью 0,1% требуется около 350 итераций, что является приемлемым показателем для итерационного процесса.

Замечание: Абсолютная погрешность сильно возрастает, если a<<b, если a и b большие. Первая проблема (a<<b) вызвана тем, что отрезов AB<<BC, поэтому небольшой сдвиг точки A сильно сдвигает точку C - увеличивая её шаг и снижая вероятность поймать точный экстремум. Вторая проблема(a и b большие) возникает из-за того, что метод по сути контролирует только относительную погрешность, а не абсолютную. Относительная погрешность всегда держиться в районе 0.1% при данных настройках. Можно лучше, если уменьшить step_coef, увеличив пропорционально число итераций.

Если вас заинтересовало моё решение, буду рад услышать обратную связь. 
Не жалейте звезд, если дочитали до сюда. 
