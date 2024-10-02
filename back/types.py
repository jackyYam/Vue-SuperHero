from typing import List, TypedDict


class Powerstats(TypedDict):
    intelligence: int
    strength: int
    speed: int
    durability: int
    power: int
    combat: int
    AS: int


class Biography(TypedDict):
    full_name: str
    alter_egos: str
    aliases: List[str]
    place_of_birth: str
    first_appearance: str
    publisher: str
    alignment: str


class Hero(TypedDict):
    id: int
    name: str
    powerstats: Powerstats
    alignment: str
    biography: Biography
    image: str


class HeroFull(Hero):
    hp: int
    fb: int
    actualStats: Powerstats


class Team(TypedDict):
    alignment: str
    heroes: List[HeroFull]
