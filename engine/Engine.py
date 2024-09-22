import pygame
import sys

class Engine:     
    def __init__(self, width=640, height=480, title="Minha Engine Gráfica", fps=60, base_bg_color=(0, 0, 0)):
        # Inicializa o pygame
        pygame.init()

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        self.fps = fps
        self.clock = pygame.time.Clock()

        self.background_color = base_bg_color 

        self.running = True

        self.game_objects = []

    def add_object(self, game_object):
        """Adiciona um objeto para ser renderizado"""
        self.game_objects.append(game_object)

    def handle_events(self):
        """Lida com os eventos como o fechamento da janela"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        """Atualiza a lógica do jogo ou engine"""
        for obj in self.game_objects:
            obj.update()

    def draw(self):
        """Desenha todos os objetos na tela"""
        self.screen.fill(self.background_color)
        for obj in self.game_objects:
            obj.draw(self.screen)
        pygame.display.flip()

    def step(self):
        """Método principal para iniciar o loop do jogo"""
        self.handle_events()  
        self.update()        
        self.draw()     

        if not self.running:
            pygame.quit()
            sys.exit()
        