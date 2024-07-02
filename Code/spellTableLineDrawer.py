import pygame

class SpellTableLineDrawer:
    WIDTH = 1000

    def __init__(self):
        self.lines = []
        self.moves = []
        self.drawing = True
        self.current_x = (1000 - (64 * 2))
        self.current_y = (64 * 2)

    def draw(self, window):
        for line in self.lines:
            pygame.draw.line(window, (255, 0, 0), line[0], line[1], 5)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # x and y in center of spell table
                self.current_x = (1000 - (64 * 2))
                self.current_y = (64 * 2)

                self.lines.clear()
                print("Clear moves")

            if event.key == pygame.K_UP:
                if self.drawing: # 40 px from one rune to another
                    new_x = self.current_x
                    new_y = self.current_y - (40 * 2)

                    self.lines.append(((self.current_x, self.current_y), (self.current_x, new_y))) # y is negative upwards
                    self.moves.append("UP")

                    self.current_x = new_x
                    self.current_y = new_y

                    print(self.moves)

            if event.key == pygame.K_DOWN:
                if self.drawing:
                    new_x = self.current_x
                    new_y = self.current_y + (40 * 2)

                    self.lines.append(((self.current_x, self.current_y), (new_x, new_y)))
                    self.moves.append("DOWN")

                    self.current_x = new_x
                    self.current_y = new_y

                    print(self.moves)

            if event.key == pygame.K_LEFT:
                if self.drawing: # 40 px from one rune to another
                    new_x = self.current_x - (40 * 2)
                    new_y = self.current_y

                    self.lines.append(((self.current_x, self.current_y), (new_x, new_y)))
                    self.moves.append("LEFT")

                    self.current_x = new_x
                    self.current_y = new_y

                    print(self.moves)

            if event.key == pygame.K_RIGHT:
                if self.drawing:
                    new_x = self.current_x + (40 * 2)
                    new_y = self.current_y

                    self.lines.append(((self.current_x, self.current_y), (new_x, new_y)))
                    self.moves.append("RIGHT")

                    self.current_x = new_x
                    self.current_y = new_y

                    print(self.moves)