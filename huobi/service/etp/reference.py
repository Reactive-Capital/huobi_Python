from huobi.connection.restapi_sync_client import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.etp.etp_referance import ETPReference


class GetEtpReference:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        channel = "/v2/etp/reference"

        def parse(dict_data):
            data_info = dict_data.get("data", {})
            etp_ref = ETPReference.json_parse(data_info)
            etp_ref.maxRedemptionAmount = int(etp_ref.maxRedemptionAmount)
            etp_ref.minRedemptionAmount = int(etp_ref.minRedemptionAmount)
            etp_ref.dailyRedemptionAmount = int(etp_ref.dailyRedemptionAmount)
            etp_ref.creationFeeRate = float(etp_ref.creationFeeRate)
            etp_ref.redemptionFeeRate = float(etp_ref.redemptionFeeRate)
            return etp_ref

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET, channel, self.params, parse)
