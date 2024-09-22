import pygame

class GameObject: 
    def __init__(self, x, y, color=(255, 255, 255)):
        """Inicializa um objeto de jogo básico"""
        self.x = x
        self.y = y
        self.color = color

    def update(self):
        """Método que pode ser sobrescrito para movimentação ou lógica"""
        pass

    def draw(self, screen):
        """Método que desenha o objeto na tela"""
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, 50, 50))