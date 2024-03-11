from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Optional
from enum import Enum
from itm_schema.kdma_ids import KDMAId


class ValidatedBaseModel(BaseModel):
    """
    Contains standard validation settings used for all models
    """

    model_config = ConfigDict(
        
        extra='forbid' # raise error if extra values are passed to model
    )

    

class KDMA(ValidatedBaseModel):
    """
    Single KDMA value with values between 0 and 1
    """
    kdma: KDMAId = Field(description="Name of KDMA.")
    value: float = Field(
        description="Numeric score for a given KDMA, 0-1 scale.",
        ge=0.0, le=1.0
    )


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
    target_id: Optional[str] = Field(description='Unique ID of the target')
    


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
    options: list[ProbeChoice]




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
    kdmaValues: list[KDMA] = Field(description="Computed KDMA's for decision maker.")


class AlignmentTarget(ValidatedBaseModel):
    """
    Desired profile of KDMA values for an algorithmic decision maker to align to.
    """
    id: str = Field(description="Globally unique ID for profile")
    kdma_values: list[KDMA] = Field(description='kdmas for target')

    @field_validator('kdmas')
    @classmethod
    def kdmas_are_unique(cls, kdmas: list[KDMA]) -> list[KDMA]:
        """
        Ensures there are no duplicate entries for KDMAs for a given target.

        Parameters
        ----------
        kdma_values: list[KDMA]
            list of KDMAs associated with alignment target.
        
        Returns
        ----------
        kdma_values: list[KDMA]
            Original input is returned if it is valid.
        
        Raises
        -----------
        ValueError: raised if duplicate KDMAs are found
        """

        # count kdma names to find duplicate entries
        counts = {}
        for kdma in kdmas:
            name = kdma.kdma.value
            if name not in counts:
                counts[name] = 0
            counts[name] += 1
        
        # note we keep track of all duplicates instead of raising an error
        # the first time one is found so that they can all be listed in
        # the error message.
        duplicates = {k:v for k,v in counts.items() if v > 1}

        if duplicates:
            entries = [f"{name} ({count} occurrences)"
                       for name, count in sorted(duplicates.items())]
            
            err_str = "Duplicate entries for kdma{}: {}".format(
                "" if len(entries) == 1 else "s",
                ", ".join(entries)
            )

            raise ValueError(err_str)
        
        return kdmas
            
            



class AlignmentSource(ValidatedBaseModel):
    """
    Describes which session/probe responses were used to
    compute an alignment score, allowing for lots
    of flexibility.
    """
    scenario_id: str = Field(description="Unique ID for user session.")
    probes: list[str] = Field(
        description="List of ID's of probes used to compute alignment.")


class AlignmentResults(ValidatedBaseModel):
    """
    Computed KDMA profile and alignment score for a set of decisions.
    """
    alignment_source: list[AlignmentSource]
    alignment_target_id: str = Field(
        description="ID of desired profile to align responses to.")
    score: float = Field(
        desc="Measured alignment, 0 (completely unaligned) - "
             "1 (completely aligned).",
        ge=0, le=1)
    kdma_values: list[KDMA] = Field(description="Computed KDMA profile from results")

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
