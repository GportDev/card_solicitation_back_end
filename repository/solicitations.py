from uuid import UUID
from bson import ObjectId
from pymongo import MongoClient
from utils.serialize_data import serialize_data
from models.solicitation import Solicitation


class SolicitationsRepository:
    def __init__(self):
        self.__client = MongoClient(host='172.17.0.2')
        self.__db = self.__client.credit
        self.__collection = self.__db.solicitations

    # Recupera todas as solicitações
    def get_all_solicitations(self):
        solicitations = self.__collection.find({})
        return serialize_data(solicitations)

    # Insere uma nova solicitação
    def insert_one_solicitation(self, solicitation: Solicitation):
        solicitation_dict = solicitation.dict()
        inserted_solicitation = self.__collection.insert_one(
            solicitation_dict).inserted_id
        return serialize_data(inserted_solicitation, is_singular=True)

    # Recupera uma solicitação pelo id
    def get_one_solicitation(self, solicitation_id: UUID):
        solicitation = self.__collection.find_one(
            {"_id": ObjectId(solicitation_id)})
        return serialize_data(solicitation, is_singular=True)

    # Deleta a solicitação pelo id
    def delete_one_solicitation(self, solicitation_id: UUID):
        self.__collection.delete_one({"_id": ObjectId(solicitation_id)})
