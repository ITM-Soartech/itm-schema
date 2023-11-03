"""
Contains pydantic models for endpoints for endpoints for STATS server for TA1
data collect. These objects are not included in the ITM public api schema shared with
other TAs.
"""
from pydantic import Field
from itm_schema import pydantic_schema as ps


class StatsProbe(ps.Probe):
    display_scene: bool = Field(
        description="indicates if the intro should be shown due to a scene transition")