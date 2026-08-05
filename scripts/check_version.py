import os
import sys
from pathlib import Path

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib


def read_project_version(
    pyproject_path: Path = Path("pyproject.toml"),
) -> str:
    with pyproject_path.open("rb") as file:
        pyproject = tomllib.load(file)

    version = pyproject["project"]["version"]

    if not isinstance(version, str):
        raise TypeError("project.version must be a string")

    return version


def read_tag_version() -> str:
    git_ref = os.getenv("GITHUB_REF_NAME")

    if not git_ref:
        raise RuntimeError("GITHUB_REF_NAME is not set")

    if not git_ref.startswith("v"):
        raise ValueError("Release tag must start with 'v'")

    return git_ref.removeprefix("v")


def main() -> int:
    project_version = read_project_version()
    tag_version = read_tag_version()

    print(f"Project version: {project_version}")
    print(f"Tag version: {tag_version}")

    if project_version != tag_version:
        print("Version mismatch")
        return 1

    print("Version check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
