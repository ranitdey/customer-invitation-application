from typing import List


class ExtractorError(Exception):
    def __init__(self, message):
        self.message = message


class Extractor:
    @staticmethod
    def extract_customer(customer_records):
        """
        Extracts customer object from Customer Record object.
        :param customer_records: List of Customer Record objects
        :return: List of Customer objects
        """
        if not isinstance(customer_records, List):
            raise ExtractorError("Customer extractor expects input to be a list")
        extracted_users = []
        for record in customer_records:
            extracted_users.append(record.customer)
        return extracted_users
