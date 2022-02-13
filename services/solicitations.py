from uuid import UUID

import utils.score_manipulation
from repository.solicitations import SolicitationsRepository
from models.solicitation import Solicitation
from utils.score_manipulation import ScoreManipulation

class SolicitationsService:
    @staticmethod
    def get_all_solicitations() -> dict:
        try:
            solicitations_repository = SolicitationsRepository()
            solicitations = solicitations_repository.get_all_solicitations()
        finally:
            del solicitations_repository
        return solicitations

    # Responsável por inserir um novo item
    @staticmethod
    def insert_one_solicitation(solicitations: Solicitation):
        try:
            solicitations_repository = SolicitationsRepository()
            solicitations.score = ScoreManipulation.score_generator()
            solicitations.limit = ScoreManipulation.limit_calculator(solicitations.score, solicitations.income)
            solicitations.approval = ScoreManipulation.approval(solicitations.score)
            inserted_solicitation = solicitations_repository.insert_one_solicitation(solicitations)
        finally:
            del solicitations_repository
        return inserted_solicitation

    # Responsável por recuperar apenas um item através do seu ID
    @staticmethod
    def get_one_solicitation(solicitation_id: UUID):
        try:
            solicitation_repository = SolicitationsRepository()
            solicitation = solicitation_repository.get_one_solicitation(solicitation_id)
        finally:
            del solicitation_repository
        return solicitation

    # Deleta a solicitação selecionada pelo id
    @staticmethod
    def delete_solicitation(solicitation_id: UUID):
        try:
            solicitation_repository = SolicitationsRepository()
            solicitation_repository.delete_one_solicitation(solicitation_id)
        finally:
            del solicitation_repository