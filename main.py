from engine.GameObject import GameObject
from engine.Engine import Engine

engine = Engine(
    base_bg_color=(255, 255, 255),
    fps=30,
    height=400,
    width=500,
    title="Engine"
)

while True: 
    engine.step()

