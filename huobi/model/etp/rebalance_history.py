from huobi.utils.json_parser import fill_obj
from huobi.model.etp.creation_quota import CreationQuota


class ETPRebalanceHistory:

    """
       Reference data of ETP

       :member
           symbol: ETP Code.
           rebalTime: Position rebalance time (unix time in millisecond).
           rebalType: Position rebalance type (valid values: daily, adhoc).
       """

    def __init__(self):
        self.symbol = ""
        self.rebalTime = ""
        self.rebalType = {}

    @staticmethod
    def json_parse(json_data):
        ref = fill_obj(json_data, ETPRebalanceHistory)
        creation_quota = fill_obj(ref.CreationQuota, CreationQuota)
        ref.creationQuota = creation_quota
        return ref

    @staticmethod
    def json_parse_list(dict_data):
        ret_list = list()
        for item in dict_data:
            item_obj = ETPRebalanceHistory.json_parse(item)
            if item_obj is not None:
                ret_list.append(item_obj)
        return ret_list

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.symbol, format_data + "Symbol")
        PrintBasic.print_basic(self.rebalTime, format_data + "Rebalance Time")
        PrintBasic.print_basic(self.rebalType, format_data + "Rebalance Type")
