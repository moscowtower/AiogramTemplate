from dataclasses import dataclass


@dataclass
class Config:
    token: str
    project: str
    admins: list


bot_config = Config(
    token='',
    project='',
    admins=[]
)