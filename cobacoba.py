#%%
def decorFunc(oriFunc):
    def wrapperFunc():
        print("Mampus lu")
        return oriFunc()

    return wrapperFunc


@decorFunc
def display():
    print("Woah")


display()

#%%
import re

def count_eatable_chocolates(total_money, cost_of_one_chocolate):
    money = int(re.findall(r"-?\d+", total_money)[0])
    cost = int(re.findall(r"-?\d+", cost_of_one_chocolate)[0])

    if money < 1 or cost < 1:
        return "Invalid Input"
    chocolate = money // cost
    w = chocolate
    while w > 2:
        new = w // 3
        chocolate += new
        w -= 2*new
    return chocolate

print(count_eatable_chocolates("Arun has 2074$", "One chocolate costs 2$"))
print(count_eatable_chocolates("Arun has got 22$", "One chocolate costs 2$"))
print(count_eatable_chocolates("36$", "3 $"))
print(count_eatable_chocolates("I have 4 dollars", "1   $"))
print(count_eatable_chocolates("-28$", "2$"))
print(count_eatable_chocolates("0$", "0$"))
print(count_eatable_chocolates("8$", "-2$"))

#%%
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Snowman"

def draw_grass():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)

def draw_snowman(x, y):
    # For reference
    arcade.draw_point(x, y, arcade.color.RED, 5)    

    # Snow
    arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)

def on_draw(delta_time):
    arcade.start_render()

    draw_grass()
    draw_snowman(on_draw.snowman1_x, 140)
    draw_snowman(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Add one to the x value, making the snow person move right
    # Negative numbers move left. Larger numbers move faster.
    on_draw.snowman1_x += 1

on_draw.snowman1_x = 150

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.DARK_BLUE)
    # arcade.start_render()  # Clear screen and start render process

    arcade.schedule(on_draw, 1/60)

    # arcade.finish_render()  # Finish drawing and display the result
    arcade.run()

if __name__ == '__main__':
    main()