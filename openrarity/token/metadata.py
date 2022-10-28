from logging import Logger
from typing import Literal, Optional

from pydantic import BaseModel, root_validator, validator

from openrarity.validators.string import clean_lower_string

logger = Logger(__name__)


class MetadataAttributeModel(BaseModel):
    """A validator for Token Metadata."""

    name: str
    value: float | int | str
    display_type: Optional[Literal["string", "number", "date"]] = "string"

    name_validator = validator("name", allow_reuse=True)(clean_lower_string)

    @root_validator(pre=True)
    def clean_attribute_value(cls, values: dict[str, str | float | int | None]):
        if "trait_type" in values:
            values["name"] = values.pop("trait_type")
        dtype = values.setdefault("display_type", "string")
        value = values["value"]
        if dtype in ["number", "date"]:
            logger.warn(
                f"'{dtype}' are not supported and will not be considered when ranking."
            )
        if isinstance(value, str):
            values["value"] = clean_lower_string(value)
        return values
