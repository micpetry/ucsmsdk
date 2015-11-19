"""This module contains the general information for LstorageLunClone ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LstorageLunCloneConsts():
    pass


class LstorageLunClone(ManagedObject):
    """This is LstorageLunClone class."""

    consts = LstorageLunCloneConsts()
    naming_props = set([])

    mo_meta = MoMeta("LstorageLunClone", "lstorageLunClone", "lun-clone", VersionMeta.Version302a, "InputOutput", 0x7fL, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage", "ls-storage-policy", "read-only"], [u'lstorageSanScsiLun'], [], [None])

    prop_meta = {
        "array_name": MoPropertyMeta("array_name", "arrayName", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x1L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "backstore_dn": MoPropertyMeta("backstore_dn", "backstoreDn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302a, MoPropertyMeta.INTERNAL, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "lun_name": MoPropertyMeta("lun_name", "lunName", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x8L, 0, 510, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "partition_name": MoPropertyMeta("partition_name", "partitionName", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "arrayName": "array_name", 
        "backstoreDn": "backstore_dn", 
        "childAction": "child_action", 
        "dn": "dn", 
        "lunName": "lun_name", 
        "name": "name", 
        "partitionName": "partition_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.array_name = None
        self.backstore_dn = None
        self.child_action = None
        self.lun_name = None
        self.name = None
        self.partition_name = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "LstorageLunClone", parent_mo_or_dn, **kwargs)
