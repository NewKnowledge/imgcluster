# Imgcluster

quick start to cluster an equal number of different images according to their spectral similarity with the SIFT algorithm

```python
import sys
import os
import pandas as pd
import pickle
sys.path.append('imgcluster')
from imgcluster import *
from utils import *

# how many images do you want to sample from each bin?
images_per_group = 10

# sample images
sample_imgs('imgs', 'images', images_per_group)

# run clustering algo
img_dir = 'images'
c, sim_mat = do_cluster(img_dir, images_per_group, algorithm='SIFT',
                        print_metrics=True)

# save important stuff as pickle files
with open('cluster_groups.pkl', 'wb') as output:
    pickle.dump(c, output, pickle.HIGHEST_PROTOCOL)

with open('cluster_matrix.pkl', 'wb') as output:
    pickle.dump(sim_mat, output, pickle.HIGHEST_PROTOCOL)

""" This could take _a while_. You can run the script to this point and 
	then resume later on by loading the pickle files like so:
"""
# pick it up after the similarity computation:
# c = pickle.load(open('cluster_obj.pkl', 'rb'))
# sim_mat = pickle.load(open('cluster_matrix.pkl', 'rb'))

# make a dataframe of the cluster membership predictions
img_files = [item for item in os.listdir(img_dir) if not item.startswith('.')]
label_map = pd.DataFrame(list(zip(img_files, c.tolist())),
                         columns=['filename', 'group'])
label_map = label_map.infer_objects()
label_map = label_map.sort_values('group')

# sort the images based on cluster membership
sort_imgs(label_map, img_dir)
```

# Imgcluster - Forked from llvll
### Image clustering using the similarity algorithms: SIFT, SSIM, CW-SSIM, MSE

This project aims to implement the clustering of images by utilizing *Spectral Clustering* and *Affinity Propagation Clustering* together with a number of similarity algorithms, like: 

 * SIFT: Scale-invariant Feature Transform
 * SSIM: Structural Similarity Index
 * CW-SSIM: Complex Wavelet Structural Similarity Index
 * MSE: Mean Squared Error

The best clustering results are selected according to the calculated performance metrics for clustering:

 * Silhouette Coefficient
 * Completeness Score
 * Homogeneity Score

IPython Notebook (.ipynb file) is included for step-by-step execution of the demo application with extra comments.

The project is using *OpenCV 3.1*, *Scikit-Learn*, *Scikit-Image* and *PySSIM* for image manipulations, similarity measurements and clustering.

All images have been downloaded from the free-of-charge online service Pixabay: https://pixabay.com

Any kind of copyrights, ownership rights or distribution rights have been considered according to the information, which
is available on Pixabay.

Please feel free to ask any questions: oleg.v.puzanov@gmail.com

