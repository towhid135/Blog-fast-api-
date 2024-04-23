from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator

# Represents an ObjectId field in the database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.
# PyObjectId = Annotated[str, BeforeValidator(str)]

PyObjectId = Annotated[str, BeforeValidator(str)]