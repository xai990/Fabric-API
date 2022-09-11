#!/usr/bin/env python3

from set_env import set_env_vars
from fabrictestbed_extensions.fablib.fablib import FablibManager as fablib_manager


if __name__ == '__main__':
    fablib = fablib_manager()
    print(fablib.show_config())

    #upload data
    """
    try:
        node = slice.get_node(name="Node1")
        # upload file API parameters
        # local_file_path (str) – the path to the file to upload
        # remote_file_path (str) – the destination path of the file on the node
        node.upload_file(<local_file_path>, <remote_file_path>)
    except Exception as e:
        print(f"Exception: {e}")
    """


    # download data
    """
    try:
        node = slice.get_node(name="Node1")
        # download file API parameters
        # local_file_path (str) – the destination path for the remote file
        # remote_file_path (str) – the path to the remote file to download
        node.download_file(<local_file_path>, <remote_file_path>)

    except Exception as e:
        print(f"Exception: {e}")
    """
