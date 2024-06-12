import json

from pydantic import field_validator

from contextcheck.connectors.connector_http import ConnectorHTTP
from contextcheck.endpoints.endpoint import EndpointBase
from contextcheck.models.request import RequestBase


class EndpointTGChatBot(EndpointBase):
    class RequestModel(EndpointBase.RequestModel):
        asr_build: dict | None = None

        @field_validator("asr_build", mode="before")
        @classmethod
        def asr_converstion(cls, obj: str | dict) -> dict:
            """Get ASR as dict or string encoded as JSON"""
            if isinstance(obj, str):
                return json.loads(obj)
            elif isinstance(obj, dict):
                return obj
            else:
                raise ValueError(
                    "ASR provided in a wrong format (should be str or dict)"
                )

    def model_post_init(self, __context) -> None:
        self.connector = ConnectorHTTP(
            url=self.config.url,
            additional_headers=self.config.additional_headers,
        )
