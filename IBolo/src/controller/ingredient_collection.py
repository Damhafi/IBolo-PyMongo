from .mongodb import MongoDB
from src.model.ingredient import Ingredient, Lista_Preco


class Ingredient_Collection(MongoDB):

    def __init__(self, DBName='IBolo'):
        MongoDB.__init__(self, DBName)

    def ingredient_in_collection(self, ingredient_name: str) -> bool:

        returned_object = self.ingr_collection.find_one(
            {'name': ingredient_name})

        if returned_object is None:
            return False

        return True

    def findall(self):
        returnObj = []
        return_objected = self.ingr_collection.find()
        for i in return_objected:
            returnObj += [i['name']]
        if return_objected is None:
            raise RuntimeError('Erro - Não há ingredientes inseridos na coleção.')

        return returnObj

    def ingredient_in_collection_by_id(self, ingredient_id: str) -> bool:
        returned_object = self.ingr_collection.find_one({'_id': ingredient_id})

        if returned_object is None:
            return False

        return True

    def insert_ingredient(self, ingredient: Ingredient) -> dict:
        if self.ingredient_in_collection(ingredient.dict_data['name']):
            raise ValueError('Ingrediente já inserido na coleção.')
        returned_object = self.ingr_collection.insert_one(
            ingredient.dict_data)

        if returned_object.acknowledged is False:
            raise RuntimeError('Erro - Ingrediente não inserido na coleção.')

        return returned_object.inserted_id

    def find_ingredient(self, ingredient_name: str) -> dict:
        ingredient_dict = self.ingr_collection.find_one(
            {'name': ingredient_name})

        if ingredient_dict is None:
            raise ValueError("Ingrediente não encontrado na coleção.")
        return ingredient_dict

    def find_ingredient_by_id(self, _id: str) -> dict:
        ingredient_dict = self.ingr_collection.find_one(
            {'_id': _id})

        if ingredient_dict is None:
            raise ValueError('Ingrediente não encontrado na coleção.')

        return ingredient_dict

    def delete_ingredient_by_id(self, _id: str) -> bool:
        if not self.ingredient_in_collection_by_id(_id):
            raise ValueError('Ingrediente não inserido na coleção.')

        returned_object = self.ingr_collection.delete_one(
            {'_id': _id})

        if returned_object is None:
            raise Exception('Ingrediente não excluído da coleção.')

        return True

    def update_ingredient(self, ingredient: Ingredient, lista_preco: Lista_Preco) -> dict:
        global dataAtual
        for i in ingredient['lista_preco']:
            if lista_preco['date'] > i['date']:
                dataAtual = i

        ingredient_dict = self.ingr_collection.update_one(
            {'name': ingredient['name'], 'lista_preco': dataAtual},
            {'$set': {'cost': (lista_preco['price_buy'] / float(lista_preco['unit_buy'])), 'lista_preco.$': lista_preco
                      }},
        )
        if ingredient_dict is None:
            raise ValueError('Ingrediente não encontrado na coleção.')

        return ingredient_dict

    def new_cost_ingredient(self, ingredient: Ingredient, lista_preco: Lista_Preco) -> dict:
        ingredient_dict = self.ingr_collection.update_one(
            {'name': ingredient['name']},
            {'$push': {'lista_preco': lista_preco}}
        )
        if ingredient_dict is None:
            raise ValueError('Ingrediente não encontrado na coleção.')

        return ingredient_dict
