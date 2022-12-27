import requests
import json

class GetPages:
    def __init__(self, cookies=None, headers=None, guid=None, url=None) -> None:
        self.cookies = cookies
        self.headers = headers
        self.guid = guid
        self.url = url

    def __call__(self):
        resp = JsonReader(self.url, self.cookies, self.headers).read()
        urls = []
        pageNumber = 1
        currentPage = 1
        while 1:
            try:
                resp = JsonReader(
                    f"{self.url}?pageNumber={pageNumber}&currentPage={currentPage}",
                    self.cookies,
                    self.headers,
                ).read()
                if resp.json["result"]:
                    for x in resp.json["result"]:
                        urls.append(
                            f'https://api-plataforma.carguero.com.br/queries/ofertas/frotista/{x["id"]}/detalhe'
                        )
                else:
                    break
                pageNumber += 1
                currentPage += 1
            except Exception as ex:
                print(ex)
                break
        return urls

class JsonReader:
    def __init__(self, url, cookies, headers) -> None:
        self.url = url
        self.cookies = cookies
        self.headers = headers

    def read(self):
        try:
            r = requests.get(self.url, cookies=self.cookies, headers=self.headers)
            self.request = r
            try:
                json.loads(r)
                self.json = r.json()
            except ValueError as erro:
                return self
            return self
        except requests.exceptions.ConnectionError:
            pass