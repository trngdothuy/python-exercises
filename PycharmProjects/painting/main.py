# import colorgram
#
# rgb = []
# colors = colorgram.extract('IMG_0083.JPG', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb.append(new_color)
#
# print(rgb)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(67, 90, 73), (199, 149, 111), (243, 228, 185), (149, 95, 61), (15, 12, 14), (25, 18, 15), (219, 61, 128), (229, 197, 134), (43, 60, 46), (224, 98, 46), (50, 73, 55), (183, 49, 100), (13, 13, 15), (162, 129, 83), (191, 141, 157), (238, 240, 239), (165, 22, 45), (129, 39, 20), (234, 220, 223), (81, 83, 130), (159, 163, 158), (225, 179, 165), (152, 152, 165), (73, 66, 47), (229, 230, 238), (223, 171, 183), (116, 138, 104), (118, 116, 154), (49, 57, 118), (181, 184, 214)]

tim.setheading(225)
tim.fd(300)
tim.setheading(0)
number_dot = 100

for dot_count in range(1, number_dot + 1):
    tim.dot(20, random.choice(color_list))
    tim.fd(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)

