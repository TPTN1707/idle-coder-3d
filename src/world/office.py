from ursina import *

class OfficeRoom:
    def __init__(self):
        # 1. Spawn Floor (Large gray plane)
        self.floor = Entity(
            model='plane',
            color=color.light_gray,
            scale=(20, 1, 20),
            position=(0, 0, 0)
        )

        # 2. Spawn Back Wall (Thick wall behind the desk)
        self.back_wall = Entity(
            model='cube',
            color=color.gray,
            scale=(20, 10, 1),
            position=(0, 5, 10)
        )

        # 3. Spawn Side Wall (Left wall of the room)
        self.left_wall = Entity(
            model='cube',
            color=color.gray,
            scale=(1, 10, 20),
            position=(-10, 5, 0)
        )

        # 4. Spawn Desk (Wooden table. Top surface is at Y = 1.5)
        self.desk = Entity(
            model='cube',
            color=color.brown,
            scale=(4, 1.5, 2),
            position=(0, 0.75, 5) # Center is raised to Y = 0.75, making top surface Y = 1.5
        )

        # 5. Spawn Level 1 CRT Monitor (Sits exactly on top of the desk)
        self.monitor = Entity(
            model='cube',
            color=color.black,
            scale=(1.2, 1.0, 1.0),
            position=(0, 2.0, 5.2) # Raised to Y = 2.0 (Desk top Y=1.5 + half monitor height Y=0.5)
        )

        # 6. Spawn Keyboard (Flat gray plate on the desk)
        self.keyboard = Entity(
            model='cube',
            color=color.light_gray,
            scale=(1.5, 0.1, 0.6),
            position=(0, 1.55, 4.5)
        )

        # 7. Spawn Level 1 Office Chair
        self.chair = Entity(
            model='cube',
            color=color.dark_gray,
            scale=(1.2, 1.0, 1.2),
            position=(0, 0.5, 3.2) # Placed behind the desk
        )