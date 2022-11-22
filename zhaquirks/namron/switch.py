"""Device handler for a Namron four channel switch."""
from zigpy.profiles import zha
from zigpy.quirks import CustomDevice
from zigpy.zcl.clusters.general import (
    Basic,
    Groups,
    Identify,
    LevelControl,
    OnOff,
    Ota,
    PowerConfiguration,
    Scenes,
)
from zigpy.zcl.clusters.homeautomation import Diagnostic
from zigpy.zcl.clusters.lighting import Color
from zigpy.zcl.clusters.lightlink import LightLink

from zhaquirks.const import (
    BUTTON_1,
    BUTTON_2,
    BUTTON_3,
    BUTTON_4,
    BUTTON_5,
    BUTTON_6,
    BUTTON_7,
    BUTTON_8,
    CLUSTER_ID,
    COMMAND,
    COMMAND_MOVE_ON_OFF,
    COMMAND_OFF,
    COMMAND_ON,
    COMMAND_STOP_ON_OFF,
    DEVICE_TYPE,
    ENDPOINT_ID,
    ENDPOINTS,
    INPUT_CLUSTERS,
    LONG_PRESS,
    LONG_RELEASE,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PARAMS,
    PROFILE_ID,
    SHORT_PRESS,
)
from zhaquirks.namron import NAMRON


class NamronFourChSwitch(CustomDevice):
    """Custom device representing Namron four channel switch."""

    signature = {
        # <SimpleDescriptor endpoint=1, profile=260, device_type=1024,
        # device_version=0,
        # input_clusters=[0, 6, 10, 25, 1281],
        # output_clusters=[1, 32, 1280, 1282]>
        MODELS_INFO: [(NAMRON, "4512703")],
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.LEVEL_CONTROL_SWITCH,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    PowerConfiguration.cluster_id,
                    Identify.cluster_id,
                    Diagnostic.cluster_id,
                    LightLink.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    Groups.cluster_id,
                    OnOff.cluster_id,
                    Scenes.cluster_id,
                    LevelControl.cluster_id,
                    Ota.cluster_id,
                    Color.cluster_id,
                    LightLink.cluster_id,
                ],
            },
            2: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.LEVEL_CONTROL_SWITCH,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    PowerConfiguration.cluster_id,
                    Identify.cluster_id,
                    Diagnostic.cluster_id,
                    LightLink.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    Groups.cluster_id,
                    OnOff.cluster_id,
                    Scenes.cluster_id,
                    LevelControl.cluster_id,
                    Ota.cluster_id,
                    Color.cluster_id,
                    LightLink.cluster_id,
                ],
            },
            3: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.LEVEL_CONTROL_SWITCH,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    PowerConfiguration.cluster_id,
                    Identify.cluster_id,
                    Diagnostic.cluster_id,
                    LightLink.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    Groups.cluster_id,
                    OnOff.cluster_id,
                    Scenes.cluster_id,
                    LevelControl.cluster_id,
                    Ota.cluster_id,
                    Color.cluster_id,
                    LightLink.cluster_id,
                ],
            },
            4: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.LEVEL_CONTROL_SWITCH,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    PowerConfiguration.cluster_id,
                    Identify.cluster_id,
                    Diagnostic.cluster_id,
                    LightLink.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    Groups.cluster_id,
                    OnOff.cluster_id,
                    Scenes.cluster_id,
                    LevelControl.cluster_id,
                    Ota.cluster_id,
                    Color.cluster_id,
                    LightLink.cluster_id,
                ],
            },
        },
    }

    replacement = {
        ENDPOINTS: {
            1: {
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    PowerConfiguration.cluster_id,
                    Identify.cluster_id,
                    Diagnostic.cluster_id,
                    LightLink.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    Groups.cluster_id,
                    OnOff.cluster_id,
                    Scenes.cluster_id,
                    LevelControl.cluster_id,
                    Ota.cluster_id,
                    Color.cluster_id,
                    LightLink.cluster_id,
                ],
            },
            2: {
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    PowerConfiguration.cluster_id,
                    Identify.cluster_id,
                    Diagnostic.cluster_id,
                    LightLink.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    Groups.cluster_id,
                    OnOff.cluster_id,
                    Scenes.cluster_id,
                    LevelControl.cluster_id,
                    Ota.cluster_id,
                    Color.cluster_id,
                    LightLink.cluster_id,
                ],
            },
            3: {
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    PowerConfiguration.cluster_id,
                    Identify.cluster_id,
                    Diagnostic.cluster_id,
                    LightLink.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    Groups.cluster_id,
                    OnOff.cluster_id,
                    Scenes.cluster_id,
                    LevelControl.cluster_id,
                    Ota.cluster_id,
                    Color.cluster_id,
                    LightLink.cluster_id,
                ],
            },
            4: {
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    PowerConfiguration.cluster_id,
                    Identify.cluster_id,
                    Diagnostic.cluster_id,
                    LightLink.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    Groups.cluster_id,
                    OnOff.cluster_id,
                    Scenes.cluster_id,
                    LevelControl.cluster_id,
                    Ota.cluster_id,
                    Color.cluster_id,
                    LightLink.cluster_id,
                ],
            },
        }
    }

    device_automation_triggers = {
        (SHORT_PRESS, BUTTON_1): {
            COMMAND: COMMAND_ON,
            CLUSTER_ID: 6,
            ENDPOINT_ID: 1,
        },
        (LONG_PRESS, BUTTON_1): {
            COMMAND: COMMAND_MOVE_ON_OFF,
            CLUSTER_ID: 8,
            ENDPOINT_ID: 1,
            PARAMS: {"move_mode": 0, "rate": 50},
        },
        (LONG_RELEASE, BUTTON_1): {
            COMMAND: COMMAND_STOP_ON_OFF,
            CLUSTER_ID: 8,
            ENDPOINT_ID: 1,
        },
        (SHORT_PRESS, BUTTON_2): {
            COMMAND: COMMAND_OFF,
            CLUSTER_ID: 6,
            ENDPOINT_ID: 1,
        },
        (LONG_PRESS, BUTTON_2): {
            COMMAND: COMMAND_MOVE_ON_OFF,
            CLUSTER_ID: 8,
            ENDPOINT_ID: 1,
            PARAMS: {"move_mode": 1, "rate": 50},
        },
        (LONG_RELEASE, BUTTON_2): {
            COMMAND: COMMAND_STOP_ON_OFF,
            CLUSTER_ID: 8,
            ENDPOINT_ID: 1,
        },
        (SHORT_PRESS, BUTTON_3): {
            COMMAND: COMMAND_ON,
            CLUSTER_ID: 6,
            ENDPOINT_ID: 2,
        },
        (LONG_PRESS, BUTTON_3): {
            COMMAND: COMMAND_MOVE_ON_OFF,
            CLUSTER_ID: 8,
            ENDPOINT_ID: 2,
            PARAMS: {"move_mode": 0, "rate": 50},
        },
        (LONG_RELEASE, BUTTON_3): {
            COMMAND: COMMAND_STOP_ON_OFF,
            CLUSTER_ID: 8,
            ENDPOINT_ID: 2,
        },
        (SHORT_PRESS, BUTTON_4): {
            COMMAND: COMMAND_OFF,
            CLUSTER_ID: 6,
            ENDPOINT_ID: 2,
        },
        (LONG_PRESS, BUTTON_4): {
            COMMAND: COMMAND_MOVE_ON_OFF,
            CLUSTER_ID: 8,
            ENDPOINT_ID: 2,
            PARAMS: {"move_mode": 1, "rate": 50},
        },
        (LONG_RELEASE, BUTTON_4): {
            COMMAND: COMMAND_STOP_ON_OFF,
            CLUSTER_ID: 8,
            ENDPOINT_ID: 2,
        },
        (SHORT_PRESS, BUTTON_5): {
            COMMAND: COMMAND_ON,
            CLUSTER_ID: 6,
            ENDPOINT_ID: 3,
        },
        (LONG_PRESS, BUTTON_5): {
            COMMAND: COMMAND_MOVE_ON_OFF,
            CLUSTER_ID: 8,
            ENDPOINT_ID: 3,
            PARAMS: {"move_mode": 0, "rate": 50},
        },
        (LONG_RELEASE, BUTTON_5): {
            COMMAND: COMMAND_STOP_ON_OFF,
            CLUSTER_ID: 8,
            ENDPOINT_ID: 3,
        },
        (SHORT_PRESS, BUTTON_6): {
            COMMAND: COMMAND_OFF,
            CLUSTER_ID: 6,
            ENDPOINT_ID: 3,
        },
        (LONG_PRESS, BUTTON_6): {
            COMMAND: COMMAND_MOVE_ON_OFF,
            CLUSTER_ID: 8,
            ENDPOINT_ID: 3,
            PARAMS: {"move_mode": 1, "rate": 50},
        },
        (LONG_RELEASE, BUTTON_6): {
            COMMAND: COMMAND_STOP_ON_OFF,
            CLUSTER_ID: 8,
            ENDPOINT_ID: 3,
        },
        (SHORT_PRESS, BUTTON_7): {
            COMMAND: COMMAND_ON,
            CLUSTER_ID: 6,
            ENDPOINT_ID: 4,
        },
        (LONG_PRESS, BUTTON_7): {
            COMMAND: COMMAND_MOVE_ON_OFF,
            CLUSTER_ID: 8,
            ENDPOINT_ID: 4,
            PARAMS: {"move_mode": 0, "rate": 50},
        },
        (LONG_RELEASE, BUTTON_7): {
            COMMAND: COMMAND_STOP_ON_OFF,
            CLUSTER_ID: 8,
            ENDPOINT_ID: 4,
        },
        (SHORT_PRESS, BUTTON_8): {
            COMMAND: COMMAND_OFF,
            CLUSTER_ID: 6,
            ENDPOINT_ID: 4,
        },
        (LONG_PRESS, BUTTON_8): {
            COMMAND: COMMAND_MOVE_ON_OFF,
            CLUSTER_ID: 8,
            ENDPOINT_ID: 4,
            PARAMS: {"move_mode": 1, "rate": 50},
        },
        (LONG_RELEASE, BUTTON_8): {
            COMMAND: COMMAND_STOP_ON_OFF,
            CLUSTER_ID: 8,
            ENDPOINT_ID: 4,
        },
    }
