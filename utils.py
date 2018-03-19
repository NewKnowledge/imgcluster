
import os
import shutil
import imghdr
import numpy as np


def sample_imgs(image_dirs, target_dir, sample_size):
    """ Take a directory full of sub-directories full of images, a target
        directory, and a sample size and move n randomly sampled images into
        the target directory.
    """

    # clean up target imgs
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    os.makedirs(target_dir)

    all_imgs = list()

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
        all_imgs.append(images)

        # move images to target dir
        for img_file in images:
            shutil.copyfile(os.path.join(image_dirs, image_dir, img_file),
                            os.path.join(target_dir, img_file))

    # TODO: save labels
    # {filename: [os.listdir(target_dir)], labels = 


def sort_imgs(label_map, target_dir):
    if os.path.exists('output'):
        shutil.rmtree('output')
    os.makedirs('output')
    for folder_path in range(0, max(label_map.ix[:, 'group'])):
        full_folder_path = os.path.join('output', str(folder_path))
        os.makedirs(full_folder_path)

        for i in label_map[label_map['group'] == folder_path].filename:
            shutil.move(os.path.join(target_dir, i), 
                        os.path.join('output', str(folder_path), i))



    
