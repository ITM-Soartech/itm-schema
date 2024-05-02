"""
Contains pydantic models for machine learning pipeline objects.
"""
from typing import Optional, List, Dict, Union
from sklearn.neighbors import KernelDensity
from .kdma_ids import KDMAId
from . import pydantic_schema as ps
from pydantic import field_serializer, field_validator
import numpy as np

KDE_MAX_VALUE = 1.0 # Value ranges from 0 to 1.0
KDE_BANDWIDTH = 0.75 * (KDE_MAX_VALUE / 10.0)

class SimpleHistogram(ps.ValidatedBaseModel):
    # Should match output of np.histogram
    bin_values: List[float]
    bin_edges: List[float]


class KDMAMeasurement(ps.ValidatedBaseModel):
    """

    """
    # an enum that represented which KDMA this measurement corresponds to
    kdma_id: KDMAId

    # Plain value for this KDMA
    value: float

    # probability distribution representation of KDMA
    kde: Optional[Union[list[float],KernelDensity]]

    # histogram representation of KDMA
    hist: Optional[SimpleHistogram]

    @field_serializer('kde')
    def serialize_kde(self, kde: KernelDensity, _info) -> list[float]:
        X = np.linspace(0, 1, 100)[:, np.newaxis]
        log_dens = kde.score_samples(X)
        samples = np.exp(log_dens)
        print(samples)
        return list(samples)


    @field_validator('kde')
    @classmethod
    def validate_kde(cls, kde: Union[list[float], KernelDensity]) -> Optional[KernelDensity]:
        if isinstance(kde, KernelDensity):
            return kde
        else:
            X = np.array(kde)
            return KernelDensity(kernel="gaussian", bandwidth=KDE_BANDWIDTH).fit(X[:, np.newaxis])

    class Config:
        # Allow non-pydantic KernelDensity
        arbitrary_types_allowed = True


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

class AlignmentTarget(ps.ValidatedBaseModel):
    """
    Dict's str is the dm_id 
    """
    target: Dict[str, KDMAProfile]

class KDMAAlignment(ps.ValidatedBaseModel):
    """
    This object describes per KMDA of alignment of an ADM to 1 RDM
    """
    # this dict contains list of KDMAs for 1 decision maker
    kdma_alignments: Dict[KDMAId, float]

class RDMAlignment(ps.ValidatedBaseModel):
    """
    # This object describes the alignment of an ADM to 1 RDM
    """
    rdm_id: str
    # this is the overall alignment of the ADM to a single RDM
    individual_alignment: float
    alignment_detail: KDMAAlignment

# used by the alignment visualizer to show an analysis of the quality of the alignment
class AlignmentPackage(ps.ValidatedBaseModel):

    # overall alignment of one ADM to the target alignment group
    overall_alignment: float

    # alignment of the ADM to each invididual RDM in the alignment target
    rdm_alignments: List[RDMAlignment]

    # used to indicate what was aligning to the RD (usually the ADM)
    aligner_id: str

    # used to indicate the KDMAs of whatever was aligning to the RD
    aligner_profile: KDMAProfile
    # we might need to distinguish between more than 1 kind of reference distribution
    # reference_distribution: ReferenceDistribution
    
    # target to which the ADM is aligned 
    alignment_target: AlignmentTarget
