import yaml
from pathlib import Path

def test_config_yaml_loads():
    root = Path(__file__).resolve().parents[1]
    config_path = root / "config.yaml"

    assert config_path.exists(), "config.yaml is missing"

    config = yaml.safe_load(open(config_path))

    required_keys = [
        "calcdir",
        "potcar_path",
        "qmofbase",
        "resultstestdir",
        "alldatafiles"
    ]

    for key in required_keys:
        assert key in config, f"Missing key in config.yaml: {key}"
