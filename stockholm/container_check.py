def in_container() -> bool:
    with open("/proc/1/attr/current", "rb") as f:
        return f.read().find(b"container_t") != -1
