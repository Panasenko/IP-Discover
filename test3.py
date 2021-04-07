#!/usr/bin/python3

import json

from prettytable import PrettyTable
x = PrettyTable()

data = """
{
    "ipr": {
        "ip": "92.222.129.112",
        "history": [
            {
                "created": "2012-03-22T07:26:00.000Z",
                "reason": "Regional Internet Registry",
                "geo": {
                    "country": "Germany",
                    "countrycode": "DE"
                },
                "ip": "92.192.0.0/11",
                "categoryDescriptions": {},
                "reasonDescription": "One of the five RIRs announced a (new) location mapping of the IP.",
                "score": 1,
                "cats": {}
            },
            {
                "created": "2012-04-13T13:34:00.000Z",
                "reason": "DNS heuristics",
                "cats": {
                    "Dynamic IPs": 100
                },
                "geo": {
                    "country": "Germany",
                    "countrycode": "DE"
                },
                "ip": "92.192.0.0/11",
                "categoryDescriptions": {
                    "Dynamic IPs": "This category contains IP addresses of dialup hosts and DSL lines."
                },
                "reasonDescription": "Based on statistical DNS analysis.",
                "score": 1
            },
            {
                "created": "2013-05-04T06:27:00.000Z",
                "reason": "Regional Internet Registry",
                "geo": {
                    "country": "Germany",
                    "countrycode": "DE"
                },
                "ip": "92.222.0.0/15",
                "cats": {
                    "Dynamic IPs": 100
                },
                "categoryDescriptions": {
                    "Dynamic IPs": "This category contains IP addresses of dialup hosts and DSL lines."
                },
                "reasonDescription": "One of the five RIRs announced a (new) location mapping of the IP.",
                "score": 1
            },
            {
                "created": "2013-05-04T19:00:00.000Z",
                "reason": "DNS heuristics",
                "geo": {
                    "country": "Germany",
                    "countrycode": "DE"
                },
                "ip": "92.222.0.0/15",
                "cats": {
                    "Dynamic IPs": 100
                },
                "categoryDescriptions": {
                    "Dynamic IPs": "This category contains IP addresses of dialup hosts and DSL lines."
                },
                "reasonDescription": "Based on statistical DNS analysis.",
                "score": 1
            },
            {
                "created": "2013-10-18T06:27:00.000Z",
                "reason": "Regional Internet Registry",
                "geo": {
                    "country": "Germany",
                    "countrycode": "DE"
                },
                "ip": "92.222.0.0/16",
                "cats": {
                    "Dynamic IPs": 100
                },
                "categoryDescriptions": {
                    "Dynamic IPs": "This category contains IP addresses of dialup hosts and DSL lines."
                },
                "reasonDescription": "One of the five RIRs announced a (new) location mapping of the IP.",
                "score": 1
            },
            {
                "created": "2014-01-22T00:00:00.000Z",
                "reason": "DNS heuristics",
                "geo": {
                    "country": "Germany",
                    "countrycode": "DE"
                },
                "ip": "92.222.0.0/16",
                "cats": {
                    "Dynamic IPs": 100
                },
                "categoryDescriptions": {
                    "Dynamic IPs": "This category contains IP addresses of dialup hosts and DSL lines."
                },
                "reasonDescription": "Based on statistical DNS analysis.",
                "score": 1
            },
            {
                "created": "2014-01-23T15:07:00.000Z",
                "reason": "DNS heuristics",
                "geo": {
                    "country": "Germany",
                    "countrycode": "DE"
                },
                "ip": "92.222.0.0/16",
                "deleted": true,
                "categoryDescriptions": {},
                "reasonDescription": "Based on statistical DNS analysis.",
                "score": 1,
                "cats": {}
            },
            {
                "created": "2014-11-04T10:29:00.000Z",
                "reason": "Regional Internet Registry",
                "deleted": true,
                "ip": "92.222.0.0/16",
                "geo": {
                    "country": "Germany",
                    "countrycode": "DE"
                },
                "categoryDescriptions": {},
                "reasonDescription": "One of the five RIRs announced a (new) location mapping of the IP.",
                "score": 1,
                "cats": {}
            },
            {
                "created": "2014-11-11T13:31:00.000Z",
                "reason": "Regional Internet Registry",
                "deleted": true,
                "ip": "92.222.0.0/16",
                "categoryDescriptions": {},
                "reasonDescription": "One of the five RIRs announced a (new) location mapping of the IP.",
                "score": 1,
                "cats": {}
            },
            {
                "created": "2014-11-11T14:51:00.000Z",
                "reason": "Regional Internet Registry",
                "deleted": true,
                "ip": "92.222.0.0/16",
                "geo": {
                    "country": "France",
                    "countrycode": "FR"
                },
                "categoryDescriptions": {},
                "reasonDescription": "One of the five RIRs announced a (new) location mapping of the IP.",
                "score": 1,
                "cats": {}
            },
            {
                "created": "2017-07-26T06:24:00.000Z",
                "reason": "Regional Internet Registry",
                "deleted": true,
                "ip": "92.222.0.0/16",
                "asns": {
                    "16276": {
                        "Company": "OVH, FR",
                        "cidr": 16
                    }
                },
                "geo": {
                    "country": "France",
                    "countrycode": "FR"
                },
                "categoryDescriptions": {},
                "reasonDescription": "One of the five RIRs announced a (new) location mapping of the IP.",
                "score": 1,
                "cats": {}
            },
            {
                "created": "2017-10-10T06:23:00.000Z",
                "reason": "Regional Internet Registry",
                "deleted": true,
                "ip": "92.222.0.0/16",
                "geo": {
                    "country": "France",
                    "countrycode": "FR"
                },
                "categoryDescriptions": {},
                "reasonDescription": "One of the five RIRs announced a (new) location mapping of the IP.",
                "score": 1,
                "cats": {}
            },
            {
                "created": "2017-10-18T06:23:00.000Z",
                "reason": "Regional Internet Registry",
                "deleted": true,
                "ip": "92.222.0.0/16",
                "asns": {
                    "16276": {
                        "Company": "OVH, FR",
                        "cidr": 16
                    }
                },
                "geo": {
                    "country": "France",
                    "countrycode": "FR"
                },
                "categoryDescriptions": {},
                "reasonDescription": "One of the five RIRs announced a (new) location mapping of the IP.",
                "score": 1,
                "cats": {}
            },
            {
                "created": "2020-03-21T07:52:00.000Z",
                "reason": "Regional Internet Registry",
                "deleted": true,
                "ip": "92.222.0.0/16",
                "geo": {
                    "country": "France",
                    "countrycode": "FR"
                },
                "categoryDescriptions": {},
                "reasonDescription": "One of the five RIRs announced a (new) location mapping of the IP.",
                "score": 1,
                "cats": {}
            },
            {
                "created": "2020-03-22T07:54:00.000Z",
                "reason": "Regional Internet Registry",
                "deleted": true,
                "ip": "92.222.0.0/16",
                "geo": {
                    "country": "France",
                    "countrycode": "FR"
                },
                "categoryDescriptions": {},
                "reasonDescription": "One of the five RIRs announced a (new) location mapping of the IP.",
                "score": 1,
                "cats": {}
            },
            {
                "created": "2020-03-28T07:52:00.000Z",
                "reason": "Regional Internet Registry",
                "deleted": true,
                "ip": "92.222.0.0/16",
                "asns": {
                    "16276": {
                        "Company": "UNALLOCATED",
                        "cidr": 16
                    }
                },
                "geo": {
                    "country": "France",
                    "countrycode": "FR"
                },
                "categoryDescriptions": {},
                "reasonDescription": "One of the five RIRs announced a (new) location mapping of the IP.",
                "score": 1,
                "cats": {}
            },
            {
                "created": "2020-03-29T06:52:00.000Z",
                "reason": "Regional Internet Registry",
                "deleted": true,
                "ip": "92.222.0.0/16",
                "asns": {
                    "16276": {
                        "Company": "OVH, FR",
                        "cidr": 16
                    }
                },
                "geo": {
                    "country": "France",
                    "countrycode": "FR"
                },
                "categoryDescriptions": {},
                "reasonDescription": "One of the five RIRs announced a (new) location mapping of the IP.",
                "score": 1,
                "cats": {}
            }
        ],
        "subnets": [
            {
                "created": "2020-03-29T06:52:00.000Z",
                "reason": "Regional Internet Registry",
                "asns": {
                    "16276": {
                        "Company": "OVH, FR",
                        "cidr": 16
                    }
                },
                "geo": {
                    "country": "France",
                    "countrycode": "FR"
                },
                "ip": "92.222.0.0",
                "categoryDescriptions": {},
                "reasonDescription": "One of the five RIRs announced a (new) location mapping of the IP.",
                "score": 1,
                "cats": {},
                "subnet": "92.222.0.0/16"
            }
        ],
        "cats": {},
        "geo": {
            "country": "France",
            "countrycode": "FR"
        },
        "score": 1,
        "reason": "Regional Internet Registry",
        "reasonDescription": "One of the five RIRs announced a (new) location mapping of the IP.",
        "categoryDescriptions": {},
        "tags": []
    },
    "hosting": null,
    "geo": null,
    "provider": null
}
"""


loadjson = json.loads(data)
data = loadjson['ipr']

x.field_names = ["param", "value"]

view = ["geo", "ip", "score", "country"]

report = []

for key in data:
    # print(f"{key} -- {type(data[key])}")
    key_data = data[key]

    if key in view:
        if type(key_data) is str or type(key_data) is int:
            report.append([key, key_data])

        if type(key_data) is dict:
            for i in key_data:
                if i in view:
                    report.append([i, key_data[i]])


print(report)

# print(type(data[key]))


