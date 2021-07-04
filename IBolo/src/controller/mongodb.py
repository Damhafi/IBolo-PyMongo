from pymongo import MongoClient


class MongoDB():

    def __init__(self, DBName='IBolo'):
        self.client = MongoClient('localhost', 27017)

        self.data_base = self.client[DBName]

        self.ingr_collection = self.data_base['Ingredientes']
        self.recp_collection = self.data_base['Receitas']
        self.bolo_collection = self.data_base['Bolo']

    def close(self):
        self.client.close()