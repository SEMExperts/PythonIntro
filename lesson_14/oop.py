"""
class ClassName(parent_list):
    body_of_class

"""
class Point:
    xx = 0                               # атрибуты класса
    yy = 0

    def __init__(self, X=0, Y=0):
        self.x = X                      # атрибуты объекта
        self.y = Y


pt1 = Point(3, 6) # объект класса
print(id(pt1))
print(pt1.x)
pt2 = Point()
print(id(pt2))
print(pt1.x)
print(pt1.y)
Point.xx = 9
print(pt1.xx)
print(pt2.xx)
