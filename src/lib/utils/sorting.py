class Sorting:
    @staticmethod
    def sort_customers(records, ascending: bool):
        """
        Sorts the given List based on user_id attribute of Customer object.
        :param records: List of Customer objects
        :param ascending: Will the sorting happen on ascending order or descending order
        :return:
        """
        records.sort(key=lambda x: x.user_id, reverse=not ascending)


