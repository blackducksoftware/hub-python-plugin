from bdsplugin.api.RestConnection import RestConnection


class LinkedDataDataService(object):

    rest_connection = None

    def __init__(self, rest_connection):
        self.rest_connection = rest_connection

    def upload_bdio(self, bdio):
        path = "api/bom-import"
        headers = self.rest_connection.headers_jsonld()
        proxies = self.rest_connection.get_proxies()
        response = self.rest_connection.make_post_request(
            path, bdio, headers=headers, proxies=proxies)
        response.raise_for_status()
        print("Black Duck I/O successfully deployed to the hub")
        return response