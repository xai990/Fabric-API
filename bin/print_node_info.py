#!/usr/bin/env python3

from set_env import set_env_vars
from fabrictestbed_extensions.fablib.fablib import FablibManager as fablib_manager

if __name__ == '__main__':
    set_env_vars()
    fablib = fablib_manager()

    print(fablib.show_config())

    # print the node information
    try:
        slice = fablib.get_slice(name="MySlice")
        for node in slice.get_nodes():
            print(f"{node}")
    except Exception as e:
        print(f"Exception: {e}")
