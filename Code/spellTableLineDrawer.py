import pygame

class SpellTableLineDrawer:
    WIDTH = 1000

    def __init__(self):
        self.lines = []
        self.moves = []
        self.drawing = True
        self.start_x = (1000 - (64 * 2))
        self.start_y = (64 * 2)
        self.current_x = self.start_x
        self.current_y = self.start_y

    def draw(self, window):
        for line in self.lines:
            pygame.draw.line(window, (26, 26, 26), line[0], line[1], 5)

    def getMoves(self):
        return self.moves
    
    def clearMovesAndLines(self):
        self.lines.clear()
        self.moves.clear()


    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # x and y in center of spell table. Start pos
                self.current_x = self.start_x
                self.current_y = self.start_y

            if event.key == pygame.K_UP:
                if self.drawing: # 40 (* 2) px from one rune to another
                    new_x = self.current_x
                    new_y = self.current_y - (40 * 2)

                    if ((new_y >= self.start_y - (40 * 2)) and (new_y <= self.start_y + (40 * 2))):
                        self.lines.append(((self.current_x, self.current_y), (self.current_x, new_y))) # y is negative upwards
                        self.moves.append("UP")

                        self.current_x = new_x
                        self.current_y = new_y

                        print(self.moves)
                    else:
                        print("Outside table")

            if event.key == pygame.K_DOWN:
                if self.drawing:
                    new_x = self.current_x
                    new_y = self.current_y + (40 * 2)

                    if ((new_y >= self.start_y - (40 * 2)) and (new_y <= self.start_y + (40 * 2))):
                        self.lines.append(((self.current_x, self.current_y), (new_x, new_y)))
                        self.moves.append("DOWN")

                        self.current_x = new_x
                        self.current_y = new_y

                        print(self.moves)
                    else:
                        print("Outside table")

            if event.key == pygame.K_LEFT:
                if self.drawing: # 40 px from one rune to another
                    new_x = self.current_x - (40 * 2)
                    new_y = self.current_y

                    if ((new_x >= self.start_x - (40 * 2)) and (new_x <= self.start_x + (40 * 2))):
                        self.lines.append(((self.current_x, self.current_y), (new_x, new_y)))
                        self.moves.append("LEFT")

                        self.current_x = new_x
                        self.current_y = new_y

                        print(self.moves)
                    else:
                        print("Outside table")

            if event.key == pygame.K_RIGHT:
                if self.drawing:
                    new_x = self.current_x + (40 * 2)
                    new_y = self.current_y

                    if ((new_x >= self.start_x - (40 * 2)) and (new_x <= self.start_x + (40 * 2))):
                        self.lines.append(((self.current_x, self.current_y), (new_x, new_y)))
                        self.moves.append("RIGHT")

                        self.current_x = new_x
                        self.current_y = new_y

                        print(self.moves)
                    else:
                        print("Outside table")