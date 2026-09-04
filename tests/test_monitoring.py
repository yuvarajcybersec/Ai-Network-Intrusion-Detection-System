from pathlib import Path

import src.monitoring.alert_monitor as alert_monitor


def test_load_alerts_parses_valid_alerts(tmp_path, monkeypatch):
    alert_log = tmp_path / "alerts.log"

    alert_log.write_text(
        "[ALERT] 2026-09-04 18:00:00 | "
        "Prediction=suspicious | "
        "10.0.3.15:4444 -> 10.0.3.2:80 | "
        "Protocol=TCP | Length=512\n"
        "[ALERT] 2026-09-04 18:01:00 | "
        "Prediction=suspicious | "
        "10.0.3.20:5353 -> 10.0.3.2:53 | "
        "Protocol=UDP | Length=128\n"
    )

    monkeypatch.setattr(
        alert_monitor,
        "ALERT_LOG",
        str(alert_log)
    )

    alerts = alert_monitor.load_alerts()

    assert len(alerts) == 2

    assert alerts[0]["prediction"] == "suspicious"
    assert alerts[0]["src_ip"] == "10.0.3.15"
    assert alerts[0]["src_port"] == 4444
    assert alerts[0]["dst_ip"] == "10.0.3.2"
    assert alerts[0]["dst_port"] == 80
    assert alerts[0]["protocol"] == "TCP"
    assert alerts[0]["length"] == 512

    assert alerts[1]["protocol"] == "UDP"
    assert alerts[1]["length"] == 128


def test_invalid_alert_lines_are_ignored(tmp_path, monkeypatch):
    alert_log = tmp_path / "alerts.log"

    alert_log.write_text(
        "This is not a valid alert\n"
        "[ALERT] 2026-09-04 18:00:00 | "
        "Prediction=suspicious | "
        "10.0.3.15:4444 -> 10.0.3.2:80 | "
        "Protocol=TCP | Length=512\n"
        "Another invalid line\n"
    )

    monkeypatch.setattr(
        alert_monitor,
        "ALERT_LOG",
        str(alert_log)
    )

    alerts = alert_monitor.load_alerts()

    assert len(alerts) == 1
    assert alerts[0]["src_ip"] == "10.0.3.15"


def test_calculate_statistics():
    alerts = [
        {
            "timestamp": "2026-09-04 18:00:00",
            "prediction": "suspicious",
            "src_ip": "10.0.3.15",
            "src_port": 4444,
            "dst_ip": "10.0.3.2",
            "dst_port": 80,
            "protocol": "TCP",
            "length": 512
        },
        {
            "timestamp": "2026-09-04 18:01:00",
            "prediction": "suspicious",
            "src_ip": "10.0.3.20",
            "src_port": 5353,
            "dst_ip": "10.0.3.2",
            "dst_port": 53,
            "protocol": "UDP",
            "length": 128
        },
        {
            "timestamp": "2026-09-04 18:02:00",
            "prediction": "suspicious",
            "src_ip": "10.0.3.15",
            "src_port": 5555,
            "dst_ip": "10.0.3.2",
            "dst_port": 443,
            "protocol": "TCP",
            "length": 256
        }
    ]

    statistics = alert_monitor.calculate_statistics(alerts)

    assert statistics["total_alerts"] == 3

    assert statistics["protocol_distribution"] == {
        "TCP": 2,
        "UDP": 1
    }

    assert statistics["source_distribution"] == {
        "10.0.3.15": 2,
        "10.0.3.20": 1
    }

    assert statistics["destination_distribution"] == {
        "10.0.3.2": 3
    }

    assert statistics["average_packet_length"] == (512 + 128 + 256) / 3
    assert statistics["minimum_packet_length"] == 128
    assert statistics["maximum_packet_length"] == 512


def test_calculate_statistics_with_no_alerts():
    statistics = alert_monitor.calculate_statistics([])

    assert statistics["total_alerts"] == 0
    assert statistics["protocol_distribution"] == {}
    assert statistics["source_distribution"] == {}
    assert statistics["destination_distribution"] == {}
    assert statistics["average_packet_length"] == 0
    assert statistics["minimum_packet_length"] == 0
    assert statistics["maximum_packet_length"] == 0
