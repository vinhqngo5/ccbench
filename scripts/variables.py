# Array of event names and special requirements
EVENTS = {
    "STORE_ON_MODIFIED": {
        "cores": 2,
        "event_id": 0,
        "which_core_to_get_result": 1

    },
    "STORE_ON_MODIFIED_NO_SYNC": {
        "cores": 2,
        "event_id": 1,
        "which_core_to_get_result": 1

    },
    "STORE_ON_EXCLUSIVE": {
        "cores": 2,
        "event_id": 2,
        "which_core_to_get_result": 1

    },
    "STORE_ON_SHARED": {
        "cores": 3,
        "event_id": 3,
        "which_core_to_get_result": 1,
        "distance_setting": {
            "same_core": "-x1 -y257 -z3",
            "same_ccx": "-x1 -y263 -z3",
            "same_ccd": "-x1 -y271 -z3",
            "same_socket": "-x1 -y383 -z3",
            "2_sockets": "-x1 -y499 -z3"
        }
    },
    "STORE_ON_OWNED_MINE": {
        "cores": 2,
        "event_id": 4,
        "which_core_to_get_result": 1

    },
    "STORE_ON_OWNED": {
        "cores": 2,
        "event_id": 5,
        "which_core_to_get_result": 1

    },
    "STORE_ON_INVALID": {
        "cores": 2,
        "event_id": 6,
        "which_core_to_get_result": 0

    },
    "LOAD_FROM_MODIFIED": {
        "cores": 2,
        "event_id": 7,
        "which_core_to_get_result": 1

    },
    "LOAD_FROM_EXCLUSIVE": {
        "cores": 2,
        "event_id": 8,
        "which_core_to_get_result": 1

    },
    "LOAD_FROM_SHARED": {
        "cores": 3,
        "event_id": 9,
        "which_core_to_get_result": 2,
        "distance_setting": {
            "same_core": "-x1 -y3 -z257",
            "same_ccx": "-x1 -y3 -z263",
            "same_ccd": "-x1 -y3 -z271",
            "same_socket": "-x1 -y3 -z383",
            "2_sockets": "-x1 -y3 -z499"
        }
    },
    "LOAD_FROM_OWNED": {
        "cores": 3,
        "event_id": 10,
        "which_core_to_get_result": 2,
        "distance_setting": {
            "same_core": "-x1 -y3 -z257",
            "same_ccx": "-x1 -y3 -z263",
            "same_ccd": "-x1 -y3 -z271",
            "same_socket": "-x1 -y3 -z383",
            "2_sockets": "-x1 -y3 -z499"
        }

    },
    "LOAD_FROM_INVALID": {
        "cores": 2,
        "event_id": 11,
        "which_core_to_get_result": 0

    },
    "CAS": {
        "cores": 2,
        "event_id": 12,

    },
    "FAI": {
        "cores": 2,
        "event_id": 13,

    },
    "TAS": {
        "cores": 2,
        "event_id": 14,

    },
    "SWAP": {
        "cores": 2,
        "event_id": 15,

    },
    "CAS_ON_MODIFIED": {
        "cores": 2,
        "event_id": 16,
        "which_core_to_get_result": 1

    },
    "FAI_ON_MODIFIED": {
        "cores": 2,
        "event_id": 17,
        "which_core_to_get_result": 1

    },
    "TAS_ON_MODIFIED": {
        "cores": 2,
        "event_id": 18,
        "which_core_to_get_result": 1
    },
    "SWAP_ON_MODIFIED": {
        "cores": 2,
        "event_id": 19,
        "which_core_to_get_result": 1
    },
    "CAS_ON_SHARED": {
        "cores": 3,
        "event_id": 20,
        "which_core_to_get_result": 1,
        "distance_setting": {
            "same_core": "-x1 -y257 -z3",
            "same_ccx": "-x1 -y263 -z3",
            "same_ccd": "-x1 -y271 -z3",
            "same_socket": "-x1 -y383 -z3",
            "2_sockets": "-x1 -y499 -z3"
        }
    },
    "FAI_ON_SHARED": {
        "cores": 3,
        "event_id": 21,
        "which_core_to_get_result": 1,
        "distance_setting": {
            "same_core": "-x1 -y257 -z3",
            "same_ccx": "-x1 -y263 -z3",
            "same_ccd": "-x1 -y271 -z3",
            "same_socket": "-x1 -y383 -z3",
            "2_sockets": "-x1 -y499 -z3"
        }
    },
    "TAS_ON_SHARED": {
        "cores": 3,
        "event_id": 22,
        "which_core_to_get_result": 1,
        "distance_setting": {
            "same_core": "-x1 -y257 -z3",
            "same_ccx": "-x1 -y263 -z3",
            "same_ccd": "-x1 -y271 -z3",
            "same_socket": "-x1 -y383 -z3",
            "2_sockets": "-x1 -y499 -z3"
        }
    },
    "SWAP_ON_SHARED": {
        "cores": 3,
        "event_id": 23,
        "which_core_to_get_result": 1,
        "distance_setting": {
            "same_core": "-x1 -y257 -z3",
            "same_ccx": "-x1 -y263 -z3",
            "same_ccd": "-x1 -y271 -z3",
            "same_socket": "-x1 -y383 -z3",
            "2_sockets": "-x1 -y499 -z3"
        }
    },
    "CAS_CONCURRENT": {
        "cores": 2,
        "event_id": 24,

    },
    "FAI_ON_INVALID": {
        "cores": 2,
        "event_id": 25,

    },
    "LOAD_FROM_L1": {
        "cores": 2,
        "event_id": 26,
        "which_core_to_get_result": 0
    },
    "LOAD_FROM_MEM_SIZE": {
        "cores": 2,
        "event_id": 27,

    },
    "LFENCE": {
        "cores": 2,
        "event_id": 28,

    },
    "SFENCE": {
        "cores": 2,
        "event_id": 29,

    },
    "MFENCE": {
        "cores": 2,
        "event_id": 30,

    },
    "PROFILER": {
        "cores": 2,
        "event_id": 31,

    },
    "PAUSE": {
        "cores": 2,
        "event_id": 32,

    },
    "NOP": {
        "cores": 2,
        "event_id": 33,

    },
}

DEFAULT_DISTANCE_SETTINGS = {
    "same_core": "-x1 -y257",
    "same_ccx": "-x1 -y263",
    "same_ccd": "-x1 -y271",
    "same_socket": "-x1 -y383",
    "2_sockets": "-x1 -y499"
}

DEFAULT_CORES = 2
DEFAULT_CORE_TO_GET_RESULT = 1
