__author__ = "Minghao Gou"
__version__ = "1.0"

import argparse
from rgb_matters.data.utils.gen_label import (
    gen_scene_label, parallel_gen_scene_label, parallel_gen_camera_label
)
from rgb_matters.constant import GRASPNET_ROOT, LABEL_DIR

if __name__ == "__main__":

    # parallel_gen_scene_label(
    #     graspnet_root=GRASPNET_ROOT,
    #     scene_ids=list(range(5,190)),
    #     dump_folder=LABEL_DIR,
    #     proc=6,
    # )
    parallel_gen_camera_label(
        graspnet_root=GRASPNET_ROOT,
        scene_ids=list(range(0,5)),
        camera="kinect",
        dump_folder=LABEL_DIR,
        proc=6,
    )
