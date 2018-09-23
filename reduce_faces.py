#!/usr/bin/env python

import sys
import os
import subprocess
import argparse
import glob
import ntpath

# Filter parameters to reduce the number of faces from .ply file.
# (Filters > Remeshing, Simplification and Reconstruction >
# Quadric Edge Collapse Decimation, with parameters:
# 0.9 percentage reduction (10%), 0.3 Quality threshold (70%)
# Target number of faces is ignored with those parameters
# conserving face normals, planar simplification and
# post-simplimfication cleaning)
# And going to Filter > Show current filter script



def create_tmp_filter_file(expected_face_value, filename='filter_file.mlx'):
    filter_parameters = """<!DOCTYPE FilterScript>
    <FilterScript>
     <filter name="Quadric Edge Collapse Decimation">
      <Param type="RichInt" value="{expected_face_value}" name="TargetFaceNum"/>
      <Param type="RichFloat" value="0.0" name="TargetPerc"/>
      <Param type="RichFloat" value="0.3" name="QualityThr"/>
      <Param type="RichBool" value="false" name="PreserveBoundary"/>
      <Param type="RichFloat" value="1" name="BoundaryWeight"/>
      <Param type="RichBool" value="true" name="PreserveNormal"/>
      <Param type="RichBool" value="false" name="PreserveTopology"/>
      <Param type="RichBool" value="false" name="OptimalPlacement"/>
      <Param type="RichBool" value="true" name="PlanarQuadric"/>
      <Param type="RichBool" value="false" name="QualityWeight"/>
      <Param type="RichBool" value="true" name="AutoClean"/>
      <Param type="RichBool" value="false" name="Selected"/>
     </filter>
    </FilterScript>
    """
    filter_parameters = filter_parameters.format(expected_face_value=expected_face_value)
    with open('/tmp/' + filename, 'w') as f:
        f.write(filter_parameters)
    return '/tmp/' + filename


def reduce_faces(in_file, out_file, face_value):
    """
    Reduces the number of faces from .ply file.
    :param in_file:
    :param out_file:
    :param filter_script_path:
    :return:
    """
    filter_script_path = create_tmp_filter_file(face_value)
    command = "meshlabserver -i " + in_file
    # Add the filter script
    command += " -s " + filter_script_path
    # Add the output filename and output flags
    command += " -o " + out_file + " -om vn fn"
    # Execute command
    print("Started executing the command: {command}".format(command=command))
    output = subprocess.check_output(command, shell=True)
    last_line = output.splitlines()[-1]
    print("Completed the conversion")
    print('{in_file} > {out_file} : {last_line}'.format(in_file=in_file, out_file=out_file, last_line=last_line))



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Reduceíng ply file faces')
    parser.add_argument('--input_file', required=True)
    parser.add_argument('--output_file', required=True)
    parser.add_argument('--face_value', required=True)
    args = parser.parse_args()
    reduce_faces(args.input_file, args.output_file, args.face_value)




