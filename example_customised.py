# A test of pyglet_grid with customised parameters
#
# Copyright 2011 Jacob Conrad Martin
# http://jacobconradmartin.com
#
# This file is part of pyglet_grid.
#
# pyglet_grid is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyglet_grid is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyglet_grid. If not, see <http://www.gnu.org/licenses/>.


import pyglet
from pyglet_grid import pyglet_grid

from random import random

# How many elements to draw each time through the loop
how_many = 1000

# Get an instance of pyglet_grid
grid = pyglet_grid.Grid()
# Set up the grid with custom parameters
# 1. Set up the window
grid.window_width = 400
grid.window_height = 800
grid.background = (255, 255, 255, 255)
grid.init_window()
# 2. Set up the cell size and border
grid.cell_height = 20
grid.cell_width = 80
grid.cell_border = 5
grid.init_grid()
# 3. Initialise the vertex list
grid.init_vertex_list()

# It's slightly faster not to have to look these up every time through a loop
w = grid.w
h = grid.h

# Global variable used for saving images
counter = 0


# ----- EXAMPLE ONE -----

def update(dt):
    "Basic example showing simple usage."
    
    # Clear the grid
    grid.clear_all_cells()
    # Set the colours of some random cells in the grid
    for x in range(how_many):
        x = int(w * random())
        y = int(h * random())
        r = int(255 * random())
        g = int(255 * random())
        b = int(255 * random())
        c = (r, g, b)
        grid.set_cell(x, y, c)
    # Draw the grid
    grid.draw()
    # Uncomment the following three lines to save images
    #global counter
    #counter += 1
    #pyglet.image.get_buffer_manager().get_color_buffer().save('data/'+str(counter).zfill(10)+'.png')
    

# ----- EXAMPLE TWO -----

# Set up a list to track the "dirty" cells
dirty_cells = []

def update_faster(dt):
    """More complicated example showing how to speed things up slightly.
    We do this by clearing only the colours of specific cells instead of all of them."""
    
    # Unset the colours of the dirty cells
    global dirty_cells
    dc = dirty_cells[:] # Iterate over a copy of the list, but modify the real list
    for x, y in dc:
        # Allow the dots to stick around for a while
        if random() < 0.1:
            # Unset the colour of the cell (to the grid's background_colour)
            grid.unset_cell(x, y)
            dirty_cells.remove([x, y])
    # Set the colours of some random cells in the grid
    for x in range(how_many):
        x = int(w * random())
        y = int(h * random())
        r = int(255 * random())
        g = int(255 * random())
        b = int(255 * random())
        c = (r, g, b)
        grid.set_cell(x, y, c)
        # Add this cell to the list of dirty cells
        dirty_cells.append([x, y])
    # Draw the grid
    grid.window.clear()
    grid.draw()
    # Uncomment the following three lines to save images
    #global counter
    #counter += 1
    #pyglet.image.get_buffer_manager().get_color_buffer().save('data/'+str(counter).zfill(10)+'.png')
    

# ----- RUN EXAMPLES -----

# UNCOMMENT FOR EXAMPLE ONE
pyglet.clock.schedule(update)

# UNCOMMENT FOR EXAMPLE TWO
#pyglet.clock.schedule(update_faster)

# Go!
pyglet.app.run()