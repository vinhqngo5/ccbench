# Array of event names and special requirements
EVENTS = {
    "STORE_ON_MODIFIED": {
        "core": 2,
        "event_id": 0,

    },
    "STORE_ON_MODIFIED_NO_SYNC": {
        "core": 2,
        "event_id": 1,

    },
    "STORE_ON_EXCLUSIVE": {
        "core": 2,
        "event_id": 2,

    },
    "STORE_ON_SHARED": {
        "core": 2,
        "event_id": 3,

    },
    "STORE_ON_OWNED_MINE": {
        "core": 2,
        "event_id": 4,

    },
    "STORE_ON_OWNED": {
        "core": 2,
        "event_id": 5,

    },
    "STORE_ON_INVALID": {
        "core": 2,
        "event_id": 6,

    },
    "LOAD_FROM_MODIFIED": {
        "core": 2,
        "event_id": 7,

    },
    "LOAD_FROM_EXCLUSIVE": {
        "core": 2,
        "event_id": 8,

    },
    "LOAD_FROM_SHARED": {
        "core": 2,
        "event_id": 9,

    },
    "LOAD_FROM_OWNED": {
        "core": 2,
        "event_id": 10,

    },
    "LOAD_FROM_INVALID": {
        "core": 2,
        "event_id": 11,

    },
    "CAS": {
        "core": 2,
        "event_id": 12,

    },
    "FAI": {
        "core": 2,
        "event_id": 13,

    },
    "TAS": {
        "core": 2,
        "event_id": 14,

    },
    "SWAP": {
        "core": 2,
        "event_id": 15,

    },
    "CAS_ON_MODIFIED": {
        "core": 2,
        "event_id": 16,

    },
    "FAI_ON_MODIFIED": {
        "core": 2,
        "event_id": 17,

    },
    "TAS_ON_MODIFIED": {
        "core": 2,
        "event_id": 18,

    },
    "SWAP_ON_MODIFIED": {
        "core": 2,
        "event_id": 19,

    },
    "CAS_ON_SHARED": {
        "core": 2,
        "event_id": 20,

    },
    "FAI_ON_SHARED": {
        "core": 2,
        "event_id": 21,

    },
    "TAS_ON_SHARED": {
        "core": 2,
        "event_id": 22,

    },
    "SWAP_ON_SHARED": {
        "core": 2,
        "event_id": 23,

    },
    "CAS_CONCURRENT": {
        "core": 2,
        "event_id": 24,

    },
    "FAI_ON_INVALID": {
        "core": 2,
        "event_id": 25,

    },
    "LOAD_FROM_L1": {
        "core": 2,
        "event_id": 26,

    },
    "LOAD_FROM_MEM_SIZE": {
        "core": 2,
        "event_id": 27,

    },
    "LFENCE": {
        "core": 2,
        "event_id": 28,

    },
    "SFENCE": {
        "core": 2,
        "event_id": 29,

    },
    "MFENCE": {
        "core": 2,
        "event_id": 30,

    },
    "PROFILER": {
        "core": 2,
        "event_id": 31,

    },
    "PAUSE": {
        "core": 2,
        "event_id": 32,

    },
    "NOP": {
        "core": 2,
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
DEFAULT_CORE_TO_GET_RESULT= 1