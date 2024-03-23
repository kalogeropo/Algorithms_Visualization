import pygame

from astar import algorithm, get_clicked_pos
from properties import colour_map



class Node:

    def __init__(self, row, col, width, total_row):
        self.nbr = []
        self.status = colour_map['G']
        self.row = row
        self.col = col
        self.width = width
        self.total_row = total_row
        self.coord_x = row * width
        self.coord_y = col * width

    def get_position(self):
        return self.row, self.col

    # --------STATES----------------------
    def is_closed(self):
        return self.status == colour_map['C']

    def is_opened(self):
        return self.status == colour_map['O']

    def is_wall(self):
        return self.status == colour_map['BLACK']

    def is_start(self):
        return self.status == colour_map['S']

    def is_end(self):
        return self.status == colour_map['E']

    # ---------- Change States
    def set_status(self, new_status):
        self.status = new_status

    def draw(self, pygame_window):
        pygame.draw.rect(pygame_window, self.status, (self.coord_x, self.coord_y, self.width, self.width))

    def update_nbr(self, grid):  # check up down right left for walls
        if self.row < self.total_row - 1 and not grid[self.row + 1][self.col].is_wall():  # down
            self.nbr.append(grid[self.row + 1][self.col])
        if self.row > 0 and not grid[self.row - 1][self.col].is_wall():  # up
            self.nbr.append(grid[self.row - 1][self.col])
        if self.col < self.total_row - 1 and not grid[self.row][self.col + 1].is_wall():  # right
            self.nbr.append(grid[self.row][self.col + 1])
        if self.col > 0 and not grid[self.row][self.col - 1].is_wall():  # left
            self.nbr.append(grid[self.row][self.col - 1])


class Grid:

    def __init__(self, width, rows):
        self.grid = []
        gap = width // rows
        for i in range(rows):
            self.grid.append([])
            for j in range(rows):
                node = Node(i, j, gap, rows)
                self.grid[i].append(node)

    def draw_grid(self, pygame_window, width, rows):
        gap = width // rows
        for i in range(rows):
            pygame.draw.line(pygame_window, colour_map["E"], (0, i * gap), (width, i * gap))
            for j in range(rows):
                pygame.draw.line(pygame_window, colour_map["E"], (j * gap, 0), (j * gap, width))

    def draw(self, pygame_window, width, rows):
        pygame_window.fill(colour_map["G"])

        for row in self.grid:
            for node in row:
                node.draw(pygame_window)
        self.draw_grid(pygame_window, width, rows)
        pygame.display.update()


def main(win, width, rows):
    g = Grid(width, rows)
    start = None
    end = None
    running = True
    started = False
    while running:
        g.draw(win, width, rows)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if started:
                continue
            if pygame.mouse.get_pressed()[0]:  # pressed left mouse button
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, width)
                current_node = g.grid[row][col]
                if not start and current_node != end:
                    start = current_node
                    start.set_status(colour_map["S"])
                    print(f"Started at {start}")
                elif not end and current_node != start:
                    end = current_node
                    end.set_status(colour_map["E"])
                elif current_node != end and current_node != start:
                    current_node.set_status(colour_map["BLACK"])
            elif pygame.mouse.get_pressed()[2]:  # pressed right mouse button
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, width)
                current_node = g.grid[row][col]
                if current_node == start:
                    start = None
                elif current_node == end:
                    end = None
                current_node.set_status(colour_map["G"])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in g.grid:
                        for node in row:
                            node.update_nbr(g.grid)

                    algorithm(lambda: g.draw(win, rows, width), g.grid, start, end)
