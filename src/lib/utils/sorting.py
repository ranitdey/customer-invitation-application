class Sorting:
    @staticmethod
    def sort_customers(records, ascending: bool):
        records.sort(key=lambda x: x.user_id, reverse=not ascending)


