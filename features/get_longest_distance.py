import cv2
import matplotlib.pyplot as plt
from fil_finder import FilFinder2D
import astropy.units as u

def get_longest_distance(img):
    skeleton = cv2.imread(img, 0) #in numpy array format
    fil = FilFinder2D(skeleton, distance=250 * u.pc, mask=skeleton)
    fil.preprocess_image(flatten_percent=85)
    fil.create_mask(border_masking=True, verbose=False, use_existing_mask=True)
    fil.medskel(verbose=False)
    fil.analyze_skeletons(branch_thresh=40 * u.pix, skel_thresh=10 * u.pix, prune_criteria='length')

    plt.imshow(fil.skeleton, cmap='gray')
    plt.contour(fil.skeleton_longpath, colors='r')
    plt.axis('off')
    # plt.show()
    return fil.lengths()[0]
