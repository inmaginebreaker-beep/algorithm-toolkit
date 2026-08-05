from pathlib import Path

import pytest
from _pytest.monkeypatch import MonkeyPatch
from scripts.check_version import (
    main,
    read_project_version,
    read_tag_version,
)


def test_read_project_version(tmp_path: Path) -> None:
    pyproject_path = tmp_path / "pyproject.toml"
    pyproject_path.write_text(
        """
[project]
name = "example-package"
version = "9.8.7"
""".strip(),
        encoding="utf-8",
    )

    result = read_project_version(pyproject_path)

    assert result == "9.8.7"


def test_read_project_version_rejects_non_string_version(
    tmp_path: Path,
) -> None:
    pyproject_path = tmp_path / "pyproject.toml"
    pyproject_path.write_text(
        """
[project]
name = "example-package"
version = 123
""".strip(),
        encoding="utf-8",
    )

    with pytest.raises(
        TypeError,
        match="project.version must be a string",
    ):
        read_project_version(pyproject_path)


def test_read_tag_version(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("GITHUB_REF_NAME", "v0.1.1")

    result = read_tag_version()

    assert result == "0.1.1"


def test_read_tag_version_requires_v_prefix(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.setenv("GITHUB_REF_NAME", "0.1.1")

    with pytest.raises(
        ValueError,
        match="Release tag must start with 'v'",
    ):
        read_tag_version()


def test_read_tag_version_requires_environment_variable(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.delenv(
        "GITHUB_REF_NAME",
        raising=False,
    )

    with pytest.raises(
        RuntimeError,
        match="GITHUB_REF_NAME is not set",
    ):
        read_tag_version()


def test_main_returns_zero_when_versions_match(
    monkeypatch: MonkeyPatch,
    tmp_path: Path,
) -> None:
    pyproject_path = tmp_path / "pyproject.toml"
    pyproject_path.write_text(
        """
[project]
version = "0.1.1"
""".strip(),
        encoding="utf-8",
    )

    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("GITHUB_REF_NAME", "v0.1.1")

    result = main()

    assert result == 0


def test_main_returns_one_when_versions_do_not_match(
    monkeypatch: MonkeyPatch,
    tmp_path: Path,
) -> None:
    pyproject_path = tmp_path / "pyproject.toml"
    pyproject_path.write_text(
        """
[project]
version = "0.1.1"
""".strip(),
        encoding="utf-8",
    )

    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("GITHUB_REF_NAME", "v0.2.0")

    result = main()

    assert result == 1
