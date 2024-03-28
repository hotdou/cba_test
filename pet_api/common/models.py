from random import randint

class Pet:
    def __init__(self, name, id=None, status="available"):
        if not id:
            self.id = randint(200, 300)
        else:
            self.id = id
        self.name = name
        self.status = status
        self.category = {"id":100, "name":"anna_test"}
        self.photo_urls = ["anna_test_url"]
        self.tags = [{"id": 100, "name": "anna_tag"}]

    def as_dict(self):
        a_dict = {
                    "id": self.id,
                    "category": self.category,
                    "name": self.name,
                    "photoUrls": self.photo_urls,
                    "tags": self.tags,
                    "status": self.status
                }
        
        return a_dict