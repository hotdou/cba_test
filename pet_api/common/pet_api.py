import json
from helpers.http_client import HTTPClient
from pet_api.config import PET_STORE_BASE_URL


class PetAPI:
    base_url = PET_STORE_BASE_URL + "v2/pet"
    header = {"Content-Type": "application/json", "accept": "application/json"}
    header_with_key = {"x-api-key":"special-key"}

    @classmethod
    def add_pet(cls, pet):
        url = cls.base_url
        resp = HTTPClient.post(url, pet.as_dict(), headers=cls.header)
        if resp.ok:
            print("added pet =>\n", resp.json())
        else:
            print("sent request to url =>", url)
            print("\n", resp.status_code, "\n", resp.content)

        return resp
    
    @classmethod
    def update_pet_by_form(cls, id, **params):
        header = {"Content-Type": "application/x-www-form-urlencoded", "accept": "application/json"}
        url = cls.base_url + f"/{id}"
        resp = HTTPClient.post(url, data=params, headers=header)
        if resp.ok:
            print("updated pet =>\n", resp.json())
        else:
            print("sent request to url =>", url)
            print(resp.content)

        return resp
    
    @classmethod
    def update_pet(cls, pet):
        url = cls.base_url
        resp = HTTPClient.put(url, pet.as_dict(), headers=cls.header)

        if resp.ok:
            # result = resp.json()
            print("updated pet =>\n", resp.json())

        return resp
    
    @classmethod
    def get_pet_by_id(cls, id):
        url = cls.base_url + f"/{id}"
        res = HTTPClient.get(url, headers=cls.header)
        if res.ok:
            print(f"retrieved pet by id {id}")

        return res
    
    @classmethod
    def get_pet_by_status(cls, status):
        url = cls.base_url + f"/findByStatus?status={status}"
        res = HTTPClient.get(url, headers=cls.header)
        if res.ok:
            print(f"retrieved pet by status {status}")

        return res
    
    @classmethod
    def delete_pet_by_id(cls, id):
        url = cls.base_url + f"/{id}"
        res = HTTPClient.delete(url, headers=cls.header)
        
        if res.ok:
            print(f"deleted pet by id {id}")

        return res
    
    @classmethod
    def upload_image(cls, id, file_path, file, meta=""):
        url = cls.base_url + f"/{id}/uploadImage"
        header = {"accept": "application/json"}
        files = {
                    'additionalMetadata': (None, meta),
                    'file': (file, open(file_path, 'rb'), 'image/jpeg'),
                }

        resp = HTTPClient.post(url, files=files, headers=header)
        if resp.ok:
            print("uploaded image =>\n", resp.json())
        else:
            print("sent request to url =>", url)
            print(resp.text)

        return resp
    


