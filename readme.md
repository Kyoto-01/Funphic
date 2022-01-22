# Funphic

Funphic is a program capable of plotting simple function graphs. The graphics can be plotted as .PNG images or directly in your terminal.

## Command

in src/

~~~shell
python3 funphic.py [function] [x_range_start] [x_range_end] [y_range_start] [y_range_end] [x_increment] [point_color] [back_color] [render_type]
~~~

### Command options
* `function`: The function to plot the graph
* `x_range_start`: Initial value of the range of x values in the Cartesian map
* `x_range_end`: Final value of the range of x values in the Cartesian map
* `y_range_start`: Start value of the range of y values in the Cartesian map
* `y_range_end`: Final value of the range of y values in the Cartesian map
* `x_increment`: Amount by which the value x will be incremented at each point
* `point_color`: Color of the representation of a filled point on the map
* `back_color`: Color of the representation of an empty point on the map
* `render_type`: rendering type ('image', 'term')