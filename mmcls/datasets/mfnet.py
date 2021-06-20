import numpy as np

from .base_dataset import BaseDataset
from .builder import DATASETS


@DATASETS.register_module()
class MFNet(BaseDataset):
    """`Molecular Formula`_ Dataset.

    """

    IMG_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.ppm', '.bmp', '.pgm', '.tif')
    CLASSES = [
        'none',
        'molecular formula',
        'uncertain'
    ]

    def __init__(self,
                 data_prefix,
                 pipeline,
                 classes=None,
                 ann_file=None,
                 test_mode=False,
                 with_class_balance=False):
        super(MFNet, self).__init__(data_prefix, pipeline, classes, ann_file, test_mode)
        self.with_class_balance = with_class_balance

    def load_annotations(self):
        if isinstance(self.ann_file, str):
            with open(self.ann_file) as f:
                self.samples = [x.strip().split(' ') for x in f.readlines()]
        else:
            raise TypeError('ann_file must be a str or None')

        data_infos = []
        for filename, gt_label in self.samples:
            info = {'img_prefix': self.data_prefix}
            info['img_info'] = {'filename': filename}
            info['gt_label'] = np.array(gt_label, dtype=np.int64)
            data_infos.append(info)
        return data_infos

    def get_cat_ids(self, idx):
        if self.with_class_balance:
            return [int(self.data_infos[idx]['gt_label'])]
        return super(MFNet, self).get_cat_ids(idx)
