from src.config import DUBLIN_OFFICE_LOCATION, INVITATION_RANGE_THRESHOLD_IN_KILOMETERS, FILE_OUTPUT_PATH, \
    CUSTOMER_RECORDS_FILE_PATH
from src.deserializers.customer_record_deserializer import CustomerRecordDeserializer
from src.filters.filter_by_distance import FilterByDistance
from src.io.file_reader import FileReader
from src.io.file_writer import FileWriter
from src.lib.sorting import Sorting
from src.serializers.customer_record_serializer import CustomerRecordSerializer


class App:
    def __init__(self):
        self.customer_record_deserializer = CustomerRecordDeserializer()
        self.filter_by_distance = FilterByDistance()
        self.customer_record_serializer = CustomerRecordSerializer()

    def execute(self, filepath: str):
        raw_data = FileReader.read_file(filepath)
        deserialized_data = self.customer_record_deserializer.deserialize(raw_data)
        filtered_data = self.filter_by_distance.filter(deserialized_data, DUBLIN_OFFICE_LOCATION,
                                                       INVITATION_RANGE_THRESHOLD_IN_KILOMETERS)
        filtered_by_user = []
        for item in filtered_data:
            filtered_by_user.append(item.customer)
        Sorting.sort_records(filtered_by_user)
        serialized_output_data = self.customer_record_serializer.serialize(filtered_by_user)
        FileWriter.write_to_file(serialized_output_data, FILE_OUTPUT_PATH)


if __name__ == '__main__':
    App().execute(CUSTOMER_RECORDS_FILE_PATH)
