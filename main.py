from app.services.calculator_service import CalculatorService
from app.utils.logger import get_logger
from app.config.settings import APP_NAME, VERSION

logger = get_logger(__name__)

def main():
    logger.info(f"Starting {APP_NAME} v{VERSION}")

    service = CalculatorService()

    operations = [
        ("add", 10, 5),
        ("subtract", 10, 5),
        ("multiply", 10, 5),
        ("divide", 10, 5)
    ]

    for op, a, b in operations:
        try:
            result = service.calculate(op, a, b)
            logger.info(f"{op.upper()} Result: {result}")
        except Exception as e:
            logger.error(e)

if __name__ == "__main__":
    main()
