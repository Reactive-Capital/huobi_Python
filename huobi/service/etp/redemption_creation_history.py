from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import *
from huobi.utils.json_parser import default_parse_data_as_long


class GetETPCreationRedemptionHistoryService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/etp/transactions"

        def parse(dict_data):
            return default_parse_data_as_long(dict_data, None)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, channel, self.params, parse)
