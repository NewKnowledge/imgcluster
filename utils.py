
import os
import shutil
import imghdr
import numpy as np


def sample_imgs(image_dirs, target_dir, sample_size):
    # clean up target imgs
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    os.makedirs(target_dir)
    # path to images to be sampled

    for image_dir in os.listdir(image_dirs):
        # confirm directory
        if not os.path.isdir(os.path.join(image_dirs, image_dir)):
            continue
        # get image names
        images = os.listdir(os.path.join(image_dirs, image_dir))
        # check img type
        image_type = list(
            map(imghdr.what,
                [os.path.join(image_dirs, image_dir, img_file)
                    for img_file in images]))
        # todo if needed: convert to jpg
        # save jpegs only for now
        images = [d for (d, keep) in zip(images, image_type) if keep == 'jpeg']

        # shuffle and sample
        img_idx = np.arange(len(images))
        np.random.shuffle(img_idx)

        images = [images[i] for i in img_idx[:sample_size]]

        # move images to target dir
        for img_file in images:
            shutil.copyfile(os.path.join(image_dirs, image_dir, img_file),
                            os.path.join(target_dir, img_file))
