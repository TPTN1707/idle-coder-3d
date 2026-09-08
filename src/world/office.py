from ursina import *

class OfficeRoom:
    def __init__(self):
        # 1. Floor (Soft light warm gray pastel)
        self.floor = Entity(
            model='plane',
            color=color.rgb(230, 230, 225),
            scale=(20, 1, 20),
            position=(0, 0, 0)
        )

        # 2. Back Wall (Soft warm gray)
        self.back_wall = Entity(
            model='cube',
            color=color.rgb(215, 215, 210),
            scale=(20, 10, 0.5),
            position=(0, 5, 10)
        )

        # 3. Left Wall (Soft warm gray)
        self.left_wall = Entity(
            model='cube',
            color=color.rgb(215, 215, 210),
            scale=(0.5, 10, 20),
            position=(-10, 5, 0)
        )

        # 4. Desk (Pastel light wood color. Top surface is at Y = 1.2)
        self.desk = Entity(
            model='cube',
            color=color.rgb(190, 145, 120),
            scale=(4.0, 1.2, 2.0),
            position=(0, 0.6, 5) # Perfectly sits on the floor
        )

        # 5. Monitor Body (Dark slate gray CRT body)
        self.monitor_body = Entity(
            model='cube',
            color=color.rgb(60, 65, 70),
            scale=(1.4, 1.0, 1.0),
            position=(0, 1.7, 5.3) # Placed on the desk
        )
        
        # 6. Monitor Screen (Glowing retro green screen on the front of the monitor body)
        self.monitor_screen = Entity(
            model='cube',
            color=color.rgb(50, 200, 100), # Retro green glow
            scale=(1.2, 0.8, 0.05),
            position=(0, 1.7, 4.79) # Offset slightly forward
        )

        # 7. Keyboard (Sleek light gray)
        self.keyboard = Entity(
            model='cube',
            color=color.rgb(210, 210, 210),
            scale=(1.6, 0.08, 0.6),
            position=(0, 1.24, 4.4)
        )

        # 8. Office Chair (Constructed from distinct parts: base, seat, backrest)
        self.chair_base = Entity(
            model='cube',
            color=color.rgb(45, 45, 45),
            scale=(0.2, 0.6, 0.2),
            position=(0, 0.3, 3.2)
        )
        self.chair_seat = Entity(
            model='cube',
            color=color.rgb(65, 105, 120), # Teal blue cushion
            scale=(1.2, 0.15, 1.2),
            position=(0, 0.6, 3.2)
        )
        self.chair_back = Entity(
            model='cube',
            color=color.rgb(65, 105, 120),
            scale=(1.2, 1.0, 0.15),
            position=(0, 1.15, 2.65)
        )