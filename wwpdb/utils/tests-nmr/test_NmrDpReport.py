import unittest
import os
import sys
import logging
import json

from wwpdb.utils.nmr.NmrDpReport import NmrDpReport, NmrDpReportInputSource, NmrDpReportSequenceAlignment, NmrDpReportError, NmrDpReportWarning
from testfixtures import LogCapture

logger = logging.getLogger('')

class TestNmrDpReport(unittest.TestCase):

    def setUp(self):
        self.report = NmrDpReport()
        pass

    def tearDown(self):
        pass

    def test_init(self):
        self.assertEqual(self.report.isOk(), True)
        self.assertEqual(self.report.isError(), False)

    def test_report_generation(self):
        self.report.input_sources[0].setItemValue('file_type', 'nef')
        self.report.input_sources[0].setItemValue('content_type', 'nmr-unified-data')
        self.report.input_sources[0].setItemValue('content_subtype', {'poly_seq': 1, 'chem_shift': 1, 'dist_restraint': 2})

        with self.assertRaises(IndexError):
            self.report.input_sources[1].setItemValue('file_type', 'pdbx')

        self.report.addInputSource()

        self.report.input_sources[1].setItemValue('file_type', 'pdbx')
        self.report.input_sources[1].setItemValue('content_type', 'model')
        self.report.input_sources[1].setItemValue('content_subtype', {'poly_seq': 1, 'coordinate': 1})

        self.report.sequence_alignment.setItemValue('coordinate_vs_poly_seq', 'foo');

        self.report.warning.addDescription('missing_content', 'foo')
        self.report.setWarning()

        self.assertEqual(self.report.isOk(), False)
        self.assertEqual(self.report.isError(), False)

        self.report.error.addDescription('format_issue', 'foo')
        self.report.setError()

        self.assertEqual(self.report.isOk(), False)
        self.assertEqual(self.report.isError(), True)

        self.report.get()

        result = json.dumps(self.report.get(), sort_keys=True)
        answer = json.dumps(json.loads('{"error": {"anomalous_data": null, "duplicated_chem_shift": null, "duplicated_index": null, "format_issue": "foo", "internal_error": null, "invalid_ambiguity_code": null, "invalid_atom_nomenclature": null, "invalid_atom_type": null, "invalid_data": null, "invalid_isotope_number": null, "missing_mandatory_content": null, "missing_mandatory_item": null, "multiple_data": null, "sequence_mismatch": null}, "information": {"input_sources": [{"content_subtype": {"chem_shift": 1, "dist_restraint": 2, "poly_seq": 1}, "content_type": "nmr-unified-data", "file_name": null, "file_type": "nef", "non_standard_residue": null, "polymer_sequence": null, "polymer_sequence_in_loop": null, "sequence_coverage_by_exptl_data": null, "statistics_of_exptl_data": null}, {"content_subtype": {"coordinate": 1, "poly_seq": 1}, "content_type": "model", "file_name": null, "file_type": "pdbx", "non_standard_residue": null, "polymer_sequence": null, "polymer_sequence_in_loop": null, "sequence_coverage_by_exptl_data": null, "statistics_of_exptl_data": null}], "sequence_alignments": {"coordinate_vs_poly_seq": "foo", "poly_seq_vs_chem_shift": null, "poly_seq_vs_dihed_restraint": null, "poly_seq_vs_dist_restraint": null, "poly_seq_vs_rdc_restraint": null, "poly_seq_vs_spectral_peak": null}, "status": "ERROR"}, "warning": {"disordered_index": null, "missing_content": "foo", "missing_data": null, "missing_saveframe": null, "sequence_mismatch": null, "suspicious_data": null}}'), sort_keys=True)

        self.assertEqual(result, answer)

        with LogCapture() as logs:
            with self.assertRaises(UserWarning):
                self.report.setWarning()

class TestNmrDpInputSource(unittest.TestCase):

    def setUp(self):
        self.input_source = NmrDpReportInputSource()
        pass

    def tearDown(self):
        pass

    def test_setitemvalue(self):
        for item in set(self.input_source.items) - {'file_type', 'content_type', 'content_subtype'}:
            self.input_source.setItemValue(item, 'foo')

        for file_type in self.input_source.file_types:
            self.input_source.setItemValue('file_type', file_type)

        with LogCapture() as logs:
            with self.assertRaises(KeyError):
                self.input_source.setItemValue('unknown', 'foo')

        with LogCapture() as logs:
            with self.assertRaises(ValueError):
                self.input_source.setItemValue('file_type', 'unknown')

        for content_type in self.input_source.content_types:
            self.input_source.setItemValue('content_type', content_type)

        with LogCapture() as logs:
            with self.assertRaises(ValueError):
                self.input_source.setItemValue('content_type', 'unknown')

        for content_subtype in self.input_source.content_subtypes:
            self.input_source.setItemValue('content_subtype', {content_subtype: 1})

        with LogCapture() as logs:
            with self.assertRaises(AttributeError):
                self.input_source.setItemValue('content_subtype', 'unknown')

        with LogCapture() as logs:
            with self.assertRaises(AttributeError):
                self.input_source.setItemValue('content_subtype', ['unknown'])

        with LogCapture() as logs:
            with self.assertRaises(ValueError):
                self.input_source.setItemValue('content_subtype', {'unknown': 1})

        with LogCapture() as logs:
            with self.assertRaises(ValueError):
                self.input_source.setItemValue('content_subtype', {'chem_shift': 'unknown'})

        self.input_source.setItemValue('content_subtype', {'poly_seq': 1, 'chem_shift': 0})
        self.assertEqual(self.input_source.get()['content_subtype'], {'poly_seq': 1})

class TestNmrDpSequenceAlignment(unittest.TestCase):

    def setUp(self):
        self.sequence_alignment = NmrDpReportSequenceAlignment()
        pass

    def tearDown(self):
        pass

    def test_setitemvalue(self):
        for item in self.sequence_alignment.items:
            self.sequence_alignment.setItemValue(item, 'foo')

        with LogCapture() as logs:
            with self.assertRaises(KeyError):
                self.sequence_alignment.setItemValue('unknown', 'foo')

        for item in self.sequence_alignment.items:
            self.assertEqual(self.sequence_alignment.get()[item], 'foo')

class TestNmrDpError(unittest.TestCase):

    def setUp(self):
        self.error = NmrDpReportError()
        pass

    def tearDown(self):
        pass

    def test_setitemvalue(self):
        for item in self.error.items:
            self.error.addDescription(item, 'foo')

        with LogCapture() as logs:
            with self.assertRaises(KeyError):
                self.error.addDescription('unknown', 'foo')

        for item in self.error.items:
            self.assertEqual(self.error.get()[item], 'foo')

        for item in self.error.items:
            self.error.addDescription(item, 'foo2')

        for item in self.error.items:
            self.assertEqual(self.error.get()[item], 'foo\nfoo2')

class TestNmrDpWarning(unittest.TestCase):

    def setUp(self):
        self.warning = NmrDpReportWarning()
        pass

    def tearDown(self):
        pass

    def test_setitemvalue(self):
        for item in self.warning.items:
            self.warning.addDescription(item, 'foo')

        with LogCapture() as logs:
            with self.assertRaises(KeyError):
                self.warning.addDescription('unknown', 'foo')

        for item in self.warning.items:
            self.assertEqual(self.warning.get()[item], 'foo')

        for item in self.warning.items:
            self.warning.addDescription(item, 'foo2')

        for item in self.warning.items:
            self.assertEqual(self.warning.get()[item], 'foo\nfoo2')

if __name__ == '__main__':
    unittest.main()
