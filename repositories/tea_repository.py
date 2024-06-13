from models.tea import Tea

class TeaRepository:
    """Manages tea varieties in memory"""
    def __init__(self):
        self.teas = []

    def add_tea(self, tea: Tea):
        """Add a tea variety to the repository"""
        self.teas.append(tea)

    def get_all_teas(self):
        """Get all tea varieties in the repository"""
        return self.teas