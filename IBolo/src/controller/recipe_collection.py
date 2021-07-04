from .mongodb import MongoDB
from src.model.recipe import Recipe


class Recipe_Collection(MongoDB):

    def __init__(self, DBName='IBolo'):
        MongoDB.__init__(self, DBName)

    def recipe_in_collection(self, recipe_name: str) -> bool:

        returned_object = self.recp_collection.find_one(
            {'name': recipe_name})

        if returned_object is None:
            return False

        return True

    def recipe_in_collection_by_id(self, recipe_id: str) -> bool:
        returned_object = self.recp_collection.find_one({'_id': recipe_id})

        if returned_object is None:
            return False

        return True


    def insert_recipe(self, recipe: Recipe) -> dict:
        if self.recipe_in_collection(recipe.dict_data['name']):
            raise ValueError('Receita já inserido na coleção.')

        returned_object = self.recp_collection.insert_one(
            recipe.dict_data)

        if returned_object.acknowledged is False:
            raise RuntimeError('Erro - Receita não inserida na coleção.')

        return returned_object.inserted_id


    def find_recipe(self, recipe_name: str) -> dict:
        recipe_dict = self.recp_collection.find_one(
            {'name': recipe_name})

        if recipe_dict is None:
            raise ValueError('Receita não encontrado na coleção.')
        return recipe_dict


    def find_recipe_by_id(self, _id: str) -> dict:
        recipe_dict = self.recp_collection.find_one(
            {'_id': _id})

        if recipe_dict is None:
            raise ValueError('Receita não encontrado na coleção.')

        return recipe_dict


    def delete_recipe_by_id(self, _id: str) -> bool:
        if not self.recipe_in_collection_by_id(_id):
            raise ValueError('Receita não inserido na coleção.')

        returned_object = self.recp_collection.delete_one(
            {'_id': _id})

        if returned_object is None:
            raise Exception('Receita não excluído da coleção.')

        return True
