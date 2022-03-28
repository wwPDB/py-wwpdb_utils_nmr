##
# File: test_NmrDpReport.py
# Date:  29-Jul-2019  M. Yokochi
#
# Updates:
# 09-Oct-2019  M. Yokochi - add 'enum_failure_ignorable' warning type
# 15-Oct-2019  M. Yokochi - add 'encouragement' waring type
# 27-Jan-2020  M. Yokochi - change warning type 'enum_failure' to 'enum_mismatch'
# 05-Feb-2020  M. Yokochi - move conflicted_data error to warning
# 21-Feb-2020  M. Yokochi - update content-type definitions
# 13-Mar-2020  M. Yokochi - change warning type from suspicious_data to anomalous_data
# 18-Mar-2020  M. Yokochi - rename warning type from skipped_sf/lp_category to skipped_saveframe/loop_category
# 23-Mar-2020  M. Yokochi - add 'anomalous_chemical_shift' and 'unusual_chemical_shift' warning types
# 19 Apr-2020  M. Yokochi - add 'not_superimposed_model' warning type (DAOTHER-4060)
# 20 Apr-2020  M. Yokochi - add 'concatenated_sequence' warning type (DAOTHER-5594)
# 22-Apr-2020  M. Yokochi - add 'ambiguity_code_mismatch' warning type (DAOTHER-5601)
# 25-Apr-2020  M. Yokochi - add 'corrected_format_issue' warning type (DAOTHER-5611)
# 27-Apr-2020  M. Yokochi - add 'auth_atom_nomenclature_mismatch' warning type (DAOTHER-5611)
# 15-May-2020  M. Yokochi - add 'content_mismatch' error for NMR legacy deposition (DAOTHER-5687)
# 25-Jun-2020  M. Yokochi - add 'anomalous_bond_length' warning
# 16-Mov-2021  M. Yokochi - add 'original_file_name' (DAOTHER-7478)
# 27-Jan-2022  M. Yokochi - add restraint types described by XPLOR-NIH, CNS, CYANA, and AMBER systems (NMR restraint remediation)
# 04-Mar-2022  M. Yokochi - add coordinate geometry restraint (DAOTHER-7690, NMR restraint remediation)
##
import unittest
import json

from wwpdb.utils.nmr.NmrDpReport import NmrDpReport, NmrDpReportInputSource, NmrDpReportSequenceAlignment, NmrDpReportChainAssignment, NmrDpReportError, NmrDpReportWarning
from testfixtures import LogCapture


class TestNmrDpReport(unittest.TestCase):

    def setUp(self):
        self.report = NmrDpReport()

    def tearDown(self):
        pass

    def test_init(self):
        self.assertEqual(self.report.isOk(), True)
        self.assertEqual(self.report.isError(), False)

    def test_report_generation(self):
        self.report.input_sources[0].setItemValue('file_type', 'nef')
        self.report.input_sources[0].setItemValue('content_type', 'nmr-data-nef')
        self.report.input_sources[0].setItemValue('content_subtype', {'poly_seq': 1, 'chem_shift': 1, 'dist_restraint': 2})

        with self.assertRaises(IndexError):
            self.report.input_sources[1].setItemValue('file_type', 'pdbx')

        self.report.appendInputSource()

        self.report.input_sources[1].setItemValue('file_type', 'pdbx')
        self.report.input_sources[1].setItemValue('content_type', 'model')
        self.report.input_sources[1].setItemValue('content_subtype', {'poly_seq': 1, 'coordinate': 1})

        self.report.sequence_alignment.setItemValue('model_poly_seq_vs_nmr_poly_seq', 'foo')
        self.report.chain_assignment.setItemValue('model_poly_seq_vs_nmr_poly_seq', 'foo')

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
        answer = json.dumps(json.loads('{"corrected_warning": null, "error": {"format_issue": ["foo"], "total": 1}, "information": {"chain_assignments": {"model_poly_seq_vs_nmr_poly_seq": "foo", "nmr_poly_seq_vs_model_poly_seq": null}, "cyclic_polymer": false, "diamagnetic": true, "disulfide_bond": false, "input_sources": [{"content_subtype": {"chem_shift": 1, "dist_restraint": 2, "poly_seq": 1}, "content_type": "nmr-data-nef", "disulfide_bond": null, "file_name": null, "file_type": "nef", "non_standard_residue": null, "original_file_name": null, "other_bond": null, "polymer_sequence": null, "polymer_sequence_in_loop": null, "stats_of_exptl_data": null}, {"content_subtype": {"coordinate": 1, "poly_seq": 1}, "content_type": "model", "disulfide_bond": null, "file_name": null, "file_type": "pdbx", "non_standard_residue": null, "original_file_name": null, "other_bond": null, "polymer_sequence": null, "polymer_sequence_in_loop": null, "stats_of_exptl_data": null}], "other_bond": false, "sequence_alignments": {"model_poly_seq_vs_adist_restraint": null, "model_poly_seq_vs_ang_restraint": null, "model_poly_seq_vs_coordinate": null, "model_poly_seq_vs_csa_restraint": null, "model_poly_seq_vs_diff_restraint": null, "model_poly_seq_vs_dihed_restraint": null, "model_poly_seq_vs_dist_restraint": null, "model_poly_seq_vs_geo_restraint": null, "model_poly_seq_vs_hbond_restraint": null, "model_poly_seq_vs_hvycs_restraint": null, "model_poly_seq_vs_jcoup_restraint": null, "model_poly_seq_vs_nbase_restraint": null, "model_poly_seq_vs_nmr_poly_seq": "foo", "model_poly_seq_vs_noepk_restraint": null, "nmr_poly_seq_vs_chem_shift": null, "model_poly_seq_vs_pang_restraint": null, "model_poly_seq_vs_pccr_restraint": null, "model_poly_seq_vs_pcs_restraint": null, "model_poly_seq_vs_plane_restraint": null, "model_poly_seq_vs_prdc_restraint": null, "model_poly_seq_vs_pre_restraint": null, "model_poly_seq_vs_procs_restraint": null, "model_poly_seq_vs_radi_restraint": null, "model_poly_seq_vs_rama_restraint": null, "model_poly_seq_vs_rdc_restraint": null, "nmr_poly_seq_vs_dihed_restraint": null, "nmr_poly_seq_vs_dist_restraint": null, "nmr_poly_seq_vs_model_poly_seq": null, "nmr_poly_seq_vs_rdc_restraint": null, "nmr_poly_seq_vs_spectral_peak": null, "nmr_poly_seq_vs_spectral_peak_alt": null}, "status": "Error"}, "warning": {"missing_content": ["foo"], "total": 1}}'), sort_keys=True)  # noqa: E501

        self.assertEqual(result, answer)

        with LogCapture() as _logs:  # noqa: F841
            with self.assertRaises(UserWarning):
                self.report.setWarning()


class TestNmrDpInputSource(unittest.TestCase):

    def setUp(self):
        self.input_source = NmrDpReportInputSource()

    def tearDown(self):
        pass

    def test_setitemvalue(self):
        for item in set(self.input_source.items) - {'file_type', 'content_type', 'content_subtype'}:
            self.input_source.setItemValue(item, 'foo')

        for file_type in self.input_source.file_types:
            self.input_source.setItemValue('file_type', file_type)

        with LogCapture() as _logs:  # noqa: F841
            with self.assertRaises(KeyError):
                self.input_source.setItemValue('unknown', 'foo')

        with LogCapture() as _logs:  # noqa: F841
            with self.assertRaises(ValueError):
                self.input_source.setItemValue('file_type', 'unknown')

        for content_type in self.input_source.content_types:
            self.input_source.setItemValue('content_type', content_type)

        with LogCapture() as _logs:  # noqa: F841
            with self.assertRaises(ValueError):
                self.input_source.setItemValue('content_type', 'unknown')

        for content_subtype in self.input_source.content_subtypes:
            self.input_source.setItemValue('content_subtype', {content_subtype: 1})

        with LogCapture() as _logs:  # noqa: F841
            with self.assertRaises(AttributeError):
                self.input_source.setItemValue('content_subtype', 'unknown')

        with LogCapture() as _logs:  # noqa: F841
            with self.assertRaises(AttributeError):
                self.input_source.setItemValue('content_subtype', ['unknown'])

        with LogCapture() as _logs:  # noqa: F841
            with self.assertRaises(ValueError):
                self.input_source.setItemValue('content_subtype', {'unknown': 1})

        with LogCapture() as _logs:  # noqa: F841
            with self.assertRaises(ValueError):
                self.input_source.setItemValue('content_subtype', {'chem_shift': 'unknown'})

        self.input_source.setItemValue('content_subtype', {'poly_seq': 1, 'chem_shift': 0})
        self.assertEqual(self.input_source.get()['content_subtype'], {'poly_seq': 1})


class TestNmrDpSequenceAlignment(unittest.TestCase):

    def setUp(self):
        self.sequence_alignment = NmrDpReportSequenceAlignment()

    def tearDown(self):
        pass

    def test_setitemvalue(self):
        for item in self.sequence_alignment.items:
            self.sequence_alignment.setItemValue(item, 'foo')

        with LogCapture() as _logs:  # noqa: F841
            with self.assertRaises(KeyError):
                self.sequence_alignment.setItemValue('unknown', 'foo')

        for item in self.sequence_alignment.items:
            self.assertEqual(self.sequence_alignment.get()[item], 'foo')


class TestNmrDpChainAssignment(unittest.TestCase):

    def setUp(self):
        self.chain_assignment = NmrDpReportChainAssignment()

    def tearDown(self):
        pass

    def test_setitemvalue(self):
        for item in self.chain_assignment.items:
            self.chain_assignment.setItemValue(item, 'foo')

        with LogCapture() as _logs:  # noqa: F841
            with self.assertRaises(KeyError):
                self.chain_assignment.setItemValue('unknown', 'foo')

        for item in self.chain_assignment.items:
            self.assertEqual(self.chain_assignment.get()[item], 'foo')


class TestNmrDpError(unittest.TestCase):

    def setUp(self):
        self.error = NmrDpReportError()

    def tearDown(self):
        pass

    def test_setitemvalue(self):
        for item in self.error.items:
            self.error.appendDescription(item, {'foo': 'value'})

        with LogCapture() as _logs:  # noqa: F841
            with self.assertRaises(KeyError):
                self.error.appendDescription('unknown', {'foo': 'value'})

        for item in self.error.items:
            self.assertEqual(self.error.get()[item], [{'foo': 'value'}])

        for item in self.error.items:
            self.error.appendDescription(item, {'foo2': 'value2'})

        for item in self.error.items:
            self.assertEqual(self.error.get()[item], [{'foo': 'value'}, {'foo2': 'value2'}])


class TestNmrDpWarning(unittest.TestCase):

    def setUp(self):
        self.warning = NmrDpReportWarning()

    def tearDown(self):
        pass

    def test_setitemvalue(self):
        for item in self.warning.items:
            self.warning.appendDescription(item, {'foo': 'value'})

        with LogCapture() as _logs:  # noqa: F841
            with self.assertRaises(KeyError):
                self.warning.appendDescription('unknown', {'foo': 'value'})

        for item in self.warning.items:
            self.assertEqual(self.warning.get()[item], [{'foo': 'value'}])

        for item in self.warning.items:
            self.warning.appendDescription(item, {'foo2': 'value2'})

        for item in self.warning.items:
            self.assertEqual(self.warning.get()[item], [{'foo': 'value'}, {'foo2': 'value2'}])


if __name__ == '__main__':
    unittest.main()
