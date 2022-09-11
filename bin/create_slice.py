#!/usr/bin/env python3

from set_env import set_env_vars
from fabrictestbed_extensions.fablib.fablib import FablibManager as fablib_manager


if __name__ == '__main__':
    set_env_vars()
    fablib = fablib_manager()
    print(fablib.show_config())
    try:
        #Create a slice
        slice = fablib.new_slice(name="MySlice")

        # Add a node
        slice.add_node(name="Node1")
        """
        # specific node resources if needed
        node1.set_capacities(cores=cores, ram=ram, disk=disk)
        node1.set_image(image)
        iface1 = node1.add_component(model='NIC_Basic', name=node_nic_name[0]).get_interfaces()[0]
        """
        slice.submit()
    except Exception as e:
        print(f"Exception: {e}")
