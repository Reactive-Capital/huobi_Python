from huobi.utils.json_parser import fill_obj


class ETPCreationRedemptionHistory:

    """
       ETP Creation & Redemption history

       :member
           etpName: ETP Code.
           transactId: Transaction ID.
           transactTime: Transaction time (unix time in millisecond).
           transactType: Transaction type (valid value: creation, redemption).
           transactAmount: Actual transaction amount (in base currency).
           transactAmountOrig: Original transaction amount(in base currency; only valid for transactType=redemption)
           transactValue: Actual transaction value (in quote currency).
           transactValueOrig: Original transaction value(in quote currency; only valid for transactType=creation).
           transactPrice: Transaction price (in quote currency).
           currency: Quote currency.
           transactFee: Transaction fee.
           feeCurrency: Transaction fee currency.
           transactStatus: Transaction status (valid values: completed, processing, clearing, rejected).
           redemptionFeeRate: Redemption fee rate.
           etpStatus: ETP status（normal, creation-only, redemption-only, halted.
       """

    def __init__(self):
        self.etpName = ""
        self.transactId = 0
        self.transactTime = 0
        self.transactType = ""
        self.transactAmount = 0.0
        self.transactAmountOrig = 0.0
        self.transactValue = 0.0
        self.transactValueOrig = 0.0
        self.transactPrice = 0.0
        self.currency = ""
        self.transactFee = 0.0
        self.feeCurrency = ""
        self.transactStatus = ""

    @staticmethod
    def json_parse(json_data):
        history = fill_obj(json_data, ETPCreationRedemptionHistory)
        return history

    @staticmethod
    def json_parse_list(dict_data):
        ret_list = list()
        for item in dict_data:
            item_obj = ETPCreationRedemptionHistory.json_parse(item)
            if item_obj is not None:
                ret_list.append(item_obj)
        return ret_list

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.etpName, format_data + "ETP Name")
        PrintBasic.print_basic(self.transactId, format_data + "Transaction Id")
        PrintBasic.print_basic(self.transactTime, format_data + "Transaction Time")
        PrintBasic.print_basic(self.transactType, format_data + "Transaction Type")
        PrintBasic.print_basic(self.transactAmount, format_data + "Transaction Amount")
        PrintBasic.print_basic(self.transactAmountOrig, format_data + "Transaction Original Amount")
        PrintBasic.print_basic(self.transactValue, format_data + "Transaction Value")
        PrintBasic.print_basic(self.transactValueOrig, format_data + "Transaction Original Value")
        PrintBasic.print_basic(self.transactPrice, format_data + "Transaction Price")
        PrintBasic.print_basic(self.currency, format_data + "Currency")
        PrintBasic.print_basic(self.transactFee, format_data + "Transaction Fee")
        PrintBasic.print_basic(self.feeCurrency, format_data + "Fee Currency")
        PrintBasic.print_basic(self.transactStatus, format_data + "Transaction Status")


