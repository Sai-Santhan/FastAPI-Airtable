from dataclasses import dataclass

import requests


@dataclass()
class Airtable:
    base_id: str
    api_key: str
    table_name: str
    url: str

    def create_records(self, data={}):
        if len(data.keys()) == 0:
            return False
        url = f"{self.url}/{self.base_id}/{self.table_name}"
        payload = {"records": [{"fields": data}]}
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        response = requests.post(url, json=payload, headers=headers)
        print(url)
        print(payload)
        print(headers)
        print(response)
        return response.status_code == 200
