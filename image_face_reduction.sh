#!/bin/bash
set -x
function check_size() {
    cur_dir=`pwd`
    for file in ${cur_dir}/input/*.ply
    do
        if [[ -f ${file} ]]; then
            current_face_value=`head -20 ${file} | grep -a 'element face' | cut -d' ' -f3`
        fi

        if [[ ${current_face_value} -gt 1000000 ]]; then
            just_file_name=$(basename ${file})
            just_file_name=`echo ${just_file_name} | cut -d'.' -f1`
            out_file=${just_file_name}_reduced.ply
            python3 reduce_faces.py --input_file ${file} --output_file ${cur_dir}/output/${out_file} --face_value $1
            #blender -b -P mesh2img.py -- --paths ${cur_dir}/output/${out_file} --dimensions 800 -i jpg
        else
            cp ${file} ${cur_dir}/output/
            #blender -b -P mesh2img.py -- --paths D:/Ganesh_Work/plyFiles/ --dimensions 800 -i jpg
        fi
    done
    export PATH=$PATH:${blender_path}
    blender -b -P mesh2img.py -- --paths  ${cur_dir}/output/ --dimensions 800 -i jpg
}

blender_path='/home/sree/Ply_conversion/blender'
check_size 1000000
