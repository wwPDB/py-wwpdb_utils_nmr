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

    def test_init_state(self):
        self.assertEqual(self.report.isOk(), True)
        self.assertEqual(self.report.isError(), False)

        self.report.input_sources[0].setItemValue('format_type', 'nmr-nef')
        self.report.input_sources[0].setItemValue('content_type', 'nmr-unified-data')
        self.report.input_sources[0].setItemValue('content_subtype', {'poly_seq': 1, 'chem_shift': 1, 'dist_restraint': 2})

        with self.assertRaises(IndexError):
            self.report.input_sources[1].setItemValue('format_type', 'pdbx')

        self.report.addInputSource()

        self.report.input_sources[1].setItemValue('format_type', 'pdbx')
        self.report.input_sources[1].setItemValue('content_type', 'model')
        self.report.input_sources[1].setItemValue('content_subtype', {'poly_seq': 1, 'coordinate': 1})

        self.report.sequence_alignment.setItemValue('coordinate_vs_poly_seq', 'foo');

        self.report.warning.setItemValue('missing_content', 'foo')
        self.report.setWarning()

        self.assertEqual(self.report.isOk(), False)
        self.assertEqual(self.report.isError(), False)

        self.report.error.setItemValue('format_issue', 'foo')
        self.report.setError()

        self.assertEqual(self.report.isOk(), False)
        self.assertEqual(self.report.isError(), True)

        self.report.get()

        result = json.dumps(self.report.get(), sort_keys=True)
        answer = json.dumps(json.loads('{"information": {"status": "ERROR", "input_sources": [{"content_subtype": {"chem_shift": 1, "poly_seq": 1, "dist_restraint": 2}, "non_standard_residue": null, "file_name": null, "polymer_sequence": null, "statistics_of_exptl_data": null, "content_type": "nmr-unified-data", "polymer_sequence_in_loop": null, "sequence_coverage_by_exptl_data": null, "polymer_sequence_id": null, "polymer_sequence_id_in_loop": null, "format_type": "nmr-nef"}, {"content_subtype": {"coordinate": 1, "poly_seq": 1}, "non_standard_residue": null, "file_name": null, "polymer_sequence": null, "statistics_of_exptl_data": null, "content_type": "model", "polymer_sequence_in_loop": null, "sequence_coverage_by_exptl_data": null, "polymer_sequence_id": null, "polymer_sequence_id_in_loop": null, "format_type": "pdbx"}], "sequence_alignments": {"poly_seq_vs_dist_restraint": null, "poly_seq_vs_rdc_restraint": null, "poly_seq_vs_dihed_restraint": null, "poly_seq_vs_spectral_peak": null, "coordinate_vs_poly_seq": "foo", "poly_seq_vs_chem_shift": null}}, "warning": {"missing_content": "foo", "blanked_item": null, "missing_item": null, "suspicious_data": null, "sequence_mismatche": null, "missing_saveframe": null}, "error": {"anomalous_data": null, "missing_mandatory_content": null, "invalid_ambiguity_code": null, "blanked_mandatory_value": null, "format_issue": "foo", "invalid_atom_type": null, "invalid_atom_isotope_number": null, "duplicated_data": null, "missing_mandatory_item": null, "sequence_mismatche": null, "invalid_atom_nomenclature": null}}'), sort_keys=True)

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
        for item in set(self.input_source.items) - {'format_type', 'content_type', 'content_subtype'}:
            self.input_source.setItemValue(item, 'foo')

        for format_type in self.input_source.format_types:
            self.input_source.setItemValue('format_type', format_type)

        with LogCapture() as logs:
            with self.assertRaises(KeyError):
                self.input_source.setItemValue('unknown', 'foo')

        with LogCapture() as logs:
            with self.assertRaises(ValueError):
                self.input_source.setItemValue('format_type', 'unknown')

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
            self.error.setItemValue(item, 'foo')

        with LogCapture() as logs:
            with self.assertRaises(KeyError):
                self.error.setItemValue('unknown', 'foo')

        for item in self.error.items:
            self.assertEqual(self.error.get()[item], 'foo')

class TestNmrDpWarning(unittest.TestCase):

    def setUp(self):
        self.warning = NmrDpReportWarning()
        pass

    def tearDown(self):
        pass

    def test_setitemvalue(self):
        for item in self.warning.items:
            self.warning.setItemValue(item, 'foo')

        with LogCapture() as logs:
            with self.assertRaises(KeyError):
                self.warning.setItemValue('unknown', 'foo')

        for item in self.warning.items:
            self.assertEqual(self.warning.get()[item], 'foo')

if __name__ == '__main__':
    unittest.main()
