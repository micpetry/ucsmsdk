"""This module contains the general information for SwUtilityDomainFsmStage ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class SwUtilityDomainFsmStageConsts():
    LAST_UPDATE_TIME_ = ""
    NAME_DEPLOY_BEGIN = "DeployBegin"
    NAME_DEPLOY_FAIL = "DeployFail"
    NAME_DEPLOY_SUCCESS = "DeploySuccess"
    NAME_DEPLOY_UPDATE_CONNECTIVITY = "DeployUpdateConnectivity"
    NAME_NOP = "nop"
    STAGE_STATUS_FAIL = "fail"
    STAGE_STATUS_IN_PROGRESS = "inProgress"
    STAGE_STATUS_NOP = "nop"
    STAGE_STATUS_PENDING = "pending"
    STAGE_STATUS_SKIP = "skip"
    STAGE_STATUS_SUCCESS = "success"
    STAGE_STATUS_THROTTLED = "throttled"


class SwUtilityDomainFsmStage(ManagedObject):
    """This is SwUtilityDomainFsmStage class."""

    consts = SwUtilityDomainFsmStageConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("SwUtilityDomainFsmStage", "swUtilityDomainFsmStage", "stage-[name]", VersionMeta.Version211a, "OutputOnly", 0x7L, [], [""], [u'swUtilityDomainFsm'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x1L, 0, 256, None, [], []), 
        "last_update_time": MoPropertyMeta("last_update_time", "lastUpdateTime", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [""], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, None, None, None, None, ["DeployBegin", "DeployFail", "DeploySuccess", "DeployUpdateConnectivity", "nop"], []), 
        "order": MoPropertyMeta("order", "order", "ushort", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "retry": MoPropertyMeta("retry", "retry", "byte", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "stage_status": MoPropertyMeta("stage_status", "stageStatus", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["fail", "inProgress", "nop", "pending", "skip", "success", "throttled"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x4L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "lastUpdateTime": "last_update_time", 
        "name": "name", 
        "order": "order", 
        "retry": "retry", 
        "rn": "rn", 
        "sacl": "sacl", 
        "stageStatus": "stage_status", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.last_update_time = None
        self.order = None
        self.retry = None
        self.sacl = None
        self.stage_status = None
        self.status = None

        ManagedObject.__init__(self, "SwUtilityDomainFsmStage", parent_mo_or_dn, **kwargs)
