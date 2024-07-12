from enum import Enum

class KDMAId(str, Enum):
    """
    KDMA Identifier Strings
    """
    # TODO make capitalization consistent
    maximization = "maximization"
    orthodoxy = "Orthodoxy"
    values = "Values"
    risk_tol = "RiskTolerance"
    negative_urgency = "NegativeUrgency"
    ambiguity_tol = "AmbiguityTolerance"
    satisficing = "Satisficing"
    deny_care = "DenyCare"
    mission_success = "MissionSuccess"
    deviate_policy = "DeviatePolicy"
    deviate_standards = "DeviateStandards"
    qol = "QualityOfLife"
    pquant = "PerceivedQuantityOfLivesSaved"
    trait_bias = "TraitBias"
    frugality = "Frugality"
    
