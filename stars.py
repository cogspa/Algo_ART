import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_star(ax, x, y, n_points, size, rotation=0, color='white'):
    """Generate a star shape on given ax."""
    star = patches.RegularPolygon((x, y), numVertices=n_points, radius=size, orientation=np.radians(rotation), facecolor=color)
    ax.add_patch(star)

def generate_rounded_square(ax, x, y, size, corner_radius, color='black'):
    """Generate a rounded square."""
    square = patches.FancyBboxPatch((x-size/2, y-size/2), size, size, boxstyle="round,pad=0.03,rounding_size="+str(corner_radius), facecolor=color)
    ax.add_patch(square)

def main():
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect('equal')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')  # Turn off the axis
    ax.set_facecolor('white')
    
    grid_size = 10
    square_size = 0.9
    corner_radius = 0.15

    for x in np.linspace(0.5, 9.5, grid_size):
        for y in np.linspace(0.5, 9.5, grid_size):
            generate_rounded_square(ax, x, y, square_size, corner_radius)
            
            n_points = np.random.choice([4, 5, 6, 8])  # number of star points
            star_size = 0.3  # size can be adjusted
            rotation = np.random.randint(0, 360)  # random rotation
            generate_star(ax, x, y, n_points, star_size, rotation)
    
    plt.show()

main()
