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

        :param etp_symbol: The symbol, currently only support hb10. (mandatory)
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

    def post_etp_creation(self, etp_name: str, value: int, currency: str) -> None:
        """
        ETP Order creation.

        :param etp_name: The symbol, currently only support hb10. (mandatory)
        :param value: The amount to create, based on quote currency. (mandatory)
        :param currency: Quote currency of creation. (mandatory)
        :return: No return
        """
        check_symbol(etp_name)
        check_should_not_none(value, "amount")

        params = {
            "etpName": etp_name,
            "value": value,
            "currency": currency
        }

        from huobi.service.etp.creation import PostCreationETPService
        return PostCreationETPService(params).request(**self.__kwargs)

    def post_etp_redemption(self, etf_name: 'str', amount: 'int') -> None:
        """
        Order creation or redemption of ETF.

        :param etf_name: The symbol, currently only support hb10. (mandatory)
        :param amount: The amount to create or redemption. (mandatory)
        :return: No return
        """

        check_symbol(etf_name)
        check_should_not_none(amount, "amount")

        params = {
            "etf_name": etf_name,
            "amount": amount
        }

        from huobi.service.etf.post_etf_swap_out import PostEtfSwapOutService
        return PostEtfSwapOutService(params).request(**self.__kwargs)

