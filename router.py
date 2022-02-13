from starlette.routing import Route
from actions.solicitationsactions import SolicitationsActions


BASE_PATH = '/credit'


class Router:
    @staticmethod
    def get_routes() -> list:
        return [
            Route(f'{BASE_PATH}/', SolicitationsActions.inicio,
                  methods=['GET']),
            Route(f'{BASE_PATH}/solicitation',
                  SolicitationsActions.get_solicitations, methods=['GET']),
            Route(f'{BASE_PATH}/solicitation/{{solicitation_id}}', SolicitationsActions.get_one_solicitation,
                  methods=['GET']),
            Route(f'{BASE_PATH}/solicitation',
                  SolicitationsActions.insert_one_solicitation, methods=['POST']),
            Route(f'{BASE_PATH}/solicitation/{{solicitation_id}}', SolicitationsActions.delete_one_solicitation,
                  methods=['DELETE'])
        ]
