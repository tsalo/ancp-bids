import sys

import ancpbids
import bids
from base_test_case import *

OPENNEURO_DS001734 = os.path.join(os.environ['TEST_DATASETS'], 'ds001734')

if not os.path.isdir(OPENNEURO_DS001734):
    print('test dataset not found: ' + OPENNEURO_DS001734)
    sys.exit(1)


class BenchmarkTestCase(BaseTestCase):
    def _assert_on(self, layout_type):
        layout = layout_type(OPENNEURO_DS001734)
        subjects = layout.get_subjects()
        self.assertEqual(108, len(subjects))
        self.assertEqual(0, len(layout.get_sessions()))

        bold_run1 = layout.get(suffix='bold', run='01', extension='.nii.gz', return_type='filename')
        self.assertEqual(108, len(bold_run1))

    def test_ancpbids_openneuro_ds001734(self):
        self._assert_on(ancpbids.BIDSLayout)

    def test_pybids_measure_scan_ds001734(self):
        self._assert_on(bids.BIDSLayout)
