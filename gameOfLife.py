import numpy as np
import time
import pygame as pg 

color_background = (10, 64, 128)    
color_grid = (40, 40, 40)   
color_alive = (255, 255, 255)

def update(screen, cells, size):
    """
    Met à jour l'état des cellules et dessine les nouvelles cellules.

    Args:
        screen: Surface de pygame pour afficher le jeu.
        cells: Grille numpy représentant les cellules.
        size: Taille des cellules en pixels.

    Returns:
        Grille numpy mise à jour.
    """
    updated_cells=np.zeros((cells.shape[0], cells.shape[1])) 
    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color= color_background if cells[row, col]==0 else color_alive

        if cells[row, col] == 1 and (alive == 2 or alive == 3):
            updated_cells[row, col] = 1
        elif alive==3:
            updated_cells[row, col] = 1
        pg.draw.rect(screen, color, (col*size, row*size, size-1, size-1))   
    return updated_cells

def main():
    pg.init()

    width, height = 800, 800    
    size = 10

    screen = pg.display.set_mode((width, height))
    pg.display.set_caption('Game of Life')

    screen.fill(color_background)
    cells = np.zeros((width//size, height//size))
    screen.fill(color_background)
    update(screen, cells, size)

    pg.display.flip()
    running = False

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    running = not running
                    update(screen, cells, size)
                    pg.display.update()

            if pg.mouse.get_pressed()[0]:
                pos = pg.mouse.get_pos()
                cells[pos[1] // size, pos[0] // size] = 1
                update(screen, cells, size)
                pg.display.update()

        screen.fill(color_background)

        if running:
            cells = update(screen, cells, size)
            pg.display.update()

        time.sleep(0.01)

if __name__ == '__main__':
    main()











