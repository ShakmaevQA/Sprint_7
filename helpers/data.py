import random

class Data:
    login_bases = ["ninja", "shadow", "ghost", "dragon", "tiger", "wolf", "storm", "fire"]

    @staticmethod
    def create_random_login():
        login = f"{random.choice(Data.login_bases)}{random.randint(1000, 9999)}"
        return login

    @staticmethod
    def create_valid_courier():
        result = {
            "login": Data.create_random_login(),
            "password": "testpassword",
            "firstname": "Pupa"
        }
        return result

    @staticmethod
    def create_invalid_courier():
        result = {
            "login": Data.create_random_login()
        }
        return result

    @staticmethod
    def create_order(color):
        result =  {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2024-06-06",
            "comment": "Saske, come back to Konoha",
            "color": color
        }
        return result



