#!/usr/bin/python3.8

import optparse
import re
import requests
from prettytable import PrettyTable


CONFIG = {
        'auth': {
            'APIKEY': *******,
            'APIPASS': ******
        },
        'URL': 'https://exchange.xforce.ibmcloud.com/api/ipr/'
}


class Main(object):
    def __init__(self):
        self.option = Options()
        self.call = Call()
        self.start()

    def start(self):
        ip = self.option.opt_parser()
        res_json = self.call.call_service(ip, CONFIG)
        report = Report()
        res = report.generet_report(res_json)
        report.draw_report(res)


class Options(object):
    def opt_parser(self):
        parser = optparse.OptionParser()
        parser.add_option("-s", "--source",
                          dest="ip_source",
                          help="Add ip source for discover")

        return self.check_input(parser)

    def check_input(self, parser):

        options = parser.parse_args()[0]

        if not options.ip_source:
            mes = "[-] Please specify an interface, use -- help for more info."
            parser.error(mes)

        ip_candidates = re.findall(
            r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",
            options.ip_source
        )

        if not len(ip_candidates):
            mes = "[-] Please put source ip address."
            parser.error(mes)
        else:
            return ip_candidates[0]


class Call(object):
    def __init__(self):
        self.respons = {}

    def get_resp(self, **dicts):
        try:
            if dicts['auth'] is not None:
                user = dicts['auth']['APIKEY']
                passwd = dicts['auth']['APIPASS']

                res = requests.get(
                    f"{dicts['url']}{dicts['ip']}",
                    auth=(user, passwd))

                return res.json()
        except Exception:
            print("Ошибка при вызове сервиса")

    def call_service(self, IP, CONF):
        return self.get_resp(
            url=CONF['URL'],
            ip=IP,
            auth=CONF.get('auth'))


class Report(object):
    def __init__(self):
        self.table = PrettyTable()
        self.table.field_names = ["Parameter", "Value"]
        self.view = ["geo", "ip", "score", "country"]
        self.report = []

    def generet_report(self, data):
        for key in data:
            key_data = data[key]

            if key in self.view:
                if type(key_data) is str or type(key_data) is int:
                    self.report.append([key, key_data])

                if type(key_data) is dict:
                    for i in key_data:
                        if i in self.view:
                            self.report.append([i, key_data[i]])

        return self.report

    def draw_report(self, data):
        self.table.add_rows(data)
        print(self.table)


if __name__ == "__main__":
    main = Main()
