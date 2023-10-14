import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_irregular_star(ax, x, y, size, n_points, rotation=0, color='white'):
    """Generate an irregular star shape on given ax."""
    outer_r = size
    inner_r = size * np.random.uniform(0.3, 0.5)  # Random inner radius

    angles = np.linspace(0, 2*np.pi, n_points, endpoint=False)
    coords = []

    for i, angle in enumerate(angles):
        if i % 2 == 0:
            r = outer_r
        else:
            r = inner_r
        coords.append((x + r * np.cos(angle + rotation), y + r * np.sin(angle + rotation)))

    polygon = patches.Polygon(coords, closed=True, facecolor=color)
    ax.add_patch(polygon)

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

            n_points = np.random.choice([8, 10, 12])  # Choose even numbers for symmetric stars
            star_size = 0.3  # size can be adjusted
            rotation = np.random.uniform(0, np.pi/n_points)  # Random rotation
            generate_irregular_star(ax, x, y, star_size, n_points, rotation)

    plt.show()

main()
