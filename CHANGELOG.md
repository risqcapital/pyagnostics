# Changelog

## [3.0.2](https://github.com/risqcapital/pyagnostics/compare/v3.0.1...v3.0.2) (2026-02-25)


### Bug Fixes

* **deps:** bump rich from 14.3.2 to 14.3.3 ([#119](https://github.com/risqcapital/pyagnostics/issues/119)) ([1b0b937](https://github.com/risqcapital/pyagnostics/commit/1b0b937421b7dd1cbacf55285f909e28b71d9a79))

## [3.0.1](https://github.com/risqcapital/pyagnostics/compare/v3.0.0...v3.0.1) (2026-02-02)


### Bug Fixes

* **deps:** bump rich from 14.3.1 to 14.3.2 ([#114](https://github.com/risqcapital/pyagnostics/issues/114)) ([f9b1456](https://github.com/risqcapital/pyagnostics/commit/f9b1456cdb6ae4a0339b39cc8fc1ffb7a89e71e4))

## [3.0.0](https://github.com/risqcapital/pyagnostics/compare/v2.1.0...v3.0.0) (2026-01-26)


### ⚠ BREAKING CHANGES

* add multi-source diagnostics ([#110](https://github.com/risqcapital/pyagnostics/issues/110))

### Features

* add multi-source diagnostics ([#110](https://github.com/risqcapital/pyagnostics/issues/110)) ([ca7ebd5](https://github.com/risqcapital/pyagnostics/commit/ca7ebd59c07cff01fce4e1ae668899c4b59acea9))


### Bug Fixes

* **deps:** bump rich from 14.2.0 to 14.3.1 ([#112](https://github.com/risqcapital/pyagnostics/issues/112)) ([6ef6959](https://github.com/risqcapital/pyagnostics/commit/6ef6959b9d22a27119bf2e0613d0a1f784089d13))

## [2.1.0](https://github.com/risqcapital/pyagnostics/compare/v2.0.3...v2.1.0) (2026-01-19)


### Features

* improve source spans and add tests ([#106](https://github.com/risqcapital/pyagnostics/issues/106)) ([0791eab](https://github.com/risqcapital/pyagnostics/commit/0791eab064981a5d2b5474cfb351a2e88879957d))


### Bug Fixes

* render labels on wrapped lines ([#108](https://github.com/risqcapital/pyagnostics/issues/108)) ([e2e154e](https://github.com/risqcapital/pyagnostics/commit/e2e154ebbf73dc468ddd8b7f9e78e28784885775))

## [2.0.3](https://github.com/risqcapital/pyagnostics/compare/v2.0.2...v2.0.3) (2026-01-15)


### Bug Fixes

* **deps:** bump supported rich major ([#103](https://github.com/risqcapital/pyagnostics/issues/103)) ([7f90e8a](https://github.com/risqcapital/pyagnostics/commit/7f90e8a81851e76c05c1a52f531867c6bf1e6703))

## [2.0.2](https://github.com/risqcapital/pyagnostics/compare/v2.0.1...v2.0.2) (2024-11-05)


### Bug Fixes

* **deps:** bump rich from 13.9.3 to 13.9.4 ([#22](https://github.com/risqcapital/pyagnostics/issues/22)) ([531f8d7](https://github.com/risqcapital/pyagnostics/commit/531f8d7a3a1716cbb28e7347fdac09ee6c0d7788))
* Wrap cause list content ([#24](https://github.com/risqcapital/pyagnostics/issues/24)) ([8a416de](https://github.com/risqcapital/pyagnostics/commit/8a416def1f9a473e551a993b90dc13fd59d7ee7a))

## [2.0.1](https://github.com/risqcapital/pyagnostics/compare/v2.0.0...v2.0.1) (2024-10-28)


### Bug Fixes

* suppress stack frames in causes ([#20](https://github.com/risqcapital/pyagnostics/issues/20)) ([ca76dee](https://github.com/risqcapital/pyagnostics/commit/ca76dee920be9e90d3d696f67cfd571d6354e9ea))

## [2.0.0](https://github.com/risqcapital/pyagnostics/compare/v1.1.0...v2.0.0) (2024-10-24)


### ⚠ BREAKING CHANGES

* Add support for Syntax Highlighting diagnostic source ([#17](https://github.com/risqcapital/pyagnostics/issues/17))

### Features

* Add support for Syntax Highlighting diagnostic source ([#17](https://github.com/risqcapital/pyagnostics/issues/17)) ([f972107](https://github.com/risqcapital/pyagnostics/commit/f972107062004ec69b7b3021f7ae58070777b134))


### Bug Fixes

* Crop label to line length ([#16](https://github.com/risqcapital/pyagnostics/issues/16)) ([b6230cd](https://github.com/risqcapital/pyagnostics/commit/b6230cd9b036d1c5c17d5664b13bba90684b9ed8))
* **deps:** bump rich from 13.9.2 to 13.9.3 ([#15](https://github.com/risqcapital/pyagnostics/issues/15)) ([da96db2](https://github.com/risqcapital/pyagnostics/commit/da96db2cfe49706bcea8ae10ec3f7f8894413215))

## [1.1.0](https://github.com/risqcapital/pyagnostics/compare/v1.0.3...v1.1.0) (2024-10-21)


### Features

* Allow suppressing stack frames in diag reports ([#12](https://github.com/risqcapital/pyagnostics/issues/12)) ([91d17d0](https://github.com/risqcapital/pyagnostics/commit/91d17d09fc5d3f9f22b9717bac30e4aaede33452))


### Bug Fixes

* Off by one/whitespace bugs in labeled span printing ([#11](https://github.com/risqcapital/pyagnostics/issues/11)) ([c8f6dc3](https://github.com/risqcapital/pyagnostics/commit/c8f6dc33023a3f0834a7a123b0cf60cae1c565a3))

## [1.0.3](https://github.com/risqcapital/pyagnostics/compare/v1.0.1...v1.0.3) (2024-10-21)


### ⚠ BREAKING CHANGES

* Swap LabeledSpan argument order

### Bug Fixes

* Swap LabeledSpan argument order ([f20239e](https://github.com/risqcapital/pyagnostics/commit/f20239eb933b4dbcd05555137be0ed6a82b8dcbc))

## [1.0.1](https://github.com/risqcapital/pyagnostics/compare/v1.0.0...v1.0.1) (2024-10-21)


### Bug Fixes

* Add py.typed ([2bc42e2](https://github.com/risqcapital/pyagnostics/commit/2bc42e2b97b3d9a0aba20e2abffc89fc276d45df))

## [1.0.0](https://github.com/risqcapital/pyagnostics/compare/v0.1.0...v1.0.0) (2024-10-21)


### Miscellaneous Chores

* release 1.0.0 ([f7c76d8](https://github.com/risqcapital/pyagnostics/commit/f7c76d89c16791e6d03f59e9a88e32dbfb9139c3))

## 0.1.0 (2024-10-21)


### ⚠ BREAKING CHANGES

* Initial version ([#1](https://github.com/risqcapital/pyagnostics/issues/1))

### Features

* Initial version ([#1](https://github.com/risqcapital/pyagnostics/issues/1)) ([0cdabb2](https://github.com/risqcapital/pyagnostics/commit/0cdabb255e695fa907948e008d0cfc022f34891e))
