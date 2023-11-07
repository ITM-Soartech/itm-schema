from pydantic import BaseModel, Field, validator, ValidationError, Extra, validator
from typing import Optional, List
from enum import Enum
import json


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
    

class StateSetting(BaseModel):
    """
    Contains text descriptions of various settings.
    """
    
    initial_setting: Optional[str] = Field(default=None,
                    description="Background info about the scenario.")
    current_setting: Optional[str] = Field(default=None,
                    description="Background info about current set of probes.")
    casualty_setting: Optional[str] = Field(default=None,
       description="Brief description of casualties that are currently being triaged.")
    

# Depreciated: Use kdma_ids.KDMAId instead
class KDMA_name(str, Enum):
    """
    Depreciated: Use kdma_ids.KDMAId instead
    Possible KDMA names.
    """
    # TODO standardize casing- first letter upper case?
    denial = "denial"
    mission = "mission"
    Knowledge = "Knowledge"


class KDMA(ValidatedBaseModel):
    """
    Single KDMA value with values between 0 and 10
    """
    kdma: KDMA_name  # TODO rename to "name" or something
    # -1 means masked
    value: float = Field(ge=0, le=10)


class MissionType(str, Enum):
    """
    Enumeration over different mission objectives.
    """
    protect_mvp = "ProtectMVP"
    deliver_cargo = "DeliverCargo"
    defend_base = "DefendBase"
    protect_civilians = "ProtectCivilians"
    other = "Other"


class Mission(ValidatedBaseModel):
    """
    Text description of mission, and enum mission type.
    """
    unstructured: str = Field(description="Text description of state.")
    mission_type: MissionType = Field(description="Mission objective")


class ThreatType(str, Enum):
    """
    Enum over different possible types of threats.
    """
    gunshots = "gunshots"
    shelling = "shelling"


class Threat(ValidatedBaseModel):
    """
    Type and severity of threat.
    """
    threat_type: ThreatType
    severity: float = Field(
        description="Severity of threat, 0 (no threat) - 1 (max threat)",
        ge=0, le=1)


class ThreatState(ValidatedBaseModel):
    """
    Text description of threats, and list of individual threats.
    """
    unstructured: str = Field(description="Text description of current threats.")
    threats: List[Threat]


class SupplyType(str, Enum):
    """
        Enum over possible supply types.
        """
    iv_kits = "IV Kits"
    bags_of_saline = "Bags of Saline"
    fast_kit = "Fast Kit"
    junctional_tourniquets = "Junctional Tourniquets"
    combat_gauze = "Combat Gauze"
    cat_tourniquets = "CAT Tourniquets"
    pressure_dressings = "Pressure Dressings"
    bulky_dressings = "Bulky Dressings"
    over_the_needle_catheters = "Over the Needle Catheters"
    vented_chest_seals = "Vented Chest Seals"
    non_vented_chest_seals = "Non-Vented Chest Seals"
    nasal_trumpet = "Nasal Trumpet"
    oropharangeal_airway = "Oropharangeal-Airway"
    cric_kit = "Cric Kit"
    alcohol_swabs = "Alcohol Swabs"
    tranexamic_acid = "Tranexamic Acid"
    intraoss_device = "Intraoss Device"
    blood_products = "Blood Products"
    morphine = "Morphine"
    burn_kit = "Burn Kit"
    improvised_tourniquets = "Improvised Tourniquets"
    elastic_dressings = "Elastic Dressings"
    hemostatic_dressings = "Hemostatic Dressings"
    oxygen = "Oxygen"
    oral_painkillers = "Oral Painkillers"
    sam_splints = "SAM Splints"
    spinal_splints = "Spinal Splints"    


class Supply(ValidatedBaseModel):
    """
    Type and quantity of currently available supplies.
    """
    type: SupplyType
    # again, I changed this to allow negatives to make it easier to apply a delta to supplies
    # in the scene definition
    quantity: int = Field(description="Quantity (count) of supply.")


class IndividualSex(str, Enum):
    """
    Sex of individual assigned at birth.
    """
    male = "M"
    female = "F"


class IndividualRank(str, Enum):
    """
    Describes an individual's rank or importance to a given mission.
    """
    civillian = "Civilian"
    military = "Military"
    vip = "VIP"


class DemographicInfo(ValidatedBaseModel):
    """
    Demographic information about an individual.
    """
    age: int = Field(description="Age in years.")
    sex: IndividualSex
    rank: IndividualRank


class InjuryType(str, Enum):
    """
    Enum of possible types of injuries
    """
    laceration = "Laceration"
    brokenBone = "Broken Bone"
    bruising = "Bruising"
    puncture = "Puncture"
    burn = "Burn"
    amputation = "Amputation"


class InjuryLocation(str, Enum):
    """
    Enum of possible location of an injury
    """
    arm = "Arm"
    hand = "Hand"
    leg = "Leg"
    foot = "Foot"
    torso = "Torso"
    head = "Head"
    neck = "Neck"
    chest = "Chest"
    lungs = "Lungs"
    heart = "Heart"
    brain = "Brain"
    kidney = "Kidney"
    spleen = "Spleen"
    stomach = "Stomach"


class IndividualInjury(ValidatedBaseModel):
    """
    Injury class. Initial implementation is to define injuries with
    type(enum), location(enum), and severity(float,0-1). Although there are
    a large number of injuries, they really only serve as window dressing for
    conveying severity of injury. That is, we don't need to worry about
    the ability to convey the full range of injuries as long as DMs can get a
    sense of the relative severity of injuries between casualties.
    """
    injury_type: InjuryType = Field(description="enum denoting the type of injury")
    injury_location: InjuryLocation = Field(description="enum denoting the location of injury")
    injury_description: str = Field(description="additional unstructured description of injury", default="")
    injury_severity: float = Field(description="the severity of the injury, from 0-1")


class IndividualVitals(ValidatedBaseModel):
    """
    Vitals for an individual determined from Triage. Values of 0 indicate
    vitals that were not able to be measured. For example, unconscious patient cannot
    describe their level of pain, so their pain measurement would be 0.
    """
    # TODO come up with upper bounds for vitals
    # I'm planning on using this object to determine both the current vitals but also
    # the change in vitals. So, I want to allow negative values for now. I could also
    # just add each of these manually in the effect object, but then I would need to
    # update in each place if we change vitals at all
    hrpmin: int = Field(description="heart rate, beats per minute",
                        default=0)
    # TODO is this systolic or diastolic?
    mmHg: int = Field(description="blood pressure, mmHg",
                      default=0)
    spO2: int = Field(description="Blood oxygen percent",
                      default=0)
    rr: int = Field(description="Respiration rate, breaths/min",
                    default=0)
    pain: int = Field(description="Pain, 0 (no pain) - 10 (max pain)",
                      default=0)
    gc: int = Field(description="Glascow Coma Scale...",
                    default=0)


class ActionType(str, Enum):
    airway = "Airway"
    saline_lock = "Saline Lock"
    chest_seal = "Chest Seal"
    needle_decomp = "Needle Decomp"
    iv_fluids = "IV Fluids"
    tranexamic_acid = "Tranexamic Acid"
    intraoss_device = "Intraoss Device"
    blood_products = "Blood Products"
    general_assessment = "General Assessment"
    morphine = "Morphine"
    burn_kit = "Burn Kit"
    combat_gauze = "Combat Gauze"
    cat_tourniquets = "CAT Tourniquets"
    improvised_tourniquets = "Improvised Tourniquets"
    junctional_tourniquets = "Junctional Tourniquets"
    elastic_dressings = "Elastic Dressings"
    hemostatic_dressings = "Hemostatic Dressings"
    oxygen = "Oxygen"
    oral_painkillers = "Oral Painkillers"
    alcohol_swabs = "Alcohol Swabs"
    sam_splints = "SAM Splints"
    spinal_splints = "Spinal Splints"
    direct_pressure = "Direct Pressure"
    diagnose_intracranial_pressure = "Diagnose Intracranial Pressure"
    tag_green = "Add Green Tag"
    tag_red = "Add Red Tag"
    tag_yellow = "Add Yellow Tag"
    tag_black = "Add Black Tag"
    remove_tag = "Remove Tag"
    # special action for declining to take further action and
    # moving on to the next set of casualties
    other = "Other"
    no_action = "No action"


class EnvironmentType(str, Enum):
    """
    Enumeration over different environment types.
    """
    jungle = "Jungle"
    desert = "Desert"
    urban = "Urban"
    temperate = "Temperate"
    beach = "Beach"
    submarine = "Submarine"


class Environment(ValidatedBaseModel):
    """
    Information about location, environment, etc.
    """
    unstructured: str = Field(description="Text description of environment.")
    aid_delay: float = Field(
        description="Time in minutes until evac, reinforcements, extra supply"
                    "delivery, etc.", ge=0)
    humidity: float = Field(description="Humidity of environment in units of grams "
                                        "of water vapour per cubic metre of air, 0-100")
    temperature: float = Field(description="Temperature of environment in celsius, 0-100")
    time_of_day: int = Field(description="Time of day military time in minutes, 0-2400")
    day_of_year: int = Field(description="Day of year in days since beginning of year, 0-364")
    location: str = Field(description="Text description of location.")
    region_type: EnvironmentType = Field(description="Enum describing region")


# I wanted this to be more generic but it's ended up being a bit specific, some of this may need
# refactoring if we go outside of the medical triage domain
class Effect(ValidatedBaseModel):
    injuries: List[IndividualInjury] = Field(description='The injuries that this effect modifies,'
                                                         'delta of severity indicates effectiveness')
    individual_vitals: IndividualVitals = Field(description='Delta to vitals', default=IndividualVitals())


class Interaction(ValidatedBaseModel):
    action_type: ActionType = Field(description='The type of action')
    time_taken: int = Field(description='the simulated time this action was taken', default=0)
    description: str = Field(default="",
                    description="Text description of interaction with casualty")

class Action(ValidatedBaseModel):
    action_type: ActionType = Field(description='The type of action')
    duration: int = Field(description='The number of seconds this action takes')
    # most actions will have a count of 1
    # however, some actions may be 'free' (ie patient tagging)
    # and some actions may be more expensive (ie a complex procedure may use 2 actions)
    
    action_count: int = Field(default=1,
        description="If the scenario is thought of as a turn-based game, this is "
        "how many 'turns' a given actions takes.", ge=0)
    cost: List[Supply] = []
    effect: List[Effect] = []
    description: str = Field(description='Text description of action taken.',
                                    default="")
    # ideally we could stipulate which vitals to update, but I think this is good enough for now
    update_vitals: bool = Field(description='If true, update vitals for casualty',
                                default=False)

class Casualty(ValidatedBaseModel):
    """
    Collection of information about an individual casualty.
    """
    id: str = Field(description="Globally unique casualty identifier")
    name: str = Field(description="Human displayable name of casualty")
    unstructured: str = Field(description="Text description of casualty/injuries.")
    demographics: DemographicInfo
    vitals: IndividualVitals
    injuries: List[IndividualInjury] = []
    threat: float = Field(description="The level of threat to the casualty and the medic, 0-1",
                          default=0)
    probability_of_survival: float = Field(description="TRISS PoS, avg of blunt and penetrating",
                                           default=0)
    revised_trauma_score: float = Field(description="TRISS revised trauma score",
                                        default=0)
    injury_severity_score: int = Field(description="TRISS injury severity score",
                                       default=0)
    # an ordered list of actions taken on this casualty
    action_history: List[Interaction] = []

class State(ValidatedBaseModel):
    """
    Describes current state of scenario, "including casualties, supplies,
    environmental info, etc.
    """
    setting: StateSetting
    mission: Mission
    environment: Environment
    elapsed_time: int = Field(description="The number of seconds of simulated time thathave elapsed", 
                              default=0, ge=0)
    threat_state: ThreatState
    supplies: List[Supply] = []
    casualties: List[Casualty]


# TODO standardize formats of enums and properties- snake_case vs camelCase vs
# PascalCase etc
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
    state: State
    options: List[ProbeChoice]


class ProbeWrapper(Probe):
    display_scene: bool = Field(description="indicates if the intro should be shown due to a scene transition")


class Scenario(ValidatedBaseModel):
    """
    Fixed information about a scenario
    """
    name: str = Field(default=None,
                      description="Human-readable scenario name, not necessarily unique")
    id: str = Field(description="globally unique id for scenario")
    state: State


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

# TODO can this be merged into ProbeResponse???
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


class ProbeResponseBatch(ValidatedBaseModel):
    """
    Response to multiple probes sent together.
    """
    session_id: str = Field(description="Unique ID for user session.")
    responses: List[Response] = Field(description="List of probe responses")


if __name__ == "__main__":
    print(Scenario.schema_json(indent=2))
    print([x.value for x in KDMA_name])
    try:
        from pydantic.error_wrappers import ValidationError

        x = KDMA.parse_obj({"kdma": "mission2", "value": None, "extra": 4})
    except ValidationError as e:
        print(e)
    kdma_obj = KDMA.parse_obj({"kdma": "mission", "value": 2, })
    print(kdma_obj.json())
