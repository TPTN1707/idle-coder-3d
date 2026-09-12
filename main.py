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

# 2. Configure Beautiful Isometric Orthographic Camera
camera.orthographic = True
camera.fov = 6.0 # Zoom level (lower value is closer)
camera.position = (6, 5, -6)
camera.rotation = (28, -45, 0)

# 3. Add Directional Light (Sun) to create beautiful 3D shading/shadows
sun = DirectionalLight()
sun.look_at(Vec3(-1, -1.5, 1))

# 4. Create a clean HUD on screen to show currency
hud_text = Text(
    text=f"Money: ${state.money:.2f}  |  Passive: ${state.income_per_second:.1f}/s",
    position=(-0.85, 0.45), # Top-left corner of the screen
    scale=2.0,
    color=color.black
)

# Press Tab to toggle mouse lock
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