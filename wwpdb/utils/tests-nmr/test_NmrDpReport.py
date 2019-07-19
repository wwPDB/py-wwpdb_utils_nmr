import unittest
import os
import sys
import json

from wwpdb.utils.nmr.NmrDpReport import NmrDpReport, NmrDpReportInputSource, NmrDpReportSequenceAlignment, NmrDpReportChainAssignment, NmrDpReportError, NmrDpReportWarning
from testfixtures import LogCapture

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
        self.report.input_sources[0].setItemValue('content_type', 'nmr-unified-data-nef')
        self.report.input_sources[0].setItemValue('content_subtype', {'poly_seq': 1, 'chem_shift': 1, 'dist_restraint': 2})

        with self.assertRaises(IndexError):
            self.report.input_sources[1].setItemValue('file_type', 'pdbx')

        self.report.appendInputSource()

        self.report.input_sources[1].setItemValue('file_type', 'pdbx')
        self.report.input_sources[1].setItemValue('content_type', 'model')
        self.report.input_sources[1].setItemValue('content_subtype', {'poly_seq': 1, 'coordinate': 1})

        self.report.sequence_alignment.setItemValue('model_poly_seq_vs_nmr_poly_seq', 'foo');
        self.report.chain_assignment.setItemValue('model_poly_seq_vs_nmr_poly_seq', 'foo');

        self.report.warning.appendDescription('missing_content', 'foo')
        self.report.setWarning()

        self.assertEqual(self.report.isOk(), False)
        self.assertEqual(self.report.isError(), False)

        self.report.error.appendDescription('format_issue', 'foo')
        self.report.setError()

        self.assertEqual(self.report.isOk(), False)
        self.assertEqual(self.report.isError(), True)

        self.report.get()

        result = json.dumps(self.report.get(), sort_keys=True)
        answer = json.dumps(json.loads('{"corrected_warning": null, "error": {"anomalous_data": null, "duplicated_index": null, "format_issue": ["foo"], "internal_error": null, "invalid_ambiguity_code": null, "invalid_atom_nomenclature": null, "invalid_atom_type": null, "invalid_data": null, "invalid_isotope_number": null, "missing_mandatory_content": null, "missing_mandatory_item": null, "missing_data": null, "multiple_data": null, "sequence_mismatch": null, "total": 1}, "information": {"cyclic_polymer": false, "chain_assignments": {"model_poly_seq_vs_nmr_poly_seq": "foo", "nmr_poly_seq_vs_model_poly_seq": null}, "diamagnetic": true, "disulfide_bond": false, "input_sources": [{"content_subtype": {"chem_shift": 1, "dist_restraint": 2, "poly_seq": 1}, "content_type": "nmr-unified-data-nef", "disulfide_bond": null, "file_name": null, "file_type": "nef", "non_standard_residue": null, "other_bond": null, "polymer_sequence": null, "polymer_sequence_in_loop": null, "stats_of_exptl_data": null}, {"content_subtype": {"coordinate": 1, "poly_seq": 1}, "content_type": "model", "disulfide_bond": null, "file_name": null, "file_type": "pdbx", "non_standard_residue": null, "other_bond": null, "polymer_sequence": null, "polymer_sequence_in_loop": null, "stats_of_exptl_data": null}], "sequence_alignments": {"model_poly_seq_vs_coordinate": null, "model_poly_seq_vs_nmr_poly_seq": "foo", "nmr_poly_seq_vs_model_poly_seq": null, "nmr_poly_seq_vs_chem_shift": null, "nmr_poly_seq_vs_dihed_restraint": null, "nmr_poly_seq_vs_dist_restraint": null, "nmr_poly_seq_vs_rdc_restraint": null, "nmr_poly_seq_vs_spectral_peak": null}, "other_bond": false, "status": "Error"}, "warning": {"atom_nomenclature_mismatch": null, "ccd_mismatch": null, "disordered_index": null, "enum_failure": null, "missing_content": ["foo"], "missing_data": null, "missing_saveframe": null, "remarkable_data": null, "sequence_mismatch": null, "skipped_lp_category": null, "skipped_sf_category": null, "suspicious_data": null, "total": 1, "unsufficient_data": null, "unusual_data": null}}'), sort_keys=True)

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

class TestNmrDpChainAssignment(unittest.TestCase):

    def setUp(self):
        self.chain_assignment = NmrDpReportChainAssignment()
        pass

    def tearDown(self):
        pass

    def test_setitemvalue(self):
        for item in self.chain_assignment.items:
            self.chain_assignment.setItemValue(item, 'foo')

        with LogCapture() as logs:
            with self.assertRaises(KeyError):
                self.chain_assignment.setItemValue('unknown', 'foo')

        for item in self.chain_assignment.items:
            self.assertEqual(self.chain_assignment.get()[item], 'foo')

class TestNmrDpError(unittest.TestCase):

    def setUp(self):
        self.error = NmrDpReportError()
        pass

    def tearDown(self):
        pass

    def test_setitemvalue(self):
        for item in self.error.items:
            self.error.appendDescription(item, 'foo')

        with LogCapture() as logs:
            with self.assertRaises(KeyError):
                self.error.appendDescription('unknown', 'foo')

        for item in self.error.items:
            self.assertEqual(self.error.get()[item], ['foo'])

        for item in self.error.items:
            self.error.appendDescription(item, 'foo2')

        for item in self.error.items:
            self.assertEqual(self.error.get()[item], ['foo','foo2'])

class TestNmrDpWarning(unittest.TestCase):

    def setUp(self):
        self.warning = NmrDpReportWarning()
        pass

    def tearDown(self):
        pass

    def test_setitemvalue(self):
        for item in self.warning.items:
            self.warning.appendDescription(item, 'foo')

        with LogCapture() as logs:
            with self.assertRaises(KeyError):
                self.warning.appendDescription('unknown', 'foo')

        for item in self.warning.items:
            self.assertEqual(self.warning.get()[item], ['foo'])

        for item in self.warning.items:
            self.warning.appendDescription(item, 'foo2')

        for item in self.warning.items:
            self.assertEqual(self.warning.get()[item], ['foo', 'foo2'])

if __name__ == '__main__':
    unittest.main()
