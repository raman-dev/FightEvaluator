from datetime import date,datetime
from enum import Enum
from sqlmodel import SQLModel, Field
from typing import Optional


class ImageLinkIn(SQLModel):
    fighter_id : int
    img_link: str

class AttributeQualifier(Enum):
    positive = "positive"
    negative = "negative"
    neutral = "neutral"
    untested = "untested"

class WeightClass(Enum):
    CATCH_WEIGHT = "Catch weight"
    STRAWWEIGHT = "Strawweight"
    FLYWEIGHT = "Flyweight"
    BANTAMWEIGHT = "Bantamweight"
    FEATHERWEIGHT = "Featherweight"
    LIGHTWEIGHT = "Lightweight"
    WELTERWEIGHT = "Welterweight"
    MIDDLEWEIGHT = "Middleweight"
    LIGHT_HEAVYWEIGHT = "Light Heavyweight"
    HEAVYWEIGHT = "Heavyweight"

class FightEvent(SQLModel,table=True):
    id: int = Field(primary_key=True)
    name: str
    date: date
    location: str
    link: Optional[str]

class MatchupIn(SQLModel):
    event_id: int
    fighter_a_id: int
    fighter_b_id: int
    weight_class: str
    rounds: str

class MatchUp(SQLModel,table=True):
    id: int = Field(primary_key=True)
    # date: Optional[date]
    weight_class: WeightClass
    
    fighter_a: str
    fighter_a_link: Optional[str]
    fighter_a_id: Optional[int]
    
    fighter_b: str
    fighter_b_link: Optional[str]
    fighter_b_id: Optional[int]

    rounds: Optional[str]
    isprelim: Optional[bool]
    #almost always 3 unless main-event or championship fight
    max_rounds: Optional[int]
    #optional foreign key to the fightevent table
    event_id: Optional[int] = Field(default=None, foreign_key="fightevent.id")
    # fighters: List["Fighter"] = Relationship(back_populates="matchup")

class TempMatchUp(SQLModel,table=True):
    id: int = Field(primary_key=True)
    weight_class: WeightClass
    
    fighter_a: str
    fighter_a_link: Optional[str]
    fighter_a_id: Optional[int]
    
    fighter_b: str
    fighter_b_link: Optional[str]
    fighter_b_id: Optional[int]

    isprelim: Optional[bool]
    rounds: Optional[str]
    max_rounds: Optional[int]
    event_id: Optional[int] = Field(default=None, foreign_key="fightevent.id")



class AssessmentUpdate(SQLModel):
    id: int
    head_movement: Optional[AttributeQualifier] = None
    gas_tank: Optional[AttributeQualifier] = None
    aggression: Optional[AttributeQualifier] = None
    desire_to_win: Optional[AttributeQualifier] = None
    striking: Optional[AttributeQualifier] = None
    chinny: Optional[AttributeQualifier] = None
    grappling_offense: Optional[AttributeQualifier] = None
    grappling_defense: Optional[AttributeQualifier] = None

class Assessment(SQLModel,table=True):
    id: int = Field(primary_key=True)
    head_movement: Optional[AttributeQualifier]
    gas_tank: Optional[AttributeQualifier]
    aggression: Optional[AttributeQualifier]
    desire_to_win: Optional[AttributeQualifier]
    striking: Optional[AttributeQualifier]
    chinny: Optional[AttributeQualifier]
    grappling_offense: Optional[AttributeQualifier]
    grappling_defense: Optional[AttributeQualifier]

class NoteIn(SQLModel):
    assessment_id: int
    data: str

class Note(SQLModel,table=True):
    id: int = Field(primary_key=True)
    assessment_id: int = Field(foreign_key="assessment.id")
    data: str
    timestamp: str = Field(default=datetime.now().isoformat())

class Fighter(SQLModel,table=True):
    id: int = Field(primary_key=True)
    first_name: str
    last_name: str
    nick_name: Optional[str] 
    weight_class: Optional[WeightClass]
    height: Optional[str]
    date_of_birth: Optional[date]
    reach: Optional[str]
    stance: Optional[str]
    record: Optional[str]
    img_link: Optional[str]
    #optional since a fighter may need to still be assessed
    assessment_id: Optional[int] = Field(default=None, foreign_key="assessment.id")
    # assesment: Optional["Assessment"] = Relationship(back_populates="fighters")

class FighterIn(SQLModel):
    first_name: str
    last_name: str
    nick_name: Optional[str]
    weight_class: Optional[str]
    height: Optional[str]
    date_of_birth: Optional[date]
    reach: Optional[str]
    stance: Optional[str]

class FighterUpdateIn(SQLModel):
    id: int
    first_name: Optional[str]
    last_name: Optional[str]
    nick_name: Optional[str] 
    weight_class: Optional[str]
    height: Optional[str]
    date_of_birth: Optional[date]
    reach: Optional[str]
    stance: Optional[str]
    record: Optional[str]
    img_link: Optional[str]

class FighterSearchOut(SQLModel):
    fighter_id: int
    first_name: str
    last_name: str
    weight_class: Optional[WeightClass]