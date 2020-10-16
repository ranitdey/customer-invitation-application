from src.config import DUBLIN_OFFICE_LOCATION, INVITATION_RANGE_THRESHOLD_IN_KILOMETERS, FILE_OUTPUT_PATH, \
    CUSTOMER_RECORDS_FILE_PATH
from src.lib.deserializers.customer_record_deserializer import CustomerRecordDeserializer
from src.lib.filters.filter_by_distance import FilterByDistance
from src.lib.io.file_reader import FileReader
from src.lib.io.file_writer import FileWriter
from src.lib.utils.extractor import Extractor
from src.lib.utils.sorting import Sorting
from src.lib.serializers.customer_record_serializer import CustomerRecordSerializer


class App:
    def __init__(self):
        self.customer_record_deserializer = CustomerRecordDeserializer()
        self.filter_by_distance = FilterByDistance()
        self.customer_record_serializer = CustomerRecordSerializer()

    def execute(self, input_filepath: str, output_filepath: str):
        raw_data = FileReader.read_file(input_filepath)
        deserialized_data = self.customer_record_deserializer.deserialize(raw_data)
        filtered_data = self.filter_by_distance.filter(deserialized_data, DUBLIN_OFFICE_LOCATION,
                                                       INVITATION_RANGE_THRESHOLD_IN_KILOMETERS)
        filtered_by_user = Extractor.extract_customer(filtered_data)
        Sorting.sort_customers(filtered_by_user, ascending=True)
        serialized_output_data = self.customer_record_serializer.serialize(filtered_by_user)
        FileWriter.write_to_file(serialized_output_data, output_filepath)


if __name__ == '__main__':
    App().execute(CUSTOMER_RECORDS_FILE_PATH, FILE_OUTPUT_PATH)
