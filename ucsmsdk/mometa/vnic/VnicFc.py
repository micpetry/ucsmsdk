"""This module contains the general information for VnicFc ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class VnicFcConsts():
    ADDR_DERIVED = "derived"
    ADMIN_HOST_PORT_1 = "1"
    ADMIN_HOST_PORT_2 = "2"
    ADMIN_HOST_PORT_ANY = "ANY"
    ADMIN_HOST_PORT_NONE = "NONE"
    ADMIN_VCON_1 = "1"
    ADMIN_VCON_2 = "2"
    ADMIN_VCON_3 = "3"
    ADMIN_VCON_4 = "4"
    ADMIN_VCON_ANY = "any"
    BOOT_DEV_DISABLED = "disabled"
    BOOT_DEV_ENABLED = "enabled"
    CONFIG_STATE_APPLIED = "applied"
    CONFIG_STATE_APPLYING = "applying"
    CONFIG_STATE_FAILED_TO_APPLY = "failed-to-apply"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    INST_TYPE_DEFAULT = "default"
    INST_TYPE_DYNAMIC = "dynamic"
    INST_TYPE_DYNAMIC_VF = "dynamic-vf"
    INST_TYPE_MANUAL = "manual"
    NODE_ADDR_VNIC_DERIVED = "vnic-derived"
    OPER_HOST_PORT_1 = "1"
    OPER_HOST_PORT_2 = "2"
    OPER_HOST_PORT_ANY = "ANY"
    OPER_HOST_PORT_NONE = "NONE"
    OPER_ORDER_UNSPECIFIED = "unspecified"
    OPER_SPEED_LINE_RATE = "line-rate"
    OPER_VCON_1 = "1"
    OPER_VCON_2 = "2"
    OPER_VCON_3 = "3"
    OPER_VCON_4 = "4"
    OPER_VCON_ANY = "any"
    ORDER_UNSPECIFIED = "unspecified"
    OWNER_CONN_POLICY = "conn_policy"
    OWNER_INITIATOR_POLICY = "initiator_policy"
    OWNER_LOGICAL = "logical"
    OWNER_PHYSICAL = "physical"
    OWNER_POLICY = "policy"
    OWNER_UNKNOWN = "unknown"
    PERS_BIND_DISABLED = "disabled"
    PERS_BIND_ENABLED = "enabled"
    PERS_BIND_CLEAR_FALSE = "false"
    PERS_BIND_CLEAR_NO = "no"
    PERS_BIND_CLEAR_TRUE = "true"
    PERS_BIND_CLEAR_YES = "yes"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"
    TYPE_ETHER = "ether"
    TYPE_FC = "fc"
    TYPE_IPC = "ipc"
    TYPE_SCSI = "scsi"
    TYPE_UNKNOWN = "unknown"


class VnicFc(ManagedObject):
    """This is VnicFc class."""

    consts = VnicFcConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("VnicFc", "vnicFc", "fc-[name]", VersionMeta.Version101e, "InputOutput", 0xfffffL, [], ["admin", "ls-config", "ls-server", "ls-storage"], [u'lsServer', u'vnicSanConnPolicy'], [u'fabricEthMonSrcEp', u'fabricFcMonSrcEp', u'fabricNetflowMonSrcEp', u'faultInst', u'vnicBootTarget', u'vnicFcIf', u'vnicWwpnHistory'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "adaptor_profile_name": MoPropertyMeta("adaptor_profile_name", "adaptorProfileName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2L, 0, 256, """(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", ["derived"], []), 
        "admin_cdn_name": MoPropertyMeta("admin_cdn_name", "adminCdnName", "string", VersionMeta.Version224a, MoPropertyMeta.READ_WRITE, 0x4L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "admin_host_port": MoPropertyMeta("admin_host_port", "adminHostPort", "string", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["1", "2", "ANY", "NONE"], []), 
        "admin_vcon": MoPropertyMeta("admin_vcon", "adminVcon", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["1", "2", "3", "4", "any"], []), 
        "boot_dev": MoPropertyMeta("boot_dev", "bootDev", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x20L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, """((defaultValue|not-applicable|adaptor-protected-eth-capability|vif-resources-overprovisioned|ungrouped-domain|unsupported-nvgre|unresolved-remote-vlan-name|invalid-wwn|service-profile-virtualization-conflict|unsupported-roce-netflow|unsupported-vxlan-netflow|fcoe-capacity|wwpn-derivation-virtualized-port|unresolved-vlan-name|vnic-virtualization-netflow-conflict|unsupported-vxlan-usnic|pinning-vlan-mismatch|adaptor-requirement|vnic-not-ha-ready|missing-ipv4-inband-mgmt-addr|unsupported-nvgre-dynamic-vnic|unresolved-remote-vsan-name|mac-derivation-virtualized-port|vnic-virtualization-conflict|unsupported-roce|unsupported-nvgre-netflow|vnic-vlan-assignment-error|insufficient-vhba-capacity|inaccessible-vlan|unable-to-update-ucsm|soft-pinning-vlan-mismatch|unsupported-nvgre-vmq|connection-placement|vnic-vcon-provisioning-change|missing-ipv6-inband-mgmt-addr|unsupported-nvgre-usnic|missing-primary-vlan|adaptor-fcoe-capability|vfc-vnic-pvlan-conflict|virtualization-not-supported|unsupported-vxlan|unresolved-vsan-name|insufficient-vnic-capacity|unassociated-vlan|unsupported-roce-vmq|unsupported-vxlan-vmq|dynamic-vf-vnic|wwpn-assignment|missing-ipv4-addr|unsupported-vxlan-dynamic-vnic|pinned-target-misconfig),){0,50}(defaultValue|not-applicable|adaptor-protected-eth-capability|vif-resources-overprovisioned|ungrouped-domain|unsupported-nvgre|unresolved-remote-vlan-name|invalid-wwn|service-profile-virtualization-conflict|unsupported-roce-netflow|unsupported-vxlan-netflow|fcoe-capacity|wwpn-derivation-virtualized-port|unresolved-vlan-name|vnic-virtualization-netflow-conflict|unsupported-vxlan-usnic|pinning-vlan-mismatch|adaptor-requirement|vnic-not-ha-ready|missing-ipv4-inband-mgmt-addr|unsupported-nvgre-dynamic-vnic|unresolved-remote-vsan-name|mac-derivation-virtualized-port|vnic-virtualization-conflict|unsupported-roce|unsupported-nvgre-netflow|vnic-vlan-assignment-error|insufficient-vhba-capacity|inaccessible-vlan|unable-to-update-ucsm|soft-pinning-vlan-mismatch|unsupported-nvgre-vmq|connection-placement|vnic-vcon-provisioning-change|missing-ipv6-inband-mgmt-addr|unsupported-nvgre-usnic|missing-primary-vlan|adaptor-fcoe-capability|vfc-vnic-pvlan-conflict|virtualization-not-supported|unsupported-vxlan|unresolved-vsan-name|insufficient-vnic-capacity|unassociated-vlan|unsupported-roce-vmq|unsupported-vxlan-vmq|dynamic-vf-vnic|wwpn-assignment|missing-ipv4-addr|unsupported-vxlan-dynamic-vnic|pinned-target-misconfig){0,1}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["applied", "applying", "failed-to-apply", "not-applied"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40L, 0, 256, None, [], []), 
        "equipment_dn": MoPropertyMeta("equipment_dn", "equipmentDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "ident_pool_name": MoPropertyMeta("ident_pool_name", "identPoolName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, [], []), 
        "inst_type": MoPropertyMeta("inst_type", "instType", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["default", "dynamic", "dynamic-vf", "manual"], []), 
        "max_data_field_size": MoPropertyMeta("max_data_field_size", "maxDataFieldSize", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, [], ["256-2112"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x200L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "node_addr": MoPropertyMeta("node_addr", "nodeAddr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, """(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", ["vnic-derived"], []), 
        "nw_templ_name": MoPropertyMeta("nw_templ_name", "nwTemplName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "oper_adaptor_profile_name": MoPropertyMeta("oper_adaptor_profile_name", "operAdaptorProfileName", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_cdn_name": MoPropertyMeta("oper_cdn_name", "operCdnName", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_host_port": MoPropertyMeta("oper_host_port", "operHostPort", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["1", "2", "ANY", "NONE"], []), 
        "oper_ident_pool_name": MoPropertyMeta("oper_ident_pool_name", "operIdentPoolName", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_nw_templ_name": MoPropertyMeta("oper_nw_templ_name", "operNwTemplName", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_order": MoPropertyMeta("oper_order", "operOrder", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]), 
        "oper_pin_to_group_name": MoPropertyMeta("oper_pin_to_group_name", "operPinToGroupName", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_qos_policy_name": MoPropertyMeta("oper_qos_policy_name", "operQosPolicyName", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_speed": MoPropertyMeta("oper_speed", "operSpeed", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["line-rate"], ["8-40000000"]), 
        "oper_stats_policy_name": MoPropertyMeta("oper_stats_policy_name", "operStatsPolicyName", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_vcon": MoPropertyMeta("oper_vcon", "operVcon", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["1", "2", "3", "4", "any"], []), 
        "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x800L, None, None, None, ["unspecified"], ["0-256"]), 
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["conn_policy", "initiator_policy", "logical", "physical", "policy", "unknown"], []), 
        "pers_bind": MoPropertyMeta("pers_bind", "persBind", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1000L, None, None, None, ["disabled", "enabled"], []), 
        "pers_bind_clear": MoPropertyMeta("pers_bind_clear", "persBindClear", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2000L, None, None, None, ["false", "no", "true", "yes"], []), 
        "pin_to_group_name": MoPropertyMeta("pin_to_group_name", "pinToGroupName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4000L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "qos_policy_name": MoPropertyMeta("qos_policy_name", "qosPolicyName", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8000L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10000L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "stats_policy_name": MoPropertyMeta("stats_policy_name", "statsPolicyName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20000L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40000L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80000L, None, None, None, ["A", "B", "NONE"], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ether", "fc", "ipc", "scsi", "unknown"], []), 
    }

    prop_map = {
        "adaptorProfileName": "adaptor_profile_name", 
        "addr": "addr", 
        "adminCdnName": "admin_cdn_name", 
        "adminHostPort": "admin_host_port", 
        "adminVcon": "admin_vcon", 
        "bootDev": "boot_dev", 
        "childAction": "child_action", 
        "configQualifier": "config_qualifier", 
        "configState": "config_state", 
        "dn": "dn", 
        "equipmentDn": "equipment_dn", 
        "fltAggr": "flt_aggr", 
        "identPoolName": "ident_pool_name", 
        "instType": "inst_type", 
        "maxDataFieldSize": "max_data_field_size", 
        "name": "name", 
        "nodeAddr": "node_addr", 
        "nwTemplName": "nw_templ_name", 
        "operAdaptorProfileName": "oper_adaptor_profile_name", 
        "operCdnName": "oper_cdn_name", 
        "operHostPort": "oper_host_port", 
        "operIdentPoolName": "oper_ident_pool_name", 
        "operNwTemplName": "oper_nw_templ_name", 
        "operOrder": "oper_order", 
        "operPinToGroupName": "oper_pin_to_group_name", 
        "operQosPolicyName": "oper_qos_policy_name", 
        "operSpeed": "oper_speed", 
        "operStatsPolicyName": "oper_stats_policy_name", 
        "operVcon": "oper_vcon", 
        "order": "order", 
        "owner": "owner", 
        "persBind": "pers_bind", 
        "persBindClear": "pers_bind_clear", 
        "pinToGroupName": "pin_to_group_name", 
        "qosPolicyName": "qos_policy_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "statsPolicyName": "stats_policy_name", 
        "status": "status", 
        "switchId": "switch_id", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.adaptor_profile_name = None
        self.addr = None
        self.admin_cdn_name = None
        self.admin_host_port = None
        self.admin_vcon = None
        self.boot_dev = None
        self.child_action = None
        self.config_qualifier = None
        self.config_state = None
        self.equipment_dn = None
        self.flt_aggr = None
        self.ident_pool_name = None
        self.inst_type = None
        self.max_data_field_size = None
        self.node_addr = None
        self.nw_templ_name = None
        self.oper_adaptor_profile_name = None
        self.oper_cdn_name = None
        self.oper_host_port = None
        self.oper_ident_pool_name = None
        self.oper_nw_templ_name = None
        self.oper_order = None
        self.oper_pin_to_group_name = None
        self.oper_qos_policy_name = None
        self.oper_speed = None
        self.oper_stats_policy_name = None
        self.oper_vcon = None
        self.order = None
        self.owner = None
        self.pers_bind = None
        self.pers_bind_clear = None
        self.pin_to_group_name = None
        self.qos_policy_name = None
        self.sacl = None
        self.stats_policy_name = None
        self.status = None
        self.switch_id = None
        self.type = None

        ManagedObject.__init__(self, "VnicFc", parent_mo_or_dn, **kwargs)
