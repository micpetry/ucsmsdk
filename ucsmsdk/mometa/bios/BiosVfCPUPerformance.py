"""This module contains the general information for BiosVfCPUPerformance ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class BiosVfCPUPerformanceConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_CPUPERFORMANCE_CUSTOM = "custom"
    VP_CPUPERFORMANCE_ENTERPRISE = "enterprise"
    VP_CPUPERFORMANCE_HIGH_THROUGHPUT = "high-throughput"
    VP_CPUPERFORMANCE_HPC = "hpc"
    VP_CPUPERFORMANCE_PLATFORM_DEFAULT = "platform-default"
    VP_CPUPERFORMANCE_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfCPUPerformance(ManagedObject):
    """This is BiosVfCPUPerformance class."""

    consts = BiosVfCPUPerformanceConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfCPUPerformance", "biosVfCPUPerformance", "CPU-Performance", VersionMeta.Version141i, "InputOutput", 0x1fL, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], [u'biosSettings', u'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_cpu_performance": MoPropertyMeta("vp_cpu_performance", "vpCPUPerformance", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["custom", "enterprise", "high-throughput", "hpc", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpCPUPerformance": "vp_cpu_performance", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.supported_by_default = None
        self.vp_cpu_performance = None

        ManagedObject.__init__(self, "BiosVfCPUPerformance", parent_mo_or_dn, **kwargs)
