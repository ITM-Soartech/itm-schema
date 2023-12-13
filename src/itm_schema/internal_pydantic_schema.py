"""
Contains pydantic models for internal backend logic. These objects are not included
in the ITM public api schema shared with other TAs.
"""
from typing import Optional
from pydantic import Field, model_validator
from . import placeholders as ph
from . import pydantic_schema as ps


class Trigger(ps.ValidatedBaseModel):
    time: int = Field(description='After this amount of time in seconds, switch the scene (-1 means no trigger)',
                      default=-1)
    action_count: int = Field(description='After this number of actions, swtich the scene (-1 means no trigger)',
                              default=-1)


class Scene(ps.ValidatedBaseModel):
    """
    Situation in which participant will be given a prompt and make selections
    internal use only, defines structure of scenarios for orchestration from TA1 server
    """
    id: str = Field(description="Globally unique scene ID")
    scenario: str = Field(description="id of scenario that probe belongs to")
    type: ps.ProbeType
    prompt: str = Field(
        description="Question being asked to decision maker during probe.")
    # a list of the casualties that are present in this scene
    casualties: list[str]
    # modifications to the supplies. this precludes the ability to directly set them,
    # as this list will be used to add or subtract them and won't be determined by the
    # current amount (what if we try to subtract an amount that is greater than
    # what we have left?). As part of the computation for the new state, make sure that
    # we enforce that the number of supplies is ge 0.
    supplies: list[ps.Supply] = []
    # eventually I would like this to be generated, but for now they will be manually defined
    probes: list[ps.Probe]
    
    state: dict = Field(description="modifications to scenario state")

    @model_validator(mode='after')
    def only_actions_for_included_casualties(self):
        casualties = set([x for x in self.casualties
                          if x != ph.PROBE_CHOICE_END_SCENE.target_id])
        targets = set()
        for option in self.options:
            targets.add(option.target_id)
            if ((option.target_id not in casualties) and
                    (option.target_id != ph.PROBE_CHOICE_END_SCENE.target_id)):
                msg = ''.join((
                    f'Scenario {self.scenario} Scene {self.id} '
                    f'Choice {option.id} targets casualty {option.target_id} ',
                    'who is not included in scene casualties ',
                    f'({", ".join(sorted(casualties))})'))
                raise ValueError(msg)
        for casualty in casualties:
            if casualty not in targets:
                raise ValueError(f'No options for casualty {casualty}')
        return self


class AnnotatedProbe(ps.ValidatedBaseModel):
    """
    Probe packaged with extra info for internal/stats use.
    """
    # probe being wrapped
    probe: ps.Probe = Field(default=None,
                            description="Probe derived from initial_state")
    # additional fields
    step_idx: int = Field(default=0, ge=0,
                          description='index of step in scenario')
    scene_idx: int = Field(default=0, ge=0,
                           description='index of scene in list of scenes composing scenario.')
    scene_action_count: int = Field(default=0, ge=0,
                                    description="number of actions BEFORE response")
    scene_elapsed_time_s: int = Field(default=0, ge=0,
                                      description="Number of seconds elapsed in current scene BEFORE response")
    response: Optional[str] = Field(default=None,
                                    description="response to probe. None means no response has been submitted.")
    new_scene: Optional[bool] = Field(default=None,
                                      description="Flag for StatsProbe to indicate whether STATS should display "
                                                  "new scene info. If None this hasn't been determined yet.")
