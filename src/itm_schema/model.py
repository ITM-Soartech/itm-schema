from . import pydantic_schema as ps
from .ml_pipeline import KDMAProfile
from .demographics import DMDemographics
from typing import List

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

