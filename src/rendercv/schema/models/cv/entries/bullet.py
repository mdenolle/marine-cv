import pydantic

from .bases.entry import BaseEntry



class BulletEntry(BaseEntry):
    bullet: str | None = pydantic.Field(
        default=None,
        examples=["Python, JavaScript, C++", "Excellent communication skills"],
    )
    date: str | None = None
    name: str | None = None
    institution: str | None = None
    topic: str | None = None
