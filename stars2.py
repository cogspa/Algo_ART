import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

# Global lists to keep track of stars and their properties
stars = []
rotations = []
pulsation_speeds = []
rotation_directions = []

def generate_irregular_star(ax, x, y, size, n_points):
    """Generate an irregular star shape on given ax."""
    outer_r = size
    inner_r = size * np.random.uniform(0.3, 0.5)
    
    angles = np.linspace(0, 2*np.pi, n_points, endpoint=False)
    coords = []

    for angle in angles:
        r = np.random.choice([outer_r, inner_r])
        coords.append((x + r * np.cos(angle), y + r * np.sin(angle)))

    star = patches.Polygon(coords, closed=True, facecolor='white')
    ax.add_patch(star)
    
    # Store star and its properties
    stars.append(star)
    rotations.append(np.random.uniform(0, np.pi/n_points))  # Random initial rotation
    pulsation_speeds.append(np.random.uniform(0.005, 0.015))
    rotation_directions.append(np.random.choice([-1, 1]))  # Clockwise or Counter-Clockwise

    return star

def update(num):
    """Update function for animation."""
    for i, star in enumerate(stars):
        x, y = star.xy.mean(axis=0)  # Star's center
        
        # Pulsate the star
        scale_factor = 1 + np.sin(pulsation_speeds[i] * num) * 0.05
        star.set_xy(scale_factor * (star.xy - [x, y]) + [x, y])
        
        # Rotate the star
        rotations[i] += rotation_directions[i] * 0.01  # Adjust the value for speed
        coords = np.dot(star.xy - [x, y], [[np.cos(rotations[i]), -np.sin(rotations[i])], [np.sin(rotations[i]), np.cos(rotations[i])]]) + [x, y]
        star.set_xy(coords)
    
    return stars

def main():
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect('equal')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_facecolor('white')
    
    grid_size = 10
    square_size = 0.9
    corner_radius = 0.15

    for x in np.linspace(0.5, 9.5, grid_size):
        for y in np.linspace(0.5, 9.5, grid_size):
            square = patches.FancyBboxPatch((x-square_size/2, y-square_size/2), square_size, square_size, boxstyle="round,pad=0.03,rounding_size="+str(corner_radius), facecolor='black')
            ax.add_patch(square)
            
            n_points = np.random.choice([8, 10, 12])
            star_size = 0.3
            generate_irregular_star(ax, x, y, star_size, n_points)
            
    ani = FuncAnimation(fig, update, frames=200, blit=True, repeat=True)
    plt.show()

main()
