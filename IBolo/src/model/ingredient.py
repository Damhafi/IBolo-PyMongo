from datetime import datetime

class Lista_Preco():

    def __init__(self, data):
        self.dict_data = data

    # origem: https://www.programiz.com/python-programming/property
    # Getter method
    @property
    def dict_data(self):

        if self.__dict_data is None:
            raise ValueError('Lista preço não populado.')

        return self.__dict_data

    # Setter method
    @dict_data.setter
    def dict_data(self, data):

        if not self.validate(data):
            raise ValueError('Dados inválidos para instanciar a lista preço.')

        self.__dict_data = data

    def validate(self, data):

        if(self.validate_dict_type(data) and
                self.validate_dict_keys(data) and
                self.validate_dict_data(data)
        ):
            return True
        else:
            return False

    def validate_dict_type(self, data):
        if not isinstance(data, type({})):
            return False
        else:
            return True

    def validate_dict_keys(self, data):
        if 'price_buy' not in data:
            return False
        elif 'unit_buy' not in data:
            return False
        elif 'date' not in data:
            return False
        else:
            return True

    def validate_dict_data(self, data):

        if not isinstance(data['unit_buy'], str):
            return False
        elif data['unit_buy'] == '':
            return False
        elif not isinstance(data['date'], datetime):
            return False
        elif data['date'] is None:
            return False

        try:
            float(data['price_buy'])
        except ValueError:
            return False

        return True

    # origem: https://iscinumpy.gitlab.io/post/factory-classmethods-in-python/
    @classmethod
    def from_data(cls,
                  price_buy: float,
                  date: datetime,
                  unit_buy: str,
                  ):
        dict_data = {
                'price_buy': price_buy,
                'unit_buy': unit_buy,
                'date': date,
        }

        return cls(dict_data)

class Ingredient():

    def __init__(self, data):
        self.dict_data = data

    # origem: https://www.programiz.com/python-programming/property
    # Getter method
    @property
    def dict_data(self):

        if self.__dict_data is None:
            raise ValueError('Ingrediente não populado.')

        return self.__dict_data

    # Setter method
    @dict_data.setter
    def dict_data(self, data):

        if not self.validate(data):
            raise ValueError('Dados inválidos para instanciar o ingrediente.')

        self.__dict_data = data

    def validate(self, data):

        if(self.validate_dict_type(data) and
                self.validate_dict_keys(data) and
                self.validate_dict_data(data)
        ):
            return True
        else:
            return False

    def validate_dict_type(self, data):
        if not isinstance(data, type({})):
            return False
        else:
            return True

    def validate_dict_keys(self, data):
        if 'name' not in data:
            return False
        elif 'cost' not in data:
            return False
        elif 'unit' not in data:
            return False
        else:
            return True

    def validate_dict_data(self, data):

        if not isinstance(data['name'], str):
            return False
        elif data['name'] == '':
            return False
        elif not isinstance(data['unit'], str):
            return False
        elif data['unit'] == '':
            return False

        try:
            float(data['cost'])
        except ValueError:
            return False

        return True

    # origem: https://iscinumpy.gitlab.io/post/factory-classmethods-in-python/
    @classmethod
    def from_data(cls, name: str, cost: float, unit: str, lista_preco: { }):
        dict_data = {
            'name': name,
            'cost': cost,
            'unit': unit,
            'lista_preco': [
                lista_preco
            ]
        }

        return cls(dict_data)

