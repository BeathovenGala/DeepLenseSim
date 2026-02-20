import matplotlib.pyplot as plt
import numpy as np
import random
import os

from deeplense.lens import DeepLens


# Number of sims
num_sim = int(5e3)

base_dir = os.path.dirname(os.path.abspath(__file__))
save_dir = os.path.join(base_dir, "../data/Model_I/cdm/")
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

for i in range(num_sim):
    lens = DeepLens()
    lens.make_single_halo(1e12)
    lens.make_old_cdm()
    lens.make_source_light()
    lens.simple_sim()
    File = lens.image_real
    np.save(save_dir + "cdm_sim_" + str(random.getrandbits(128)), File)


if False:
    plt.figure(figsize=(10, 5))
    plt.subplot(2, 2, 1)
    plt.imshow(lens.image_real)
    plt.colorbar()
    plt.subplot(2, 2, 2)
    plt.imshow(np.sqrt(lens.image_real))
    plt.colorbar()
    plt.subplot(2, 2, 3)
    plt.imshow(lens.poisson)
    plt.colorbar()
    plt.subplot(2, 2, 4)
    plt.imshow(lens.bkg)
    plt.colorbar()
    plt.show()
