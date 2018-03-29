#!/usr/bin/env python3
# Modified from:
# https://gist.githubusercontent.com/gab50000/4ce3a2c59e5100a5f21338292fb96aa3/raw/722cb4a1d656279e260b52d3d62740d0a138f1fc/filter.py
 
import os
import sys
import argparse
import json
from copy import deepcopy

def contained_tags(list_of_tags, cell):
    if "tags" not in cell["metadata"]:
        return []
    return [tag for tag in list_of_tags if tag in cell["metadata"]["tags"]]
        


def read_notebook(fname):
    with open(fname, "r") as f:
        data = json.load(f)
    return data


def write_notebook(fname,data):
  with open(fname, "w+") as f:
        json.dump(data, f)





def filter_notebook_ie(data,include_tags=None,exclude_tags=None,
                       return_idx=True,return_data=True):

    if return_data == True: data = deepcopy(data)

    if include_tags:
      include_idx = filter_notebook_data(data,include_tags,
                                         exclude=False,return_idx=True)
    else:
      include_idx = []

    if exclude_tags:
      exclude_idx = filter_notebook_data(data,exclude_tags,
                                         exclude=False,return_idx=True)
    else:
      exclude_idx = []


    keepidx = include_idx + exclude_idx
   
    if return_data == False:
      return keepidx
    else:
      result = []
      for cell_it,cell in enumerate(data["cells"]):
        if cell_it in keepidx:
          result.append(cell)
      data['cells'] = result

    return keepidx,data


def filter_notebook_data(data, list_of_tags, exclude=False,return_idx=False):

    if return_idx==False: data = deepcopy(data)

    include = not exclude
    result = []
    for cell_it,cell in enumerate(data["cells"]):
        if any(contained_tags(list_of_tags, cell)):
            if include:
                if return_idx:
                  result.append(cell_it)
                else:
                  result.append(cell)
        elif exclude:
            if return_idx:
              result.append(cell_it)
            else:
              result.append(cell)

    if return_idx:
      return result
    else:
      data["cells"] = result
      return data





"""
def main():
    parser = argparse.ArgumentParser("Filter Notebook using tags")
    parser.add_argument("file", help="Jupyter Notebook file")
    parser.add_argument("tags", nargs="+", help="List of tags")
    parser.add_argument("--exclude", action="store_true", help="Exclude list of tags")
    parser.set_defaults()
    args = parser.parse_args()

    result = filter_notebook(args.file, args.tags, args.exclude)
    
    fname, fext = os.path.splitext(args.file)
    new_fname = fname + "-filtered" + fext

    write_notebook(new_fname,result)


if __name__ == "__main__":
    main()

"""
