from huobi.utils.json_parser import fill_obj

class CreationQuota:
    """
       Creation quota of ETP

       :member
        maxCreationValue: Maximum creation value per request.
        minCreationValue: Minimal creation value per request.
        dailyCreationValue: Maximum creation value per day.
        creationCurrency: Quote currency of creation.
       """
    def __init__(self):
        self.maxCreationValue = 0
        self.minCreationValue = 0
        self.dailyCreationValue = 0
        self.creationCurrency = ""

    @staticmethod
    def json_parse(json_data):
        ref = fill_obj(json_data, CreationQuota)
        ref.maxCreationValue = int(ref.maxCreationValue)
        ref.minCreationValue = int(ref.minCreationValue)
        ref.dailyCreationValue = int(ref.dailyCreationValue)
        return ref

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.maxCreationValue, format_data + "Max Creation Value")
        PrintBasic.print_basic(self.minCreationValue, format_data + "Min Creation Value")
        PrintBasic.print_basic(self.dailyCreationValue, format_data + "Daily Creation Value")
        PrintBasic.print_basic(self.creationCurrency, format_data + "Creation Currency")