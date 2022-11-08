#!/usr/bin/env python3

"""Unit tests for add_tag_to_filename
"""

import unittest

from ctsm import unit_testing
from unittest.mock import patch
from datetime import date

from ctsm import utils

# Allow names that pylint doesn't like, because otherwise I find it hard
# to make readable unit test names
# pylint: disable=invalid-name


class TestUtilsAddTag(unittest.TestCase):
    """Tests of utils: add_tag_to_filename"""

    @staticmethod
    def _fake_today():
        """Set the fake date to Halloween"""
        return date(year=2022, month=10, day=31)

    def testSimple(self):
        """Simple test of surface dataset name"""

        fsurf_in = "surfdata_0.9x1.25_hist_16pfts_Irrig_CMIP6_simyr2000_c221105.nc"
        with patch("ctsm.utils.date") as mock_date:
            mock_date.today.side_effect = self._fake_today

            fsurf_out = utils.add_tag_to_filename(fsurf_in, "tag")

        expect_fsurf = "surfdata_0.9x1.25_hist_16pfts_Irrig_CMIP6_simyr2000_tag_c221031.nc"
        self.assertEqual(expect_fsurf, fsurf_out, "Expect filenames to be as expected")

    def testSimpleLanduse(self):
        """Simple test of landuse dataset name"""

        landuse_in = "landuse.timeseries_0.9x1.25_hist_78pfts_CMIP6_simyr1850-2015_c190214.nc"
        with patch("ctsm.utils.date") as mock_date:
            mock_date.today.side_effect = self._fake_today

            landuse_out = utils.add_tag_to_filename(landuse_in, "tag")

        expect_landuse = "landuse.timeseries_0.9x1.25_hist_78pfts_CMIP6_simyr1850-2015_tag_c221031.nc"
        self.assertEqual(expect_landuse, landuse_out, "Expect filenames to be as expected")

    def testSimpleDatmDomain(self):
        """Simple test of datm domain dataset name"""

        file_in = "domain.lnd.360x720_gswp3.0v1.c170606.nc"
        with patch("ctsm.utils.date") as mock_date:
            mock_date.today.side_effect = self._fake_today

            file_out = utils.add_tag_to_filename(file_in, "tag")

        expect_filename = "domain.lnd.360x720_gswp3.0v1_tag_c221031.nc"
        self.assertEqual(expect_filename, file_out, "Expect filenames to be as expected")

if __name__ == "__main__":
    unit_testing.setup_for_tests()
    unittest.main()
