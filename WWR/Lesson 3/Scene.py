
import math
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.


def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="turquoise1")
    
    sun_center_x = 150
    sun_bottom = 450
    sun_height = 470
    draw_sun(canvas, sun_center_x,
            sun_bottom, sun_height)
    cloud_center_x = 50
    cloud_bottom = 400
    cloud_height = 1300
    draw_cloud(canvas, cloud_center_x,
            cloud_bottom, cloud_height)
    cloud_center_x = 90
    cloud_bottom = 400
    cloud_height = 1300
    draw_cloud(canvas, cloud_center_x,
            cloud_bottom, cloud_height)
    cloud_center_x = 700
    cloud_bottom = 400
    cloud_height = 1300
    draw_cloud(canvas, cloud_center_x,
            cloud_bottom, cloud_height)
    cloud_center_x = 550
    cloud_bottom = 330
    cloud_height = 1300
    draw_cloud(canvas, cloud_center_x,
            cloud_bottom, cloud_height)
    cloud_center_x = 520
    cloud_bottom = 330
    cloud_height = 1300
    draw_cloud(canvas, cloud_center_x,
            cloud_bottom, cloud_height)
    cloud_center_x = 500
    cloud_bottom = 330
    cloud_height = 1300
    draw_cloud(canvas, cloud_center_x,
            cloud_bottom, cloud_height)
    cloud_center_x = 490
    cloud_bottom = 330
    cloud_height = 1300
    draw_cloud(canvas, cloud_center_x,
            cloud_bottom, cloud_height)
    cloud_center_x = 470
    cloud_bottom = 330
    cloud_height = 1300
    draw_cloud(canvas, cloud_center_x,
            cloud_bottom, cloud_height)

  
    
    
def draw_sun (canvas, center_x, bottom, height):
    sun_width = height / 10
    sun_height = height / 10
    sun_left = center_x - sun_width / 2
    sun_right = center_x + sun_width / 2
    sun_top = bottom + sun_height

    draw_oval(canvas,
            sun_left, sun_top, sun_right, bottom,
            outline="gold1", width=1, fill="gold1")

def draw_cloud (canvas, center_x, bottom, height):
    cloud_width = height / 10
    cloud_height = height / 30
    cloud_left = center_x - cloud_width / 2
    cloud_right = center_x + cloud_width / 2
    cloud_top = bottom + cloud_height

    draw_oval(canvas,
            cloud_left, cloud_top, cloud_right, bottom,
            outline="snow1", width=1, fill="snow1")

def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="darkorange2")
    tree_center_x = 100
    tree_bottom = 100
    tree_height = 85
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 110
    tree_bottom = 100
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 120
    tree_bottom = 100
    tree_height = 90
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 130
    tree_bottom = 100
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 140
    tree_bottom = 100
    tree_height = 85
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 150
    tree_bottom = 100
    tree_height = 90
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 160
    tree_bottom = 100
    tree_height = 90
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 180
    tree_bottom = 100
    tree_height = 85
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 190
    tree_bottom = 100
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 200
    tree_bottom = 100
    tree_height = 90
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 210
    tree_bottom = 100
    tree_height = 90
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 220
    tree_bottom = 100
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 230
    tree_bottom = 100
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 90
    tree_bottom = 100
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 50
    tree_bottom = 100
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 10
    tree_bottom = 100
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 20
    tree_bottom = 100
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 30
    tree_bottom = 100
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 40
    tree_bottom = 100
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 60
    tree_bottom = 100
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 70
    tree_bottom = 100
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 80
    tree_bottom = 100
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 90
    tree_bottom = 100
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    sea_center_x = 390
    sea_bottom = 1
    sea_height = 1670
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    sea_center_x = 420
    sea_bottom = 1
    sea_height = 1670
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    sea_center_x = 440
    sea_bottom = 1
    sea_height = 1670
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    sea_center_x = 460
    sea_bottom = 1
    sea_height = 1670
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    sea_center_x = 480
    sea_bottom = 1
    sea_height = 1670
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    sea_center_x = 500
    sea_bottom = 1
    sea_height = 1670
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    sea_center_x = 520
    sea_bottom = 1
    sea_height = 1670
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    sea_center_x = 540
    sea_bottom = 1
    sea_height = 1670
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    sea_center_x = 560
    sea_bottom = 1
    sea_height = 1670
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    sea_center_x = 580
    sea_bottom = 1
    sea_height = 1670
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    sea_center_x = 600
    sea_bottom = 1
    sea_height = 1670
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    sea_center_x = 620
    sea_bottom = 1
    sea_height = 1670
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    sea_center_x = 640
    sea_bottom = 1
    sea_height = 1670
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    sea_center_x = 660
    sea_bottom = 1
    sea_height = 1670
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    sea_center_x = 680
    sea_bottom = 1
    sea_height = 1670
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    sea_center_x = 700
    sea_bottom = 1
    sea_height = 1670
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    sea_center_x = 720
    sea_bottom = 1
    sea_height = 1670
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    sea_center_x = 350
    sea_bottom = -5
    sea_height = 700
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    sea_center_x = 740
    sea_bottom = 1
    sea_height = 1670
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    sea_center_x = 760
    sea_bottom = 1
    sea_height = 1670
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    sea_center_x = 780
    sea_bottom = 1
    sea_height = 1670
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    sea_center_x = 800
    sea_bottom = 1
    sea_height = 1670
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    tree_center_x = 95
    tree_bottom = 90
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 85
    tree_bottom = 90
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 75
    tree_bottom = 90
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 65
    tree_bottom = 90
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 55
    tree_bottom = 90
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 45
    tree_bottom = 90
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 35
    tree_bottom = 90
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 25
    tree_bottom = 90
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 15
    tree_bottom = 90
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 5
    tree_bottom = 90
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 105
    tree_bottom = 90
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 115
    tree_bottom = 90
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 125
    tree_bottom = 90
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 135
    tree_bottom = 90
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 145
    tree_bottom = 90
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 155
    tree_bottom = 90
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 165
    tree_bottom = 90
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 175
    tree_bottom = 90
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 185
    tree_bottom = 90
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 195
    tree_bottom = 90
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 205
    tree_bottom = 90
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 215
    tree_bottom = 90
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    beach_center_x = 335
    beach_bottom = 1
    beach_height = 1670
    draw_beach(canvas, beach_center_x,
            beach_bottom, beach_height)
    beach_center_x = 305
    beach_bottom = 1
    beach_height = 800
    draw_beach(canvas, beach_center_x,
            beach_bottom, beach_height)
    beach_center_x = 290
    beach_bottom = 1
    beach_height = 800
    draw_beach(canvas, beach_center_x,
            beach_bottom, beach_height)
    beach_center_x = 290
    beach_bottom = 20
    beach_height = 800
    draw_beach(canvas, beach_center_x,
            beach_bottom, beach_height)
    sea_center_x = 350
    sea_bottom = 1
    sea_height = 1670
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    sea_center_x = 320
    sea_bottom = 1
    sea_height = 1000
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    sea_center_x = 360
    sea_bottom = 1
    sea_height = 1670
    draw_sea(canvas, sea_center_x,
            sea_bottom, sea_height)
    
def draw_pine_tree(canvas, center_x, bottom, height):
    
    trunk_width = height / 20
    trunk_height = height / 4
    trunk_left = center_x - trunk_width / 20
    trunk_right = center_x + trunk_width / 20
    trunk_top = bottom + trunk_height

    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 10
    skirt_right = center_x + skirt_width / 10
    skirt_top = bottom + height

    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")

def draw_sea (canvas, center_x, bottom, height):
    sea_width = height / 10
    sea_height = height / 10
    sea_left = center_x - sea_width / 2
    sea_right = center_x + sea_width / 2
    sea_top = bottom + sea_height

    draw_oval(canvas,
            sea_left, sea_top, sea_right, bottom,
            outline="steelblue1", width=1, fill="steelblue1")

def draw_beach (canvas, center_x, bottom, height):
    beach_width = height / 10
    beach_height = height / 10
    beach_left = center_x - beach_width / 2
    beach_right = center_x + beach_width / 2
    beach_top = bottom + beach_height

    draw_oval(canvas,
            beach_left, beach_top, beach_right, bottom,
            outline="khaki1", width=1, fill="khaki1")
    

    

# Call the main function so that
# this program will start executing.
main()