import sys
from pathlib import Path

def test_workflow_imports():
    scripts_path = Path(__file__).resolve().parents[1] / "scripts"
    sys.path.append(str(scripts_path))

    from step1_prepare_opt_inputs import VASPInputPreparer
    from step2_opt_output_check import OptOutputCheck
    from step3_prepare_piezo_inputs import PiezoInputPreparer
    from step4_piezo_output_check import PiezoOutputCheck

    assert VASPInputPreparer is not None
    assert OptOutputCheck is not None
    assert PiezoInputPreparer is not None
    assert PiezoOutputCheck is not None
