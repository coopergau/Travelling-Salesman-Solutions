import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def plot_path(nodes, path, map_length):
    ''' Plot the nodes and show the path get drawn in real time. '''
    x_values, y_values = zip(*nodes)
    
    # Create the figure and axis
    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values)

    # Create an empty line object that will be updated during the animation
    line, = ax.plot([], [], 'g-', lw=2)

    ax.set_xlim(0, map_length)
    ax.set_ylim(0, map_length)

    # Line initialization function
    def init():
        line.set_data([], [])
        return (line,)  

    # Update function to draw each new line
    def update(frame):
        # Get the x and y coordinates for the path up to the current frame
        path_x = [x_values[i] for i in path[:frame+1]]
        path_y = [y_values[i] for i in path[:frame+1]]
        
        # Update the line with the new path data
        line.set_data(path_x, path_y)
        return (line,)

    # Animate the path
    ani = FuncAnimation(fig, update, frames=len(path), init_func=init, blit=True, interval=200)

    plt.show()