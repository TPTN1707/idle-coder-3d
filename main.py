from ursina import *
from src.core.state import GameState
from src.world.office import OfficeRoom

app = Ursina(
    title="3D Idle IT Coder",
    borderless=False
)

# 1. Initialize our game State and 3D Office Room
state = GameState()
office = OfficeRoom()

# 2. Configure Static Isometric Studio Camera for Idle Game view
# We position the camera diagonally and tilt it downwards
camera.position = (8, 8, -6)
camera.rotation = (32, -50, 0) # Pitch (X), Yaw (Y), Roll (Z)

# 3. Create a clean HUD on screen to show currency
hud_text = Text(
    text=f"Money: ${state.money:.2f}  |  Passive: ${state.income_per_second:.1f}/s",
    position=(-0.85, 0.45), # Top-left corner of the screen
    scale=2.0,
    color=color.black
)

def input(key):
    if key == 'escape':
        application.quit()
    elif key == 'tab':
        mouse.locked = not mouse.locked

def update():
    """This core game loop runs every frame"""
    state.update_passive_income(time.dt)
    
    hud_text.text = f"Money: ${state.money:.2f}  |  Passive: ${state.income_per_second:.1f}/s"

app.run()