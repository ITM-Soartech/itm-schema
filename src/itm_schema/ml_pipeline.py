"""
Contains pydantic models for machine learning pipeline objects.
"""
from pydantic import Field, model_validator
import src.itm_schema.placeholders as ph
from src.itm_schema import pydantic_schema as ps
from typing import Optional, List, Dict
from sklearn.neighbors import KernelDensity
from src.itm_schema import pydantic_schema as ps
from enum import Enum


class KDMAId(str, Enum):
    """

    """
    risk_tol = "RiskTolerance"
    negative_urgency = "NegativeUrgency"
    ambiguity_tol = "AmbiguityTolerance"
    satisficing = "Satisficing"
    deny_care = "DenyCare"
    mission_success = "MissionSuccess"
    deviate_policy = "DeviatePolicy"
    deviate_standards = "DeviateStandards"
    qol = "QualityOfLife"
    trait_bias = "TraitBias"
    frugality = "Frugality"


class KDMAMeasurement(ps.ValidatedBaseModel):
    """

    """
    # initial representation of KDMA from pydantic schema, may not include int "score" value
    # may be removed in the future
    kdma: ps.KDMA

    # an enum that represented which KDMA this measurement corresponds to
    kdma_id: KDMAId

    # probability distribution representation of KDMA
    kde: KernelDensity

    # histogram representation of KDMA
    bin_values: List[float]
    bin_size: float


class KDMAProfile(ps.ValidatedBaseModel):
    """

    """
    # using a dict instead of a list allows for slightly better efficiency, even though ID is redundant
    dm_id: str
    kdma_measurements: Dict[KDMAId, KDMAMeasurement]


#todo: stub, expand
class ReferenceDistribution(ps.ValidatedBaseModel):
    """

    """
    rdms: Dict[str, KDMAProfile]


#todo: stub, expand
class AlignmentScore(ps.ValidatedBaseModel):
    """

    """
    score: float


class KDMAScore(ps.ValidatedBaseModel):
    """

    """
    kdma: ps.KDMA
    kdma_id: KDMAId
    kdma_probes: List[ps.Probe]

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
    nurse = "Nurse"
    clinical_coordinator = "Clinical Coordinator"
    doctor = "Doctor"
    physician_assistant = "Physician's assistant"
    surgeon = "Surgeon"
    emt = "EMT"


class Occupation(ps.ValidatedBaseModel):
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


class MilitaryExperience(ps.ValidatedBaseModel):
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


class DMDemographics(ps.ValidatedBaseModel):
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


class RawModelInput(ps.ValidatedBaseModel):
    """

    """
    probe: ps.Probe
    probe_response: ps.ProbeResponse
    dm_demographics: DMDemographics


class Feature(ps.ValidatedBaseModel):
    """

    """
    value: float
    label: str


class RefinedModelInput(ps.ValidatedBaseModel):
    """

    """
    features: List[Feature]


class RawModelTarget(ps.ValidatedBaseModel):
    """

    """
    # id of decision maker
    dm_id: str
    kdma_baseline_estimate: KDMAProfile

