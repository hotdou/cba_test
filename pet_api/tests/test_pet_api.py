import os
import unittest
from pet_api.common.pet_api import PetAPI
from pet_api.common.models import Pet


class PetAPITest(unittest.TestCase):
    def test_add_new_pet(self):
        self.pet = Pet("turtle")
        resp = PetAPI.add_pet(self.pet)
        self.check_resp(resp)

    def test_get_pet_by_id(self):
        self.pet = Pet("turtle")
        PetAPI.add_pet(self.pet)
        resp = PetAPI.get_pet_by_id(self.pet.id)
        self.check_resp(resp)

    def test_update_pet(self):
        self.pet = Pet("turtle")
        PetAPI.add_pet(self.pet)
        self.pet.status = "pending"
        resp = PetAPI.update_pet(self.pet)
        self.check_resp(resp)

    def test_delete_pet(self):
        self.pet = Pet("turtle")
        PetAPI.add_pet(self.pet)
        resp = PetAPI.delete_pet_by_id(self.pet.id)
        self.assertEqual(resp.status_code, 200)
        self.pet = None

    def test_get_pet_by_status(self):
        self.pet = Pet("turtle", status="sold")
        PetAPI.add_pet(self.pet)
        resp = PetAPI.get_pet_by_status("sold")
        self.assertEqual(resp.status_code, 200)

        found = False
        for pet in resp.json():
            self.assertEqual(pet["status"], "sold")
            if pet["id"] == self.pet.id:
                print("pet is found!")
                found = True
        
        self.assertTrue(found, "new pet is not returned when searching by status...")

    def test_update_pet_by_form(self):
        self.pet = Pet("turtle")
        PetAPI.add_pet(self.pet)

        # update name and status
        self.pet.name = "Guinea pig"
        self.pet.status = "pending"
        resp = PetAPI.update_pet_by_form(self.pet.id, name=self.pet.name, status=self.pet.status)
        self.assertEqual(resp.status_code, 200)

        # verify data is updated
        resp = PetAPI.get_pet_by_id(self.pet.id)
        self.check_resp(resp)

    def test_upload_image(self):
        self.pet = Pet("turtle")
        PetAPI.add_pet(self.pet)

        file_path = os.path.join(os.getcwd(), "pet_api", "tests", "data", "duck.jpg")
        resp = PetAPI.upload_image(self.pet.id, file_path=file_path, file="duck.jpg", meta="test")

        self.assertEqual(resp.status_code, 200)

    def check_resp(self, resp):
        self.assertEqual(resp.status_code, 200)
        content = resp.json()
        self.assertEqual(self.pet.id, content["id"])
        self.assertEqual(self.pet.name, content["name"])
        self.assertListEqual(self.pet.photo_urls, content["photoUrls"])
        self.assertListEqual(self.pet.tags, content["tags"])
        self.assertDictEqual(self.pet.category, content["category"])
        self.assertEqual(self.pet.status, content["status"])

    def tearDown(self):
        if self.pet:
            PetAPI.delete_pet_by_id(self.pet.id)

    