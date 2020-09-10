from huobi.utils.json_parser import fill_obj


class ETPCreation:

    """
       ETP Creation

       :member
           transactId: Transaction Id.
           transactTime: Transaction time (unix time in millisecond).
       """

    def __init__(self):
        self.transactId = 0
        self.transactTime = 0

    @staticmethod
    def json_parse(json_data):
        creation = fill_obj(json_data, ETPCreation)
        return creation

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.transactId, format_data + "Transaction Id")
        PrintBasic.print_basic(self.transactTime, format_data + "Transaction Time")