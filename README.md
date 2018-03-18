# Imgcluster

quick start to cluster an equal number of different images according to their spectral similarity with the SIFT algorithm

```python
import sys
sys.path.append('imgcluster')
from imgcluster import *
from utils import *

images_per_group = 5

sample_imgs('imgs', 'images', images_per_group)

img_dir = 'images'
c = do_cluster(img_dir, images_per_group, algorithm='SIFT',
               print_metrics=True)

with open('cluster_obj.pkl', 'wb') as output:
    pickle.dump(c, output, pickle.HIGHEST_PROTOCOL)
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

