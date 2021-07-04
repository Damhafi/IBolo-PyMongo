

class Recipe():

    def __init__(self, data):
        self.dict_data = data

    # origem: https://www.programiz.com/python-programming/property
    # Getter method
    @property
    def dict_data(self):

        if self.__dict_data is None:
            raise ValueError('Receita não populado.')

        return self.__dict_data

    # Setter method
    @dict_data.setter
    def dict_data(self, data):

        if not self.validate(data):
            raise ValueError('Dados inválidos para instanciar a receita.')

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
        else:
            return True

    def validate_dict_data(self, data):

        if not isinstance(data['name'], str):
            return False
        elif data['name'] == '':
            return False

        return True

    # origem: https://iscinumpy.gitlab.io/post/factory-classmethods-in-python/
    @classmethod
    def from_data(cls,
                  name: str,
                  ingredientes,
                  ):
        dict_data = {
            'name': name,
            'ingredientes': ingredientes,

        }

        return cls(dict_data)
