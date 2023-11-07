"""
Contains pydantic models for machine learning pipeline objects.
"""
from typing import Optional, List, Dict
from sklearn.neighbors import KernelDensity
from .kdma_ids import KDMAId
from . import pydantic_schema as ps

class SimpleHistogram(ps.ValidatedBaseModel):
    bin_values: List[float]
    bin_size: float



class KDMAMeasurement(ps.ValidatedBaseModel):
    """

    """
    # initial representation of KDMA from pydantic schema, may not include int "score" value
    # may be removed in the future
    kdma: Optional[ps.KDMA]

    # an enum that represented which KDMA this measurement corresponds to
    kdma_id: Optional[KDMAId]

    # probability distribution representation of KDMA
    _kde: Optional[KernelDensity]

    # histogram representation of KDMA
    hist: Optional[SimpleHistogram]


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
    kdma_alignments: Dict[KDMAId, float]


class AlignmentTarget(ps.ValidatedBaseModel):
    kdma_values: Dict[KDMAId, float]


# used by the alignment visualizer to show an analysis of the quality of the alignment
class AlignmentPackage(ps.ValidatedBaseModel):

    # used to determine the quality of the alignment
    alignment_score: float

    # used to indicate what was aligning to the RD
    aligner_id: str

    # used to indicate the KDMAs of whatever was aligning to the RD
    aligner_profile: KDMAProfile
    # we might need to distinguish between more than 1 kind of reference distribution
    # reference_distribution: ReferenceDistribution
    
    # the target given to the aligner prior to it's attempt at aligning
    # which version do we use?
    #alignment_target: List[KDMAProfile]
    alignment_target: AlignmentTarget


class KDMAScore(ps.ValidatedBaseModel):
    """

    """
    kdma: ps.KDMA
    kdma_id: KDMAId
    kdma_probes: List[ps.Probe]


