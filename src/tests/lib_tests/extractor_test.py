import pytest

from src.lib.utils.extractor import ExtractorError, Extractor
from src.models.customer import Customer
from src.models.customer_record import CustomerRecord
from src.models.location import Location


class TestExtractor:

    @staticmethod
    def test_extractor_with_invalid_data():
        with pytest.raises(ExtractorError) as exception_info:
            Extractor.extract_customer(None)
        assert exception_info.value.message == "Customer extractor expects input to be a list"

    @staticmethod
    def test_extractor_happy_scenario():
        data = [CustomerRecord(Customer(user_id=1, name="Alice Cahill"), Location(latitude=51.92893, longitude=-10.27699))]
        result = Extractor.extract_customer(data)
        assert len(result) == 1
        assert isinstance(result[0], Customer)
        assert result[0].user_id == 1
        assert result[0].name == "Alice Cahill"