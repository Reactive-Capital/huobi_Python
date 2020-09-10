from huobi.utils.json_parser import fill_obj
from huobi.model.etp.creation_quota import CreationQuota


class ETPReferance:

    """
       Reference data of ETP

       :member
           etpName: ETP Code.
           displayName: ETP display name.
           creationQuota:
                maxCreationValue: Maximum creation value per request.
                minCreationValue: Minimal creation value per request.
                dailyCreationValue: Maximum creation value per day.
                creationCurrency: Quote currency of creation.
           maxRedemptionAmount: Maximum redemption amount per request.
           minRedemptionAmount: Minimal redemption amount per request.
           dailyRedemptionAmount: Maximum redemption amount per day.
           creationFeeRate: Creation fee rate.
           redemptionFeeRate: Redemption fee rate.
           etpStatus: ETP status（normal, creation-only, redemption-only, halted.
       """

    def __init__(self):
        self.etpName = ""
        self.displayName = ""
        self.creationQuota = {}
        self.maxCreationValue = 0
        self.minCreationValue = 0
        self.dailyCreationValue = 0
        self.creationCurrency = ""
        self.maxRedemptionAmount = 0
        self.minRedemptionAmount = 0
        self.dailyRedemptionAmount = 0
        self.creationFeeRate = 0.0
        self.redemptionFeeRate = 0.0
        self.etpStatus = ""

    @staticmethod
    def json_parse(json_data):
        ref = fill_obj(json_data, ETPReferance)
        creation_quota = fill_obj(ref.CreationQuota, CreationQuota)
        ref.creationQuota = creation_quota
        return ref

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.etpName, format_data + "ETP Name")
        PrintBasic.print_basic(self.displayName, format_data + "Display Name")
        PrintBasic.print_basic(self.creationQuota, format_data + "Creation Quota")
        PrintBasic.print_basic(self.maxCreationValue, format_data + "Max Creation Value")
        PrintBasic.print_basic(self.minCreationValue, format_data + "Min Creation Value")
        PrintBasic.print_basic(self.dailyCreationValue, format_data + "Daily Creation Value")
        PrintBasic.print_basic(self.creationCurrency, format_data + "Creation Currency")
        PrintBasic.print_basic(self.maxRedemptionAmount, format_data + "Max Redemption Amount")
        PrintBasic.print_basic(self.minRedemptionAmount, format_data + "Min Redemption Amount")
        PrintBasic.print_basic(self.creationFeeRate, format_data + "Creation Fee Rate")
        PrintBasic.print_basic(self.redemptionFeeRate, format_data + "Redemption Fee Rate")
