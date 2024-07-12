import pydantic
from typing import Any

from collections.abc import Callable
from typing import Annotated, Any, get_args, get_origin

def invalid_to_none(v: Any, handler: Callable[[Any], Any]) -> Any:
    try:
        return handler(v)
    except pydantic.ValidationError:
        print(f'!!! Error loading {v}')
        return v #None


class UnValidatedBaseModel(pydantic.BaseModel):
    def __init_subclass__(cls, **kwargs: Any) -> None:
        for name, annotation in cls.__annotations__.items():
            if name.startswith("_"):  # exclude protected/private attributes
                continue
            validator = pydantic.WrapValidator(invalid_to_none)
            if get_origin(annotation) is Annotated:
                cls.__annotations__[name] = Annotated[
                    *get_args(annotation),
                    validator,
                ]
            else:
                cls.__annotations__[name] = Annotated[annotation, validator]


