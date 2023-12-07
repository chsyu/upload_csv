from pydantic import BaseModel
from typing import List


class HomeworkRequestSchema(BaseModel):
    school: str
    semester: str
    workName: str
    githubUrl: str
    websiteUrl: str
    pptUrl: str
    imgUrl: str
    clkCnt: int
    skill: List[str]
    name: List[str]


class HomeworkResponseSchema(HomeworkRequestSchema):
    id: int

    class Config:
        from_attributes = True

