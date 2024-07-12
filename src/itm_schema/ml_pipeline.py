"""
Contains pydantic models for machine learning pipeline objects.
"""
from typing import Optional, List, Dict
from sklearn.neighbors import KernelDensity
from .kdma_ids import KDMAId
from . import pydantic_schema as ps
from pydantic import field_serializer
import numpy as np
from enum import Enum

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
    value: Optional[float] = None

    # probability distribution representation of KDMA
    kde: Optional[KernelDensity] = None

    # from https://github.com/ITM-Soartech/itm-api/issues/3
    # The KDE variants that can be made available at this time
    # (detailed documentation for each variant coming soon):
    #   - rawscores: 1D KDE; built from raw scores of the probe choices the use
    #     made. This is the KDE that was used to compute alignment during the
    #     metric refinement eval.
    #   - globalnorm: 1d KDE; Same as rawscores but normalized across all
    #     available choices the user saw in the scenario (for instance, if the
    #     scenario only had a lowest value of 0.1 and a highest value of 0.9,
    #     this KDE would be stretched out to be from 0 to 1.
    #   - localnorm: 1D KDE; Normalized for each probe individually. I.e. did
    #     the user pick the best possible option available?
    #   - globalnormx_localnormy: A 2D KDE constructed from globalnorm and
    #     localnorm. This is the KDE that will be used to compute alignment
    #     between two decision makers
    
    kdes: Optional[dict[str, KernelDensity]] = None

    # histogram representation of raw scores
    hist: Optional[SimpleHistogram] = None

    # 0 = low confidence, 1 = high confidence
    # Deliberately vague so that different TA1 performers can use different appropriate computations
    confidence: Optional[float] = None

    confidence_reasons: Optional[List[str]] = None

    # Effective Sample size
    kde_ess: Optional[float] = None

    # Number of observations used to build the measurement
    num_observations: Optional[float] = None

    @field_serializer('kde')
    def serialize_kde(self, kde: KernelDensity, _info) -> list[float]:
        X = np.linspace(0, 1, 100)[:, np.newaxis]
        log_dens = kde.score_samples(X)
        samples = np.exp(log_dens)
        print(samples)
        return list(samples)

    class Config:
        # Allow non-pydantic KernelDensity
        arbitrary_types_allowed = True


class KDMAProfile(ps.ValidatedBaseModel):
    """

    """
    # using a dict instead of a list allows for slightly better efficiency, even though ID is redundant
    dm_id: str
    kdma_measurements: Dict[KDMAId, KDMAMeasurement]


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


# TODO I think this is unused? Verify that no one is using it and remove
# used by the alignment visualizer to show an analysis of the quality of the alignment
class AlignmentPackage(ps.ValidatedBaseModel):

    # overall alignment of one ADM to the target alignment group
    overall_alignment: float

    # 0 = low confidence, 1 = high confidence
    # Deliberately vague so that different TA1 performers can use different appropriate computations
    confidence: Optional[float] = None

    confidence_reasons: Optional[List[str]] = None

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
