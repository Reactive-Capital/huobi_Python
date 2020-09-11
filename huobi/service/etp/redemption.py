from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import *
from huobi.model.etp.etp_redemption import ETPRedemption


class PostETPRedemptionService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/etp/redemption"

        def parse(dict_data):
            return ETPRedemption.json_parse(dict_data)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)
