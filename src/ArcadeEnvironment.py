
import arcade
from classes import sClass

SCREEN_TITLE = "Swarm Collision Example"

swarm_member_count = 10
swarm = []
collided = []

for i in range(swarm_member_count):
    swarm.append(sClass.Floater())

def on_draw(delta_time):
    arcade.start_render()

    for i in swarm:
        i.move_to_destination()
        if not i.has_collided:
            arcade.draw_circle_filled(i.position.x, i.position.y, i.size,arcade.color.BLUE_GREEN)
        else:
            arcade.draw_circle_filled(i.position.x,i.position.y,i.size,arcade.color.RED_DEVIL)

    for i in swarm:
        for j in swarm:
            if i.id != j.id and i.position.x == j.position.x and i.position.y == j.position.y:
                i.collide()
                j.collide()

def main():
    # Open up our window
    arcade.open_window(sClass.squarea, sClass.squarea, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.WHITE)

    # Tell the computer to call the draw command at the specified interval.
    arcade.schedule(on_draw, 1/80)

    # Run the program
    arcade.run()


if __name__ == "__main__":
    main()