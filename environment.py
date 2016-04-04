import pygame
import graphics
import guiBase

class Environment():
    def __init__(self):
        self.surface = graphics.SCREEN
        self.surface.fill((255,0,0))
        self.gui_group = pygame.sprite.Group()
        self.blue_square = guiBase.VisualElement(40,40,80,80,(50,200,50))
        self.green_rect = guiBase.ClickableElement(40,120,120,40,(50,200,50))
        self.gui_group.add(self.blue_square, self.green_rect)

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.green_rect.on_click(self.green_rect.dim)

                print("mouse clicked")
            if event.type == pygame.QUIT:
                self.terminate()

    def update(self):
        pass
    def render(self):
        self.gui_group.draw(self.surface)
        self.green_rect.on_hover(self.green_rect.highlight)
        self.blue_square.render_text('Hello')
        self.blue_square.render_text('World', ((0,20)))
