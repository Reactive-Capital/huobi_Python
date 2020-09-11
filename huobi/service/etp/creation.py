from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant import *
from huobi.utils.json_parser import default_parse_data_as_long
from huobi.model.etp.etp_creation import ETPCreation


class PostETPCreationService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/etp/creation"

        def parse(dict_data):
            return ETPCreation.json_parse(dict_data)

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.POST_SIGN, channel, self.params, parse)
