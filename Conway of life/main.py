import time
import pygame
import numpy as np

# Configurable constants
CELL_SIZE = 10  # Size of each cell in pixels
GRID_ROWS = 60  
GRID_COLS = 80  
FPS = 10  # Frames per second for smooth animations

# Colors
COLOR_BG = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
COLOR_DIE_NEXT = (170, 170, 170)
COLOR_ALIVE_NEXT = (255, 255, 255)
COLOR_TEXT = (255, 255, 255)  # White text color


def update_grid(screen, cells, cell_size, with_progress=False):
    """
    Updates the grid based on Conway's Game of Life rules.
    """
    next_gen_cells = np.zeros_like(cells)  # Initialize the next generation grid
    for row, col in np.ndindex(cells.shape):
        # Count alive neighbors
        alive_neighbors = np.sum(cells[row - 1:row + 2, col - 1:col + 2]) - cells[row, col]
        color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT

        # Apply the rules of the game
        if cells[row, col] == 1:  # Current cell is alive
            if alive_neighbors < 2 or alive_neighbors > 3:  # Dies due to under/overpopulation
                if with_progress:
                    color = COLOR_DIE_NEXT
            else:  # Survives
                next_gen_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        else:  # Current cell is dead
            if alive_neighbors == 3:  # Becomes alive
                next_gen_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT

        # Draw the cell
        pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size - 1, cell_size - 1))

    return next_gen_cells


def draw_generation_count(screen, generation):
    """
    Draws the generation count on the screen.
    """
    font = pygame.font.Font(None, 36)  # Default font, size 36
    text = f"Generation: {generation}"
    text_surface = font.render(text, True, COLOR_TEXT)
    screen.blit(text_surface, (10, 10))  # Position the text at the top-left corner


def main():
    """
    Main function to initialize the game and handle user interaction.
    """
    # Initialize pygame and create the screen
    pygame.init()
    screen = pygame.display.set_mode((GRID_COLS * CELL_SIZE, GRID_ROWS * CELL_SIZE))
    pygame.display.set_caption("Conway's Game of Life")
    clock = pygame.time.Clock()

    # Initialize grid with all cells dead
    cells = np.zeros((GRID_ROWS, GRID_COLS))
    generation = 0  # Track the number of generations
    running = False  # Start in paused state

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Toggle simulation state
                    running = not running
            elif pygame.mouse.get_pressed()[0]:  # Left-click to toggle cells
                pos = pygame.mouse.get_pos()
                cells[pos[1] // CELL_SIZE, pos[0] // CELL_SIZE] = 1

        # Clear the screen
        screen.fill(COLOR_GRID)
        # Update the grid if running, else just display current state
        if running:
            cells = update_grid(screen, cells, CELL_SIZE, with_progress=True)
            generation += 1  # Increment generation count when running
        else:
            update_grid(screen, cells, CELL_SIZE)

        # Draw the generation count
        draw_generation_count(screen, generation)

        # Refresh the display
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()

