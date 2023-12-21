"""
Contains pydantic models for machine learning pipeline objects.
"""
from typing import Optional, List, Dict
from sklearn.neighbors import KernelDensity
from .kdma_ids import KDMAId
from . import pydantic_schema as ps

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
    kde: Optional[KernelDensity]

    # histogram representation of KDMA
    hist: Optional[SimpleHistogram]

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