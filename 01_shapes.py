# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):

    def vector(vector_start, length, angle):
        v = sd.get_vector(vector_start, angle, length)
        return v.end_point

    def polygon(point, angle, length):
        angle_start = angle
        angle_polygon = 360 / n
        point_polygon = point
        for _ in range(n):
            if _ == 0:
                angle = angle_start
            else:
                angle += angle_polygon
            if _ < (n - 1):
                end_point = vector(point, length, angle)
            else:
                end_point = point_polygon
            sd.line(start_point=point, end_point=end_point, color=sd.COLOR_YELLOW, width=1)
            point = end_point
    return polygon


draw_triangle = get_polygon(n=6)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)


sd.pause()
