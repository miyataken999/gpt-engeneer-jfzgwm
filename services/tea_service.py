from repositories.tea_repository import TeaRepository

class TeaService:
    """Provides business logic for tea varieties"""
    def __init__(self, tea_repository: TeaRepository):
        self.tea_repository = tea_repository

    def add_tea(self, name: str, origin: str, description: str):
        """Add a new tea variety"""
        tea = Tea(len(self.tea_repository.teas) + 1, name, origin, description)
        self.tea_repository.add_tea(tea)

    def get_all_teas(self):
        """Get all tea varieties"""
        return self.tea_repository.get_all_teas()