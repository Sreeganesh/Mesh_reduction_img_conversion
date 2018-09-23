#Quadratic edge decimation

This tool helps to reduce the number of faces for ply file using `meshlab` in command mode and generate `jpg` images.

##Prerequisites

* Use linux machine
* Install meshlab in your machine
* Install python 3.6 or more
* Install Blender

## Steps to run the tool

* Download the zip/tar/rar file to your machine and extract it.
* After extraction `FaceReduction` folder will be created.
* Keep all the `ply` which needs to be reduces into `input directory`.
* Change the blender path in [image_face_reduction.sh](./image_face_reduction.sh)
Below is the snapshot of the code. This path should be changed to your blender installed directory.
```
blender_path='/home/sree/Ply_conversion/blender' 
check_size 1000000
```

* After setting the path run [image_face_reduction.sh](./image_face_reduction.sh)


```
cd FaceRecution
./image_face_reduction.sh

```

## Output

After completion of the scripts, you can find the reduced `ply` files and `jpg` files in `FaceReduction/output` directory.


