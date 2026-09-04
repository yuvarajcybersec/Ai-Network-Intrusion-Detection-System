from pathlib import Path

import src.alerts.alert_manager as alert_manager


def test_suspicious_prediction_generates_alert(tmp_path, monkeypatch):
    alert_log = tmp_path / "alerts.log"

    monkeypatch.setattr(
        alert_manager,
        "ALERT_LOG",
        str(alert_log)
    )

    alert_manager.generate_alert(
        src_ip="10.0.3.15",
        dst_ip="10.0.3.2",
        protocol="TCP",
        src_port=4444,
        dst_port=80,
        packet_length=512,
        prediction="suspicious"
    )

    assert alert_log.exists()

    content = alert_log.read_text()

    assert "Prediction=suspicious" in content
    assert "10.0.3.15:4444" in content
    assert "10.0.3.2:80" in content
    assert "Protocol=TCP" in content
    assert "Length=512" in content


def test_normal_prediction_does_not_generate_alert(tmp_path, monkeypatch):
    alert_log = tmp_path / "alerts.log"

    monkeypatch.setattr(
        alert_manager,
        "ALERT_LOG",
        str(alert_log)
    )

    alert_manager.generate_alert(
        src_ip="10.0.3.15",
        dst_ip="10.0.3.2",
        protocol="ICMP",
        src_port=0,
        dst_port=0,
        packet_length=64,
        prediction="normal"
    )

    assert not alert_log.exists()


def test_multiple_suspicious_alerts_are_appended(tmp_path, monkeypatch):
    alert_log = tmp_path / "alerts.log"

    monkeypatch.setattr(
        alert_manager,
        "ALERT_LOG",
        str(alert_log)
    )

    alert_manager.generate_alert(
        src_ip="10.0.3.15",
        dst_ip="10.0.3.2",
        protocol="TCP",
        src_port=4444,
        dst_port=80,
        packet_length=512,
        prediction="suspicious"
    )

    alert_manager.generate_alert(
        src_ip="10.0.3.20",
        dst_ip="10.0.3.2",
        protocol="UDP",
        src_port=5353,
        dst_port=53,
        packet_length=128,
        prediction="suspicious"
    )

    content = alert_log.read_text().strip().splitlines()

    assert len(content) == 2
    assert "10.0.3.15:4444" in content[0]
    assert "10.0.3.20:5353" in content[1]
