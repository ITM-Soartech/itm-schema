from enum import Enum


#   TODO make sure to update the following site with the current KDMAs
#        we selected maximization as our sole KDMA for the current iteration,
#        but it is not yet listed:
#   https://soartech.sharepoint.us/:x:/r/sites/DARPA-ITM/_layouts/15/Doc.aspx?sourcedoc=%7B44D255B3-C829-4144-85C0-35AF300C3D81%7D&file=ITM%20Survey%20Mapping%20Template.xlsx&action=default&mobileredirect=true
class KDMAId(str, Enum):
    """
    Names of currently supported KDMAs
    """
    MAXIMIZATION = "maximization"
    