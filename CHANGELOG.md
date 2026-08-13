# Changelog

All notable changes to this project will be documented in this file


## [Unreleased]


### Added


### Changed

- Optimized queue dequeue operations by replacing list-based storage with `collections.deque`.
- Generalized `Queue` with static generic typing so it can safely store different element types.
- Introduced an immutable `AlgorithmResult` data model for application-layer results.
- Standardized application services to return structured result objects.
- Replaced algorithm-name magic strings with the typed `AlgorithmName` enum.
- Introduced Protocol-based application service interfaces to reduce coupling to concrete implementations.
- Decoupled CLI command execution from the concrete algorithm service using dependency injection.
- Improved CLI isolation tests using mocked service dependencies and behavior verification.
### Fixed


### Removed


## [0.2.0] - 2026-08-06


### Added

- Added the `find-max` CLI command.
- Added CLI and application tests for maximum-value lookup.


## [0.1.1] - 2026-08-04


### Added


- Added a command-line interface for running algorithms.
- Added automated PyPI publishing through GitHub Actions.
- Added package build and metadata validation.
- Added static type checking with mypy.
- Added automated tests with pytest.


### Changed 


- Organized algorithm execution through an application service layer.
- Improved package metadata and installation documentation.


### Fixed 


- Declared `python-dotenv` as a runtime dependency.
- Improved CLI testing and exit-code handling.


## [0.1.0] - 2026-08-02


### Added


- Added the initial algorithm toolkit package.
- Added array, queue, and linked-list implementations.
- Added logging and environment-based configuration.
- Added Ruff formatting and lint checks.
- Added GitHub Actions continuous integration.


[Unreleased]: https://github.com/inmaginebreaker-beep/algorithm-toolkit/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/inmaginebreaker-beep/algorithm-toolkit/compare/v0.1.1...v0.2.0
[0.1.1]: https://github.com/inmaginebreaker-beep/algorithm-toolkit/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/inmaginebreaker-beep/algorithm-toolkit/releases/tag/v0.1.0