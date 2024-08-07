from PIL import Image
import numpy as np
import scipy
import scipy.misc
import scipy.cluster

NUM_CLUSTERS = 5


def dominant_color(image_path):
  
    image = Image.open(image_path)
    image = image.resize((50, 50))
    image_array = np.asarray(image)
    image_shape = image_array.shape
    image_array = image_array.reshape(
        scipy.product(image_shape[:2]),
        image_shape[2]).astype(float)
    codes, dist = scipy.cluster.vq.kmeans(image_array, NUM_CLUSTERS)
    vecs, dist = scipy.cluster.vq.vq(image_array, codes)
    counts, bins = scipy.histogram(vecs, len(codes))
    index_max = scipy.argmax(counts)
    peak = codes[index_max]
    return tuple(peak)
