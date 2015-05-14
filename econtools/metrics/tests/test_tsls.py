from os import path

import pandas as pd

from metrics.util.testing import RegCompare
from metrics.othregs import tsls
from data.src_tsls import tsls_std, tsls_robust, tsls_cluster


class TslsCompare(RegCompare):

    def __init__(self):
        super(TslsCompare, self).__init__()
        self.precision['F'] = 8
        self.precision['pF'] = 8
        self.precision['CI_high'] = 4
        self.precision['ssr'] = 2   # ssr gets weird in 2SLS
        self.precision['mss'] = 2   # ssr gets weird in 2SLS

    def test_r2(self):
        pass

    def test_r2_a(self):
        pass


class TestTsls_std(TslsCompare):

    @classmethod
    def setup_class(cls):
        """Stata reg output from `sysuse auto; reg price mpg`"""
        test_path = path.split(path.relpath(__file__))[0]
        auto_path = path.join(test_path, 'data', 'auto.dta')
        autodata = pd.read_stata(auto_path)
        y = 'price'
        x_end = ['mpg', 'length']
        z = ['trunk', 'weight']
        x_exog = []
        cls.result = tsls(autodata, y, x_end, z, x_exog, addcons=True)
        cls.expected = tsls_std


class TestTsls_hc1(TslsCompare):

    @classmethod
    def setup_class(cls):
        """Stata reg output from `sysuse auto; reg price mpg`"""
        test_path = path.split(path.relpath(__file__))[0]
        auto_path = path.join(test_path, 'data', 'auto.dta')
        autodata = pd.read_stata(auto_path)
        y = 'price'
        x_end = ['mpg', 'length']
        z = ['trunk', 'weight']
        x_exog = []
        cls.result = tsls(autodata, y, x_end, z, x_exog, vce_type='hc1',
                          addcons=True)
        cls.expected = tsls_robust


class TestTsls_cluster(TslsCompare):

    @classmethod
    def setup_class(cls):
        """Stata reg output from `sysuse auto; reg price mpg`"""
        test_path = path.split(path.relpath(__file__))[0]
        auto_path = path.join(test_path, 'data', 'auto.dta')
        autodata = pd.read_stata(auto_path)
        y = 'price'
        x_end = ['mpg', 'length']
        z = ['trunk', 'weight']
        x_exog = []
        cls.result = tsls(autodata, y, x_end, z, x_exog, cluster='gear_ratio',
                          addcons=True)
        cls.expected = tsls_cluster


if __name__ == '__main__':
    import sys
    from nose import runmodule
    argv = [__file__, '-vs'] + sys.argv[1:]
    runmodule(argv=argv, exit=False)
