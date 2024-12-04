from collections.abc import Sequence
from typing import Any

from rest_framework.fields import Field
from rest_framework.pagination import BasePagination
from rest_framework.request import Request
from rest_framework.serializers import BaseSerializer
from typing_extensions import TypedDict

from .generators import BaseSchemaGenerator as BaseSchemaGenerator
from .inspectors import ViewInspector as ViewInspector

# OpenAPI requires its own typings. Below are minimal typing.
# TODO: evaluate using a 3rd party typing package for this, e.g.: https://github.com/meeshkan/openapi-typed

class DRFOpenAPIInfo(TypedDict, total=False):
    title: str
    version: str
    description: str

class DRFOpenAPISchema(TypedDict, total=False):
    openapi: str
    info: DRFOpenAPIInfo
    paths: dict[str, dict[str, Any]]
    components: dict[str, dict[str, Any]]
    security: list[dict[str, list[Any]]]
    tags: list[dict[str, Any]]
    servers: list[dict[str, Any]]

class SchemaGenerator(BaseSchemaGenerator):
    def get_info(self) -> DRFOpenAPIInfo: ...
    def check_duplicate_operation_id(self, paths: dict[str, dict[str, Any]]) -> None: ...
    def get_schema(self, request: Request = ..., public: bool = ...) -> DRFOpenAPISchema: ...  # type: ignore[override]

class AutoSchema(ViewInspector):
    operation_id_base: str | None
    component_name: str | None
    request_media_types: list[str]
    response_media_types: list[str]
    method_mapping: dict[str, str]
    def __init__(
        self, tags: Sequence[str] = ..., operation_id_base: str | None = ..., component_name: str | None = ...
    ) -> None: ...
    def get_operation(self, path: str, method: str) -> dict[str, Any]: ...
    def get_component_name(self, serializer: BaseSerializer) -> str: ...
    def get_components(self, path: str, method: str) -> dict[str, Any]: ...
    def get_operation_id_base(self, path: str, method: str, action: Any) -> str: ...
    def get_operation_id(self, path: str, method: str) -> str: ...
    def get_path_parameters(self, path: str, method: str) -> list[dict[str, Any]]: ...
    def get_filter_parameters(self, path: str, method: str) -> list[dict[str, Any]]: ...
    def allows_filters(self, path: str, method: str) -> bool: ...
    def get_pagination_parameters(self, path: str, method: str) -> list[dict[str, Any]]: ...
    def map_choicefield(self, field: Field) -> dict[str, Any]: ...
    def map_field(self, field: Field) -> dict[str, Any]: ...
    def map_serializer(self, serializer: BaseSerializer) -> dict[str, Any]: ...
    def map_field_validators(self, field: Any, schema: Any) -> None: ...
    def get_field_name(self, field: Field) -> str: ...
    def get_paginator(self) -> type[BasePagination] | None: ...
    def map_parsers(self, path: str, method: str) -> list[str]: ...
    def map_renderers(self, path: str, method: str) -> list[str]: ...
    def get_serializer(self, path: str, method: str) -> BaseSerializer | None: ...
    def get_request_serializer(self, path: str, method: str) -> BaseSerializer | None: ...
    def get_response_serializer(self, path: str, method: str) -> BaseSerializer | None: ...
    def get_reference(self, serializer: BaseSerializer) -> dict[str, str]: ...
    def get_request_body(self, path: str, method: str) -> dict[str, Any]: ...
    def get_responses(self, path: str, method: str) -> dict[str, Any]: ...
    def get_tags(self, path: str, method: str) -> list[str]: ...
