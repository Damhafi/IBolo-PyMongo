import datetime


class Bolo():

    def __init__(self, data):
        self.dict_data = data

    # origem: https://www.programiz.com/python-programming/property
    # Getter method
    @property
    def dict_data(self):

        if self.__dict_data is None:
            raise ValueError('Bolo não populado.')

        return self.__dict_data

    # Setter method
    @dict_data.setter
    def dict_data(self, data):

        if not self.validate(data):
            raise ValueError('Dados inválidos para instanciar o bolo.')

        self.__dict_data = data

    def validate(self, data):

        if (self.validate_dict_type(data) and
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
        elif 'cliente' not in data:
            print('to no cliente')
            return False
        elif 'price_sell' not in data:
            print('to no price_sell')
            return False
        elif 'cost_ingredients' not in data:
            print('to no cost_ingredients')
            return False
        else:
            return True

    def validate_dict_data(self, data):
        if not isinstance(data['name'], str):
            return False
        elif data['name'] == '':
            return False
        elif not isinstance(data['cliente'], str):
            return False
        elif data['cliente'] == '':
            return False
        elif data['sell_date'] == '':
            return False

        try:
            float(data['cost_ingredients'])
            float(data['price_sell'])
        except ValueError:
            return False
        return True

    # origem: https://iscinumpy.gitlab.io/post/factory-classmethods-in-python/
    @classmethod
    def from_data(cls,
                  name: str,
                  name_client: str,
                  cost_ingredients: float,
                  date: datetime,
                  price_sell: float,
                  receita,
                  ):
        dict_data = {
            'name': name,
            'cliente': name_client,
            'price_sell': price_sell,
            'cost_ingredients': cost_ingredients,
            'sell_date': date,
            'receita': receita,
        }
        return cls(dict_data)
