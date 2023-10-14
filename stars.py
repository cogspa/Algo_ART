import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_star(ax, x, y, n_points, size, rotation=0):
    """Generate a star shape on given ax."""
    star = patches.RegularPolygon((x, y), numVertices=n_points, radius=size, orientation=np.radians(rotation))
    ax.add_patch(star)

def main():
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect('equal')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')  # Turn off the axis
    
    for x in range(10):
        for y in range(10):
            n_points = np.random.choice([4, 5, 6, 8])  # number of star points
            size = 0.3  # for this example, size is constant, but it can be varied
            rotation = np.random.randint(0, 360)  # random rotation
            generate_star(ax, x, y, n_points, size, rotation)
    
    plt.show()

main()
