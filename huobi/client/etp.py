from huobi.constant import *
from huobi.model.etp import *
from huobi.utils import *


class EtpClient(object):

    def __init__(self, **kwargs):
        """
        Create the request client instance.
        :param kwargs: The option of request connection.
            api_key: The public key applied from Huobi.
            secret_key: The private key applied from Huobi.
            url: The URL name like "https://api.huobi.pro".
            init_log: to init logger
        """
        self.__kwargs = kwargs

    def get_etp_reference(self, etp_name: 'str') -> ETPReference:
        """
        Get the ETP reference

        :param etp_symbol: ETP code (for example: btc3l).(mandatory)
        :return: The etp reference data
        """
        check_symbol(etp_name)
        params = {
            "etp_name": etp_name
        }

        from huobi.service.etp.reference import GetEtpReference
        return GetEtpReference(params).request(**self.__kwargs)

    def get_etp_creation_redemption_history(self, etp_names: 'str'='', currencies: str='',
                                            transact_types: str='', transact_status: str='',
                                            start_time: int=0, end_time: int=0, sort: str='desc',
                                            limit: int=100) -> list:
        """
        Get ETP Creation and Redemption history of the account

        :param etp_names: ETP code（multiple inputs acceptable, separated by comma; default value: all ETP codes; for example: btc3l).
        :param currencies: Quote currency (only valid for transactTypes=creation; multiple inputs acceptable, separated by comma; default value: all available quote currencies under the ETP code).
        :param transact_types: Transaction type (multiple inputs acceptable, separated by comms; valid values: creation, redemption; default value: all transaction types).
        :param transact_status: Transaction status (multiple inputs acceptable, separated by comma; valid values: completed, processing, clearing, rejected; default value: all transaction status).
        :param start_time: Farthest time (unix time in millisecond; valid value:[(endTime – 10 days), endTime]; default value: (endTime – 10 days)).
        :param end_time: Nearest time (unix time in millisecond; valid value: [(current time – 180 days), current time]; default value: current time).
        :param sort: Sorting order (valid value: asc, desc; default value: desc).
        :param limit: Maximum number of items in one page (valid range:[1,500]; default value:100).
        :return: The list of historical ETP creations, redemptions
        """
        check_symbol(etp_names)
        params = {
            "etpNames": etp_names,
            "currencies": currencies,
            "transactTypes": transact_types,
            "transactStatus": transact_status,
            "startTime": start_time,
            "endTime": end_time,
            "sort": sort,
            "limit": limit,
        }

        from huobi.service.etp.redemption_creation_history import GetETPCreationRedemptionHistoryService
        return GetETPCreationRedemptionHistoryService(params).request(**self.__kwargs)

    def post_etp_creation(self, etp_name: str, value: int, currency: str) -> ETPCreation:
        """
        ETP Order creation.

        :param etp_name: ETP code (for example: btc3l). (mandatory)
        :param value: Creation value (based on quote currency). (mandatory)
        :param currency: Quote currency of creation. (mandatory)
        :return: ETP Creation with transaction Id and time
        """
        check_symbol(etp_name)
        check_should_not_none(value, "amount")

        params = {
            "etpName": etp_name,
            "value": value,
            "currency": currency
        }

        from huobi.service.etp.creation import PostETPCreationService
        return PostETPCreationService(params).request(**self.__kwargs)

    def post_etp_redemption(self, etp_name: str, currency: str, amount: float) -> ETPRedemption:
        """
        ETP Order redemption.

        :param etp_name: ETP code (for example: btc3l). (mandatory)
        :param currency: Currency of redemption. (mandatory)
        :param amount: Redemption amount. (mandatory)
        :return: ETP Redemption with transaction Id and time
        """

        check_symbol(etp_name)
        check_should_not_none(amount, "amount")

        params = {
            "etp_name": etp_name,
            "currency": currency,
            "amount": amount
        }

        from huobi.service.etp.redemption import PostETPRedemptionService
        return PostETPRedemptionService(params).request(**self.__kwargs)

