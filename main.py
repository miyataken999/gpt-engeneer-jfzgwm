from services.tea_service import TeaService
from utils.excel_utils import export_to_excel

def main():
    tea_repository = TeaRepository()
    tea_service = TeaService(tea_repository)

    # Add some sample tea varieties
    tea_service.add_tea("Earl Grey", "UK", "A flavorful black tea")
    tea_service.add_tea("Sencha", "Japan", "A popular green tea")
    tea_service.add_tea("Assam", "India", "A strong black tea")

    teas = tea_service.get_all_teas()
    export_to_excel(teas, "tea_varieties.xlsx")

if __name__ == "__main__":
    main()