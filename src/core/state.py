class GameState:
    def __init__(self):
        # Core game currency
        self.money = 0.0

        # Upgrade levels (Monitor affects passive, Chair affects active, Coffee affects both)
        self.monitor_level = 1
        self.chair_level = 1
        self.coffee_level = 0

        # Base prices for upgrades
        self.base_monitor_cost = 10.0
        self.base_chair_cost = 15.0
        self.base_coffee_cost = 50.0

    # --- Active and Passive Rates Calculation ---
    @property
    def income_per_click(self):
        """Calculate active income per click based on Chair level"""
        # Base is $1. Each upgrade adds +$1 to click power
        return 1.0 + (self.chair_level - 1) * 1.0

    @property
    def income_per_second(self):
        """Calculate passive income per second (CPS) based on Monitor and Coffee levels"""
        # Base is $0. Each monitor adds +$0.5/sec. Each coffee adds +$3.0/sec.
        monitor_income = (self.monitor_level - 1) * 0.5
        coffee_income = self.coffee_level * 3.0
        return monitor_income + coffee_income

    # --- Upgrade Cost Calculation (Exponential Scaling) ---
    @property
    def monitor_upgrade_cost(self):
        """Monitor cost scales exponentially by a factor of 1.5 per level"""
        return round(self.base_monitor_cost * (1.5 ** (self.monitor_level - 1)), 2)

    @property
    def chair_upgrade_cost(self):
        """Chair cost scales exponentially by a factor of 1.6 per level"""
        return round(self.base_chair_cost * (1.6 ** (self.chair_level - 1)), 2)

    @property
    def coffee_upgrade_cost(self):
        """Coffee cost scales exponentially by a factor of 1.8 per level"""
        return round(self.base_coffee_cost * (1.8 ** self.coffee_level), 2)

    # --- Core Game Loop Updates ---
    def register_click(self):
        """Add active income to total money when the player clicks"""
        self.money += self.income_per_click

    def update_passive_income(self, dt):
        """Add passive income generated over elapsed time (delta time)"""
        self.money += self.income_per_second * dt

    # --- Purchase Upgrade Operations ---
    def upgrade_monitor(self):
        """Upgrade monitor to increase passive income if the player can afford it"""
        cost = self.monitor_upgrade_cost
        if self.money >= cost:
            self.money -= cost
            self.monitor_level += 1
            return True
        return False

    def upgrade_chair(self):
        """Upgrade chair to increase active click income if the player can afford it"""
        cost = self.chair_upgrade_cost
        if self.money >= cost:
            self.money -= cost
            self.chair_level += 1
            return True
        return False

    def upgrade_coffee(self):
        """Upgrade coffee to increase passive income if the player can afford it"""
        cost = self.coffee_upgrade_cost
        if self.money >= cost:
            self.money -= cost
            self.coffee_level += 1
            return True
        return False