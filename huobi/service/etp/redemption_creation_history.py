from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import *
from huobi.model.etp.etp_creation_redemption_history import ETPCreationRedemptionHistory


class GetETPCreationRedemptionHistoryService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/etp/transactions"

        def parse(dict_data):
            return ETPCreationRedemptionHistory.json_parse_list(dict_data)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)
