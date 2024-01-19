from pydantic import BaseModel, Field, validator, ValidationError, Extra, validator
from typing import Optional, List
from enum import Enum
import json
from ta3_schema import Action


class ValidatedBaseModel(BaseModel):
    """
    Contains standard validation settings used for all models
    """

    class Config:
        # don't allow undefined/extra attributes
        extra=Extra.forbid
        # validate new values if they are assined with model.field = new_value
        validate_assignment=True

    # private fields may be stored in json/yaml files from which pydantic objects
    # are derived, but should never be included in the schema
    @validator('private', '_private', check_fields=False)
    @classmethod
    def exclude_private_fields(cls, v):
        raise ValidationError('private fields not allowed')
    

# Depreciated: Use kdma_ids.KDMAId instead
class KDMA_name(str, Enum):
    """
    Depreciated: Use kdma_ids.KDMAId instead
    Possible KDMA names.
    """
    MAXIMIZATION = "maximization"

class KDMA(ValidatedBaseModel):
    """
    Single KDMA value with values between 0 and 10
    """
    kdma: KDMA_name  # TODO rename to "name" or something
    # -1 means masked
    value: float = Field(ge=0.0, le=1.0)


class ProbeType(str, Enum):
    """
    Describes the type of probe being asked (multiple choice, patient ordering, etc)
    """
    patient_interaction = 'PatientInteraction'
    multiple_choice = 'MultipleChoice'
    free_response = 'FreeResponse'
    patient_ordering = 'PatientOrdering'


class ProbeChoice(ValidatedBaseModel):
    id: str = Field(description='Unique ID for choice')
    value: str = Field(description='Text description of decision.')
    target_id: str = Field(description='Unique ID of the target')
    action: Action = Field(description='Action which this choice represents')


class Probe(ValidatedBaseModel):
    """
    Individual prompt that a decision maker must respond to.
    """
    id: str = Field(description="Globally unique probe ID")
    scenario: str = Field(description="id of scenario that probe belongs to")
    type: ProbeType
    prompt: str = Field(
        description="Question being asked to decision maker during probe.")
    # TODO instead of empty dict to denote no change in state, should be null
    options: List[ProbeChoice]




class ScenarioResults(ValidatedBaseModel):
    """
    Computed results for decision maker after responding to
    probes in a given scenario.

    Includes the scenario id, the id of the alignment kdma target profile,
    the alignment score, and the computed KDMA values for the decision
    maker.
    """
    scenario_id: str
    alignment_target_id: str
    alignment_score: float = Field(description=
                                   "Alignment between decisions and alignment target KDMA's."
                                   "0 (no alignment) - 1 (perfect alignment)", ge=0, le=1)
    kdmaValues: List[KDMA] = Field(description="Computed KDMA's for decision maker.")


class AlignmentTarget(ValidatedBaseModel):
    """
    Desired profile of KDMA values for an algorithmic decision maker to align to.
    """
    id: str = Field(description="Globally unique ID for profile")
    kdma_values: List[KDMA]


class AlignmentSource(ValidatedBaseModel):
    """
    Describes which session/probe responses were used to
    compute an alignment score, allowing for lots
    of flexibility.
    """
    scenario_id: str = Field(description="Unique ID for user session.")
    probes: List[str] = Field(
        description="List of ID's of probes used to compute alignment.")


class AlignmentResults(ValidatedBaseModel):
    """
    Computed KDMA profile and alignment score for a set of decisions.
    """
    alignment_source: List[AlignmentSource]
    alignment_target_id: str = Field(
        description="ID of desired profile to align responses to.")
    score: float = Field(
        desc="Measured alignment, 0 (completely unaligned) - "
             "1 (completely aligned).",
        ge=0, le=1)
    kdma_values: List[KDMA] = Field(description="Computed KDMA profile from results")

# Probe responses
class Response(ValidatedBaseModel):
    """
    Response to a single probe.
    Contains probe id, choice id, and optional justification of response.
    """
    scenario_id: str = Field(description="Unique ID for scenario.")
    probe_id: str = Field(description="ID of probe that response is for")
    choice: str = Field(description="string ID of choice made, or, "
                                    "for ordering problems, comma-separated string of"
                                    "id's of ordered choices.")
    justification: Optional[str] = Field(default=None,
                                         description="Optional free text justification of response to "
                                                     "provide additional context.")


class ProbeResponse(ValidatedBaseModel):
    """
    Response to an individual probe.
    """
    session_id: str = Field(description="Unique ID for user session.")
    response: Response = Field(description="The response")



class ProbeResponseTableEntry(ValidatedBaseModel):
    """
    Object to store all fields in probe response on top level,
    and contain extra fields like timestamp
    """
    pass
    
    


if __name__ == "__main__":
    pass