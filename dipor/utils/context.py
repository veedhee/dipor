import os
from functools import reduce
from collections import OrderedDict

from dipor.jinja.extensions import RoutesExtension

def get_structural_context(prefix, app_name, content_root):
    ctx = {}
    directory = OrderedDict()

    rootdir = os.path.join(prefix, content_root)
    start = content_root.rstrip(os.sep).rfind(os.sep) + 1

    for path, dirs, files in os.walk(rootdir):
        path = os.path.relpath(path, prefix)
        folders = path[start:].split(os.sep)
        subdir = {}
        if '_branches' in folders:
            folders.remove('_branches')
        parent = reduce(dict.get, folders[:-1], directory)
        parent[folders[-1]] = subdir
    processed_path = process_paths(directory['content'])
    return processed_path

def process_paths(directory, prefix="", is_subpath=False):
    ## this is the default path. allow overriding later
    route_dir = {}
    for k, v in directory.items():
        if not v:
            # directory[k] = (prefix+"/"+k, None)
            route_dir[prefix+"/"+k] = (k, None)
        else:
            sub_paths = process_paths(v, prefix="/"+k, is_subpath=True)
            # directory[k] =("/"+k, sub_paths)
            route_dir["/"+k] = (k, sub_paths)
    if is_subpath:
        return route_dir

    final_route = {'/': ('home', route_dir)}
    return final_route

        