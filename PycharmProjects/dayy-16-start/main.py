# from turtle import Screen, Turtle
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.fd(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
# table.field_names = ["Pokemon Name", "Type"]
# table.add_rows(
#     [
#         ["Pikachu", "Electric"],
#         ["Squirtle", "Water"],
#         ["Charmander", "Fire"]
#     ]
# )

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)




