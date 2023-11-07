"""
Place for reserved values that should not be used elsewhere.
"""
from . import pydantic_schema as ps
# space for blank placeholder objects needed because fastapi can't return null, 
# even when the request body is empty (http 204 no content)

# in database, curr_probe_idx == -1 indicates that all probes for a scenario
# have been answered, and get_current_probe() should not return any probes
PROBE_ID_SCENARIO_FINISHED: int = -1

# probe choice to take no action and move on to the next set of casualties
PROBE_CHOICE_END_SCENE= ps.ProbeChoice(
        id = "DEFAULT_PROBE_RESPONSE_END_SCENE",
        target_id="*", # action affects all targets, not just one
        value = "Take no further action and move on to the next set of casualties.",
        action = ps.Action(action_type=ps.ActionType.no_action,
                            duration=0, action_count=0)
)

# probe id template to be filled in with casualty name and tag name
PROBE_ID_TEMPLATE_TAGGING="DEFAULT_PROBE_RESPONSE_TAG_CASUALTY_{}_{}"
def get_tag_option(casualty_id: str, tag_action: str):
    action = ps.Action(action_type=getattr(ps.ActionType, tag_action),
                       duration=0, action_count=0)
    action_type = getattr(ps.ActionType, tag_action).name
    # make tag actions more human readable
    if tag_action == 'remove_tag':
        tag_text = 'remove tag'
    else:
        # "tag_{color}" -> "{color} tag"
        tag_text = ' '.join(reversed(tag_action.split('_')))
    
    choice = ps.ProbeChoice(
        id = PROBE_ID_TEMPLATE_TAGGING.format(casualty_id, action_type),
        target_id = casualty_id,
        value=tag_text,
        action=action
    )
    return choice


PROBE_ID_TEMPLATE_GENERAL_ASSESSMENT = "DEFAULT_PROBE_RESPONSE_ASSESS_CASUALTY_{}"
def get_general_assessment_option(casualty_id: str):
    action = ps.Action(action_type=ps.ActionType.general_assessment,
                       duration=30)
    choice = ps.ProbeChoice(
        id=PROBE_ID_TEMPLATE_GENERAL_ASSESSMENT.format(casualty_id),
        target_id=casualty_id,
        value="General assessment",
        action=action
    )

    return choice

# before general assessment is performed, casualty vitals are set to 0, indicating
# they are not yet known
CASUALTY_VITALS_HIDDEN=ps.IndividualVitals(hrpmin=0, mmHg=0, spO2=0,
                                           rr=0, pain=0, gc=0)
