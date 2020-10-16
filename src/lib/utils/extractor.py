from typing import List
import logging


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
        logging.info("Extracting Customer objects from Customer Records")
        extracted_users = []
        for record in customer_records:
            extracted_users.append(record.customer)
        logging.info("Extraction process completed")
        return extracted_users
