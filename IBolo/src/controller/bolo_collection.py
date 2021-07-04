from .mongodb import MongoDB
from src.model.bolo import Bolo


class Bolo_Collection(MongoDB):

    def __init__(self, DBName='IBolo'):
        MongoDB.__init__(self, DBName)

    def bolo_in_collection(self, bolo_name: str) -> bool:

        returned_object = self.bolo_collection.find_one(
            {'name': bolo_name})

        if returned_object is None:
            return False

        return True

    def insert_bolo(self, bolo: Bolo) -> dict:
        if self.bolo_in_collection(bolo.dict_data['name']):
            raise ValueError('Bolo já inserido na coleção.')
        returned_object = self.bolo_collection.insert_one(
            bolo.dict_data)

        if returned_object.acknowledged is False:
            raise RuntimeError('Erro - Bolo não inserido na coleção.')

        return returned_object.inserted_id

    def find_bolo(self, bolo_name: str) -> dict:
        bolo_dict = self.bolo_collection.find_one(
            {'name': bolo_name})

        if bolo_dict is None:
            raise ValueError("Bolo não encontrado na coleção.")
        return bolo_dict

    def find_bolo_by_id(self, _id: str) -> dict:
        bolo_dict = self.bolo_collection.find_one(
            {'_id': _id})

        if bolo_dict is None:
            raise ValueError('Bolo não encontrado na coleção.')

        return bolo_dict

    def delete_bolo_by_id(self, _id: str) -> bool:
        if not self.bolo_in_collection_by_id(_id):
            raise ValueError('Bolo não inserido na coleção.')

        returned_object = self.bolo_collection.delete_one(
            {'_id': _id})

        if returned_object is None:
            raise Exception('Bolo não excluído da coleção.')

        return True

    def bolo_in_collection_by_id(self, bolo_id: str) -> bool:
        returned_object = self.recp_collection.find_one({'_id': bolo_id})

        if returned_object is None:
            return False

        return True
