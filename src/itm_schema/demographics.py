from enum import Enum
from .pydantic_schema import ValidatedBaseModel
from typing import List, Dict

#todo: for each qualtrics Enum, make sure to align with what is actually collected from qualtrics
class GenderIdentity(str, Enum):
    """

    """
    male = "Male"
    female = "Female"
    other = "Other"


class Education(str, Enum):
    """

    """
    none = "None"
    high_school = "High School"
    college = "College"
    grad_school = "Grad School"
    medical_school = "Medical School"
    hard_knocks = "School of Hard Knocks"


class OccupationType(str, Enum):
    """

    """
    none = "None"
    nurse = "Nurse"
    clinical_coordinator = "Clinical Coordinator"
    clinical_staff = "Clinical Staff"
    doctor = "Doctor"
    physician = "Physician"
    physician_assistant = "Physician's Assistant"
    surgeon = "Surgeon"
    emt = "EMT"
    paramedic = "Paramedic"
    firefighter = "Firefighter"
    resident = "Resident"
    engineer = "Engineer"


class Occupation(ValidatedBaseModel):
    """

    """
    type: OccupationType
    length: int


class Certification(str, Enum):
    """

    """
    c1 = "Certification 1"
    c2 = "Certification 2"
    c3 = "Certification 3"


class MilitaryPosition(str, Enum):
    """

    """
    p1 = "Position 1"
    p2 = "Position 2"
    p3 = "Position 3"


class MilitaryExperience(ValidatedBaseModel):
    """
    
    """
    position: MilitaryPosition
    length: int


class Race(str, Enum):
    """

    """
    black_african_american = "Black/AfricanAmerican"
    white = "White"
    hispanic_latino = "Hispanic/Latino"
    asian = "Asian"
    american_indian_alaska_native = "AmericanIndian/AlaskaNative"
    middle_eastern_north_african = "MiddleEastern/NorthAfrican"
    native_hawaiin_pacific_islander = "NativeHawaiin/PacificIslander"


class DMDemographics(ValidatedBaseModel):
    """

    """
    # id of decision maker
    dm_id: str
    age: int
    gender: GenderIdentity
    race: Race
    occupations: List[Occupation]
    certifications: List[Certification]
    military_experience: List[MilitaryExperience]

class DMPopulation(ValidatedBaseModel):
    """
    Container object for DM Demographics
    String id is the Qualtrics user id
    """
    population: Dict[str, DMDemographics]
