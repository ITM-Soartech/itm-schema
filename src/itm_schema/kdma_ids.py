from enum import Enum

# see: https://soartech.sharepoint.us/:x:/r/sites/DARPA-ITM/_layouts/15/Doc.aspx?sourcedoc=%7B44D255B3-C829-4144-85C0-35AF300C3D81%7D&file=ITM%20Survey%20Mapping%20Template.xlsx&action=default&mobileredirect=true
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
