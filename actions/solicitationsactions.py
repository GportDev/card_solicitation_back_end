import json
from json import JSONDecodeError
from bson.errors import InvalidId
from pydantic import ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from models.solicitation import Solicitation
from services.solicitations import SolicitationsService


class SolicitationsActions:

    @staticmethod
    async def inicio(request: Request) -> JSONResponse:
        return JSONResponse({"hello": "welcome to my sistem"})

    @staticmethod
    async def get_solicitations(request: Request) -> JSONResponse:
        solicitations = SolicitationsService.get_all_solicitations()
        return JSONResponse(solicitations)

    @staticmethod
    async def get_one_solicitation(request: Request) -> JSONResponse:
        try:
            solicitation_id = request.path_params['solicitation_id']
            solicitation = SolicitationsService.get_one_solicitation(solicitation_id)
            return JSONResponse(solicitation, status_code=200)

        except JSONDecodeError as error:
            return JSONResponse({
                "error": "Payload error, please check the docs"
            }, status_code=400)

        except InvalidId as error:
            return JSONResponse({})

    @staticmethod
    async def insert_one_solicitation(request: Request) -> JSONResponse:
        try:
            body_payload = await request.json()
            solicitation = Solicitation(**body_payload)
            inserted_solicitation = SolicitationsService.insert_one_solicitation(solicitation)
            return JSONResponse({"solicitation": inserted_solicitation})

        except ValidationError as validations:
            return JSONResponse(
                json.loads(validations.json()), status_code=400
            )

        except JSONDecodeError as error:
            return JSONResponse({
                "error": "Payload error, please check the docs"
            }, status_code=400)

        except Exception as E:
            return JSONResponse({"ERROR": str(E)}, status_code=400)

    @staticmethod
    async def delete_one_solicitation(request: Request) -> JSONResponse:
        solicitation_id = request.path_params['solicitation_id']
        SolicitationsService.delete_solicitation(solicitation_id)
        return JSONResponse({"_id": solicitation_id})
