# Changelog

Since we follow [Conventional
Commits](https://decisions.seedcase-project.org/why-conventional-commits/) for
commit messages, we can automatically create releases of the Python package
based on those messages. The releases are also published to Zenodo for easier
discovery, archiving, and citation.

We use
[Cocogitto](https://decisions.seedcase-project.org/why-semantic-release-with-cocogitto/)
to automate releases, which uses [SemVar](https://semverdoc.org) as the version
numbering scheme, and [Git
Cliff](https://decisions.seedcase-project.org/why-changelog-with-git-cliff/) to
generate the changelog from commit messages.

Because releases are generated automatically, new versions are released
often---sometimes several times in a day--- and each release usually contains
only a small number of changes. Below is a list of the releases and the changes
within each one.

Commits from bots, like `dependabot` or `pre-commit-ci`, are not included in the
changelog.

## [0.52.8](https://github.com/seedcase-project/seedcase-sprout/compare/0.52.7..0.52.8) - 2026-10-15

### ♻️ Refactor

- Remove unused `write_resource_data()`
  [#1865](https://github.com/seedcase-project/seedcase-sprout/pull/1865)
  ([e08bfdf](https://github.com/seedcase-project/seedcase-sprout/commit/e08bfdf7dce66951b93e5945436ae99794f45982))

### 📝 Documentation

- Update overall design of Sprout to match current focus
  [#1853](https://github.com/seedcase-project/seedcase-sprout/pull/1853)
  ([76a821c](https://github.com/seedcase-project/seedcase-sprout/commit/76a821c5ed8b721840a62d5e92ec0b08c7a3f0ce))
- Update output interface design to match current direction
  [#1861](https://github.com/seedcase-project/seedcase-sprout/pull/1861)
  ([cffe009](https://github.com/seedcase-project/seedcase-sprout/commit/cffe009e86b85a2e15393d4bae045ee87468c539))
- Update inputs design interface to match current design
  [#1868](https://github.com/seedcase-project/seedcase-sprout/pull/1868)
  ([d6d5c98](https://github.com/seedcase-project/seedcase-sprout/commit/d6d5c988d51c98feabc6e57233501e9e258ab2a0))

### 🧪 Tests

- Remove tests for deeply internal functions
  [#1866](https://github.com/seedcase-project/seedcase-sprout/pull/1866)
  ([9723cf2](https://github.com/seedcase-project/seedcase-sprout/commit/9723cf2602d38d21d61c7fdaa4d3a3cd5db9c91e))

## [0.52.7](https://github.com/seedcase-project/seedcase-sprout/compare/0.52.6..0.52.7) - 2026-10-14

### ♻️ Refactor

- Move check function into where it is mainly used
  [#1873](https://github.com/seedcase-project/seedcase-sprout/pull/1873)
  ([024bf94](https://github.com/seedcase-project/seedcase-sprout/commit/024bf94026c7c8f3766c59244a7054c47f4897ec))

## [0.52.6](https://github.com/seedcase-project/seedcase-sprout/compare/0.52.5..0.52.6) - 2026-10-14

### ♻️ Refactor

- Simplify public Python library interface
  [#1855](https://github.com/seedcase-project/seedcase-sprout/pull/1855)
  ([034fb01](https://github.com/seedcase-project/seedcase-sprout/commit/034fb0160030dce2689d8eb89511f8b8d82f9f48))

## [0.52.5](https://github.com/seedcase-project/seedcase-sprout/compare/0.52.4..0.52.5) - 2026-10-14

### ♻️ Refactor

- Remove checks in internal functions
  [#1864](https://github.com/seedcase-project/seedcase-sprout/pull/1864)
  ([49b3dfc](https://github.com/seedcase-project/seedcase-sprout/commit/49b3dfccaab2b5bbb02b339d286024b3cb773d4c))

## [0.52.4](https://github.com/seedcase-project/seedcase-sprout/compare/0.52.3..0.52.4) - 2026-10-14

### ♻️ Refactor

- Remove `write_properties()`
  [#1879](https://github.com/seedcase-project/seedcase-sprout/pull/1879)
  ([c2cf78c](https://github.com/seedcase-project/seedcase-sprout/commit/c2cf78c3c14307c8526e4feebeb8a96a5ba3ba39))

## [0.52.3](https://github.com/seedcase-project/seedcase-sprout/compare/0.52.2..0.52.3) - 2026-10-14

### ♻️ Refactor

- Move check constants into file they are used
  [#1872](https://github.com/seedcase-project/seedcase-sprout/pull/1872)
  ([ccc2851](https://github.com/seedcase-project/seedcase-sprout/commit/ccc2851b6ab79ee8766a04f63bd39bfe4f81801e))

## [0.52.2](https://github.com/seedcase-project/seedcase-sprout/compare/0.52.1..0.52.2) - 2026-10-14

### ♻️ Refactor

- Switch to `resource-name.parquet` as default
  [#1862](https://github.com/seedcase-project/seedcase-sprout/pull/1862)
  ([cc5effb](https://github.com/seedcase-project/seedcase-sprout/commit/cc5effbc38ef69e1ff700d1be5ad603e6a4de963))

## [0.52.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.52.0..0.52.1) - 2026-10-14

### ♻️ Refactor

- Remove use of `dedent()`, TOML is the recommended way now
  [#1878](https://github.com/seedcase-project/seedcase-sprout/pull/1878)
  ([8c1819a](https://github.com/seedcase-project/seedcase-sprout/commit/8c1819a000d74f605b7463a5e3fa844fc5af80b6))

## [0.52.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.51.0..0.52.0) - 2026-10-14

### ✨ Features

- Add extract metadata CLI command
  [#1766](https://github.com/seedcase-project/seedcase-sprout/pull/1766)
  ([a39ce75](https://github.com/seedcase-project/seedcase-sprout/commit/a39ce751d4a3314b04dbd666bc2b355c5a381bca))
- Add `init-metadata` CLI command
  [#1786](https://github.com/seedcase-project/seedcase-sprout/pull/1786)
  ([0c164d1](https://github.com/seedcase-project/seedcase-sprout/commit/0c164d1f0ddf2510eb695de9e1a25c0790482b0e))
- Add `Config`
  [#1825](https://github.com/seedcase-project/seedcase-sprout/pull/1825)
  ([70b91b3](https://github.com/seedcase-project/seedcase-sprout/commit/70b91b32edf31cd66e5daa6778f2319e9b6c07f6))

### 🐛 Fixes

- Resolve issues from type checker
  [#1756](https://github.com/seedcase-project/seedcase-sprout/pull/1756)
  ([125ddb6](https://github.com/seedcase-project/seedcase-sprout/commit/125ddb65c30a54ea2d7f326410b4120b805c5dd9))
- Remove extra quartodoc build step
  [#1768](https://github.com/seedcase-project/seedcase-sprout/pull/1768)
  ([4488af8](https://github.com/seedcase-project/seedcase-sprout/commit/4488af8242ec1351f4e089fb552e0bd1cf389a11))
- Resolve Python check errors (e.g. with types)
  [#1778](https://github.com/seedcase-project/seedcase-sprout/pull/1778)
  ([14017a7](https://github.com/seedcase-project/seedcase-sprout/commit/14017a7223953911ae48a1f056f36f622b3c68a1))

### ♻️ Refactor

- Remove `write_resource_batch()`, as we read from staging
  [#1759](https://github.com/seedcase-project/seedcase-sprout/pull/1759)
  ([f782b84](https://github.com/seedcase-project/seedcase-sprout/commit/f782b8478f6152a5263111fbd02bd98ff90a3233))
- Remove unused `read_resource_data()`
  [#1779](https://github.com/seedcase-project/seedcase-sprout/pull/1779)
  ([044af87](https://github.com/seedcase-project/seedcase-sprout/commit/044af876ac3d8bc6a0c0488f13f33030391cce4a))
- Rename from batches to staging
  [#1762](https://github.com/seedcase-project/seedcase-sprout/pull/1762)
  ([7acc3b3](https://github.com/seedcase-project/seedcase-sprout/commit/7acc3b3df026e3fb66cd8d8345b1c2022f90132b))
- Simplify `create_*_properties()` functions into `init.py` file
  [#1802](https://github.com/seedcase-project/seedcase-sprout/pull/1802)
  ([dbd368d](https://github.com/seedcase-project/seedcase-sprout/commit/dbd368d21d077cdca39ca581eed0cbb9bd4b8bdc))
- Remove use of `sprout` shortform for better security
  [#1823](https://github.com/seedcase-project/seedcase-sprout/pull/1823)
  ([ab86aed](https://github.com/seedcase-project/seedcase-sprout/commit/ab86aed1cf12d76670b364c45ccabc2f79c2b8a8))
- Remove use of `PackagePath` and `ExamplePackage`
  [#1805](https://github.com/seedcase-project/seedcase-sprout/pull/1805)
  ([a1a9849](https://github.com/seedcase-project/seedcase-sprout/commit/a1a9849ca99bb747b1d581f6716e11d43b50f98a))

### 📝 Documentation

- Remove glossary, moving it into internal repo
  [#1730](https://github.com/seedcase-project/seedcase-sprout/pull/1730)
  ([df0072c](https://github.com/seedcase-project/seedcase-sprout/commit/df0072c1b1d27d7e6eecd4aad334036744df0a7d))
- Update docs from template, mostly formatting changes
  [#1746](https://github.com/seedcase-project/seedcase-sprout/pull/1746)
  ([4b67287](https://github.com/seedcase-project/seedcase-sprout/commit/4b67287cb497b70e7487a5139aa04ab51794e231))
- Remove highly coupled example code in docstrings
  [#1758](https://github.com/seedcase-project/seedcase-sprout/pull/1758)
  ([0819ff4](https://github.com/seedcase-project/seedcase-sprout/commit/0819ff4390af4d6eb9262d891918b5c2c8fa4866))
- Add design of extract metadata CLI
  [#1763](https://github.com/seedcase-project/seedcase-sprout/pull/1763)
  ([2fbe3d5](https://github.com/seedcase-project/seedcase-sprout/commit/2fbe3d592eefa7db37ef4feb512fb235c2bcbe0a))
- Formatted Markdown, including in docstrings, with edits
  [#1755](https://github.com/seedcase-project/seedcase-sprout/pull/1755)
  ([c974a89](https://github.com/seedcase-project/seedcase-sprout/commit/c974a893b9a891e7c9784d5ae819bc322a1cfe24))
- Fix Markdown formatting, issue with formatter and def lists
  [#1775](https://github.com/seedcase-project/seedcase-sprout/pull/1775)
  ([7a23965](https://github.com/seedcase-project/seedcase-sprout/commit/7a23965d73d8c05d90d9757f382df410b5958003))
- Add design of `init-metadata` CLI
  [#1777](https://github.com/seedcase-project/seedcase-sprout/pull/1777)
  ([9bc7886](https://github.com/seedcase-project/seedcase-sprout/commit/9bc788648ac7254242136825ea5130a190692a6d))
- Update install guide to match current practices
  [#1782](https://github.com/seedcase-project/seedcase-sprout/pull/1782)
  ([7aa1096](https://github.com/seedcase-project/seedcase-sprout/commit/7aa1096c0a9a86886db794f272c297c8069692ff))
- Remove use of `PackagePaths` objects from design
  [#1797](https://github.com/seedcase-project/seedcase-sprout/pull/1797)
  ([670af81](https://github.com/seedcase-project/seedcase-sprout/commit/670af8168deafc2003e8cded962828b53375b848))
- Remove `create_*_scripts()` from guides, use CLI instead
  [#1799](https://github.com/seedcase-project/seedcase-sprout/pull/1799)
  ([61d4406](https://github.com/seedcase-project/seedcase-sprout/commit/61d4406b5001525cf94b7ef63b486509ee691325))
- Add design of `build-resources`
  [#1819](https://github.com/seedcase-project/seedcase-sprout/pull/1819)
  ([c12d99b](https://github.com/seedcase-project/seedcase-sprout/commit/c12d99bc108c7f7c323857fec258d30ecc1ddd29))
- Expand on deleting obs unit, move into `inputs.qmd`
  [#1820](https://github.com/seedcase-project/seedcase-sprout/pull/1820)
  ([b46def5](https://github.com/seedcase-project/seedcase-sprout/commit/b46def557766ae780d4c8d37231933c722b195c8))
- Remove no longer relevant design docs
  [#1867](https://github.com/seedcase-project/seedcase-sprout/pull/1867)
  ([eb55421](https://github.com/seedcase-project/seedcase-sprout/commit/eb554219e13b603ea8d8119c21f9168569a83ad7))
- Update overview page to reflect current use
  [#1871](https://github.com/seedcase-project/seedcase-sprout/pull/1871)
  ([076916c](https://github.com/seedcase-project/seedcase-sprout/commit/076916c9b0aef62805f296fc1053897a791b4aa3))
- Update landing page and README intros to Sprout
  [#1870](https://github.com/seedcase-project/seedcase-sprout/pull/1870)
  ([6eb65f6](https://github.com/seedcase-project/seedcase-sprout/commit/6eb65f6b540b05f2ac5bcea7e9d75bc9d4d465bb))
- Updates to Python interface design to match current designs
  [#1881](https://github.com/seedcase-project/seedcase-sprout/pull/1881)
  ([89c9d30](https://github.com/seedcase-project/seedcase-sprout/commit/89c9d30fb5de7f82c2f45727d1c29459a5af164f))

### 💄 Style

- Update Quarto theme
  [#1731](https://github.com/seedcase-project/seedcase-sprout/pull/1731)
  ([2df4a79](https://github.com/seedcase-project/seedcase-sprout/commit/2df4a7991c50c0fb12ecde7214209699b297f7b3))
- Reformat code chunks in docs via pre-commit hooks
  [#1753](https://github.com/seedcase-project/seedcase-sprout/pull/1753)
  ([c9add86](https://github.com/seedcase-project/seedcase-sprout/commit/c9add86abf6742f2bbf15447744e70a00119a645))
- Update Quarto theme and add "Part of" to navbar
  [#1774](https://github.com/seedcase-project/seedcase-sprout/pull/1774)
  ([29d5e41](https://github.com/seedcase-project/seedcase-sprout/commit/29d5e41ccc67aae909f9ae503aca1763a9cf8a1f))
- Match guide page style with other packages
  [#1783](https://github.com/seedcase-project/seedcase-sprout/pull/1783)
  ([a806f72](https://github.com/seedcase-project/seedcase-sprout/commit/a806f72b4cd59d0e19688e42611cf3dacd2713e6))
- Update Seedcase Quarto theme
  [#1826](https://github.com/seedcase-project/seedcase-sprout/pull/1826)
  ([2f71a04](https://github.com/seedcase-project/seedcase-sprout/commit/2f71a04c668de28f492b899282fd3dc5ce77c948))
- Update Seedcase Quarto theme
  [#1834](https://github.com/seedcase-project/seedcase-sprout/pull/1834)
  ([6ca86f3](https://github.com/seedcase-project/seedcase-sprout/commit/6ca86f3408b9654b80459829f1f1466f4f260e21))
- Update Quarto theme
  [#1856](https://github.com/seedcase-project/seedcase-sprout/pull/1856)
  ([a61c5ba](https://github.com/seedcase-project/seedcase-sprout/commit/a61c5bab95da4d3463a196820e9904fea005f78a))

### 👷 CI/CD

- Update workflows from template
  [#1745](https://github.com/seedcase-project/seedcase-sprout/pull/1745)
  ([5c9f522](https://github.com/seedcase-project/seedcase-sprout/commit/5c9f5225cfcb945cfc3c1f271efcca31c13dc80a))
- Remove typos check when building website
  [#1773](https://github.com/seedcase-project/seedcase-sprout/pull/1773)
  ([9322fb3](https://github.com/seedcase-project/seedcase-sprout/commit/9322fb36fac362bc3d0679d526c4abf27b248b18))
- Check commits from latest tag, earlier ones will fail
  [#1781](https://github.com/seedcase-project/seedcase-sprout/pull/1781)
  ([3a75a77](https://github.com/seedcase-project/seedcase-sprout/commit/3a75a77349a27202e4ed7850e9d387dcc9c5c01e))
- Fix release workflow, `--config` moved before `bump`
  [#1788](https://github.com/seedcase-project/seedcase-sprout/pull/1788)
  ([cb439d7](https://github.com/seedcase-project/seedcase-sprout/commit/cb439d7e33a40d71a763d260af63bdcadca50bc5))
- Run check workflows only on PRs
  [#1807](https://github.com/seedcase-project/seedcase-sprout/pull/1807)
  ([179a264](https://github.com/seedcase-project/seedcase-sprout/commit/179a264a3f452f066fa0162c1d1741f63c3349e9))
- Fix release workflow via config settings
  [#1890](https://github.com/seedcase-project/seedcase-sprout/pull/1890)
  ([a9b1bf8](https://github.com/seedcase-project/seedcase-sprout/commit/a9b1bf895c9b2f7d80ad15a6a0ba77cbf0f5d42e))

### 🧱 Build system

- Update `uv.lock` dependencies to fix security notices
  [#1737](https://github.com/seedcase-project/seedcase-sprout/pull/1737)
  ([1188264](https://github.com/seedcase-project/seedcase-sprout/commit/1188264cb1a1cf6564ad94414a2927c46ffd1e91))
- Update Quarto theme
  [#1736](https://github.com/seedcase-project/seedcase-sprout/pull/1736)
  ([2bce477](https://github.com/seedcase-project/seedcase-sprout/commit/2bce4776cad253fd4670a6ec15e32fce4862b2d1))
- Update various DevEx and build files from template
  [#1744](https://github.com/seedcase-project/seedcase-sprout/pull/1744)
  ([118466d](https://github.com/seedcase-project/seedcase-sprout/commit/118466d7d785a84b2ee00cbebbf5cf1d01da02e4))
- Small improvements to Ruff settings
  [#1757](https://github.com/seedcase-project/seedcase-sprout/pull/1757)
  ([d29bf62](https://github.com/seedcase-project/seedcase-sprout/commit/d29bf625b45bc15c0adc90af6ce92685127f2f71))
- Move quartodoc config into root where it must be
  [#1764](https://github.com/seedcase-project/seedcase-sprout/pull/1764)
  ([315dc94](https://github.com/seedcase-project/seedcase-sprout/commit/315dc945d82d0b9c73ec183fb2ffc5704a6af3d9))
- Split into `format-md` and `check-md`
  [#1776](https://github.com/seedcase-project/seedcase-sprout/pull/1776)
  ([d6c6628](https://github.com/seedcase-project/seedcase-sprout/commit/d6c6628af404095c428ec036c0fa3030341a6ed8))
- Speed up local Quarto build by caching Python results
  [#1789](https://github.com/seedcase-project/seedcase-sprout/pull/1789)
  ([8044ffc](https://github.com/seedcase-project/seedcase-sprout/commit/8044ffcca6fc711f20bffcdd331354895fd7c0a1))
- Switch to using `uv_build` for build backend
  [#1876](https://github.com/seedcase-project/seedcase-sprout/pull/1876)
  ([faffe78](https://github.com/seedcase-project/seedcase-sprout/commit/faffe78be5328b69287348a0af27efa35ebb97f8))

### 🧹 Chores

- Update GitHub DevEx files (e.g. CODEOWNERS)
  [#1747](https://github.com/seedcase-project/seedcase-sprout/pull/1747)
  ([3d7d5de](https://github.com/seedcase-project/seedcase-sprout/commit/3d7d5deb5c518bf21075d86bc2163bfcca8ce84b))
- Don't fix use of `Optional[]` by Ruff
  [#1772](https://github.com/seedcase-project/seedcase-sprout/pull/1772)
  ([6a1a8aa](https://github.com/seedcase-project/seedcase-sprout/commit/6a1a8aa92e2e6d33bba16da19939bcbe93f5ed5a))
- Remove (future) internal functions from ref sidebar
  [#1798](https://github.com/seedcase-project/seedcase-sprout/pull/1798)
  ([94984fd](https://github.com/seedcase-project/seedcase-sprout/commit/94984fdb6cbc84456f52fdded2a72c44de6e6d48))
- Add fake patient data files for guides
  [#1804](https://github.com/seedcase-project/seedcase-sprout/pull/1804)
  ([bc82b00](https://github.com/seedcase-project/seedcase-sprout/commit/bc82b00a1b178e4fc8f1c541ff7ee0a7fa245b0c))
- Remove accidentally merged `init.py`
  [#1830](https://github.com/seedcase-project/seedcase-sprout/pull/1830)
  ([6c703fa](https://github.com/seedcase-project/seedcase-sprout/commit/6c703fa06945bb3efd2695f4ab9ae30502427ae1))
- Add Joel, switch to Fru, and sort author list
  [#1833](https://github.com/seedcase-project/seedcase-sprout/pull/1833)
  ([d9fee17](https://github.com/seedcase-project/seedcase-sprout/commit/d9fee17e5b50f0fefb528c68d1079e296f2d516f))
- Remove no longer needed property generating scripts
  [#1854](https://github.com/seedcase-project/seedcase-sprout/pull/1854)
  ([e3e6902](https://github.com/seedcase-project/seedcase-sprout/commit/e3e6902bb63e215c12b5d1172feb5f662dbf377a))
- Remove leftover `README.jinja` file
  [#1852](https://github.com/seedcase-project/seedcase-sprout/pull/1852)
  ([2c52d15](https://github.com/seedcase-project/seedcase-sprout/commit/2c52d15371d95c269cc3e50369008b88a9974c04))

## [0.50.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.50.0..0.50.1) - 2026-05-19

### ♻️ Refactor

- Use `file_tree()` from `seedcase_soil`
  [#1712](https://github.com/seedcase-project/seedcase-sprout/pull/1712)
  ([c5aea71](https://github.com/seedcase-project/seedcase-sprout/commit/c5aea715f5dbdda1fe2968fb0199d4c2b2ac0f43))

### 🧱 Build system

- Upgrade \`seedcase-theme
  [#1713](https://github.com/seedcase-project/seedcase-sprout/pull/1713)
  ([46cffbb](https://github.com/seedcase-project/seedcase-sprout/commit/46cffbb60fd70497de79d947348abd35046d6ad4))

## [0.49.7](https://github.com/seedcase-project/seedcase-sprout/compare/0.49.6..0.49.7) - 2026-04-27

### ♻️ Refactor

- Use Soil when reading and writing
  [#1703](https://github.com/seedcase-project/seedcase-sprout/pull/1703)
  ([0e7036f](https://github.com/seedcase-project/seedcase-sprout/commit/0e7036ff4a34c1e5afdedc6f15a04862a3c6aba9))

## [0.49.6](https://github.com/seedcase-project/seedcase-sprout/compare/0.49.5..0.49.6) - 2026-04-22

### ♻️ Refactor

- Rename `Properties` classes to be more specific
  [#1698](https://github.com/seedcase-project/seedcase-sprout/pull/1698)
  ([b28dead](https://github.com/seedcase-project/seedcase-sprout/commit/b28deaddd6ea5aca13ef162810ab98514f81622c))

## [0.49.5](https://github.com/seedcase-project/seedcase-sprout/compare/0.49.4..0.49.5) - 2026-04-21

### ♻️ Refactor

- Make check functions private
  [#1699](https://github.com/seedcase-project/seedcase-sprout/pull/1699)
  ([e649766](https://github.com/seedcase-project/seedcase-sprout/commit/e6497668f0ba2cacc5b2c5e93ebde4c195fbed9f))

### 🧹 Chores

- Updates from template via just run all
  [#1697](https://github.com/seedcase-project/seedcase-sprout/pull/1697)
  ([807b16a](https://github.com/seedcase-project/seedcase-sprout/commit/807b16a73a90308cfd90c1b8047f90877772f3bf))

## [0.49.4](https://github.com/seedcase-project/seedcase-sprout/compare/0.49.3..0.49.4) - 2026-04-15

### ♻️ Refactor

- Import functionals from soil
  [#1696](https://github.com/seedcase-project/seedcase-sprout/pull/1696)
  ([93871bc](https://github.com/seedcase-project/seedcase-sprout/commit/93871bc7ea1c49994271adfcfbb20154bc586221))

## [0.49.3](https://github.com/seedcase-project/seedcase-sprout/compare/0.49.2..0.49.3) - 2026-04-09

### ♻️ Refactor

- Remove `as_readme_text()`
  [#1693](https://github.com/seedcase-project/seedcase-sprout/pull/1693)
  ([f0a3dc3](https://github.com/seedcase-project/seedcase-sprout/commit/f0a3dc3fac0cbd988a04b672946246175e0669f4))

## [0.49.2](https://github.com/seedcase-project/seedcase-sprout/compare/0.49.1..0.49.2) - 2026-03-20

### 🐛 Fixes

- Expose unexposed types in properties
  [#1671](https://github.com/seedcase-project/seedcase-sprout/pull/1671)
  ([8673377](https://github.com/seedcase-project/seedcase-sprout/commit/867337707147cb93fb60434a2ca87cd85d3f94c5))

### 📝 Documentation

- Add Sprout favicon to Quarto config
  [#1635](https://github.com/seedcase-project/seedcase-sprout/pull/1635)
  ([e75b688](https://github.com/seedcase-project/seedcase-sprout/commit/e75b6886db8022c2cb4ae4382f34d0c46a6a3ba8))
- Reorder interface toc to match index page
  [#1636](https://github.com/seedcase-project/seedcase-sprout/pull/1636)
  ([5072937](https://github.com/seedcase-project/seedcase-sprout/commit/507293795b64ae23353325acbedbb8f68ce7dd75))
- Slight rewrite of guide description
  [#1637](https://github.com/seedcase-project/seedcase-sprout/pull/1637)
  ([fdde5c0](https://github.com/seedcase-project/seedcase-sprout/commit/fdde5c08d34ceed7a668dbfa869a7d2cd9b50c04))
- Align collapsible callout block appearance with Flower
  [#1639](https://github.com/seedcase-project/seedcase-sprout/pull/1639)
  ([8e07725](https://github.com/seedcase-project/seedcase-sprout/commit/8e07725dfb7a8524b88d09e3d0949bee4759fd7f))
- Update landing page
  [#1654](https://github.com/seedcase-project/seedcase-sprout/pull/1654)
  ([28823ae](https://github.com/seedcase-project/seedcase-sprout/commit/28823ae2ed8f349ceb4741a818592a636445b4a4))

### 💄 Style

- Update brand
  [#1638](https://github.com/seedcase-project/seedcase-sprout/pull/1638)
  ([680a8c7](https://github.com/seedcase-project/seedcase-sprout/commit/680a8c76b38de85415b41a6e87875fe4ccb2118d))

### 🧱 Build system

- Upgrade `seedcase-theme`
  [#1655](https://github.com/seedcase-project/seedcase-sprout/pull/1655)
  ([c9f00dc](https://github.com/seedcase-project/seedcase-sprout/commit/c9f00dc0483d21d5e9c7cda9fc097d80af4864c0))

### 🧹 Chores

- Run `just run-all`
  [#1632](https://github.com/seedcase-project/seedcase-sprout/pull/1632)
  ([69cc76e](https://github.com/seedcase-project/seedcase-sprout/commit/69cc76e8730d7ad675af66b29369fb91e19a4fc0))

## [0.49.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.49.0..0.49.1) - 2026-01-06

### 🐛 Fixes

- Import and return in `generate_dataclasses`
  [#1631](https://github.com/seedcase-project/seedcase-sprout/pull/1631)
  ([cc3632f](https://github.com/seedcase-project/seedcase-sprout/commit/cc3632f55fc57fe9030d1534e04142b4fb711a0d))

### 📝 Documentation

- Color and format output
  [#1620](https://github.com/seedcase-project/seedcase-sprout/pull/1620)
  ([f5b24c2](https://github.com/seedcase-project/seedcase-sprout/commit/f5b24c26e48f58a33c8aeab517303a9784ed1d14))

## [0.49.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.48.1..0.49.0) - 2025-12-08

### ✨ Features

- Integrate `check-datapackage`
  [#1605](https://github.com/seedcase-project/seedcase-sprout/pull/1605)
  ([b5b282b](https://github.com/seedcase-project/seedcase-sprout/commit/b5b282b36dd388911351ecb1966c7aa358d73db7))

### 📝 Documentation

- Add Marton's and Kris' ORCID to CITATION
  [#1515](https://github.com/seedcase-project/seedcase-sprout/pull/1515)
  ([7765ead](https://github.com/seedcase-project/seedcase-sprout/commit/7765ead25b3db318755b93cf61dd7099d91cb5ae))
- Remove more general requirements
  [#1532](https://github.com/seedcase-project/seedcase-sprout/pull/1532)
  ([3df8d82](https://github.com/seedcase-project/seedcase-sprout/commit/3df8d82f1d3262743fb707f0fc4354f50880e16b))
- Update badges from template
  [#1542](https://github.com/seedcase-project/seedcase-sprout/pull/1542)
  ([a1ca1dd](https://github.com/seedcase-project/seedcase-sprout/commit/a1ca1dd581cb7c7e85060c9d7fc342108c7892e8))
- Update the `_contributors.yml`, add it to README and website
  [#1543](https://github.com/seedcase-project/seedcase-sprout/pull/1543)
  ([1badad6](https://github.com/seedcase-project/seedcase-sprout/commit/1badad6a74b5288b1dfa370056a4580a62640acb))
- Connect `_metadata.yml` to README
  [#1546](https://github.com/seedcase-project/seedcase-sprout/pull/1546)
  ([ec16808](https://github.com/seedcase-project/seedcase-sprout/commit/ec168089b014a1fd7672e66a6ec1a2a134f374c6))
- Move releases content into CHANGELOG
  [#1541](https://github.com/seedcase-project/seedcase-sprout/pull/1541)
  ([02841a0](https://github.com/seedcase-project/seedcase-sprout/commit/02841a0517009a849f4379c1ccb194e760ff8706))
- Remove reference to GitHub installation in guide
  [#1570](https://github.com/seedcase-project/seedcase-sprout/pull/1570)
  ([2df789f](https://github.com/seedcase-project/seedcase-sprout/commit/2df789fc84675e934d2fb1deb82d221de3bb1979))
- Clarify intro and data constraints
  [#1585](https://github.com/seedcase-project/seedcase-sprout/pull/1585)
  ([d797fe0](https://github.com/seedcase-project/seedcase-sprout/commit/d797fe07f0c5765b19cabce059a5cd01c939828a))
- Deduplicate callout
  [#1586](https://github.com/seedcase-project/seedcase-sprout/pull/1586)
  ([ea64315](https://github.com/seedcase-project/seedcase-sprout/commit/ea643152e454a66260b25ae111bf5e6b9f2d06f1))
- Minor edits to overview page
  [#1588](https://github.com/seedcase-project/seedcase-sprout/pull/1588)
  ([826ff37](https://github.com/seedcase-project/seedcase-sprout/commit/826ff371e72de93c068e9b031a09f2f76f289d29))
- Clarify and contextualize installation steps
  [#1589](https://github.com/seedcase-project/seedcase-sprout/pull/1589)
  ([298b9fe](https://github.com/seedcase-project/seedcase-sprout/commit/298b9fe09aff6652e5deae9b7c92a61a61be0c34))
- Split guide into creating vs managing a Data Package
  [#1592](https://github.com/seedcase-project/seedcase-sprout/pull/1592)
  ([c9619ab](https://github.com/seedcase-project/seedcase-sprout/commit/c9619ab3d1d3a7b30f0511734ca0b359dc73b2d0))
- Clarify guide on resource-level metadata
  [#1597](https://github.com/seedcase-project/seedcase-sprout/pull/1597)
  ([31bdff4](https://github.com/seedcase-project/seedcase-sprout/commit/31bdff41f38b54397567c632e94a4a8862872857))

### 🧪 Tests

- Fix failing test by adding scale and precision to `pl.Decimal`
  [#1568](https://github.com/seedcase-project/seedcase-sprout/pull/1568)
  ([56e72bf](https://github.com/seedcase-project/seedcase-sprout/commit/56e72bfe3aa117f0e666bbaf998aa16f43d563cf))

### 👷 CI/CD

- Don't need `update-from-template.yml` workflow
  [#1536](https://github.com/seedcase-project/seedcase-sprout/pull/1536)
  ([0dbc8e2](https://github.com/seedcase-project/seedcase-sprout/commit/0dbc8e27a2c540beee5d4a34f1d12ffd4261acef))
- Use `check-package` workflow, not `build`
  [#1537](https://github.com/seedcase-project/seedcase-sprout/pull/1537)
  ([abebcbf](https://github.com/seedcase-project/seedcase-sprout/commit/abebcbfc1a64b5c3c44ff2bf58b573dc7bd80d4b))

### 🧱 Build system

- Update template, which updates the answers file
  [#1538](https://github.com/seedcase-project/seedcase-sprout/pull/1538)
  ([b35cb15](https://github.com/seedcase-project/seedcase-sprout/commit/b35cb1526f59dc305ed16085f66fbd4a2dbed2dc))
- Moved `site-counter.html` into the includes folder
  [#1539](https://github.com/seedcase-project/seedcase-sprout/pull/1539)
  ([0ebb458](https://github.com/seedcase-project/seedcase-sprout/commit/0ebb4589b330139da5d50e853350bcb45b3193ae))
- Quartodoc files are deleted outside of `_quarto.yml`
  [#1540](https://github.com/seedcase-project/seedcase-sprout/pull/1540)
  ([ac69572](https://github.com/seedcase-project/seedcase-sprout/commit/ac69572a1e4cdfba46090acc5b7ea971d415648c))
- Ran `just install-deps` to bump versions
  [#1544](https://github.com/seedcase-project/seedcase-sprout/pull/1544)
  ([2e0e97f](https://github.com/seedcase-project/seedcase-sprout/commit/2e0e97fee1e9caedf129f13fd0edf1f8a4748bdc))
- Update justfile from template
  [#1547](https://github.com/seedcase-project/seedcase-sprout/pull/1547)
  ([07940cb](https://github.com/seedcase-project/seedcase-sprout/commit/07940cb95d9a39e0c44d7a61803e9d4e36384cb0))
- Don't need to restrict Quarto rendering
  [#1554](https://github.com/seedcase-project/seedcase-sprout/pull/1554)
  ([4a5228b](https://github.com/seedcase-project/seedcase-sprout/commit/4a5228bfdbed33b84894b68470a025fb281b2949))
- Add build step to preview docs
  [#1593](https://github.com/seedcase-project/seedcase-sprout/pull/1593)
  ([96a72b2](https://github.com/seedcase-project/seedcase-sprout/commit/96a72b28e9e03218e4787388c2253d1196bcec76))

### 🧹 Chores

- Simplify PR template
  [#1545](https://github.com/seedcase-project/seedcase-sprout/pull/1545)
  ([4e5e5ea](https://github.com/seedcase-project/seedcase-sprout/commit/4e5e5eaa7428a6542de1be9b828cbfbe0fc24ae4))
- Update quarto theme to newest version
  [#1569](https://github.com/seedcase-project/seedcase-sprout/pull/1569)
  ([855d1af](https://github.com/seedcase-project/seedcase-sprout/commit/855d1afb871bd524167f3b17f6f321e7e5c8ea42))

## [0.48.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.48.0..0.48.1) - 2025-09-01

### ⏪ Revert

- Keep Sprout-specific text
  ([cb318f3](https://github.com/seedcase-project/seedcase-sprout/commit/cb318f3e4ccb8e2bac2cdcc1d92cd7fe8b1b396d))

### ♻️ Refactor

- Apply changes from copier template
  ([2fd256f](https://github.com/seedcase-project/seedcase-sprout/commit/2fd256fd38b68e1b42b6776f816ab96b8cea3653))

### 🧹 Chores

- Update theme
  ([6419428](https://github.com/seedcase-project/seedcase-sprout/commit/6419428102d8c55c591f3bd69b9b704c7d7ed7e0))

## [0.48.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.47.3..0.48.0) - 2025-08-25

### ✨ Features

- Add field information to README
  [#1510](https://github.com/seedcase-project/seedcase-sprout/pull/1510)
  ([26c2348](https://github.com/seedcase-project/seedcase-sprout/commit/26c23480ab1dbcdd91b512d0e6cda736f170084e))

## [0.47.3](https://github.com/seedcase-project/seedcase-sprout/compare/0.47.2..0.47.3) - 2025-08-19

### 🐛 Fixes

- Improve badge quality by setting them as SVGs
  [#1507](https://github.com/seedcase-project/seedcase-sprout/pull/1507)
  ([5080c15](https://github.com/seedcase-project/seedcase-sprout/commit/5080c152d88de47c77eb14e1ae5c6ad3bf29da22))

## [0.47.2](https://github.com/seedcase-project/seedcase-sprout/compare/0.47.1..0.47.2) - 2025-08-18

### 🐛 Fixes

- Revert syncing with `template-python-package`
  [#1508](https://github.com/seedcase-project/seedcase-sprout/pull/1508)
  ([82ca4eb](https://github.com/seedcase-project/seedcase-sprout/commit/82ca4eb68d96bbb32b5dfc52851f36535d637de8))

### 📝 Documentation

- Update tagline and expand on CITATION title
  [#1497](https://github.com/seedcase-project/seedcase-sprout/pull/1497)
  ([c3457b1](https://github.com/seedcase-project/seedcase-sprout/commit/c3457b15713c04e0ef5afca4f3dd9628d6c5b747))

### 🧱 Build system

- Need to include rendering the 404 page
  [#1499](https://github.com/seedcase-project/seedcase-sprout/pull/1499)
  ([1841093](https://github.com/seedcase-project/seedcase-sprout/commit/18410931a0a79ba6f0a26a0a07e1b16fe4071397))
- Build readme as a justfile recipe, not Quarto config
  [#1498](https://github.com/seedcase-project/seedcase-sprout/pull/1498)
  ([52bb8e6](https://github.com/seedcase-project/seedcase-sprout/commit/52bb8e663c4423e258b53457d82ed865aa4aa413))

### 🧹 Chores

- *(sync)* Synced file(s) with seedcase-project/template-python-package
  ([cd49f11](https://github.com/seedcase-project/seedcase-sprout/commit/cd49f1121842cd8bf8b8b91416f46277f19a4c3a))
- *(sync)* Synced file(s) with seedcase-project/template-python-package
  ([1ebb6f2](https://github.com/seedcase-project/seedcase-sprout/commit/1ebb6f2cfcb3c94ca8f476e291002601cca4f7cc))

## [0.47.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.47.0..0.47.1) - 2025-07-25

### 🐛 Fixes

- Do not create duplicate batch files
  [#1493](https://github.com/seedcase-project/seedcase-sprout/pull/1493)
  ([84bee73](https://github.com/seedcase-project/seedcase-sprout/commit/84bee735a859a39d37802b56a361082150606b04))

## [0.47.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.46.6..0.47.0) - 2025-07-25

### ✨ Features

- Dedent resource and field descriptions in `write_properties()`
  [#1488](https://github.com/seedcase-project/seedcase-sprout/pull/1488)
  ([85eb980](https://github.com/seedcase-project/seedcase-sprout/commit/85eb980ed034be9d70d6c6edde42d53361c4df56))

### 📝 Documentation

- Fix badge quality by using `svg` instead of `png`
  [#1489](https://github.com/seedcase-project/seedcase-sprout/pull/1489)
  ([f7b23cc](https://github.com/seedcase-project/seedcase-sprout/commit/f7b23cc2dfe17fb875a2215f7edc9f39801b4e9d))

## [0.46.6](https://github.com/seedcase-project/seedcase-sprout/compare/0.46.5..0.46.6) - 2025-07-23

### 📝 Documentation

- Update DOI to refer to all versions
  [#1486](https://github.com/seedcase-project/seedcase-sprout/pull/1486)
  ([93cc0ba](https://github.com/seedcase-project/seedcase-sprout/commit/93cc0ba8c2d4fbcb0eab0e9b5cde185ebedb7d12))

### 🧹 Chores

- *(sync)* Synced file(s) with seedcase-project/template-python-package
  ([978d06a](https://github.com/seedcase-project/seedcase-sprout/commit/978d06a4823694fcd382d6f7c05053bc5cbd82f6))

## [0.46.5](https://github.com/seedcase-project/seedcase-sprout/compare/0.46.4..0.46.5) - 2025-07-23

### ♻️ Refactor

- Rename properties script to `package_properties.py`
  [#1482](https://github.com/seedcase-project/seedcase-sprout/pull/1482)
  ([e2b3550](https://github.com/seedcase-project/seedcase-sprout/commit/e2b35508b627465b62a02ad284bc9439d9273eeb))

### 🧹 Chores

- *(sync)* Synced file(s) with seedcase-project/template-python-package
  ([26ae700](https://github.com/seedcase-project/seedcase-sprout/commit/26ae700b3f8bdaf428a89ac86c4952879ac082eb))

## [0.46.4](https://github.com/seedcase-project/seedcase-sprout/compare/0.46.3..0.46.4) - 2025-07-23

### 🐛 Fixes

- Dedent `description` in `as_readme_text()` and `write_properties()`
  [#1476](https://github.com/seedcase-project/seedcase-sprout/pull/1476)
  ([cfddf43](https://github.com/seedcase-project/seedcase-sprout/commit/cfddf43b16a2634ee0319f28e1cdc6e7f38086a6))

### 📝 Documentation

- Add DOI from Zenodo
  [#1460](https://github.com/seedcase-project/seedcase-sprout/pull/1460)
  ([61cc45a](https://github.com/seedcase-project/seedcase-sprout/commit/61cc45a70e46a37d7a674848d1ffec060de35f12))
- Add OSSF badge
  [#1466](https://github.com/seedcase-project/seedcase-sprout/pull/1466)
  ([fc88fb6](https://github.com/seedcase-project/seedcase-sprout/commit/fc88fb6a04fed460799d27a63587a1eb358c1c1e))
- Update install guide to use PyPI version
  [#1463](https://github.com/seedcase-project/seedcase-sprout/pull/1463)
  ([750e157](https://github.com/seedcase-project/seedcase-sprout/commit/750e1578d73358ca3e4c25db9c755dfbc3296e8a))
- Need `?raw=true` at end of badge image link
  [#1472](https://github.com/seedcase-project/seedcase-sprout/pull/1472)
  ([5f35a0b](https://github.com/seedcase-project/seedcase-sprout/commit/5f35a0b580087993650df024125a2a5a7d407491))

### 🧹 Chores

- *(sync)* Synced file(s) with seedcase-project/template-python-package
  ([8df35cd](https://github.com/seedcase-project/seedcase-sprout/commit/8df35cdc32c43cdf49e4f4b7b667591a60c74f26))
- *(sync)* Synced file(s) with seedcase-project/template-python-package
  ([7ce555e](https://github.com/seedcase-project/seedcase-sprout/commit/7ce555e03407efdd014c94c0a2df2188c22ff272))
- *(sync)* Synced file(s) with seedcase-project/template-python-package
  ([2928948](https://github.com/seedcase-project/seedcase-sprout/commit/292894888df31f59c8eb773810adbd022064b762))
- *(sync)* Synced file(s) with seedcase-project/template-python-package
  ([0675e13](https://github.com/seedcase-project/seedcase-sprout/commit/0675e1310d7cc382c1ff84a20dfd565aae11a7a6))
- *(sync)* Synced file(s) with seedcase-project/template-python-package
  ([6fe4941](https://github.com/seedcase-project/seedcase-sprout/commit/6fe4941e9818fe36b4f4b18b4c70103ac3e5e01b))
- Add ORCID for Signe
  [#1474](https://github.com/seedcase-project/seedcase-sprout/pull/1474)
  ([18eeeea](https://github.com/seedcase-project/seedcase-sprout/commit/18eeeeaa148d205ca49110f234eee31a2d0f848b))

## [0.46.3](https://github.com/seedcase-project/seedcase-sprout/compare/0.46.2..0.46.3) - 2025-07-03

### ♻️ Refactor

- Move `_get_nested_attr()` into internals
  [#1455](https://github.com/seedcase-project/seedcase-sprout/pull/1455)
  ([3ca0fce](https://github.com/seedcase-project/seedcase-sprout/commit/3ca0fce8e3d8999931b46458cea7df4751868832))

### 📝 Documentation

- Rename leftovers and move `field_properties` into `ResourceProperties`
  [#1446](https://github.com/seedcase-project/seedcase-sprout/pull/1446)
  ([916ad1a](https://github.com/seedcase-project/seedcase-sprout/commit/916ad1af20139278320f6677e82092317b656945))
- Use correct command in docstring
  [#1453](https://github.com/seedcase-project/seedcase-sprout/pull/1453)
  ([c8fa03b](https://github.com/seedcase-project/seedcase-sprout/commit/c8fa03bc966c8e68f22e416cfaf6df551cce97cc))
- Update resource guide
  [#1449](https://github.com/seedcase-project/seedcase-sprout/pull/1449)
  ([b91937a](https://github.com/seedcase-project/seedcase-sprout/commit/b91937a0385d4d030e624ba78a401b6b23224780))
- Update the flow docs to match latest changes
  [#1452](https://github.com/seedcase-project/seedcase-sprout/pull/1452)
  ([bcd19a4](https://github.com/seedcase-project/seedcase-sprout/commit/bcd19a4fc566df82b6697eded338443749351aa0))
- Need code to create `resource_properties_patients` object
  [#1458](https://github.com/seedcase-project/seedcase-sprout/pull/1458)
  ([4d93dce](https://github.com/seedcase-project/seedcase-sprout/commit/4d93dce52d0406abc8ebb22e1e451d99b9babaf6))

### 🧱 Build system

- Should be `patients`, not `patient`
  [#1447](https://github.com/seedcase-project/seedcase-sprout/pull/1447)
  ([ebc49ba](https://github.com/seedcase-project/seedcase-sprout/commit/ebc49baa6bbc108f3365ca678289b87c72cf4092))
- Don't need warning about docs being "experimental"
  [#1451](https://github.com/seedcase-project/seedcase-sprout/pull/1451)
  ([3b38d4d](https://github.com/seedcase-project/seedcase-sprout/commit/3b38d4d7314710d81f684ecc1970151436604cde))
- Update dependency versions in uv lock and pre-commit
  [#1454](https://github.com/seedcase-project/seedcase-sprout/pull/1454)
  ([0fff19c](https://github.com/seedcase-project/seedcase-sprout/commit/0fff19c41be5cbc84429b5a92a6627c4a0cdc43c))

### 🧹 Chores

- *(sync)* Synced file(s) with seedcase-project/template-python-package
  ([6d0bca4](https://github.com/seedcase-project/seedcase-sprout/commit/6d0bca45728119fa3c47af31b0f92754606c7acb))
- *(sync)* Synced file(s) with seedcase-project/template-python-package
  ([de9913c](https://github.com/seedcase-project/seedcase-sprout/commit/de9913ca53d351a4b98b20b4896abdcf9017dfcf))
- *(sync)* Synced file(s) with seedcase-project/seedcase-theme
  ([ed1dff4](https://github.com/seedcase-project/seedcase-sprout/commit/ed1dff487af8f0ab06d6c35aba14b2a3fc055f31))

## [0.46.2](https://github.com/seedcase-project/seedcase-sprout/compare/0.46.1..0.46.2) - 2025-06-30

### ♻️ Refactor

- Simplify extraction to field properties only
  [#1443](https://github.com/seedcase-project/seedcase-sprout/pull/1443)
  ([25682a0](https://github.com/seedcase-project/seedcase-sprout/commit/25682a009fb1a80de374eab88e7be9910703f7ae))

## [0.46.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.46.0..0.46.1) - 2025-06-30

### 🐛 Fixes

- Fix `mypy` errors in strict mode
  [#1437](https://github.com/seedcase-project/seedcase-sprout/pull/1437)
  ([1c47aa7](https://github.com/seedcase-project/seedcase-sprout/commit/1c47aa70f7a0c054a743a72b4794418c62838b48))

## [0.46.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.45.2..0.46.0) - 2025-06-26

### ✨ Features

- Add `read_resource_data()`
  [#1433](https://github.com/seedcase-project/seedcase-sprout/pull/1433)
  ([4282057](https://github.com/seedcase-project/seedcase-sprout/commit/4282057fc29a718debc1dd8eeef7885c10fadcc3))

### 📝 Documentation

- Link to Code of Conduct in README
  [#1434](https://github.com/seedcase-project/seedcase-sprout/pull/1434)
  ([83c61b0](https://github.com/seedcase-project/seedcase-sprout/commit/83c61b0bedb82ebfcef5389de5ee18bcd82b28b2))
- Move contributing text into own file
  [#1436](https://github.com/seedcase-project/seedcase-sprout/pull/1436)
  ([edc46bd](https://github.com/seedcase-project/seedcase-sprout/commit/edc46bdf27a18f137ee0b5418f3a3bac85822c9f))

## [0.45.2](https://github.com/seedcase-project/seedcase-sprout/compare/0.45.1..0.45.2) - 2025-06-26

### ♻️ Refactor

- Raise error for non-Parquet batch files
  [#1428](https://github.com/seedcase-project/seedcase-sprout/pull/1428)
  ([c0599c7](https://github.com/seedcase-project/seedcase-sprout/commit/c0599c7341df29e64734001eeafe07b7eaff69cc))

### 📝 Documentation

- Update package creation guide to match new flow
  [#1386](https://github.com/seedcase-project/seedcase-sprout/pull/1386)
  ([ba54d74](https://github.com/seedcase-project/seedcase-sprout/commit/ba54d747f569fcd2958d6dccac369f2f2173791b))
- List contributors in overview page
  [#1421](https://github.com/seedcase-project/seedcase-sprout/pull/1421)
  ([41b0da6](https://github.com/seedcase-project/seedcase-sprout/commit/41b0da6d62b3930c70b457c74a6ee0a6ede646e7))
- Corrected docstring formatting issues
  [#1420](https://github.com/seedcase-project/seedcase-sprout/pull/1420)
  ([01dd284](https://github.com/seedcase-project/seedcase-sprout/commit/01dd284be98ae8c2b4866d28578a4cd0cbc1d7e9))
- README as qmd to include badges and citation
  [#1419](https://github.com/seedcase-project/seedcase-sprout/pull/1419)
  ([a039b9f](https://github.com/seedcase-project/seedcase-sprout/commit/a039b9f407b00d7157f0ce982a8c62d44b8105a2))
- Refine the purpose and description in landing page
  [#1418](https://github.com/seedcase-project/seedcase-sprout/pull/1418)
  ([ad1dd1c](https://github.com/seedcase-project/seedcase-sprout/commit/ad1dd1c5f235ea7af758d868b6933fbcc3921763))
- Standardise the docstring language
  [#1422](https://github.com/seedcase-project/seedcase-sprout/pull/1422)
  ([e7de3f7](https://github.com/seedcase-project/seedcase-sprout/commit/e7de3f74990db53a39346eae20d5b031eb93e17f))
- Add supported python and repostatus badges
  [#1432](https://github.com/seedcase-project/seedcase-sprout/pull/1432)
  ([27bdb43](https://github.com/seedcase-project/seedcase-sprout/commit/27bdb43ffc714ea176f5d44509e3d69fcc04ff61))

### 👷 CI/CD

- Update workflow to release to PyPI
  [#1425](https://github.com/seedcase-project/seedcase-sprout/pull/1425)
  ([73bb847](https://github.com/seedcase-project/seedcase-sprout/commit/73bb847d29553ed00ed8804bbd4f94187b50a1a2))

### 🧹 Chores

- *(sync)* Synced file(s) with seedcase-project/seedcase-theme
  [#1426](https://github.com/seedcase-project/seedcase-sprout/pull/1426)
  ([3c93346](https://github.com/seedcase-project/seedcase-sprout/commit/3c93346cec5c6ee5d54537f1c5c2e8e38f466914))
- *(sync)* Synced file(s) with seedcase-project/template-python-package
  [#1435](https://github.com/seedcase-project/seedcase-sprout/pull/1435)
  ([66980a0](https://github.com/seedcase-project/seedcase-sprout/commit/66980a059fdf570e3af9febfad9a43eb00e22c85))

## [0.45.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.45.0..0.45.1) - 2025-06-24

### ♻️ Refactor

- Convert to internal functions with `_` prefix
  [#1423](https://github.com/seedcase-project/seedcase-sprout/pull/1423)
  ([8f20b0d](https://github.com/seedcase-project/seedcase-sprout/commit/8f20b0d51431352c5b0300f3f0ca15e57ffaca60))

### 📝 Documentation

- Add releases and changelog to website
  [#1407](https://github.com/seedcase-project/seedcase-sprout/pull/1407)
  ([40fd06b](https://github.com/seedcase-project/seedcase-sprout/commit/40fd06b2b62f7b83ce05bd4e2f1b026cee2d960e))
- Add overview page with "what and why Sprout"
  [#1412](https://github.com/seedcase-project/seedcase-sprout/pull/1412)
  ([2d9e009](https://github.com/seedcase-project/seedcase-sprout/commit/2d9e009f93c4bce5cd3bd6e99fc3345ad8ec3117))
- Include badges on landing page
  [#1413](https://github.com/seedcase-project/seedcase-sprout/pull/1413)
  ([404200b](https://github.com/seedcase-project/seedcase-sprout/commit/404200b3e7a5af899b54d2e4ca09b1f5313a8fe0))
- Update README to include more information
  [#1414](https://github.com/seedcase-project/seedcase-sprout/pull/1414)
  ([2fa64b3](https://github.com/seedcase-project/seedcase-sprout/commit/2fa64b3b43211625092ee4f1817395678b40fc5e))
- Glossary wasn't rendering so used Polars instead
  [#1416](https://github.com/seedcase-project/seedcase-sprout/pull/1416)
  ([e4ec28b](https://github.com/seedcase-project/seedcase-sprout/commit/e4ec28b9feda794a4d72e79ea72331b20d0907bb))

### 🧹 Chores

- Add `CITATION.cff` file
  [#1405](https://github.com/seedcase-project/seedcase-sprout/pull/1405)
  ([b98fa16](https://github.com/seedcase-project/seedcase-sprout/commit/b98fa1688cb61e96c3756fdb04597806a2e727a1))

## [0.45.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.44.12..0.45.0) - 2025-06-23

### ✨ Features

- Add resource properties template
  [#1369](https://github.com/seedcase-project/seedcase-sprout/pull/1369)
  ([f18a2e4](https://github.com/seedcase-project/seedcase-sprout/commit/f18a2e48c1ac7b59f41628f3ac7af2aad0f928e4))

### 📝 Documentation

- Edit Flows page
  [#1400](https://github.com/seedcase-project/seedcase-sprout/pull/1400)
  ([701da18](https://github.com/seedcase-project/seedcase-sprout/commit/701da183b0333c03a37d8ec294be66a4d698a658))

## [0.44.12](https://github.com/seedcase-project/seedcase-sprout/compare/0.44.11..0.44.12) - 2025-06-23

### ♻️ Refactor

- Set up mypy and fix issues from it
  [#1403](https://github.com/seedcase-project/seedcase-sprout/pull/1403)
  ([bf4a598](https://github.com/seedcase-project/seedcase-sprout/commit/bf4a598b41f51dc023c326cf1e824d20eff3c290))

## [0.44.11](https://github.com/seedcase-project/seedcase-sprout/compare/0.44.10..0.44.11) - 2025-06-23

### ♻️ Refactor

- Change `fields_match` type to list
  [#1410](https://github.com/seedcase-project/seedcase-sprout/pull/1410)
  ([da17c73](https://github.com/seedcase-project/seedcase-sprout/commit/da17c73946b0ae77aa39bbf4a73283111f9fee8d))

### 📝 Documentation

- Add more badges to README
  [#1409](https://github.com/seedcase-project/seedcase-sprout/pull/1409)
  ([7d54a12](https://github.com/seedcase-project/seedcase-sprout/commit/7d54a121613960b702f056458684c8a59480a014))

## [0.44.10](https://github.com/seedcase-project/seedcase-sprout/compare/0.44.9..0.44.10) - 2025-06-20

### 🐛 Fixes

- Change `fields_match` to be an array in `extract_resource_properties()`
  [#1392](https://github.com/seedcase-project/seedcase-sprout/pull/1392)
  ([cebf1f1](https://github.com/seedcase-project/seedcase-sprout/commit/cebf1f1c3c908f8a9e7d7b7fccae0f3d5ae94571))

### 📝 Documentation

- Edit design intro section
  [#1398](https://github.com/seedcase-project/seedcase-sprout/pull/1398)
  ([1fdac8f](https://github.com/seedcase-project/seedcase-sprout/commit/1fdac8f076cadc39bbc5b536bddd24b3d24e835a))
- Update install guide to refer to template, but use uv
  [#1378](https://github.com/seedcase-project/seedcase-sprout/pull/1378)
  ([959c7a0](https://github.com/seedcase-project/seedcase-sprout/commit/959c7a0520841c97029212d97baa881607b73c9e))
- Edit interface index, inputs, and outputs page
  [#1399](https://github.com/seedcase-project/seedcase-sprout/pull/1399)
  ([5418303](https://github.com/seedcase-project/seedcase-sprout/commit/5418303ca0858b0558bf7fc95c42acdd2594d328))
- Edit architecture docs
  [#1394](https://github.com/seedcase-project/seedcase-sprout/pull/1394)
  ([5e76569](https://github.com/seedcase-project/seedcase-sprout/commit/5e76569e73420a1bfb1fa0eba8d261ab297abd66))

## [0.44.9](https://github.com/seedcase-project/seedcase-sprout/compare/0.44.8..0.44.9) - 2025-06-19

### 🐛 Fixes

- Use a temp folder in example code
  [#1396](https://github.com/seedcase-project/seedcase-sprout/pull/1396)
  ([a35de53](https://github.com/seedcase-project/seedcase-sprout/commit/a35de539d233aaa7f4ac4330a5df50d3ba724301))

### 📝 Documentation

- Link to raw sprout logo
  [#1402](https://github.com/seedcase-project/seedcase-sprout/pull/1402)
  ([0716711](https://github.com/seedcase-project/seedcase-sprout/commit/0716711fc69c16fe373847c7836d6ff063b7abda))
- Edit Functions page
  [#1401](https://github.com/seedcase-project/seedcase-sprout/pull/1401)
  ([32490ee](https://github.com/seedcase-project/seedcase-sprout/commit/32490ee2f213a7f0c96af1e2eb67f380964f3d7a))

### 🧹 Chores

- Remove unused function
  [#1397](https://github.com/seedcase-project/seedcase-sprout/pull/1397)
  ([ae6b7fe](https://github.com/seedcase-project/seedcase-sprout/commit/ae6b7feeafed6b4cf822478271d49db0ed637485))

## [0.44.8](https://github.com/seedcase-project/seedcase-sprout/compare/0.44.7..0.44.8) - 2025-06-12

### ♻️ Refactor

- Don't overwrite the `properties.py` script
  [#1383](https://github.com/seedcase-project/seedcase-sprout/pull/1383)
  ([ee9f738](https://github.com/seedcase-project/seedcase-sprout/commit/ee9f738a6454fb2a4446a823ec62d4dfd8d97066))

### 📝 Documentation

- Clarify landing page text about Sprout
  [#1391](https://github.com/seedcase-project/seedcase-sprout/pull/1391)
  ([a6f6f26](https://github.com/seedcase-project/seedcase-sprout/commit/a6f6f268489ccdea9c170eaba22f22227301640d))

### 🧹 Chores

- Remove commented code we won't create
  [#1381](https://github.com/seedcase-project/seedcase-sprout/pull/1381)
  ([e130ce5](https://github.com/seedcase-project/seedcase-sprout/commit/e130ce5e98728eeb574b0cac06d4cdfbad5eacc1))

## [0.44.7](https://github.com/seedcase-project/seedcase-sprout/compare/0.44.6..0.44.7) - 2025-06-11

### ♻️ Refactor

- Import from `internals` only, not sub-modules of it
  [#1382](https://github.com/seedcase-project/seedcase-sprout/pull/1382)
  ([9c76642](https://github.com/seedcase-project/seedcase-sprout/commit/9c76642f46ba35279f0d2878ff9c900400f0d353))

### 🧱 Build system

- Fix name to `create_properties_script` in `_quarto.yml`
  [#1379](https://github.com/seedcase-project/seedcase-sprout/pull/1379)
  ([daedd15](https://github.com/seedcase-project/seedcase-sprout/commit/daedd15178412ac8f029f0441281a07958073dde))

## [0.44.6](https://github.com/seedcase-project/seedcase-sprout/compare/0.44.5..0.44.6) - 2025-06-11

### 🐛 Fixes

- Use camel case in JSON dict
  [#1389](https://github.com/seedcase-project/seedcase-sprout/pull/1389)
  ([a1635e9](https://github.com/seedcase-project/seedcase-sprout/commit/a1635e9c77d1b29fef567622687b35bb391c5c65))

## [0.44.5](https://github.com/seedcase-project/seedcase-sprout/compare/0.44.4..0.44.5) - 2025-06-10

### ♻️ Refactor

- Re-export pprint and textwrap
  [#1385](https://github.com/seedcase-project/seedcase-sprout/pull/1385)
  ([6ff38ff](https://github.com/seedcase-project/seedcase-sprout/commit/6ff38ffa98a0f6120dad2f0c4e83741b4c01ec8f))

### 📝 Documentation

- Parameter docstring needs to be indented
  [#1384](https://github.com/seedcase-project/seedcase-sprout/pull/1384)
  ([9935afa](https://github.com/seedcase-project/seedcase-sprout/commit/9935afaba8cef04b578fb2da38ca0d12e0d4d59e))

## [0.44.4](https://github.com/seedcase-project/seedcase-sprout/compare/0.44.3..0.44.4) - 2025-06-10

### 🐛 Fixes

- Forgot to quote the function in `__all__.py`
  [#1380](https://github.com/seedcase-project/seedcase-sprout/pull/1380)
  ([d53c092](https://github.com/seedcase-project/seedcase-sprout/commit/d53c09207010976451381b870e3960c3b4c5e8fd))

### 👷 CI/CD

- Remove old scorecard
  [#1388](https://github.com/seedcase-project/seedcase-sprout/pull/1388)
  ([7841b61](https://github.com/seedcase-project/seedcase-sprout/commit/7841b617123b9cf5823d929a140d790b9965a04a))

### 🧹 Chores

- *(sync)* Synced file(s) with seedcase-project/template-python-package
  ([6aa9f50](https://github.com/seedcase-project/seedcase-sprout/commit/6aa9f5005fa23150b8818748ff141ec0938d2796))

## [0.44.3](https://github.com/seedcase-project/seedcase-sprout/compare/0.44.2..0.44.3) - 2025-06-06

### ♻️ Refactor

- Rename to properties_script
  [#1375](https://github.com/seedcase-project/seedcase-sprout/pull/1375)
  ([5f067cb](https://github.com/seedcase-project/seedcase-sprout/commit/5f067cbd551ae3391e2fa2b4805ae2acd630eb36))

## [0.44.2](https://github.com/seedcase-project/seedcase-sprout/compare/0.44.1..0.44.2) - 2025-06-06

### ♻️ Refactor

- Remove `MissingValueProperties`
  [#1374](https://github.com/seedcase-project/seedcase-sprout/pull/1374)
  ([38d2250](https://github.com/seedcase-project/seedcase-sprout/commit/38d2250884bd804ae1c8b585051713c7f3655fe3))

## [0.44.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.44.0..0.44.1) - 2025-06-03

### ♻️ Refactor

- Simplify to only `write_properties()`
  [#1366](https://github.com/seedcase-project/seedcase-sprout/pull/1366)
  ([75fdb96](https://github.com/seedcase-project/seedcase-sprout/commit/75fdb9648e080d5ae56871d67424f7e9b4d275f8))

### 📝 Documentation

- Design of `read_resource_data()`
  [#1351](https://github.com/seedcase-project/seedcase-sprout/pull/1351)
  ([7dd3e74](https://github.com/seedcase-project/seedcase-sprout/commit/7dd3e74161abc798f7b62869c1ecd986f3594409))

### 🧱 Build system

- Re-arrange the reference sidebar to be a bit cleaner
  [#1349](https://github.com/seedcase-project/seedcase-sprout/pull/1349)
  ([880f477](https://github.com/seedcase-project/seedcase-sprout/commit/880f4771bdd42e1775f9e299282e76dc71582053))
- Update quartodoc config with current functions
  [#1365](https://github.com/seedcase-project/seedcase-sprout/pull/1365)
  ([3a43f1e](https://github.com/seedcase-project/seedcase-sprout/commit/3a43f1e5f49fa1ea577cd1491233ed4d57b62c9e))
- Add jinja2 dependency explicitly
  [#1372](https://github.com/seedcase-project/seedcase-sprout/pull/1372)
  ([3cb3980](https://github.com/seedcase-project/seedcase-sprout/commit/3cb398045338765297c1306d852b51e010832105))

### 🧹 Chores

- *(sync)* Synced file(s) with seedcase-project/seedcase-theme
  ([f5646db](https://github.com/seedcase-project/seedcase-sprout/commit/f5646db3552ca98eea8069f52f9eaa21bb442391))

## [0.44.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.43.6..0.44.0) - 2025-05-30

### ✨ Features

- Add properties template
  [#1345](https://github.com/seedcase-project/seedcase-sprout/pull/1345)
  ([ca6d006](https://github.com/seedcase-project/seedcase-sprout/commit/ca6d0060bcbf6deff9b0b1408a2a074ba138c472))

## [0.43.6](https://github.com/seedcase-project/seedcase-sprout/compare/0.43.5..0.43.6) - 2025-05-28

### ♻️ Refactor

- Simplify and move into internals
  [#1348](https://github.com/seedcase-project/seedcase-sprout/pull/1348)
  ([35ccd27](https://github.com/seedcase-project/seedcase-sprout/commit/35ccd271244893670a173dd592b9c68b693e039f))

### 📝 Documentation

- Update package guide and remove update section
  [#1357](https://github.com/seedcase-project/seedcase-sprout/pull/1357)
  ([7f5aa5f](https://github.com/seedcase-project/seedcase-sprout/commit/7f5aa5f6b3c305e81351422297630dd03c1a3ca1))

## [0.43.5](https://github.com/seedcase-project/seedcase-sprout/compare/0.43.4..0.43.5) - 2025-05-28

### ♻️ Refactor

- Remove `update_package_properties()` and revise docs
  [#1355](https://github.com/seedcase-project/seedcase-sprout/pull/1355)
  ([ef58bfd](https://github.com/seedcase-project/seedcase-sprout/commit/ef58bfdc2a0fb8473cc709fd9fb41563d3d2f014))

### 📝 Documentation

- Simplify installation guide
  [#1347](https://github.com/seedcase-project/seedcase-sprout/pull/1347)
  ([3235fbe](https://github.com/seedcase-project/seedcase-sprout/commit/3235fbeb017b658264c3760b9e43bea9b75c59b8))
- Remove versioning naming of data packages
  [#1350](https://github.com/seedcase-project/seedcase-sprout/pull/1350)
  ([04ddb64](https://github.com/seedcase-project/seedcase-sprout/commit/04ddb6468fed926b98fcf2b0368923dc6b04ef2f))
- Remove functions to delete things
  [#1353](https://github.com/seedcase-project/seedcase-sprout/pull/1353)
  ([8a926a1](https://github.com/seedcase-project/seedcase-sprout/commit/8a926a1cc74565968de80f02da36a9b08f06e115))
- Convert functions to 'done' status
  [#1352](https://github.com/seedcase-project/seedcase-sprout/pull/1352)
  ([a136fa2](https://github.com/seedcase-project/seedcase-sprout/commit/a136fa215e42258b77252794519fb5a62de95905))
- Clean up the CHANGELOG
  [#1356](https://github.com/seedcase-project/seedcase-sprout/pull/1356)
  ([44e711e](https://github.com/seedcase-project/seedcase-sprout/commit/44e711e0a2d7ff34a8589729a8f1bc1d14e143f2))

## [0.43.4](https://github.com/seedcase-project/seedcase-sprout/compare/0.43.3..0.43.4) - 2025-05-27

### ♻️ Refactor

- Simplify and make `check_datapackage` self-contained
  [#1342](https://github.com/seedcase-project/seedcase-sprout/pull/1342)
  ([795fa77](https://github.com/seedcase-project/seedcase-sprout/commit/795fa77ab7187cdf28c76e90bd26f6062db6287d))

### 📝 Documentation

- "tutorials" -> "guide"
  [#1337](https://github.com/seedcase-project/seedcase-sprout/pull/1337)
  ([1dc3ba8](https://github.com/seedcase-project/seedcase-sprout/commit/1dc3ba82c2f0afe4bd3c2adbb4e59f25af8165d9))

### 🧹 Chores

- *(sync)* Synced file(s) with seedcase-project/seedcase-theme
  ([910dc96](https://github.com/seedcase-project/seedcase-sprout/commit/910dc9647ece734f738d4d527f5daccf81f176fc))
- *(sync)* Synced file(s) with seedcase-project/seedcase-theme
  ([1fa54ff](https://github.com/seedcase-project/seedcase-sprout/commit/1fa54ff6d012a8bb4ba3b02de3f84008b90b964e))
- *(sync)* Synced file(s) with seedcase-project/template-python-package
  ([9c88643](https://github.com/seedcase-project/seedcase-sprout/commit/9c88643633d58e9e0354f882b48ab6aed98db3fe))
- Remove leftover code
  [#1341](https://github.com/seedcase-project/seedcase-sprout/pull/1341)
  ([b20c989](https://github.com/seedcase-project/seedcase-sprout/commit/b20c9890516b34cfefe3871fffbf39e2eb1a525d))

## [0.43.3](https://github.com/seedcase-project/seedcase-sprout/compare/0.43.2..0.43.3) - 2025-05-22

### ♻️ Refactor

- Remove `core` folders
  [#1336](https://github.com/seedcase-project/seedcase-sprout/pull/1336)
  ([c167176](https://github.com/seedcase-project/seedcase-sprout/commit/c16717670e8e7e1108ad85af3da41809a3d877ed))

## [0.43.2](https://github.com/seedcase-project/seedcase-sprout/compare/0.43.1..0.43.2) - 2025-05-22

### ♻️ Refactor

- Action of `create_resource_structure()` into `write_resource_batch()`
  [#1295](https://github.com/seedcase-project/seedcase-sprout/pull/1295)
  ([9172284](https://github.com/seedcase-project/seedcase-sprout/commit/91722846a5ed2310e4e7811bb43928642a1dd00d))

## [0.43.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.43.0..0.43.1) - 2025-05-21

### ♻️ Refactor

- Update `extract_resource_properties()` to take `pl.DataFrame`
  [#1264](https://github.com/seedcase-project/seedcase-sprout/pull/1264)
  ([d6861a7](https://github.com/seedcase-project/seedcase-sprout/commit/d6861a723a3d58b2f3540446cc80846512ac2ac3))

## [0.43.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.42.5..0.43.0) - 2025-05-21

### ✨ Features

- Add custom package name to `ExamplePackage`
  [#1309](https://github.com/seedcase-project/seedcase-sprout/pull/1309)
  ([910b867](https://github.com/seedcase-project/seedcase-sprout/commit/910b8671d15aa1b7e867daa5f3c6c6cedc63c9cc))

### 🧱 Build system

- Build PDF locally
  [#1325](https://github.com/seedcase-project/seedcase-sprout/pull/1325)
  ([cceef56](https://github.com/seedcase-project/seedcase-sprout/commit/cceef56e34909fe1bb828df3f7f1918362c739dc))
- Update the vulture recipe
  [#1335](https://github.com/seedcase-project/seedcase-sprout/pull/1335)
  ([def26a1](https://github.com/seedcase-project/seedcase-sprout/commit/def26a153f338fef5773ebb1e17b65da2cc18e8c))

### 🧹 Chores

- *(sync)* Synced file(s) with seedcase-project/seedcase-theme
  ([107c6be](https://github.com/seedcase-project/seedcase-sprout/commit/107c6bef5114e9fc62372691e36ad06ff352fabc))
- *(sync)* Synced file(s) with seedcase-project/template-python-package
  ([8cd5191](https://github.com/seedcase-project/seedcase-sprout/commit/8cd519141ff98a4a165b79b4576ec4f70d8eec70))

## [0.42.5](https://github.com/seedcase-project/seedcase-sprout/compare/0.42.4..0.42.5) - 2025-05-19

### 🐛 Fixes

- Raise a more informative error when the data list is empty
  [#1308](https://github.com/seedcase-project/seedcase-sprout/pull/1308)
  ([0f93d3f](https://github.com/seedcase-project/seedcase-sprout/commit/0f93d3f9c976bb561a92b4173eb33219f1d4b651))

### 🧱 Build system

- Add `vulture` to `dev` with `just` recipe to check for unused code
  [#1330](https://github.com/seedcase-project/seedcase-sprout/pull/1330)
  ([190ed93](https://github.com/seedcase-project/seedcase-sprout/commit/190ed93d61f4577850848b47ae62efc52f6271ac))

### 🧹 Chores

- *(sync)* Synced file(s) with seedcase-project/template-python-package
  ([384678a](https://github.com/seedcase-project/seedcase-sprout/commit/384678a3f344c30f8daa9739f150a8709a3841fa))
- *(sync)* Synced file(s) with seedcase-project/seedcase-theme
  ([7235d51](https://github.com/seedcase-project/seedcase-sprout/commit/7235d511e5c32e0218a418807ff850b143ed385c))

## [0.42.4](https://github.com/seedcase-project/seedcase-sprout/compare/0.42.3..0.42.4) - 2025-05-13

### 🐛 Fixes

- Resolve temp paths so tests pass on MacOS as well
  [#1322](https://github.com/seedcase-project/seedcase-sprout/pull/1322)
  ([c177369](https://github.com/seedcase-project/seedcase-sprout/commit/c1773694a0789fb27088eb3a0d5ed9463065572f))

### 🧹 Chores

- *(sync)* Synced local '.pre-commit-config.yaml' with remote
  '.pre-commit-config.yaml'
  ([4861874](https://github.com/seedcase-project/seedcase-sprout/commit/48618742dc513695d290d53a2d83643f4e18d66e))
- *(sync)* Synced local '.github/workflows/update-version.yml' with remote
  '.github/workflows/update-version.yml'
  ([65578f9](https://github.com/seedcase-project/seedcase-sprout/commit/65578f9d1f4b01fff797e425675cb7bb1ac2d141))

## [0.42.3](https://github.com/seedcase-project/seedcase-sprout/compare/0.42.2..0.42.3) - 2025-05-01

### ♻️ Refactor

- Have a default method only for `PackageProperties`
  [#1304](https://github.com/seedcase-project/seedcase-sprout/pull/1304)
  ([6474fe4](https://github.com/seedcase-project/seedcase-sprout/commit/6474fe4f590231f3a58ab1dcadbbe2cbd41da2d4))

### 👷 CI/CD

- Add security code scanning workflow
  [#1306](https://github.com/seedcase-project/seedcase-sprout/pull/1306)
  ([180f32c](https://github.com/seedcase-project/seedcase-sprout/commit/180f32c7d6aecaf53a6a8571787c4584a4ec64a5))

## [0.42.2](https://github.com/seedcase-project/seedcase-sprout/compare/0.42.1..0.42.2) - 2025-04-30

### 🐛 Fixes

- Do not escape non-ASCII characters when writing JSON
  [#1305](https://github.com/seedcase-project/seedcase-sprout/pull/1305)
  ([e75489b](https://github.com/seedcase-project/seedcase-sprout/commit/e75489b00f7c6abd96534d544e851f86b903bba9))

## [0.42.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.42.0..0.42.1) - 2025-04-25

### ♻️ Refactor

- Use `ExamplePackage` in examples
  [#1301](https://github.com/seedcase-project/seedcase-sprout/pull/1301)
  ([a9ba645](https://github.com/seedcase-project/seedcase-sprout/commit/a9ba645a7fa69e6dd28b98728a6a9692e0b265eb))

## [0.42.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.41.2..0.42.0) - 2025-04-25

### ✨ Features

- `write_resource_data()`
  [#1302](https://github.com/seedcase-project/seedcase-sprout/pull/1302)
  ([13359c3](https://github.com/seedcase-project/seedcase-sprout/commit/13359c3aaa143bfc74fd6b3824fc335b7ecca520))

## [0.41.2](https://github.com/seedcase-project/seedcase-sprout/compare/0.41.1..0.41.2) - 2025-04-24

### ♻️ Refactor

- Moved functions into internals/location of use
  [#1298](https://github.com/seedcase-project/seedcase-sprout/pull/1298)
  ([62bdc55](https://github.com/seedcase-project/seedcase-sprout/commit/62bdc5522f0cf7c9fbaebca50e064f99fdd85f4b))

### 🧱 Build system

- Add auto-spell checker
  [#1299](https://github.com/seedcase-project/seedcase-sprout/pull/1299)
  ([3b2604d](https://github.com/seedcase-project/seedcase-sprout/commit/3b2604d2831887dc0801be427c6e9ff1d18bc0e7))

## [0.41.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.41.0..0.41.1) - 2025-04-24

### ♻️ Refactor

- Make master Frictionless - Polars type map
  [#1284](https://github.com/seedcase-project/seedcase-sprout/pull/1284)
  ([6077f2f](https://github.com/seedcase-project/seedcase-sprout/commit/6077f2f7a31d303f06fe8cfdeeb980b285302d28))

## [0.41.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.40.1..0.41.0) - 2025-04-23

### ✨ Features

- Add default path for path functions
  [#1285](https://github.com/seedcase-project/seedcase-sprout/pull/1285)
  ([26e6a3c](https://github.com/seedcase-project/seedcase-sprout/commit/26e6a3cb8b7711bb368efb0162a3bca8417b0968))

### 🧱 Build system

- Move pytest config to its own `pytest.ini` file
  [#1294](https://github.com/seedcase-project/seedcase-sprout/pull/1294)
  ([281ff87](https://github.com/seedcase-project/seedcase-sprout/commit/281ff87a9f66d40d500949c3094f3f77089f1225))

### 🧹 Chores

- Remove left over pseudocode file
  [#1296](https://github.com/seedcase-project/seedcase-sprout/pull/1296)
  ([d3cda9a](https://github.com/seedcase-project/seedcase-sprout/commit/d3cda9aa3b0da00d0eb1f79bc83ffeda6d066b1d))

## [0.40.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.40.0..0.40.1) - 2025-04-22

### 🐛 Fixes

- Fixed bandit flagged issues, moved dataclass gen into `tools/`
  [#1292](https://github.com/seedcase-project/seedcase-sprout/pull/1292)
  ([ab09a38](https://github.com/seedcase-project/seedcase-sprout/commit/ab09a387a39cdbac1d5cbdab67f56c6eb18fcc1b))

### 🧱 Build system

- Add coverage infrastructure and badge
  [#1289](https://github.com/seedcase-project/seedcase-sprout/pull/1289)
  ([caf5480](https://github.com/seedcase-project/seedcase-sprout/commit/caf548001efbd566b4af5afb5f4a31d98ea2478e))
- Add security checks
  [#1291](https://github.com/seedcase-project/seedcase-sprout/pull/1291)
  ([3244178](https://github.com/seedcase-project/seedcase-sprout/commit/324417862b1957bfaf5c862a5e0ad7518c667e13))

### 🧹 Chores

- *(sync)* Synced local '.gitignore' with remote '.gitignore'
  ([9d665af](https://github.com/seedcase-project/seedcase-sprout/commit/9d665af8d2128072c11d2fed0f8199ce5e094afe))
- *(sync)* Synced local 'justfile' with remote 'justfile'
  ([72f82ed](https://github.com/seedcase-project/seedcase-sprout/commit/72f82ed716be9b917de26bd40da9f4e87542bf77))
- *(sync)* Synced local '.github/workflows/build-package.yml' with remote
  '.github/workflows/build-package.yml'
  ([5b963f5](https://github.com/seedcase-project/seedcase-sprout/commit/5b963f5f649b94c802d7f8ca1853c620b4b4b6d3))
- *(sync)* Synced local 'justfile' with remote 'justfile'
  ([c4b6fcd](https://github.com/seedcase-project/seedcase-sprout/commit/c4b6fcdbf2caeed6bfa7a72a51d1199dc7dd8fd5))
- Delete unused file
  [#1286](https://github.com/seedcase-project/seedcase-sprout/pull/1286)
  ([f5919d0](https://github.com/seedcase-project/seedcase-sprout/commit/f5919d09e6169c74030c19e4253f17b4389c5539))

## [0.40.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.39.0..0.40.0) - 2025-04-16

### ✨ Features

- Only return `.parquet` files in the batch folder
  [#1283](https://github.com/seedcase-project/seedcase-sprout/pull/1283)
  ([ea66a77](https://github.com/seedcase-project/seedcase-sprout/commit/ea66a7753306d61fc07711606501049d4effe4b1))

## [0.39.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.38.3..0.39.0) - 2025-04-16

### ✨ Features

- Finish up `PackagePath` and `resource_batch_files()`
  [#1282](https://github.com/seedcase-project/seedcase-sprout/pull/1282)
  ([5b89d52](https://github.com/seedcase-project/seedcase-sprout/commit/5b89d52ec8587930a4a63d6ddcc3d5cdd6a8a994))

## [0.38.3](https://github.com/seedcase-project/seedcase-sprout/compare/0.38.2..0.38.3) - 2025-04-15

### ♻️ Refactor

- Move `check_properties.py` into root code folder
  [#1278](https://github.com/seedcase-project/seedcase-sprout/pull/1278)
  ([b040932](https://github.com/seedcase-project/seedcase-sprout/commit/b0409324ecea610a8c4ba5099bf41cc476f47123))

## [0.38.2](https://github.com/seedcase-project/seedcase-sprout/compare/0.38.1..0.38.2) - 2025-04-15

### ♻️ Refactor

- Move `cdp` constant into `constants.py`
  [#1279](https://github.com/seedcase-project/seedcase-sprout/pull/1279)
  ([7341a51](https://github.com/seedcase-project/seedcase-sprout/commit/7341a516b3b7c56085c28d27df9c773549bada41))

## [0.38.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.38.0..0.38.1) - 2025-04-15

### ♻️ Refactor

- Move all `check_data()` internals into same file
  [#1275](https://github.com/seedcase-project/seedcase-sprout/pull/1275)
  ([096e2da](https://github.com/seedcase-project/seedcase-sprout/commit/096e2da3e421d9d1a1115c2e3e59ded0c358fd6d))

## [0.38.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.37.1..0.38.0) - 2025-04-15

### ✨ Features

- Add example package
  [#1265](https://github.com/seedcase-project/seedcase-sprout/pull/1265)
  ([f454f99](https://github.com/seedcase-project/seedcase-sprout/commit/f454f99af1d62e83429165e9db950884c69c789f))

## [0.37.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.37.0..0.37.1) - 2025-04-15

### ♻️ Refactor

- Move `write_json()` into internals module
  [#1274](https://github.com/seedcase-project/seedcase-sprout/pull/1274)
  ([9358c7c](https://github.com/seedcase-project/seedcase-sprout/commit/9358c7cd262ca3636b823eef96cbafd820ad50de))

## [0.37.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.36.3..0.37.0) - 2025-04-15

### ✨ Features

- Add simple `root()` method in `PackagePath`
  [#1280](https://github.com/seedcase-project/seedcase-sprout/pull/1280)
  ([db676c4](https://github.com/seedcase-project/seedcase-sprout/commit/db676c406ccd264ad785310a286ae63054586f92))

### ♻️ Refactor

- Move `read_*` functions (one) into internal module
  [#1273](https://github.com/seedcase-project/seedcase-sprout/pull/1273)
  ([d539239](https://github.com/seedcase-project/seedcase-sprout/commit/d539239f750ecc66e7819c7310216d9923c6eff7))

### 🧹 Chores

- This function was not used
  [#1272](https://github.com/seedcase-project/seedcase-sprout/pull/1272)
  ([f455066](https://github.com/seedcase-project/seedcase-sprout/commit/f4550662fd525cd3575942a954624ddac9d20295))

## [0.36.3](https://github.com/seedcase-project/seedcase-sprout/compare/0.36.2..0.36.3) - 2025-04-15

### ♻️ Refactor

- Use `_map2()` in `read_resource_batches()`
  [#1276](https://github.com/seedcase-project/seedcase-sprout/pull/1276)
  ([efb0303](https://github.com/seedcase-project/seedcase-sprout/commit/efb03039048d078cf4aad510d5aa5fc8b718c270))

## [0.36.2](https://github.com/seedcase-project/seedcase-sprout/compare/0.36.1..0.36.2) - 2025-04-15

### ♻️ Refactor

- Move `check_is_*` into internal module
  [#1271](https://github.com/seedcase-project/seedcase-sprout/pull/1271)
  ([0cd27f2](https://github.com/seedcase-project/seedcase-sprout/commit/0cd27f289365e43c0e07dd4f18af2a1bc641a84f))

## [0.36.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.36.0..0.36.1) - 2025-04-15

### ♻️ Refactor

- Create a simpler map functional
  [#1270](https://github.com/seedcase-project/seedcase-sprout/pull/1270)
  ([0c77a10](https://github.com/seedcase-project/seedcase-sprout/commit/0c77a10eb3d6af4bdee665fd171541712d5d453f))

### 🧪 Tests

- Remove duplicate tests on `check_*` functionality
  [#1256](https://github.com/seedcase-project/seedcase-sprout/pull/1256)
  ([a99acdc](https://github.com/seedcase-project/seedcase-sprout/commit/a99acdc6f5124d5f72ad2f851290efff5ba4be4c))

### 🧱 Build system

- Needs to be numeric in order to build the website
  [#1269](https://github.com/seedcase-project/seedcase-sprout/pull/1269)
  ([ae3ddb2](https://github.com/seedcase-project/seedcase-sprout/commit/ae3ddb25f3238dc75600b9d3a9bc49aed67fb269))

## [0.36.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.35.0..0.36.0) - 2025-04-14

### ✨ Features

- `write_resource_batch()`
  [#1213](https://github.com/seedcase-project/seedcase-sprout/pull/1213)
  ([416914e](https://github.com/seedcase-project/seedcase-sprout/commit/416914e8a28af487748a54a6c0055fbec71a770a))

## [0.35.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.34.0..0.35.0) - 2025-04-14

### ✨ Features

- Get cwd at call time in `PackagePath`
  [#1266](https://github.com/seedcase-project/seedcase-sprout/pull/1266)
  ([7987067](https://github.com/seedcase-project/seedcase-sprout/commit/798706797322a7134dda8936d4369f8c949f6ce7))

## [0.34.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.33.0..0.34.0) - 2025-04-14

### ✨ Features

- `join_resource_batches()`
  [#1252](https://github.com/seedcase-project/seedcase-sprout/pull/1252)
  ([8e5c9d4](https://github.com/seedcase-project/seedcase-sprout/commit/8e5c9d4fca18d6384c784ef58e7a5db2bf192345))

## [0.33.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.32.2..0.33.0) - 2025-04-14

### ✨ Features

- Use `check_data()` in `read_resource_batches()`
  [#1263](https://github.com/seedcase-project/seedcase-sprout/pull/1263)
  ([ecc2787](https://github.com/seedcase-project/seedcase-sprout/commit/ecc27870fd6dde58bd6e11d1acb965d92eac8885))

## [0.32.2](https://github.com/seedcase-project/seedcase-sprout/compare/0.32.1..0.32.2) - 2025-04-11

### ♻️ Refactor

- Simplify imports and `__init__.py` file
  [#1257](https://github.com/seedcase-project/seedcase-sprout/pull/1257)
  ([51272b1](https://github.com/seedcase-project/seedcase-sprout/commit/51272b1eab5cd2ab5a235bb42723585d5c6a9420))

## [0.32.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.32.0..0.32.1) - 2025-04-11

### ♻️ Refactor

- Match `check_properties()` with design
  [#1255](https://github.com/seedcase-project/seedcase-sprout/pull/1255)
  ([26d9eb5](https://github.com/seedcase-project/seedcase-sprout/commit/26d9eb59a33559b54294b6a3762599f4d5724a64))

## [0.32.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.31.0..0.32.0) - 2025-04-11

### ✨ Features

- Check column names in `check_data()`
  [#1247](https://github.com/seedcase-project/seedcase-sprout/pull/1247)
  ([22b5e78](https://github.com/seedcase-project/seedcase-sprout/commit/22b5e78572266208c3b0e7bbfe3980316ddab8f0))

## [0.31.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.30.0..0.31.0) - 2025-04-11

### ✨ Features

- `check_data()` with column type checks
  [#1246](https://github.com/seedcase-project/seedcase-sprout/pull/1246)
  ([5820de1](https://github.com/seedcase-project/seedcase-sprout/commit/5820de1f269e917ff93214edb0ea625ecde3a670))

### 📝 Documentation

- Make resources guide run
  [#1200](https://github.com/seedcase-project/seedcase-sprout/pull/1200)
  ([2146e03](https://github.com/seedcase-project/seedcase-sprout/commit/2146e03c29d8c3c0e77aae4503ca05ae79e92aa3))
- `write_resource_batches()` -> `write_resource_batch()`
  [#1254](https://github.com/seedcase-project/seedcase-sprout/pull/1254)
  ([acd4ee1](https://github.com/seedcase-project/seedcase-sprout/commit/acd4ee1232d6d0674352ec9e9cbcbeda2af3e1ea))

### 🧱 Build system

- Switch to using uv, rather than poetry
  [#1248](https://github.com/seedcase-project/seedcase-sprout/pull/1248)
  ([e792d23](https://github.com/seedcase-project/seedcase-sprout/commit/e792d23e77fe637d0163717f4ab512ff311ea96c))
- Quarto seems to need pyyaml in GitHub workflow
  [#1251](https://github.com/seedcase-project/seedcase-sprout/pull/1251)
  ([50395eb](https://github.com/seedcase-project/seedcase-sprout/commit/50395eb80a7f2acf6a66efd31a7bb8c2afe9bf28))

### 🧹 Chores

- Delete old check column data types files
  [#1245](https://github.com/seedcase-project/seedcase-sprout/pull/1245)
  ([aac8120](https://github.com/seedcase-project/seedcase-sprout/commit/aac81206b62d833446d84788cdaa34df13a0587d))

## [0.30.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.29.1..0.30.0) - 2025-04-09

### ✨ Features

- Add example data frame
  [#1244](https://github.com/seedcase-project/seedcase-sprout/pull/1244)
  ([08bf704](https://github.com/seedcase-project/seedcase-sprout/commit/08bf70484cf47f23af6c5428a4e92465807ad82c))

### 🧹 Chores

- *(sync)* Synced local '.gitignore' with remote '.gitignore'
  ([ad63c1f](https://github.com/seedcase-project/seedcase-sprout/commit/ad63c1ff5120e2a812e8dc622e5e795d05a430c5))
- *(sync)* Synced local '.github/workflows/add-to-project.yml' with remote
  '.github/workflows/add-to-project.yml'
  ([7366b21](https://github.com/seedcase-project/seedcase-sprout/commit/7366b214d081b546b7597be5bc9f77518befa1cb))

## [0.29.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.29.0..0.29.1) - 2025-04-08

### 🐛 Fixes

- Update nested objects correctly
  [#1138](https://github.com/seedcase-project/seedcase-sprout/pull/1138)
  ([1a4e1e5](https://github.com/seedcase-project/seedcase-sprout/commit/1a4e1e5877d24511a416a8f31fcdd380c077ef60))

## [0.29.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.28.2..0.29.0) - 2025-04-07

### ✨ Features

- Add `read_resource_batches()` - without `check_data()`
  [#1201](https://github.com/seedcase-project/seedcase-sprout/pull/1201)
  ([81b7b13](https://github.com/seedcase-project/seedcase-sprout/commit/81b7b13afb2312f3e85a877b5ac302231c04a8c6))

### 📝 Documentation

- Revise to only accept tidy dataframes
  [#1204](https://github.com/seedcase-project/seedcase-sprout/pull/1204)
  ([532272d](https://github.com/seedcase-project/seedcase-sprout/commit/532272d1a4abf16d10adfe819d506ce1582ae2f5))

## [0.28.2](https://github.com/seedcase-project/seedcase-sprout/compare/0.28.1..0.28.2) - 2025-04-07

### ♻️ Refactor

- Clean split of `check_datapackage` sub-package
  [#1239](https://github.com/seedcase-project/seedcase-sprout/pull/1239)
  ([8ab50aa](https://github.com/seedcase-project/seedcase-sprout/commit/8ab50aa08a5ef7f7a168d43900801b32d687fd18))

### 📝 Documentation

- Add section on creating the README
  [#1207](https://github.com/seedcase-project/seedcase-sprout/pull/1207)
  ([72a738d](https://github.com/seedcase-project/seedcase-sprout/commit/72a738d016be58e768e0749a695f57c19e0f7abb))
- Pseudocode for `_check_column_names()`
  [#1194](https://github.com/seedcase-project/seedcase-sprout/pull/1194)
  ([bdba4b4](https://github.com/seedcase-project/seedcase-sprout/commit/bdba4b4e66590e898aed63e33d23e781c9882c6d))
- Flow diagram after modifying table schema
  [#1165](https://github.com/seedcase-project/seedcase-sprout/pull/1165)
  ([fafcf9f](https://github.com/seedcase-project/seedcase-sprout/commit/fafcf9f0cad7e392a4c107a8303fbd4f8641e2bd))
- Add design for deleting obs units
  [#1170](https://github.com/seedcase-project/seedcase-sprout/pull/1170)
  ([19c63a1](https://github.com/seedcase-project/seedcase-sprout/commit/19c63a1f0bbd50c2745db3b9d7472c01a86820a0))

## [0.28.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.28.0..0.28.1) - 2025-04-04

### ♻️ Refactor

- Convert `path_` functions into class without checks
  [#1173](https://github.com/seedcase-project/seedcase-sprout/pull/1173)
  ([aa5736f](https://github.com/seedcase-project/seedcase-sprout/commit/aa5736f0c1c578074ccd6b65ebb134e092f45ba0))

### 📝 Documentation

- Update based on `current_properties`
  [#1225](https://github.com/seedcase-project/seedcase-sprout/pull/1225)
  ([fa54c59](https://github.com/seedcase-project/seedcase-sprout/commit/fa54c596b544af9d5ef9a8c47cb7fa1a7ae7cf3a))
- Add white fill for mermaid subgraph
  [#1232](https://github.com/seedcase-project/seedcase-sprout/pull/1232)
  ([2b29a7b](https://github.com/seedcase-project/seedcase-sprout/commit/2b29a7b7e1173043aecb23564d239b97c04bedef))

## [0.28.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.27.1..0.28.0) - 2025-03-31

### ✨ Features

- Add `example_resource_properties()`
  [#1212](https://github.com/seedcase-project/seedcase-sprout/pull/1212)
  ([b354af5](https://github.com/seedcase-project/seedcase-sprout/commit/b354af5723a042126cbd9ab51bc5ed219cd999c2))

## [0.27.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.27.0..0.27.1) - 2025-03-31

### ♻️ Refactor

- Remove multi-user features, we won't be doing them
  [#1216](https://github.com/seedcase-project/seedcase-sprout/pull/1216)
  ([4096754](https://github.com/seedcase-project/seedcase-sprout/commit/409675462deaf814516dcac4610d47c053e55bde))

### 📝 Documentation

- Small fixes to design docs from the changes
  [#1205](https://github.com/seedcase-project/seedcase-sprout/pull/1205)
  ([4eaf51f](https://github.com/seedcase-project/seedcase-sprout/commit/4eaf51f675a2254c73566cbe97eb46b1631343fe))
- Small fixes to design docs from the changes
  [#1205](https://github.com/seedcase-project/seedcase-sprout/pull/1205)
  ([e2a7443](https://github.com/seedcase-project/seedcase-sprout/commit/e2a74436dd868423ac7e92c89fc16b218d759309))
- Design of the check functions
  [#874](https://github.com/seedcase-project/seedcase-sprout/pull/874)
  ([6e290a4](https://github.com/seedcase-project/seedcase-sprout/commit/6e290a4e936c0b16ab9f18e00d19d79f49d53391))
- Describe flow for checking properties
  [#1189](https://github.com/seedcase-project/seedcase-sprout/pull/1189)
  ([d441335](https://github.com/seedcase-project/seedcase-sprout/commit/d441335a02ffb36116df62c4619582afc7e1bf69))
- Pseudocode for `check_data()`
  [#1192](https://github.com/seedcase-project/seedcase-sprout/pull/1192)
  ([fe7848e](https://github.com/seedcase-project/seedcase-sprout/commit/fe7848e981a4170503951c87e0954bf9b439211e))
- Flow for checking data against the properties
  [#1191](https://github.com/seedcase-project/seedcase-sprout/pull/1191)
  ([74cf4ef](https://github.com/seedcase-project/seedcase-sprout/commit/74cf4ef09af19993ab69c6cd93c943162079e852))
- Update resource interface design from flow
  [#1166](https://github.com/seedcase-project/seedcase-sprout/pull/1166)
  ([3d51d88](https://github.com/seedcase-project/seedcase-sprout/commit/3d51d88201beb59a48754f7a6d888627a77a8d09))

### 🧱 Build system

- Forgot to update the args for this function
  [#1217](https://github.com/seedcase-project/seedcase-sprout/pull/1217)
  ([264be6d](https://github.com/seedcase-project/seedcase-sprout/commit/264be6d3959e3f83beba42aaa6d1e07218cedadb))

### 🧹 Chores

- *(sync)* Synced local '.pre-commit-config.yaml' with remote
  '.pre-commit-config.yaml'
  ([7f4f24e](https://github.com/seedcase-project/seedcase-sprout/commit/7f4f24eb01e2b902e12776b483fbe6777c973c0f))
- *(sync)* Synced local '.editorconfig' with remote '.editorconfig'
  ([f61eed3](https://github.com/seedcase-project/seedcase-sprout/commit/f61eed3a378c420e8c1b0c895e32df4b41018182))
- *(sync)* Synced local 'justfile' with remote 'justfile'
  ([10f6da2](https://github.com/seedcase-project/seedcase-sprout/commit/10f6da275864ef6a4cf554c1e8fe5b52680f087e))
- *(sync)* Synced local '.editorconfig' with remote '.editorconfig'
  ([3266017](https://github.com/seedcase-project/seedcase-sprout/commit/326601713ade696551ac403488d2bec88108020c))
- *(sync)* Synced local 'justfile' with remote 'justfile'
  ([447b0c9](https://github.com/seedcase-project/seedcase-sprout/commit/447b0c9a9b14d2ab2a7af0a63b3fc94e072dc4fd))

## [0.27.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.26.9..0.27.0) - 2025-03-27

### ✨ Features

- Add `read_properties()` function
  [#1156](https://github.com/seedcase-project/seedcase-sprout/pull/1156)
  ([b0ff52c](https://github.com/seedcase-project/seedcase-sprout/commit/b0ff52c9d7c1d23d0568d1ce099531b3b08ecac9))

## [0.26.9](https://github.com/seedcase-project/seedcase-sprout/compare/0.26.8..0.26.9) - 2025-03-27

### 🐛 Fixes

- Check that package and resource properties are `dict`s
  [#1179](https://github.com/seedcase-project/seedcase-sprout/pull/1179)
  ([3c3ccf7](https://github.com/seedcase-project/seedcase-sprout/commit/3c3ccf7ed5a6c763a748528f331747da5025b011))

## [0.26.8](https://github.com/seedcase-project/seedcase-sprout/compare/0.26.7..0.26.8) - 2025-03-27

### ♻️ Refactor

- Revised to `update_package_properties()`
  [#1157](https://github.com/seedcase-project/seedcase-sprout/pull/1157)
  ([5a5411b](https://github.com/seedcase-project/seedcase-sprout/commit/5a5411b9e18520211082bd8f182e6590259cf278))

### 📝 Documentation

- Add flow diagram for extracting resource properties
  [#1160](https://github.com/seedcase-project/seedcase-sprout/pull/1160)
  ([334ca00](https://github.com/seedcase-project/seedcase-sprout/commit/334ca001cdd32106332ac69f17e0107226f129b4))

## [0.26.7](https://github.com/seedcase-project/seedcase-sprout/compare/0.26.6..0.26.7) - 2025-03-27

### ♻️ Refactor

- Remove `create_package_properties()` and replace it with `write_*()`
  [#1153](https://github.com/seedcase-project/seedcase-sprout/pull/1153)
  ([6ae341a](https://github.com/seedcase-project/seedcase-sprout/commit/6ae341a6adbe8d139e43cac810ba100435633870))

### 📝 Documentation

- Add resource guide to guide sidebar
  [#1198](https://github.com/seedcase-project/seedcase-sprout/pull/1198)
  ([93d4d22](https://github.com/seedcase-project/seedcase-sprout/commit/93d4d22e57d20dfe43e9dbfa43c6ca17e7603c18))
- Minor corrections to pseudo code
  [#1177](https://github.com/seedcase-project/seedcase-sprout/pull/1177)
  ([90a42e0](https://github.com/seedcase-project/seedcase-sprout/commit/90a42e0fc30c3665566301232faf772c11e995b2))
- Flow to create the resource data
  [#1164](https://github.com/seedcase-project/seedcase-sprout/pull/1164)
  ([88afc9d](https://github.com/seedcase-project/seedcase-sprout/commit/88afc9d1fcf7eb3f9ab296e43759cb7bd4f4e150))
- Add flow diagram for updating the README
  [#1159](https://github.com/seedcase-project/seedcase-sprout/pull/1159)
  ([6dbbc14](https://github.com/seedcase-project/seedcase-sprout/commit/6dbbc144d4c47508e3f2884ae89d5ec80ee6caec))
- Flow diagram to manually create resource properties
  [#1161](https://github.com/seedcase-project/seedcase-sprout/pull/1161)
  ([3611815](https://github.com/seedcase-project/seedcase-sprout/commit/36118159136bec074c222a991a83985ca7afcd27))
- Flow diagram to update resource properties
  [#1162](https://github.com/seedcase-project/seedcase-sprout/pull/1162)
  ([c2daf31](https://github.com/seedcase-project/seedcase-sprout/commit/c2daf3132717e454f26aa86470cba58361530684))
- Simplify the deletion functions
  [#1169](https://github.com/seedcase-project/seedcase-sprout/pull/1169)
  ([a9d5399](https://github.com/seedcase-project/seedcase-sprout/commit/a9d539925d0d88b1a7ff006aa0092a60689f2314))

### 🧹 Chores

- Use asterisk to include all guides in sidebar
  [#1199](https://github.com/seedcase-project/seedcase-sprout/pull/1199)
  ([52af555](https://github.com/seedcase-project/seedcase-sprout/commit/52af5559db7556aa1ae221c6d7960179fec96374))

## [0.26.6](https://github.com/seedcase-project/seedcase-sprout/compare/0.26.5..0.26.6) - 2025-03-24

### ♻️ Refactor

- Check column data types
  [#1111](https://github.com/seedcase-project/seedcase-sprout/pull/1111)
  ([9760991](https://github.com/seedcase-project/seedcase-sprout/commit/9760991c0d82942125828df867fab7e5bf620592))

### 📝 Documentation

- Add flow for updating package properties
  [#1155](https://github.com/seedcase-project/seedcase-sprout/pull/1155)
  ([2e58d2c](https://github.com/seedcase-project/seedcase-sprout/commit/2e58d2c2053317bced78a815e43684c9d0f60c4c))
- Update the pseudocode files to match the flows
  [#1168](https://github.com/seedcase-project/seedcase-sprout/pull/1168)
  ([e6148b5](https://github.com/seedcase-project/seedcase-sprout/commit/e6148b5775eecf4a8a8294689284ef2b3c2f17d2))
- Flow diagram to add data to batch
  [#1163](https://github.com/seedcase-project/seedcase-sprout/pull/1163)
  ([c93d36b](https://github.com/seedcase-project/seedcase-sprout/commit/c93d36b6381a281b186cf5685f0bc0247c87cd9b))

## [0.26.5](https://github.com/seedcase-project/seedcase-sprout/compare/0.26.4..0.26.5) - 2025-03-21

### ♻️ Refactor

- Rename `build_` to `as_readme_text()`
  [#1172](https://github.com/seedcase-project/seedcase-sprout/pull/1172)
  ([c91f370](https://github.com/seedcase-project/seedcase-sprout/commit/c91f370703ddb702eb67302b1789bc0f51f6710f))

### 📝 Documentation

- Flow diagrams for creating data package
  [#1151](https://github.com/seedcase-project/seedcase-sprout/pull/1151)
  ([a516435](https://github.com/seedcase-project/seedcase-sprout/commit/a51643574497be50cbc57c311315661f8cf11053))

### 🧹 Chores

- Remove left over pseudocode file
  [#1167](https://github.com/seedcase-project/seedcase-sprout/pull/1167)
  ([d065d06](https://github.com/seedcase-project/seedcase-sprout/commit/d065d06103edd32b1eb9f0105628470e54eaf50a))
- Seemed to have missed deleting this previously
  [#1154](https://github.com/seedcase-project/seedcase-sprout/pull/1154)
  ([f6687e1](https://github.com/seedcase-project/seedcase-sprout/commit/f6687e189ea4452e231ac35c5952eeab5bcc5f24))
- These are not used, so deleting
  [#1158](https://github.com/seedcase-project/seedcase-sprout/pull/1158)
  ([43f1c20](https://github.com/seedcase-project/seedcase-sprout/commit/43f1c204252dcd07bead3d11b69ad974d61450c9))

## [0.26.4](https://github.com/seedcase-project/seedcase-sprout/compare/0.26.3..0.26.4) - 2025-03-19

### ♻️ Refactor

- Expose `extract_resource_properties()`
  [#1152](https://github.com/seedcase-project/seedcase-sprout/pull/1152)
  ([f31cd72](https://github.com/seedcase-project/seedcase-sprout/commit/f31cd727eab8f96bdee2f9cedd491c2d3e2de725))

## [0.26.3](https://github.com/seedcase-project/seedcase-sprout/compare/0.26.2..0.26.3) - 2025-03-19

### ♻️ Refactor

- Remove original extension and `.gz` from batch file names
  [#1147](https://github.com/seedcase-project/seedcase-sprout/pull/1147)
  ([0938d74](https://github.com/seedcase-project/seedcase-sprout/commit/0938d74b5d2d92d106923282fd50a1b7a597389f))

### 📝 Documentation

- Revise from `raw` to `batch` in design docs
  [#1142](https://github.com/seedcase-project/seedcase-sprout/pull/1142)
  ([8ad129c](https://github.com/seedcase-project/seedcase-sprout/commit/8ad129ce7a8ba4deb4b48a7a37fd25d77dac51f8))

### 🧹 Chores

- *(sync)* Synced local '\_extensions/seedcase-project/seedcase-theme/' with
  remote '\_extensions/seedcase-theme/'
  ([effcf5d](https://github.com/seedcase-project/seedcase-sprout/commit/effcf5d98a68c05bfbe21ba2da7e88ba25e85a72))
- *(sync)* Synced local '\_extensions/seedcase-project/seedcase-theme/' with
  remote '\_extensions/seedcase-theme/'
  ([51b39aa](https://github.com/seedcase-project/seedcase-sprout/commit/51b39aa2eeb20b75b4eb7289fbb0139971f169b4))

## [0.26.2](https://github.com/seedcase-project/seedcase-sprout/compare/0.26.1..0.26.2) - 2025-03-18

### ♻️ Refactor

- Rename `raw` to `batch` within Python code
  [#1145](https://github.com/seedcase-project/seedcase-sprout/pull/1145)
  ([2a2c01b](https://github.com/seedcase-project/seedcase-sprout/commit/2a2c01b881824cc16117d81c7eb2b014757260a8))

### 📝 Documentation

- Assign edited properties to variable name
  [#1146](https://github.com/seedcase-project/seedcase-sprout/pull/1146)
  ([d7161ac](https://github.com/seedcase-project/seedcase-sprout/commit/d7161ac18a7df53f2987b5a90e1c9edf6b687576))

## [0.26.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.26.0..0.26.1) - 2025-03-17

### ♻️ Refactor

- Major refactor of path functions to be local-first
  [#1114](https://github.com/seedcase-project/seedcase-sprout/pull/1114)
  ([f77b2ef](https://github.com/seedcase-project/seedcase-sprout/commit/f77b2effbffeb5bb74ded4d62c4d5735b2a4d4d2))

### 📝 Documentation

- Add start of the creating resources guide
  [#810](https://github.com/seedcase-project/seedcase-sprout/pull/810)
  ([07673cd](https://github.com/seedcase-project/seedcase-sprout/commit/07673cd9c33bb07bb8122999b1582e1a74674b1d))

## [0.26.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.24.0..0.26.0) - 2025-03-17

### ✨ Features

- Add `set_missing_values_to_null()`
  [#1131](https://github.com/seedcase-project/seedcase-sprout/pull/1131)
  ([bfccdec](https://github.com/seedcase-project/seedcase-sprout/commit/bfccdecf79408965bc10ac90cdfaecf2bd5e5283))
- Add `check_data_header()`
  [#1130](https://github.com/seedcase-project/seedcase-sprout/pull/1130)
  ([aaf3bcf](https://github.com/seedcase-project/seedcase-sprout/commit/aaf3bcfe74b77131300724cddb91ed662b7cd82e))

### 📝 Documentation

- Update example in `create_resource_structure()`
  [#1121](https://github.com/seedcase-project/seedcase-sprout/pull/1121)
  ([5ef6748](https://github.com/seedcase-project/seedcase-sprout/commit/5ef674839a5e8e336ebfb507c433a5fa5bcd6ca9))

## [0.24.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.23.0..0.24.0) - 2025-03-12

### ✨ Features

- Add `read_csv()` to load CSV as DataFrames
  [#1129](https://github.com/seedcase-project/seedcase-sprout/pull/1129)
  ([71bdfe8](https://github.com/seedcase-project/seedcase-sprout/commit/71bdfe88f72ff7cb57e4e8c11e88ff727956784d))

### 📝 Documentation

- Revise package guide to "local-first"
  [#1109](https://github.com/seedcase-project/seedcase-sprout/pull/1109)
  ([bf4a6ed](https://github.com/seedcase-project/seedcase-sprout/commit/bf4a6ed27de2168c4479d313f34fd9bb2c553a37))
- Add supported formats doc to design interface
  [#1126](https://github.com/seedcase-project/seedcase-sprout/pull/1126)
  ([b7599c7](https://github.com/seedcase-project/seedcase-sprout/commit/b7599c7fdd0dfa799ceef9e98ad375d9beb4e366))
- Include path arg of path functions in interface doc
  [#1124](https://github.com/seedcase-project/seedcase-sprout/pull/1124)
  ([d72d831](https://github.com/seedcase-project/seedcase-sprout/commit/d72d83147f02ffb251724a6254f8742e03fe1a6d))
- Delete `supported-formats.qmd`
  [#1132](https://github.com/seedcase-project/seedcase-sprout/pull/1132)
  ([0cc00e7](https://github.com/seedcase-project/seedcase-sprout/commit/0cc00e75ae19586f7998af9f7e66e1d79c39bdec))

## [0.23.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.22.0..0.23.0) - 2025-03-10

### ✨ Features

- Make `build_readme_text()` and `write_file()` public
  [#1119](https://github.com/seedcase-project/seedcase-sprout/pull/1119)
  ([e827b13](https://github.com/seedcase-project/seedcase-sprout/commit/e827b13f3700ef8d5ae11b26b1a0398edd113c64))

### 📝 Documentation

- Update these functions to done
  [#1123](https://github.com/seedcase-project/seedcase-sprout/pull/1123)
  ([45969db](https://github.com/seedcase-project/seedcase-sprout/commit/45969dbc0abc5c97f8244779e4c30a5530ef9961))

### 💄 Style

- Use normal appearance for callout blocks
  [#1122](https://github.com/seedcase-project/seedcase-sprout/pull/1122)
  ([1e72b77](https://github.com/seedcase-project/seedcase-sprout/commit/1e72b77d519ee815ab31c3e7804189fd639ceca6))

## [0.22.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.21.1..0.22.0) - 2025-03-06

### ✨ Features

- Add mapping from Frictionless data types to Polars data types
  [#1106](https://github.com/seedcase-project/seedcase-sprout/pull/1106)
  ([eca3dbd](https://github.com/seedcase-project/seedcase-sprout/commit/eca3dbd2795685684160451d82e31fe5000b959d))

## [0.21.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.21.0..0.21.1) - 2025-03-05

### 🐛 Fixes

- Only remove qmd files in reference post render to fix md formatting issues
  [#1107](https://github.com/seedcase-project/seedcase-sprout/pull/1107)
  ([52092ac](https://github.com/seedcase-project/seedcase-sprout/commit/52092ac3a9aaba765cc51359cf585f36efd6d0f2))

## [0.21.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.20.1..0.21.0) - 2025-03-04

### ✨ Features

- Add `path_readme()`
  [#1100](https://github.com/seedcase-project/seedcase-sprout/pull/1100)
  ([6a8824f](https://github.com/seedcase-project/seedcase-sprout/commit/6a8824fb4d7648aba2e4e7d9946f47eb5e93a892))

## [0.20.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.20.0..0.20.1) - 2025-03-04

### ♻️ Refactor

- Rename `create_readme_text()` to `build_readme_text()`
  [#1099](https://github.com/seedcase-project/seedcase-sprout/pull/1099)
  ([9204b9d](https://github.com/seedcase-project/seedcase-sprout/commit/9204b9d6d244c856ffee9a177758a4258a27e883))

### 🧹 Chores

- Remove "geojson", "topojson", and "ods" from `SUPPORTED_FORMATS`
  [#1097](https://github.com/seedcase-project/seedcase-sprout/pull/1097)
  ([64e14a7](https://github.com/seedcase-project/seedcase-sprout/commit/64e14a7b3a02d40da89d4e4d9c8b4429f67ad689))

## [0.20.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.19.0..0.20.0) - 2025-02-26

### ✨ Features

- Extract resource properties from `.json`, `.ndjson`, and `.jsonl` files
  [#1085](https://github.com/seedcase-project/seedcase-sprout/pull/1085)
  ([5d0bca4](https://github.com/seedcase-project/seedcase-sprout/commit/5d0bca4dda777d271634a7b9c9031d12cd39bb52))

### 🧱 Build system

- Enable properties extraction from Excel files
  [#1081](https://github.com/seedcase-project/seedcase-sprout/pull/1081)
  ([e01bbaa](https://github.com/seedcase-project/seedcase-sprout/commit/e01bbaad48f301e988ebb032fe4421d4c8c4d287))

## [0.19.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.18.2..0.19.0) - 2025-02-24

### ✨ Features

- Add conversion from resource properties to Pandera schema
  [#1051](https://github.com/seedcase-project/seedcase-sprout/pull/1051)
  ([798bab0](https://github.com/seedcase-project/seedcase-sprout/commit/798bab041a84fd09ab3bebd5c38dd0dc24bcf229))

### 📝 Documentation

- Pseudocode for `write_resource_parquet()`
  [#1077](https://github.com/seedcase-project/seedcase-sprout/pull/1077)
  ([3c014dc](https://github.com/seedcase-project/seedcase-sprout/commit/3c014dcdc7f6b250fa0908d5f40d0b57aa4e0b49))

## [0.18.2](https://github.com/seedcase-project/seedcase-sprout/compare/0.18.1..0.18.2) - 2025-02-24

### ♻️ Refactor

- Switch `create_package_structure()` to make properties only
  [#1047](https://github.com/seedcase-project/seedcase-sprout/pull/1047)
  ([5621497](https://github.com/seedcase-project/seedcase-sprout/commit/56214976550b8f6b2b4034aec1aaddb09ef350bf))

## [0.18.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.18.0..0.18.1) - 2025-02-24

### ♻️ Refactor

- Convert `example_package_properties` to function
  [#1046](https://github.com/seedcase-project/seedcase-sprout/pull/1046)
  ([719ee21](https://github.com/seedcase-project/seedcase-sprout/commit/719ee216d6b71d150264cf9fc3b58f3a0c660d09))

### 📝 Documentation

- Expand and refine naming scheme
  [#1070](https://github.com/seedcase-project/seedcase-sprout/pull/1070)
  ([25e2be4](https://github.com/seedcase-project/seedcase-sprout/commit/25e2be49854ce6e2f73a1b2a0aa5a6a2d8a623cd))
- Add some Mermaid diagrams to function design
  [#1076](https://github.com/seedcase-project/seedcase-sprout/pull/1076)
  ([f16fad9](https://github.com/seedcase-project/seedcase-sprout/commit/f16fad933fe2bf57dbbd4dfe7409cc7b9463ebef))
- Revise install guide after testing it out
  [#1068](https://github.com/seedcase-project/seedcase-sprout/pull/1068)
  ([edc14a0](https://github.com/seedcase-project/seedcase-sprout/commit/edc14a03aed14357ec973f756e8eee8725ce78d5))
- Revise to `build_resource_data()` to output a DataFrame
  [#1074](https://github.com/seedcase-project/seedcase-sprout/pull/1074)
  ([394d22a](https://github.com/seedcase-project/seedcase-sprout/commit/394d22abaeaab1f166acb98647f1e48eec2cfc1f))

### 🧪 Tests

- Add `object` field to test data
  [#1079](https://github.com/seedcase-project/seedcase-sprout/pull/1079)
  ([2402db6](https://github.com/seedcase-project/seedcase-sprout/commit/2402db607ae53862e73b275f4822ae31bfeafafa))

## [0.18.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.17.0..0.18.0) - 2025-02-21

### ✨ Features

- Add initial `extract_resource_properties()` (csv, tsv, and parquet files)
  [#1067](https://github.com/seedcase-project/seedcase-sprout/pull/1067)
  ([e7993cc](https://github.com/seedcase-project/seedcase-sprout/commit/e7993cc73bc556557945a600f2ac23b1c0430f07))

### 📝 Documentation

- Callout note about diagrams not rendering on Firefox
  [#1072](https://github.com/seedcase-project/seedcase-sprout/pull/1072)
  ([684a416](https://github.com/seedcase-project/seedcase-sprout/commit/684a416f19918ca1e4485653e46d4f4f4e829c44))
- Rename to `_dirs` rather than `_structure`
  [#1075](https://github.com/seedcase-project/seedcase-sprout/pull/1075)
  ([b01b840](https://github.com/seedcase-project/seedcase-sprout/commit/b01b840b73f6cba960d2f5c2cc472ba5bc2cd95b))
- Rename functions to `update_` rather than `edit_`
  [#1071](https://github.com/seedcase-project/seedcase-sprout/pull/1071)
  ([2eb4489](https://github.com/seedcase-project/seedcase-sprout/commit/2eb4489b8426bd150bf3b0316107058578be3e1c))
- Add guide for Sprout checks
  [#1024](https://github.com/seedcase-project/seedcase-sprout/pull/1024)
  ([9916cfc](https://github.com/seedcase-project/seedcase-sprout/commit/9916cfc2334dc10a3da6a2868fb72bb13e67a942))

### 🧹 Chores

- *(sync)* Synced local '\_extensions/seedcase-project/seedcase-theme/' with
  remote '\_extensions/seedcase-theme/'
  ([427589b](https://github.com/seedcase-project/seedcase-sprout/commit/427589badc4bfcbe7936075157c4d8ba767dbc5a))
- Add website visit counter
  [#1069](https://github.com/seedcase-project/seedcase-sprout/pull/1069)
  ([f95190b](https://github.com/seedcase-project/seedcase-sprout/commit/f95190b0c27c6c4c5822dd2532308d9220008394))
- Remove unused Data Package standard elements
  [#1066](https://github.com/seedcase-project/seedcase-sprout/pull/1066)
  ([9e17eef](https://github.com/seedcase-project/seedcase-sprout/commit/9e17eefb884834613873c2258808807588c02cd7))
- Remove leftover security design file
  [#1073](https://github.com/seedcase-project/seedcase-sprout/pull/1073)
  ([366b408](https://github.com/seedcase-project/seedcase-sprout/commit/366b4083a778a3f5b2b14109e712f1a45fc37e5c))

## [0.17.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.16.0..0.17.0) - 2025-02-19

### ✨ Features

- Add Pandera checks on the data
  [#1050](https://github.com/seedcase-project/seedcase-sprout/pull/1050)
  ([297c2a1](https://github.com/seedcase-project/seedcase-sprout/commit/297c2a1a506cb1bf3f64258b48dcc4acdbdca990))

### 📝 Documentation

- Pseudo code and docstring for `write_resource_parquet()`
  [#816](https://github.com/seedcase-project/seedcase-sprout/pull/816)
  ([71f451a](https://github.com/seedcase-project/seedcase-sprout/commit/71f451ab97ef6d06e5db9f363a3722aea70bf8a8))

### 🧱 Build system

- This should be in post-render, not pre
  ([27998f5](https://github.com/seedcase-project/seedcase-sprout/commit/27998f5920930aa91d4665c61e77ddaa5354ebd4))
- Use Poetry v2 sync (recommended over install)
  ([f27b18f](https://github.com/seedcase-project/seedcase-sprout/commit/f27b18f5beb8da47b4c353262c62c163ceab3317))

### 🧹 Chores

- *(sync)* Synced local '.editorconfig' with remote '.editorconfig'
  ([97f3745](https://github.com/seedcase-project/seedcase-sprout/commit/97f374549ee86492194fa485bfcf4bbd4916c848))
- *(sync)* Synced local 'justfile' with remote 'justfile'
  ([197746c](https://github.com/seedcase-project/seedcase-sprout/commit/197746c367cb70315c92dc89831538121dc2ccb7))
- *(sync)* Synced local '.cz.toml' with remote '.cz.toml'
  ([8257fd0](https://github.com/seedcase-project/seedcase-sprout/commit/8257fd0cf1c3e647811755bd8e8c70c2f758ced6))
- *(sync)* Synced local 'LICENSE.md' with remote 'LICENSE.md'
  ([30b2b8a](https://github.com/seedcase-project/seedcase-sprout/commit/30b2b8ae01c0b482104558d7600375324934ff5b))
- *(sync)* Synced local '.vscode/' with remote '.vscode/'
  ([4ba7585](https://github.com/seedcase-project/seedcase-sprout/commit/4ba758594113d9f671dd7a896095d7c8bf6a11b6))
- Move to `src/` layout
  [#1052](https://github.com/seedcase-project/seedcase-sprout/pull/1052)
  ([fa92e90](https://github.com/seedcase-project/seedcase-sprout/commit/fa92e90d398d20eca66f2ef46947b24022c27122))
- Ran poetry sync
  ([89d7899](https://github.com/seedcase-project/seedcase-sprout/commit/89d78999b423ad3de0507b01fbb605389cdc01b9))
- Small build fixes
  [#1062](https://github.com/seedcase-project/seedcase-sprout/pull/1062)
  ([75c5994](https://github.com/seedcase-project/seedcase-sprout/commit/75c5994407537dcb6c7331966165c50e3b5dcc50))

## [0.16.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.15.0..0.16.0) - 2025-02-12

### ✨ Features

- Add an `example_package_properties` object
  [#1044](https://github.com/seedcase-project/seedcase-sprout/pull/1044)
  ([878f31a](https://github.com/seedcase-project/seedcase-sprout/commit/878f31ad229fb5aca6000e5316415dd587676050))

### 📝 Documentation

- Fix broken link to functions.qmd
  [#1043](https://github.com/seedcase-project/seedcase-sprout/pull/1043)
  ([284cac7](https://github.com/seedcase-project/seedcase-sprout/commit/284cac794694ccb8c6699ae70775dc24e7f50074))

### 💄 Style

- Refactor so WIP status of interface are icons
  [#1041](https://github.com/seedcase-project/seedcase-sprout/pull/1041)
  ([86ae5d0](https://github.com/seedcase-project/seedcase-sprout/commit/86ae5d0afb65ccf87db80c6151f5b8d344495971))

## [0.15.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.14.3..0.15.0) - 2025-02-12

### ✨ Features

- Add `get_nested_attr()`
  [#1039](https://github.com/seedcase-project/seedcase-sprout/pull/1039)
  ([58003ed](https://github.com/seedcase-project/seedcase-sprout/commit/58003ed3603520073975c542f62abf1aedad8135))

### 📝 Documentation

- Forgot to rename `path_properties()` in docs
  ([f4ab145](https://github.com/seedcase-project/seedcase-sprout/commit/f4ab14518e47851cfe473fd74ac7db8377b90c00))
- The ResourceProperties needs title and description
  ([de31cac](https://github.com/seedcase-project/seedcase-sprout/commit/de31cac72a6f7ca1b4f38c6a56bbd6c1246a0cb7))
- Don't eval this example, needs update after 'local-first'
  ([653a118](https://github.com/seedcase-project/seedcase-sprout/commit/653a11839e04c19dcd6bdda1b0f4cd2b34bb64a7))
- Don't eval this code chunk, it was causing website build error
  ([fd62057](https://github.com/seedcase-project/seedcase-sprout/commit/fd620577492c65b6c645081b8411a12c0a122217))
- Package guide
  [#1001](https://github.com/seedcase-project/seedcase-sprout/pull/1001)
  ([d386b3a](https://github.com/seedcase-project/seedcase-sprout/commit/d386b3a47642d7486789a17536e52bcdc0243bf6))
- Move text into docstrings, remove leftover resource `.puml`
  [#1016](https://github.com/seedcase-project/seedcase-sprout/pull/1016)
  ([8460333](https://github.com/seedcase-project/seedcase-sprout/commit/846033332866f6074ac5b78b7094e4a89b5a754f))
- Indicate which functions aren't done
  [#1017](https://github.com/seedcase-project/seedcase-sprout/pull/1017)
  ([da0a6b8](https://github.com/seedcase-project/seedcase-sprout/commit/da0a6b88c96b4c6ded17565278f7f70f53979734))
- Remove references to CLI or app
  [#1013](https://github.com/seedcase-project/seedcase-sprout/pull/1013)
  ([3e9c6ce](https://github.com/seedcase-project/seedcase-sprout/commit/3e9c6ce186ab2afc67e3177abe1a3ae0561a558c))
- Update installation guide, plus add pipx instructions
  [#1014](https://github.com/seedcase-project/seedcase-sprout/pull/1014)
  ([0d95098](https://github.com/seedcase-project/seedcase-sprout/commit/0d95098703d06de864bba9c50e1ab2045bea24d4))
- Convert from PlantUML into pseudocode
  [#1019](https://github.com/seedcase-project/seedcase-sprout/pull/1019)
  ([2895ebc](https://github.com/seedcase-project/seedcase-sprout/commit/2895ebcaebca60bf96df7f96282a278dc932a74c))
- Convert `.puml` C4 diagrams into Mermaid
  [#1023](https://github.com/seedcase-project/seedcase-sprout/pull/1023)
  ([aa93b62](https://github.com/seedcase-project/seedcase-sprout/commit/aa93b62722f522e01398bf7d79daf20b091ee500))
- Move `.puml` into pseudocode
  [#1021](https://github.com/seedcase-project/seedcase-sprout/pull/1021)
  ([8a3f8a0](https://github.com/seedcase-project/seedcase-sprout/commit/8a3f8a0a3d9a9eae40c576e24824e17b174d9a45))

### 💄 Style

- Ran `just-all` and reformatted code
  ([80c29fe](https://github.com/seedcase-project/seedcase-sprout/commit/80c29fe8e3a0a9702d4ea8b93ecf9caef745f66e))

### 🧹 Chores

- *(sync)* Synced local '\_extensions/seedcase-project/seedcase-theme/' with
  remote '\_extensions/seedcase-theme/'
  ([a5f02e6](https://github.com/seedcase-project/seedcase-sprout/commit/a5f02e6a9d239c80d1b8611f724507085ce7f98c))
- Extensions are now bundled with our extension
  [#1025](https://github.com/seedcase-project/seedcase-sprout/pull/1025)
  ([17504b5](https://github.com/seedcase-project/seedcase-sprout/commit/17504b51e10852a7c8313c831b389835f7362190))
- Simplify name of file to just 'functions'
  [#1022](https://github.com/seedcase-project/seedcase-sprout/pull/1022)
  ([dfa4d4e](https://github.com/seedcase-project/seedcase-sprout/commit/dfa4d4e3fd048c2ad43838291158950ab6c524ff))

## [0.14.3](https://github.com/seedcase-project/seedcase-sprout/compare/0.14.2..0.14.3) - 2025-01-28

### ♻️ Refactor

- Use jinja template for README
  [#1011](https://github.com/seedcase-project/seedcase-sprout/pull/1011)
  ([7d14d55](https://github.com/seedcase-project/seedcase-sprout/commit/7d14d5523b944496cdff33bfc159017a0ed0ddf2))

### 📝 Documentation

- Move user types over into user personas document
  [#994](https://github.com/seedcase-project/seedcase-sprout/pull/994)
  ([cdeb2ed](https://github.com/seedcase-project/seedcase-sprout/commit/cdeb2eda01ae03c730d1fd192700233e63e9c899))
- Update path design to match 'local-first'
  [#1009](https://github.com/seedcase-project/seedcase-sprout/pull/1009)
  ([02bc68e](https://github.com/seedcase-project/seedcase-sprout/commit/02bc68e5ad03d36438340c6cf8b47698fbe3a575))

## [0.14.2](https://github.com/seedcase-project/seedcase-sprout/compare/0.14.1..0.14.2) - 2025-01-28

### ♻️ Refactor

- Commonise Sprout checks
  [#998](https://github.com/seedcase-project/seedcase-sprout/pull/998)
  ([7e70e1d](https://github.com/seedcase-project/seedcase-sprout/commit/7e70e1d147fb22075274e9ea72c842f17c319aa0))

### 📝 Documentation

- Small fixes to website build
  [#1010](https://github.com/seedcase-project/seedcase-sprout/pull/1010)
  ([0efd420](https://github.com/seedcase-project/seedcase-sprout/commit/0efd4204de44f26d2b0573856c8cd6cf7c8e6bc4))
- Don't actually need the view action, have the README
  [#1012](https://github.com/seedcase-project/seedcase-sprout/pull/1012)
  ([2488ed2](https://github.com/seedcase-project/seedcase-sprout/commit/2488ed2f8b97329f6f878361fae3607127bf9815))

### 🧹 Chores

- *(sync)* Synced local '\_extensions/seedcase-project/seedcase-theme/' with
  remote '\_extensions/seedcase-theme/'
  ([ecd7227](https://github.com/seedcase-project/seedcase-sprout/commit/ecd722720f54bf40e26e3ba90cbb86c8e003c3a9))

## [0.14.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.14.0..0.14.1) - 2025-01-27

### ♻️ Refactor

- Make schema path resolve when working directory different
  [#1000](https://github.com/seedcase-project/seedcase-sprout/pull/1000)
  ([83019a0](https://github.com/seedcase-project/seedcase-sprout/commit/83019a065d5096dfdd2e5c54b8f28750bf2af38b))

### 📝 Documentation

- Fix typo
  [#1003](https://github.com/seedcase-project/seedcase-sprout/pull/1003)
  ([7f3b8f0](https://github.com/seedcase-project/seedcase-sprout/commit/7f3b8f0656579ecf9aeda84dd1cb485cb50210d4))

### 🧹 Chores

- Remove old verify functions and related error
  [#1002](https://github.com/seedcase-project/seedcase-sprout/pull/1002)
  ([9c7a494](https://github.com/seedcase-project/seedcase-sprout/commit/9c7a494b24d203845f6f21c978ff9bc9bbd6defe))

## [0.14.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.13.3..0.14.0) - 2025-01-27

### ✨ Features

- Add `write_package_properties()`
  [#984](https://github.com/seedcase-project/seedcase-sprout/pull/984)
  ([93a1b3f](https://github.com/seedcase-project/seedcase-sprout/commit/93a1b3f14992a01f0ebf3bc20036ee4448a7d96f))

## [0.13.3](https://github.com/seedcase-project/seedcase-sprout/compare/0.13.2..0.13.3) - 2025-01-27

### ♻️ Refactor

- Use checks in `write_resource_properties()`
  [#990](https://github.com/seedcase-project/seedcase-sprout/pull/990)
  ([c10d053](https://github.com/seedcase-project/seedcase-sprout/commit/c10d05352de2d84ef04a28e61643340b7c180a50))

## [0.13.2](https://github.com/seedcase-project/seedcase-sprout/compare/0.13.1..0.13.2) - 2025-01-27

### ♻️ Refactor

- Use new checks in `create_resource_properties()`
  [#988](https://github.com/seedcase-project/seedcase-sprout/pull/988)
  ([2361dc5](https://github.com/seedcase-project/seedcase-sprout/commit/2361dc5f76d302cd7327ac1a2752e306b9f5b9f6))

## [0.13.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.13.0..0.13.1) - 2025-01-27

### ♻️ Refactor

- Use check functions in `edit_package_properties`
  [#974](https://github.com/seedcase-project/seedcase-sprout/pull/974)
  ([39db115](https://github.com/seedcase-project/seedcase-sprout/commit/39db115e7d3c8eb80f4edb0432cd22b59fe031e8))

### 📝 Documentation

- Add module docstrings
  [#983](https://github.com/seedcase-project/seedcase-sprout/pull/983)
  ([bcfd2b9](https://github.com/seedcase-project/seedcase-sprout/commit/bcfd2b925e6825bbab11d9d84bdc16ec554f450f))
- Update design interface of package section
  [#989](https://github.com/seedcase-project/seedcase-sprout/pull/989)
  ([44d0d01](https://github.com/seedcase-project/seedcase-sprout/commit/44d0d01d2fd79ece247280a62a24f2693fadc05d))
- Move docs on Properties into docstrings and edit them
  [#991](https://github.com/seedcase-project/seedcase-sprout/pull/991)
  ([7c5479b](https://github.com/seedcase-project/seedcase-sprout/commit/7c5479b8c174907802993c8955f035b60518f6ec))
- Move expected input data from design repo
  [#993](https://github.com/seedcase-project/seedcase-sprout/pull/993)
  ([ffd83aa](https://github.com/seedcase-project/seedcase-sprout/commit/ffd83aa75688e851590bb50db2838d5e5e513707))

## [0.13.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.12.2..0.13.0) - 2025-01-24

### ✨ Features

- Output everything from code cells in Reference docs
  [#997](https://github.com/seedcase-project/seedcase-sprout/pull/997)
  ([3fcfa96](https://github.com/seedcase-project/seedcase-sprout/commit/3fcfa968cd641c128512a61f0f9f7fd877d3c964))

### 📝 Documentation

- Add examples to user facing functions
  [#982](https://github.com/seedcase-project/seedcase-sprout/pull/982)
  ([42799a0](https://github.com/seedcase-project/seedcase-sprout/commit/42799a0cd06eab5812214d7b2de5fa0846d16e70))

## [0.12.2](https://github.com/seedcase-project/seedcase-sprout/compare/0.12.1..0.12.2) - 2025-01-24

### ♻️ Refactor

- `path_package_properties()` -> `path_properties()`
  [#996](https://github.com/seedcase-project/seedcase-sprout/pull/996)
  ([0976a3e](https://github.com/seedcase-project/seedcase-sprout/commit/0976a3e7a5e7571d0e9a5ca40de93ad140efde44))

## [0.12.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.12.0..0.12.1) - 2025-01-23

### ♻️ Refactor

- Use `CheckErrorMatcher` in Sprout checks
  [#973](https://github.com/seedcase-project/seedcase-sprout/pull/973)
  ([2965f75](https://github.com/seedcase-project/seedcase-sprout/commit/2965f75ab7d6be1119c547d55cdc9d250de7d0b8))

## [0.12.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.11.1..0.12.0) - 2025-01-23

### ✨ Features

- Add `CheckErrorMatcher` object
  [#972](https://github.com/seedcase-project/seedcase-sprout/pull/972)
  ([9e0899e](https://github.com/seedcase-project/seedcase-sprout/commit/9e0899ee9b3738d0051fcca88c97fa5dba99a669))

### 📝 Documentation

- Move modular design and requirements into design landing page
  [#979](https://github.com/seedcase-project/seedcase-sprout/pull/979)
  ([f3ef3ce](https://github.com/seedcase-project/seedcase-sprout/commit/f3ef3ce4c3a539382591120ba88c25d4da9193fb))

### 👷 CI/CD

- Remove left over workflows
  [#992](https://github.com/seedcase-project/seedcase-sprout/pull/992)
  ([cf98f16](https://github.com/seedcase-project/seedcase-sprout/commit/cf98f16d6a26ae8e401f29016f16098ef2820e24))

## [0.11.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.11.0..0.11.1) - 2025-01-22

### ♻️ Refactor

- User `Properties` classes in user facing functions
  [#976](https://github.com/seedcase-project/seedcase-sprout/pull/976)
  ([8c6063f](https://github.com/seedcase-project/seedcase-sprout/commit/8c6063fd7467260859c8390894acc3996f11c80a))

### 📝 Documentation

- Remove `write_resource_to_database()`
  [#986](https://github.com/seedcase-project/seedcase-sprout/pull/986)
  ([dc6e4be](https://github.com/seedcase-project/seedcase-sprout/commit/dc6e4be41cfd321ddbccfbae972e63450fbb6e6e))

### 🧹 Chores

- Remove `path_package_database()`
  [#985](https://github.com/seedcase-project/seedcase-sprout/pull/985)
  ([bf14f30](https://github.com/seedcase-project/seedcase-sprout/commit/bf14f30f79c4360121c7c777fc2baa1670fcc9d6))

## [0.11.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.10.0..0.11.0) - 2025-01-21

### ✨ Features

- Add `check_properties()`
  [#967](https://github.com/seedcase-project/seedcase-sprout/pull/967)
  ([52bf2d9](https://github.com/seedcase-project/seedcase-sprout/commit/52bf2d9c1444197535f697fa06254659706fe73f))

## [0.10.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.9.0..0.10.0) - 2025-01-21

### ✨ Features

- Add `check_package_properties()`
  [#966](https://github.com/seedcase-project/seedcase-sprout/pull/966)
  ([12a184f](https://github.com/seedcase-project/seedcase-sprout/commit/12a184f2165e8e8aba83e46ff5f0cd9226670cfb))

## [0.9.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.8.0..0.9.0) - 2025-01-21

### ✨ Features

- Add `check_resource_properties()`
  [#965](https://github.com/seedcase-project/seedcase-sprout/pull/965)
  ([07d1d4d](https://github.com/seedcase-project/seedcase-sprout/commit/07d1d4d9ef2cc5cedc26e76d4bef230d68090904))

## [0.8.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.7.0..0.8.0) - 2025-01-21

### ✨ Features

- Collect all Sprout-specific property errors
  [#964](https://github.com/seedcase-project/seedcase-sprout/pull/964)
  ([9f71923](https://github.com/seedcase-project/seedcase-sprout/commit/9f719238a17d871a8b2c5b0398de638efebf30f5))

## [0.7.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.6.0..0.7.0) - 2025-01-21

### ✨ Features

- Add functions to check required and blank fields
  [#963](https://github.com/seedcase-project/seedcase-sprout/pull/963)
  ([0f4fa55](https://github.com/seedcase-project/seedcase-sprout/commit/0f4fa5539194f67f0c2b2dd2a343816f29a234ce))

## [0.6.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.5.0..0.6.0) - 2025-01-21

### ✨ Features

- Add simple helper functions
  [#962](https://github.com/seedcase-project/seedcase-sprout/pull/962)
  ([cffc566](https://github.com/seedcase-project/seedcase-sprout/commit/cffc566f72070597288bcecf06ffa34999ad2a14))

### 🧹 Chores

- *(sync)* Synced local '.editorconfig' with remote '.editorconfig'
  ([3e7d385](https://github.com/seedcase-project/seedcase-sprout/commit/3e7d3852091d6444435b26d741b201ebec1f04fd))
- *(sync)* Synced local '.vscode/' with remote '.vscode/'
  ([a970585](https://github.com/seedcase-project/seedcase-sprout/commit/a970585d6257afa4826ef5397e2c886289ccd882))

## [0.5.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.4.0..0.5.0) - 2025-01-20

### ✨ Features

- Put required fields into constants
  [#961](https://github.com/seedcase-project/seedcase-sprout/pull/961)
  ([34d8bad](https://github.com/seedcase-project/seedcase-sprout/commit/34d8bad01ef7071006595415ee23247b50d1103e))

## [0.4.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.3.0..0.4.0) - 2025-01-20

### ✨ Features

- Add custom `CheckError` for check functions
  [#924](https://github.com/seedcase-project/seedcase-sprout/pull/924)
  ([47b8941](https://github.com/seedcase-project/seedcase-sprout/commit/47b8941d689db436d891a943254bd91461edff42))

### 📝 Documentation

- Align table colwidths on reference index page
  [#971](https://github.com/seedcase-project/seedcase-sprout/pull/971)
  ([90fe27d](https://github.com/seedcase-project/seedcase-sprout/commit/90fe27d2adfe80c64fda690a17a91ea068587f94))

## [0.3.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.2.4..0.3.0) - 2025-01-20

### ✨ Features

- Add custom renderer to remove floating `:`
  [#959](https://github.com/seedcase-project/seedcase-sprout/pull/959)
  ([f48be5a](https://github.com/seedcase-project/seedcase-sprout/commit/f48be5a8671dfc3ab6c53539b50af7dd9b34ecee))

### 📝 Documentation

- Explain that we follow Seedcase's overall design
  [#936](https://github.com/seedcase-project/seedcase-sprout/pull/936)
  ([68f7ca9](https://github.com/seedcase-project/seedcase-sprout/commit/68f7ca96b61c9a1cdd8d5301282eb12415072b71))

### 🧹 Chores

- *(sync)* Synced local '.editorconfig' with remote '.editorconfig'
  ([0276805](https://github.com/seedcase-project/seedcase-sprout/commit/0276805c79cc07633a27b3301a481c25ea58f66d))
- *(sync)* Synced local 'justfile' with remote 'justfile'
  ([1fa0e94](https://github.com/seedcase-project/seedcase-sprout/commit/1fa0e944310261248e791aae0d0a124036bfbb49))

## [0.2.4](https://github.com/seedcase-project/seedcase-sprout/compare/0.2.3..0.2.4) - 2025-01-10

### ♻️ Refactor

- Rename sprout root to sprout global
  ([1c9cb25](https://github.com/seedcase-project/seedcase-sprout/commit/1c9cb2583caedd9e52e65f3ec3aba12f4af00271))
- Can't use the word global on it's own, so renamed to path
  ([58f61d9](https://github.com/seedcase-project/seedcase-sprout/commit/58f61d9fac38ce83b26eea50499d952ab71a0c73))

### 📝 Documentation

- Revise output design to default to working dir
  ([9478936](https://github.com/seedcase-project/seedcase-sprout/commit/947893655885bc0b3bb6ee8b0580ddce67afb4d1))

### 💄 Style

- Reformatted Markdown
  ([33cf8c1](https://github.com/seedcase-project/seedcase-sprout/commit/33cf8c1f4f84073b2ef77238aaf6f2a3686152c7))

## [0.2.3](https://github.com/seedcase-project/seedcase-sprout/compare/0.2.2..0.2.3) - 2025-01-10

### ♻️ Refactor

- Rename `SPROUT_ROOT` to `SPROUT_GLOBAL`
  [#935](https://github.com/seedcase-project/seedcase-sprout/pull/935)
  ([a4e0429](https://github.com/seedcase-project/seedcase-sprout/commit/a4e04299fb08e86b2d25f6e3b2dba506593edd92))

### 📝 Documentation

- Small edits to architecture and naming page
  [#922](https://github.com/seedcase-project/seedcase-sprout/pull/922)
  ([1e1b7b3](https://github.com/seedcase-project/seedcase-sprout/commit/1e1b7b36eb11cd8a4c9a531480e1800042e9e27a))
- Minor edits to docstrings
  [#932](https://github.com/seedcase-project/seedcase-sprout/pull/932)
  ([125b331](https://github.com/seedcase-project/seedcase-sprout/commit/125b331985626ecc4f38d89ec9428d0f9bc08d05))
- Fix typo wrties -> writes
  [#941](https://github.com/seedcase-project/seedcase-sprout/pull/941)
  ([0595a6f](https://github.com/seedcase-project/seedcase-sprout/commit/0595a6f5c617f0ec5d52c0c240f8950c327ca509))
- Add package to each subsection and remove core before functions
  [#942](https://github.com/seedcase-project/seedcase-sprout/pull/942)
  ([ce4d0a7](https://github.com/seedcase-project/seedcase-sprout/commit/ce4d0a70facce6e425e09c6fdd7207401f8eb637))
- Enable quartodoc dynamic lookup
  [#948](https://github.com/seedcase-project/seedcase-sprout/pull/948)
  ([5649fae](https://github.com/seedcase-project/seedcase-sprout/commit/5649fae062f2e5bbc25cfa0472f7e15dcceee3e3))
- Add signature annotations to reference docs
  [#952](https://github.com/seedcase-project/seedcase-sprout/pull/952)
  ([255f20b](https://github.com/seedcase-project/seedcase-sprout/commit/255f20b2de12cd0f6dafb6a19d07156c659b5489))
- Revise output design to default to working dir
  [#931](https://github.com/seedcase-project/seedcase-sprout/pull/931)
  ([5480caa](https://github.com/seedcase-project/seedcase-sprout/commit/5480caae523c46ec3a6dd1efdf54253395eb3b44))

### 🧹 Chores

- *(sync)* Synced local '.pre-commit-config.yaml' with remote
  '.pre-commit-config.yaml'
  ([1648c9c](https://github.com/seedcase-project/seedcase-sprout/commit/1648c9c9a3aecd627ac398fc0d98e115ce94a9f0))
- *(sync)* Synced local '.editorconfig' with remote '.editorconfig'
  ([0f93c35](https://github.com/seedcase-project/seedcase-sprout/commit/0f93c354ecc51542f859472d6131ef35e3f77f68))
- *(sync)* Synced local 'justfile' with remote 'justfile'
  ([408b228](https://github.com/seedcase-project/seedcase-sprout/commit/408b228ffde94757dc430b8648ac9b2e77aca7b0))
- *(sync)* Synced local '.github/dependabot.yml' with remote
  '.github/\_project-dependabot.yml'
  ([7585e2d](https://github.com/seedcase-project/seedcase-sprout/commit/7585e2dd2160595480d2d8ee17d76b06f40fff1b))
- *(sync)* Synced local '.vscode/' with remote '.vscode/'
  ([1295fde](https://github.com/seedcase-project/seedcase-sprout/commit/1295fdec819705b96c6d30da8b7b8ad90b143280))
- Rename implementation -> interface
  [#916](https://github.com/seedcase-project/seedcase-sprout/pull/916)
  ([000f04d](https://github.com/seedcase-project/seedcase-sprout/commit/000f04dc3640073c69b8ca7802f2a0c9f3775e76))

## [0.2.2](https://github.com/seedcase-project/seedcase-sprout/compare/0.2.1..0.2.2) - 2024-12-18

### ♻️ Refactor

- Rename `verify_` functions to `check_`
  [#918](https://github.com/seedcase-project/seedcase-sprout/pull/918)
  ([986e3f0](https://github.com/seedcase-project/seedcase-sprout/commit/986e3f0472cb5448cff1fb8ae66f2cb353489dbb))

## [0.2.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.2.0..0.2.1) - 2024-12-18

### ♻️ Refactor

- Move `check_` tests to `checks` folder
  [#915](https://github.com/seedcase-project/seedcase-sprout/pull/915)
  ([d4dca6c](https://github.com/seedcase-project/seedcase-sprout/commit/d4dca6c4328408f82701377696372e2cbb9c87d8))

## [0.2.0](https://github.com/seedcase-project/seedcase-sprout/compare/0.1.1..0.2.0) - 2024-12-16

### ✨ Features

- Check properties against standard
  [#905](https://github.com/seedcase-project/seedcase-sprout/pull/905)
  ([45921bd](https://github.com/seedcase-project/seedcase-sprout/commit/45921bde1bf7073487b5b93453dfb04695095c13))

### 📝 Documentation

- Update hero-text to describe modules and include lib
  [#904](https://github.com/seedcase-project/seedcase-sprout/pull/904)
  ([f16e6c6](https://github.com/seedcase-project/seedcase-sprout/commit/f16e6c6ecc20b103cf85293bb945eb2d3c66e426))

### 🧱 Build system

- Add GitHub workflow to keep track of Data Package versions
  [#881](https://github.com/seedcase-project/seedcase-sprout/pull/881)
  ([ca9f30a](https://github.com/seedcase-project/seedcase-sprout/commit/ca9f30a8306ad2db6984f815d35a44b266bef55f))

### 🧹 Chores

- *(sync)* Synced local '\_extensions/seedcase-project/seedcase-theme/' with
  remote '\_extensions/seedcase-theme/'
  ([690ac44](https://github.com/seedcase-project/seedcase-sprout/commit/690ac4406d2b02e4275118785ee49708b5b86b33))
- Set `update_changelog_on_bump` to true
  [#889](https://github.com/seedcase-project/seedcase-sprout/pull/889)
  ([bf8909b](https://github.com/seedcase-project/seedcase-sprout/commit/bf8909bce19cc3b32cec13f714836a7074f4a7ba))

## [0.1.1](https://github.com/seedcase-project/seedcase-sprout/compare/0.1.0..0.1.1) - 2024-11-21

### 🐛 Fixes

- Compact form of nested properties
  [#887](https://github.com/seedcase-project/seedcase-sprout/pull/887)
  ([bfcc039](https://github.com/seedcase-project/seedcase-sprout/commit/bfcc039dca9d9d969a6105cc2dc43da360d54dc9))

### 📝 Documentation

- Describe split between `lib` and `core`
  [#872](https://github.com/seedcase-project/seedcase-sprout/pull/872)
  ([a623896](https://github.com/seedcase-project/seedcase-sprout/commit/a623896217cf34be720e34a393c093e9c843f340))
- Update requirements doc
  [#876](https://github.com/seedcase-project/seedcase-sprout/pull/876)
  ([46578d7](https://github.com/seedcase-project/seedcase-sprout/commit/46578d72200861fc42849a37c30df9a99d753a5b))

### 🧹 Chores

- *(sync)* Synced local '.editorconfig' with remote '.editorconfig'
  ([caa97c9](https://github.com/seedcase-project/seedcase-sprout/commit/caa97c99bb18e567b873be0a2aa49591c5e098c8))
- *(sync)* Synced local '.gitignore' with remote '.gitignore'
  ([3aa2716](https://github.com/seedcase-project/seedcase-sprout/commit/3aa2716a309508b6518a37977fbbaf318f483fbb))
- *(sync)* Synced local 'justfile' with remote 'justfile'
  ([c29c37a](https://github.com/seedcase-project/seedcase-sprout/commit/c29c37a4ccb11a5eaa0a72b15c7fc3e90785e95f))
- *(sync)* Synced local '.github/pull_request_template.md' with remote
  '.github/pull_request_template.md'
  ([09ba472](https://github.com/seedcase-project/seedcase-sprout/commit/09ba4726ae958c0c022473b7872860357fb31a19))
- No longer need these files
  [#877](https://github.com/seedcase-project/seedcase-sprout/pull/877)
  ([2bca370](https://github.com/seedcase-project/seedcase-sprout/commit/2bca370db2a685a29a5623066932a520707e6882))
- Convert these to draft and/or hide from website
  [#878](https://github.com/seedcase-project/seedcase-sprout/pull/878)
  ([db4a788](https://github.com/seedcase-project/seedcase-sprout/commit/db4a788840dc3c22a7b24ec57392b2828784e272))
- Remove last remains of older code and deploy files
  [#875](https://github.com/seedcase-project/seedcase-sprout/pull/875)
  ([a1675b7](https://github.com/seedcase-project/seedcase-sprout/commit/a1675b729224f8250ae9b81746fc719261852425))

## 0.1.0 - 2024-11-13

### ✨ Features

- *(dependabot)* Add dependabot for updating Python dependencies
  ([6d342f2](https://github.com/seedcase-project/seedcase-sprout/commit/6d342f237021f6ca5d188ed2a9baff5e75ca51ee))
- Create png of login sequence and remove todo item on that
  ([c5e1a4e](https://github.com/seedcase-project/seedcase-sprout/commit/c5e1a4e442797a2b274cffca95dcbb4b39b2e40c))
- Add title to login sequence diagram
  ([b19afaf](https://github.com/seedcase-project/seedcase-sprout/commit/b19afafcabdf5a32b9859af0c77091b63741dfc5))
- Add flow diagram of preparing schema for upload
  ([08d0551](https://github.com/seedcase-project/seedcase-sprout/commit/08d0551436390e7b3b0e1b0c63631352f26910ae))
- Initial flow chart of entire user flow
  ([790a2fc](https://github.com/seedcase-project/seedcase-sprout/commit/790a2fc5da429c7d4f31b6dbe9386513a232ef77))
- Split up user flow diagram into separate diagrams for user flow post
  ([97da2fa](https://github.com/seedcase-project/seedcase-sprout/commit/97da2fa4c1b1eb96982f131878671bf534a6100e))
- Add initial version of user flow post
  ([e817094](https://github.com/seedcase-project/seedcase-sprout/commit/e8170944a87568e2297e474c2d191e2566fa94c8))
- Add "system displays the number of validated rows to the user for agreement"
  ([731db85](https://github.com/seedcase-project/seedcase-sprout/commit/731db858c07c1cb6042aa432939d03fda0acf99a))
- Add user confirmation of validated row to add in upload
  ([ccf92da](https://github.com/seedcase-project/seedcase-sprout/commit/ccf92daa7fd044193f58ddaa80cf7d07f767b0a3))
- Adding of migrations
  ([df814f4](https://github.com/seedcase-project/seedcase-sprout/commit/df814f469f7a81f4edb62d9573b43803d8006aad))
- Models added for table and column meta data
  ([591221f](https://github.com/seedcase-project/seedcase-sprout/commit/591221faf174fd1cb731c3d0c028d38bd9bd89b9))
- PR review adjustments
  ([adf6e52](https://github.com/seedcase-project/seedcase-sprout/commit/adf6e529f7271e2f9f9e311875d53a887b2878a2))
- Fixing tests
  ([6253829](https://github.com/seedcase-project/seedcase-sprout/commit/62538299444676177cfa610f9ad7c4b9885d7709))
- Add "all" to generate-puml command
  ([5910e11](https://github.com/seedcase-project/seedcase-sprout/commit/5910e118ab2d86b3b0a3c4ae7b6ab86bdc4908ca))
- Add command to generate png from specific puml
  ([8c038d9](https://github.com/seedcase-project/seedcase-sprout/commit/8c038d91fe4f9dec47c6a978cc4adc3182e9c106))
- Draft
  ([1889919](https://github.com/seedcase-project/seedcase-sprout/commit/1889919199e4f0b42896246627fac0ff5d50a79c))
- Commit before merging from main
  ([a9e11be](https://github.com/seedcase-project/seedcase-sprout/commit/a9e11be79d7cb5239f9ba8f24f66e5bbbf9a21b5))
- Simple file upload is created
  ([0540aab](https://github.com/seedcase-project/seedcase-sprout/commit/0540aab8151698d10e33edb2841bad1cda8bec5e))
- Added dropzone and file information box
  ([19c0c38](https://github.com/seedcase-project/seedcase-sprout/commit/19c0c3851ba615ccd4f1115a45a4aa979797e6d1))
- Matching details with wireframe
  ([b7e39eb](https://github.com/seedcase-project/seedcase-sprout/commit/b7e39eb12969458ba8042d23e51302cd683dd206))
- Init/wip
  ([b8667cb](https://github.com/seedcase-project/seedcase-sprout/commit/b8667cb17359c18b6e31f77b8a5b8fc9d63c8977))
- Change tablecreation form to modelform
  ([aef702d](https://github.com/seedcase-project/seedcase-sprout/commit/aef702d0ad153c2e7898c2941b2b94b550fe10e1))
- Update data_import view to use and validate tablemetadataform
  ([b38c96d](https://github.com/seedcase-project/seedcase-sprout/commit/b38c96ddf271521ca8e6d2f905ba32a4cd206467))
- Hotfix - created_at defaults to none until we implement users
  ([6f1a0ea](https://github.com/seedcase-project/seedcase-sprout/commit/6f1a0ea85cdaf185f03057b901d8eee4e921afa2))
- Update html to utilise modelform fields
  ([1e07650](https://github.com/seedcase-project/seedcase-sprout/commit/1e07650ba71c3ce27b4836c1d21d7ae610330389))
- Add table id to file-upload url
  ([1af3659](https://github.com/seedcase-project/seedcase-sprout/commit/1af365992968dc38309c69b1d921a8a0f9d9d35a))
- Add validator to prevent special characters in the table name field
  ([eeda556](https://github.com/seedcase-project/seedcase-sprout/commit/eeda55680cd1e9ea22fa8f130aa4929dd4a0cf5c))
- Add validator to prevent creating tables with name that already exists
  ([46558fe](https://github.com/seedcase-project/seedcase-sprout/commit/46558feb2a05291aad51cc865d4ab9173866896d))
- Show validation errors for name field
  ([05cde3c](https://github.com/seedcase-project/seedcase-sprout/commit/05cde3c8fa85f317e673d0668bb387c8711b17a0))
- Center align dialog header
  ([dd26e4b](https://github.com/seedcase-project/seedcase-sprout/commit/dd26e4bdc5164ace9719204ae2bded73184577ee))
- Add icon to align with wireframes
  ([2e7930d](https://github.com/seedcase-project/seedcase-sprout/commit/2e7930d986c39c1c6d04054ffcb5382423cdfa8a))
- Add help button with dialog overlay
  ([0490579](https://github.com/seedcase-project/seedcase-sprout/commit/04905793b681df8d64acb32e96c878306b73351c))
- Include val of table already existing directly in the modelform
  ([7d3620e](https://github.com/seedcase-project/seedcase-sprout/commit/7d3620ec6f602501339339157fddc6d1699a4ad7))
- Update special characters validator to include field_name in error msg
  ([d1898c2](https://github.com/seedcase-project/seedcase-sprout/commit/d1898c279a8b28b91ccefe7cd9c2efc0b7659b59))
- Add error code to validate_table_name_does_not_exist
  ([8fd0934](https://github.com/seedcase-project/seedcase-sprout/commit/8fd0934bdd8da874c4d81eb2dfcf37ae161c19cf))
- Add tests for data_import view
  ([b464d1e](https://github.com/seedcase-project/seedcase-sprout/commit/b464d1e3928a2c05a5e5f1e03289ed5f8fa0a2d5))
- Add cursor pointer to card-button-size buttons
  ([dca0258](https://github.com/seedcase-project/seedcase-sprout/commit/dca02589a0a59a4fb5631f7d6f415f6fb50db353))
- Add progress bar dialog
  ([5d3d6f5](https://github.com/seedcase-project/seedcase-sprout/commit/5d3d6f5442838ae420d3dd6f764dfdfadf35d9eb))
- Show progress bar dialog at click on submit button
  ([bccaeea](https://github.com/seedcase-project/seedcase-sprout/commit/bccaeea65e195d0ea18179d198a8a7526390642c))
- Wait two seconds after click on submit to show progress bar
  ([6cd6c79](https://github.com/seedcase-project/seedcase-sprout/commit/6cd6c7912ff826cc271d2ec3e8ecf8ff2d334616))
- Central location for ColumnDataTypes
  ([45b5135](https://github.com/seedcase-project/seedcase-sprout/commit/45b5135b37c20194079a39b0b1fde7f2ab1da319))
- Adjusting docstrings
  ([2fc1f90](https://github.com/seedcase-project/seedcase-sprout/commit/2fc1f901bed41471bb94436fe30b0422f8e88de2))
- Add original name to columnmetadata
  ([f1057ea](https://github.com/seedcase-project/seedcase-sprout/commit/f1057ea916910fb07b98101989f584567bbafb19))
- Add original name as name
  ([5a0dc8a](https://github.com/seedcase-project/seedcase-sprout/commit/5a0dc8a420c97301996c86e94d13521592ada30c))
- Read csv file with polars
  ([2fe0d4f](https://github.com/seedcase-project/seedcase-sprout/commit/2fe0d4fdb6edd94082aed458fde99a6a1e162b72))
- Small adjustments
  ([2d47181](https://github.com/seedcase-project/seedcase-sprout/commit/2d471816c1cfb80cf599c0c53fae2eeb31dc2c5b))
- Persistent storage
  ([eaddb5d](https://github.com/seedcase-project/seedcase-sprout/commit/eaddb5d9843538fd1cfd7fe0fcb5a590859e7289))
- Testing preview environment
  ([f56d5b3](https://github.com/seedcase-project/seedcase-sprout/commit/f56d5b3921e186e649ac23bf5cf01ebe109d35aa))
- Upload file to persistent storage
  ([2a0dc73](https://github.com/seedcase-project/seedcase-sprout/commit/2a0dc731068d9c0af373646cab93b46f98ea0043))
- Delete method is added
  ([4b50fc6](https://github.com/seedcase-project/seedcase-sprout/commit/4b50fc6ff22035a4cbaa9078a1b9c1c079ef4837))
- Keep markdown files to preserve folder structure
  ([a768ae2](https://github.com/seedcase-project/seedcase-sprout/commit/a768ae22f79ab8793eebe7ef0ac46b15a1c11b4e))
- Add file size
  ([acd1b56](https://github.com/seedcase-project/seedcase-sprout/commit/acd1b56da4a3a88ea49a772bfd6bee0e54a2688d))
- Created_by is added
  ([8ab2710](https://github.com/seedcase-project/seedcase-sprout/commit/8ab271008a97a15c9465cfed6ca9808bc0f4c6f0))
- Adding polars_types to ColumnDataType
  ([29e0f93](https://github.com/seedcase-project/seedcase-sprout/commit/29e0f9322de879ee67ef4fb872147918d8a64cf3))
- Description as Text input and **str** added on ColumnDataType
  ([ce62540](https://github.com/seedcase-project/seedcase-sprout/commit/ce625401f8027ed57e5497305f2f569e84102fc9))
- Create test scripts for views of column data
  ([73d772b](https://github.com/seedcase-project/seedcase-sprout/commit/73d772b8199d7e434054bcdf3cf97ef45bdab7ab))
- Disable migrations by not committing migrations into git. Furthermore, the
  database is not in the persistent storage
  ([cd0511e](https://github.com/seedcase-project/seedcase-sprout/commit/cd0511e60b516cd4ddaad2a4909f11f3c82d5ee8))
- Add util function to convert string to snake case
  ([2e4ecde](https://github.com/seedcase-project/seedcase-sprout/commit/2e4ecde2d5cf86db38d10ce006a916a553bced4a))
- Use \_convert_to_snake_case for column names
  ([a0edc8e](https://github.com/seedcase-project/seedcase-sprout/commit/a0edc8ee8bea39f359c656553e6c663fe340e101))
- Init existing tables view
  ([4d33fd2](https://github.com/seedcase-project/seedcase-sprout/commit/4d33fd2ba7bc017dc4be6882f99ede028b23d493))
- Init view existing table template
  ([f4b1f63](https://github.com/seedcase-project/seedcase-sprout/commit/f4b1f638c77a43a0539297628027bcd8dd1b4553))
- Add view-existing-tables to urls
  ([1e61bcb](https://github.com/seedcase-project/seedcase-sprout/commit/1e61bcbda9089cbb2bd9a21329d019eb416cadee))
- Add existing tables view to view init
  ([7a80fe3](https://github.com/seedcase-project/seedcase-sprout/commit/7a80fe32cc97b290774bf3ab2b88505733f31fa2))
- Change from ID to Original name
  ([3679b57](https://github.com/seedcase-project/seedcase-sprout/commit/3679b578646786782a9077a4f4e7e22c0f23fef3))
- Create review list view
  ([211ca9e](https://github.com/seedcase-project/seedcase-sprout/commit/211ca9e140ad33c220d1f10348b256b313b5aa15))
- Add autocomplete="off" for form
  ([1ea1bcc](https://github.com/seedcase-project/seedcase-sprout/commit/1ea1bcc798b18da7d99c97cdc798f2be0028a818))
- Read_csv uses file path and ColumnMetaData created
  ([c3a512f](https://github.com/seedcase-project/seedcase-sprout/commit/c3a512fffd3496ebbf1e55fd83d548896f3ed067))
- Simple file download example
  ([d04d741](https://github.com/seedcase-project/seedcase-sprout/commit/d04d7418fcc0bd227d354c0df44c15b854c0b29f))
- Show files as tables
  ([8a8c044](https://github.com/seedcase-project/seedcase-sprout/commit/8a8c0446bc51daead91f77039107f28bc2c8c055))
- Files are displayed in a table
  ([8f66f93](https://github.com/seedcase-project/seedcase-sprout/commit/8f66f93980be635f958545eebd4d64cd07a20c02))
- Validates columns
  ([e78a078](https://github.com/seedcase-project/seedcase-sprout/commit/e78a0781a831d1ec3a4836ca2c171c0167807b28))
- Validates columns
  ([2624a34](https://github.com/seedcase-project/seedcase-sprout/commit/2624a34959fa6a749f1565fda6f49ab1d006982d))
- Handles more invalid csv files
  ([1acddb9](https://github.com/seedcase-project/seedcase-sprout/commit/1acddb9e6d07770cb9b918038a3b1db0b8a4fd30))
- Adding style to Kris' work
  ([ae3fb77](https://github.com/seedcase-project/seedcase-sprout/commit/ae3fb779fd54b2ca87d6cadd8ea4fdc638f1d746))
- Add tabindex with a custom templatetag
  ([abe5871](https://github.com/seedcase-project/seedcase-sprout/commit/abe58711efc9327948fd2ab8fa8f23e956989efc))
- Tabindex on all
  ([52c271d](https://github.com/seedcase-project/seedcase-sprout/commit/52c271d1458c4720086e8f8fe7b542095bf60aed))
- Show tooltips for headers
  ([71cf377](https://github.com/seedcase-project/seedcase-sprout/commit/71cf37779f6ebcc335649faaafd9d34908e2efd3))
- Add paragraph when there is not data to view
  ([2059a4c](https://github.com/seedcase-project/seedcase-sprout/commit/2059a4c7ace901183d3b9e161ca2f244b73bab4a))
- Button to switch between table vs grid view for metadata editing
  ([23fa671](https://github.com/seedcase-project/seedcase-sprout/commit/23fa671c62125c87f9e7277e6574b13dd11fe82f))
- Add that clicking row again will deselect the row
  ([aebe146](https://github.com/seedcase-project/seedcase-sprout/commit/aebe146b8be5c36ce60207fc4f1e6a0469f389a6))
- Redirect to data-import when create btn is clicked
  ([bcac1e8](https://github.com/seedcase-project/seedcase-sprout/commit/bcac1e850962ee9418b4ea595b7574466d20280e))
- Add error dialog when user clicks edit or upload without selecting a row
  ([f638ce2](https://github.com/seedcase-project/seedcase-sprout/commit/f638ce2d10596d3b4d2b6df3e4179abd96bcb65d))
- Automatically add test data when DEBUG=TRUE
  ([cc7593f](https://github.com/seedcase-project/seedcase-sprout/commit/cc7593fa4ec6d6800c83b6163bd6953f2f4cb0fa))
- Adding to description that this is test data
  ([c889e9a](https://github.com/seedcase-project/seedcase-sprout/commit/c889e9ae62d965a8d1e5a5d4475267d4942d610e))
- Disable when running unit tests
  ([ee9469d](https://github.com/seedcase-project/seedcase-sprout/commit/ee9469d99ce9bb383b23e36d06fc13ec682ccdb7))
- Ruff adjustments
  ([2a39b4b](https://github.com/seedcase-project/seedcase-sprout/commit/2a39b4b6806d332b8c74bb62fe6864a23e1a2431))
- Change dialog to disabled for button edit and upload
  ([0ac8b22](https://github.com/seedcase-project/seedcase-sprout/commit/0ac8b2207c598a75f362dec4173761184a2d4db6))
- Exclude column checkbox
  ([94429ee](https://github.com/seedcase-project/seedcase-sprout/commit/94429eea6c08af125c7c37d378b653962e76fd92))
- Preview data sample is added
  ([0cc9443](https://github.com/seedcase-project/seedcase-sprout/commit/0cc9443bc3c9271067fe0accabdeca24ce0881fb))
- Added equals sign <=5
  ([191cc20](https://github.com/seedcase-project/seedcase-sprout/commit/191cc2054acbc398902cab9564511dd773f0f253))
- Support for decimals with comma is added
  ([ea19668](https://github.com/seedcase-project/seedcase-sprout/commit/ea19668a4f1a971d935137f925ebb6b6301fedd4))
- Removed print statement
  ([2b3cb51](https://github.com/seedcase-project/seedcase-sprout/commit/2b3cb5146221ecda1b05791e73e2cddae8da873d))
- Authentication and password reset is created
  ([9d5b0e1](https://github.com/seedcase-project/seedcase-sprout/commit/9d5b0e162f0f2a842d59db3922a6009715f24f52))
- Template is moved
  ([f39ca2b](https://github.com/seedcase-project/seedcase-sprout/commit/f39ca2b6caf74965e7d89e36cd1c820805f8ccf8))
- Add column metadata expands on select
  ([3e4d9af](https://github.com/seedcase-project/seedcase-sprout/commit/3e4d9af105bd56109977343a09b50a61f1e70f0e))
- Only show first 10 columns to avoid cluttering the view too much
  ([d998685](https://github.com/seedcase-project/seedcase-sprout/commit/d998685c47ed3a8159410d7d922af1f06a894ae2))
- Column metadata is shown underneath each metadata row
  ([e893925](https://github.com/seedcase-project/seedcase-sprout/commit/e893925f625d8c7e58695082a4c36dd0433308a6))
- Column metadata is only shown when metadata row is selected
  ([5af3827](https://github.com/seedcase-project/seedcase-sprout/commit/5af3827332e49b5b230ec9f3fd35d1e0f2336ddb))
- Values preserved between view switches
  ([a4d5980](https://github.com/seedcase-project/seedcase-sprout/commit/a4d59800032bcfa3c2c794851db95a5fa160b730))
- Name change
  ([8b12074](https://github.com/seedcase-project/seedcase-sprout/commit/8b1207414e5cf385d726e73ba9ea862599ce1de8))
- Add dialog to view and html
  ([6c38745](https://github.com/seedcase-project/seedcase-sprout/commit/6c3874524b3dfdb98c17c6c017957e89f6674d8a))
- Human friendly names to hint the difference between extracted_name and
  display_name
  ([5a85fe7](https://github.com/seedcase-project/seedcase-sprout/commit/5a85fe7239b2ee92038523fe979102510107feb1))
- Working on adding upload page
  ([f39764c](https://github.com/seedcase-project/seedcase-sprout/commit/f39764c0f2c2b4504f79bf3d97a8a6b670b8819c))
- Added Django view for uploading data
  ([71a661f](https://github.com/seedcase-project/seedcase-sprout/commit/71a661fc583495b081c4efe9e6527aa4b6b5e19f))
- New page for uploading data files, finally
  ([ec426f2](https://github.com/seedcase-project/seedcase-sprout/commit/ec426f225e8c96a575032cd45c4137f3d02cd4bc))
- Synching to switch computers
  ([b4e7a73](https://github.com/seedcase-project/seedcase-sprout/commit/b4e7a735945e3d177e6a849c6d8079e0b9eb8f24))
- Update data to an existing table (but still incomplete)
  ([438c2ac](https://github.com/seedcase-project/seedcase-sprout/commit/438c2aca8fb409b81bf48df7140e27424cfc4baf))
- Add data for user test
  ([06df7e8](https://github.com/seedcase-project/seedcase-sprout/commit/06df7e8eafa876d5926a4c81dee8cdbe1a10ea2e))
- Changing the font to Rajdhani
  ([aa3c9a8](https://github.com/seedcase-project/seedcase-sprout/commit/aa3c9a8eb744f0f1b4b9f13d10d5a5cb274bf8f6))
- Add info text to metadata-id-create
  ([a8957e8](https://github.com/seedcase-project/seedcase-sprout/commit/a8957e8fa01e96319f15fabebfe24aa72e70f40f))
- Add data_rows to tables model to populate and update field at file upload
  ([1f336cd](https://github.com/seedcase-project/seedcase-sprout/commit/1f336cdc46ffee4224073524c99fb01e234c2f29))
- Populate and update last upload at data upload
  ([bf554c9](https://github.com/seedcase-project/seedcase-sprout/commit/bf554c958cc6f1ed3fbb697dd72fe1d1599f2fe3))
- Add last upload to `Tables` and update it when data_rows are not 0
  ([e59c6f1](https://github.com/seedcase-project/seedcase-sprout/commit/e59c6f13c5f47fd5d39da9dbebd6509404ed65a1))
- Add multiple outline colours and a shadow var
  ([e21abc2](https://github.com/seedcase-project/seedcase-sprout/commit/e21abc26daa9bcb49bf244e79ff95e7ecc047f2c))
- Parse existing_metadata_columns as a dict to view to be able to filter on
  table_id
  ([4f3b490](https://github.com/seedcase-project/seedcase-sprout/commit/4f3b49099edaff876ea89b9d357f74c15e0bf429))
- Add dictionary filter by key to be used in view
  ([ca27c4d](https://github.com/seedcase-project/seedcase-sprout/commit/ca27c4d2b6acbd9a6ed63adba230b2d9d328e2bd))
- Load dict tags and utilise it to show only first five cols
  ([73cabf8](https://github.com/seedcase-project/seedcase-sprout/commit/73cabf88817618d7c46fd32721650ee3d1849b3e))
- Add button to show five more cols
  ([8dfe431](https://github.com/seedcase-project/seedcase-sprout/commit/8dfe431e8870fd0dbb6eca760a421f1e470d2db6))
- Add shown class to rows that should are unhidden to hide them again later
  ([09d8c2c](https://github.com/seedcase-project/seedcase-sprout/commit/09d8c2c85288f3b75e7c32f77332a9ac61267604))
- Existing metadata view expanded to show first 5 cols
  [#359](https://github.com/seedcase-project/seedcase-sprout/pull/359)
  ([8795691](https://github.com/seedcase-project/seedcase-sprout/commit/8795691535050f295e5d370ed6dd06b794d50ef7))
- Add expand_less icon to metadata table rows
  ([8187915](https://github.com/seedcase-project/seedcase-sprout/commit/818791573987efebc135104f649c3dee245974dc))
- With js, add that icon changes to expand_more when row is selected
  ([60d6de4](https://github.com/seedcase-project/seedcase-sprout/commit/60d6de457dca6d9889747655b87a6aa198287464))
- Add expand_less/expand_more icons when metadata row is selected and unselected
  [#386](https://github.com/seedcase-project/seedcase-sprout/pull/386)
  ([19102a5](https://github.com/seedcase-project/seedcase-sprout/commit/19102a51eed920ba48ee8f2bc36481c9f2578a66))
- Add logo svg
  ([471c979](https://github.com/seedcase-project/seedcase-sprout/commit/471c9797512e64e484711c1ffe80c28030ee676c))
- Add logo to navbar and head
  ([af42719](https://github.com/seedcase-project/seedcase-sprout/commit/af4271978f0d6acefdb4eb8a8a1af3d57350620c))
- Add menu icon and enlargen navbar icons
  ([3979b05](https://github.com/seedcase-project/seedcase-sprout/commit/3979b054baf8a8f410ac31f119477dedee384583))
- Add mirrored background to use in navbar
  ([4a6444b](https://github.com/seedcase-project/seedcase-sprout/commit/4a6444b1683866954d0f45ee617b4d20b122dbc0))
- Add column descriptions
  ([55c0686](https://github.com/seedcase-project/seedcase-sprout/commit/55c0686f0840beb9f4d3f7ab80a167d266d80303))
- Authentication and password reset is created
  [#347](https://github.com/seedcase-project/seedcase-sprout/pull/347)
  ([2c72f0c](https://github.com/seedcase-project/seedcase-sprout/commit/2c72f0c43ab51728f99fa88c2568f3a3474c88ee))
- First upload of docker compose file
  ([75de511](https://github.com/seedcase-project/seedcase-sprout/commit/75de511df966c02b7043038a776241b807dd5ae8))
- Update dockerfile - remove 22 and 25
  ([5f37a8c](https://github.com/seedcase-project/seedcase-sprout/commit/5f37a8cc096db074dbf0dfaa2fd3f6df80e36404))
- Update yml file to persist data in postgres
  ([75dbbee](https://github.com/seedcase-project/seedcase-sprout/commit/75dbbee230752aaa3934b9a48fdbda629b496282))
- Remove linting issues
  ([d88a5e3](https://github.com/seedcase-project/seedcase-sprout/commit/d88a5e3aa10503b2409ef5ea4c7d9959bcdc03db))
- Update to run psycopg2-binary
  ([4c8fc41](https://github.com/seedcase-project/seedcase-sprout/commit/4c8fc41b738d719f76938d3f8358f7025c1238f2))
- Update with comments by Philip
  ([b18f042](https://github.com/seedcase-project/seedcase-sprout/commit/b18f0420f0a4398aa213f18b061ffffd7808316e))
- Small change
  ([ce60bc1](https://github.com/seedcase-project/seedcase-sprout/commit/ce60bc171a6843d4fba661da71a64eb679239431))
- First draft
  ([aec2842](https://github.com/seedcase-project/seedcase-sprout/commit/aec28422d90ac53ba629ba5ee590640985a578b0))
- View divided in steps
  ([9448a63](https://github.com/seedcase-project/seedcase-sprout/commit/9448a6301e7fcfb22595b431965f7cb501c24288))
- Small fixes
  ([82cea5a](https://github.com/seedcase-project/seedcase-sprout/commit/82cea5aa3f34b0144f6167d95a3f265815d51c1c))
- Rename refactor
  ([8c1b030](https://github.com/seedcase-project/seedcase-sprout/commit/8c1b0308eb87dc0524a323bf049788ff92045c16))
- Making it work with existing links and deleting old stuff
  ([0c11dec](https://github.com/seedcase-project/seedcase-sprout/commit/0c11deccb5bd91818bc2e01c42590025132b12b2))
- Confirmation page
  ([64415c9](https://github.com/seedcase-project/seedcase-sprout/commit/64415c9ee1262022d2a969a7dea765acb64197b7))
- Confirmation page
  ([c3e81f9](https://github.com/seedcase-project/seedcase-sprout/commit/c3e81f9483a06ffb4fa964308c0633dfed428dd6))
- Single page for metadata creation steps
  [#415](https://github.com/seedcase-project/seedcase-sprout/pull/415)
  ([6b02fbf](https://github.com/seedcase-project/seedcase-sprout/commit/6b02fbf5f7a5d7f3e0d880c668ebbb79fc90c031))
- Add sprout logo with alt label to navbar
  ([dc53c4f](https://github.com/seedcase-project/seedcase-sprout/commit/dc53c4f572cd2de63196276d247715734bab37e2))
- Add aria labels to icons in navabr
  ([231d8d3](https://github.com/seedcase-project/seedcase-sprout/commit/231d8d33c2182de20dbd9077bf3c1613d3c47a23))
- Add seedcase theme to pumls
  ([78b9476](https://github.com/seedcase-project/seedcase-sprout/commit/78b94763d102d6fe985fab708a67acd5e388adc9))
- Regenerate pumls as svgs instead of pngs
  ([dde9ef0](https://github.com/seedcase-project/seedcase-sprout/commit/dde9ef0fe8b44cecf1b400e9afec52e4183fada6))
- Format text
  ([183327a](https://github.com/seedcase-project/seedcase-sprout/commit/183327af3b854385920b1987bb641d75578b21e6))
- Add puml name
  ([36d8d08](https://github.com/seedcase-project/seedcase-sprout/commit/36d8d08c0c57c817672f3232a700aa735242c17e))
- Add seedcase theme
  ([09a6d12](https://github.com/seedcase-project/seedcase-sprout/commit/09a6d12cc7e39af62e114002d5d1de319778f4a0))
- Add `verify_is_dir()`
  [#578](https://github.com/seedcase-project/seedcase-sprout/pull/578)
  ([632ac5f](https://github.com/seedcase-project/seedcase-sprout/commit/632ac5f94dd56d403c53dfa5912f1dc7c0348d7c))
- Add `create_next_id()`
  [#585](https://github.com/seedcase-project/seedcase-sprout/pull/585)
  ([6c4e8e1](https://github.com/seedcase-project/seedcase-sprout/commit/6c4e8e1bf09ef0f0c212b346d7b67d7c49faf913))
- Add `create_resource_raw_path()`
  [#587](https://github.com/seedcase-project/seedcase-sprout/pull/587)
  ([25e3ea2](https://github.com/seedcase-project/seedcase-sprout/commit/25e3ea21a1292ffab5c64971fea9cc12d01f0d90))
- Add `create_id_path()`
  [#591](https://github.com/seedcase-project/seedcase-sprout/pull/591)
  ([4b40cb5](https://github.com/seedcase-project/seedcase-sprout/commit/4b40cb517d96a21ccacdde1b20d1d40f812d0e0c))
- Add `get_ids()` function
  [#582](https://github.com/seedcase-project/seedcase-sprout/pull/582)
  ([20a558f](https://github.com/seedcase-project/seedcase-sprout/commit/20a558f965703bdedb13b7357663178a27e20f97))
- Add `verify_format_supported()`
  [#592](https://github.com/seedcase-project/seedcase-sprout/pull/592)
  ([982c9e7](https://github.com/seedcase-project/seedcase-sprout/commit/982c9e71c235ac1f64a70dcf808c92d66a5e5bc3))
- Add `create_relative_resource_data_path()`
  [#596](https://github.com/seedcase-project/seedcase-sprout/pull/596)
  ([aeea3ef](https://github.com/seedcase-project/seedcase-sprout/commit/aeea3efd772f8b7461edb0aafbdcb47449d95d68))
- Add `verify_is_file()`
  [#597](https://github.com/seedcase-project/seedcase-sprout/pull/597)
  ([9219198](https://github.com/seedcase-project/seedcase-sprout/commit/92191985b0ebe62e44acedd0e901992604dcb3db))
- Add `create_dir()` and `create_dirs()` with tests
  [#586](https://github.com/seedcase-project/seedcase-sprout/pull/586)
  ([0d4b08a](https://github.com/seedcase-project/seedcase-sprout/commit/0d4b08aa486e2781dda3a354ed70ea6da51345ad))
- Add `extract_properties_from_file()`
  [#594](https://github.com/seedcase-project/seedcase-sprout/pull/594)
  ([1d7ca5f](https://github.com/seedcase-project/seedcase-sprout/commit/1d7ca5f5ebb4036f8d8891aa41ac1e3441b41a45))
- Add `create_resource_structure()`
  [#610](https://github.com/seedcase-project/seedcase-sprout/pull/610)
  ([a0b5b05](https://github.com/seedcase-project/seedcase-sprout/commit/a0b5b05a5f3cbd67c95e7136f17c4454fcd8a82b))
- Add `edit_resource_properties_field()`
  [#621](https://github.com/seedcase-project/seedcase-sprout/pull/621)
  ([ba4911a](https://github.com/seedcase-project/seedcase-sprout/commit/ba4911af183192a35ba94693f936243c91363dd2))
- Add `verify_resource_properties()`
  [#613](https://github.com/seedcase-project/seedcase-sprout/pull/613)
  ([7761fe5](https://github.com/seedcase-project/seedcase-sprout/commit/7761fe551f5e2c9e59165c6e20b4597962051c91))
- Add `drop_property_fields()`
  [#629](https://github.com/seedcase-project/seedcase-sprout/pull/629)
  ([ad927b3](https://github.com/seedcase-project/seedcase-sprout/commit/ad927b3a1b8d75349d7fde61c652da0109435c20))
- Add `create_properties_path()`
  [#632](https://github.com/seedcase-project/seedcase-sprout/pull/632)
  ([fd220dc](https://github.com/seedcase-project/seedcase-sprout/commit/fd220dc48b10eacabd6444bd8407d3ffcfa05a13))
- Add `create_readme_path()`
  [#630](https://github.com/seedcase-project/seedcase-sprout/pull/630)
  ([cbbb6e3](https://github.com/seedcase-project/seedcase-sprout/commit/cbbb6e3c478ab8935dcfe2b9088dddc680949150))
- Add `write_file()`
  [#631](https://github.com/seedcase-project/seedcase-sprout/pull/631)
  ([6bfd8b1](https://github.com/seedcase-project/seedcase-sprout/commit/6bfd8b19779181d1d14f1f5209194958552fabb6))
- Add `scrape_json_from_url()`
  [#628](https://github.com/seedcase-project/seedcase-sprout/pull/628)
  ([f8d0c2a](https://github.com/seedcase-project/seedcase-sprout/commit/f8d0c2a12549ba35b31f37f3cc3d9ab17996bf36))
- Add `create_resource_properties()`
  [#633](https://github.com/seedcase-project/seedcase-sprout/pull/633)
  ([4f65ed8](https://github.com/seedcase-project/seedcase-sprout/commit/4f65ed8ea878dbde65813d15c17548c18761e7be))
- Add `get_root_envvar()`
  [#688](https://github.com/seedcase-project/seedcase-sprout/pull/688)
  ([79ebe4f](https://github.com/seedcase-project/seedcase-sprout/commit/79ebe4f9d5ee286add485fdfc92c9a3887921f90))
- Add `create_root_path()`
  [#689](https://github.com/seedcase-project/seedcase-sprout/pull/689)
  ([6d514ff](https://github.com/seedcase-project/seedcase-sprout/commit/6d514ff2385977afa1e4b4165e604df3623ad83a))
- Add `path_sprout_root()`
  [#705](https://github.com/seedcase-project/seedcase-sprout/pull/705)
  ([f52972e](https://github.com/seedcase-project/seedcase-sprout/commit/f52972ece152c2a118988056e5949259744be41e))
- Auto-generate property dataclasses based on spec
  [#692](https://github.com/seedcase-project/seedcase-sprout/pull/692)
  ([cf382c3](https://github.com/seedcase-project/seedcase-sprout/commit/cf382c33d6ca3538218ca29d64ae7a066e263198))
- Add `FieldProperties` and `ConstraintsProperties`
  [#717](https://github.com/seedcase-project/seedcase-sprout/pull/717)
  ([02f706c](https://github.com/seedcase-project/seedcase-sprout/commit/02f706c2b80d01e23583c68c4c94764d32ec5487))
- Add `create_default_package_properties()`
  [#731](https://github.com/seedcase-project/seedcase-sprout/pull/731)
  ([a1916c0](https://github.com/seedcase-project/seedcase-sprout/commit/a1916c019c47b3ed8f833062f4d6b02183cf5202))
- Add `read_json()`
  [#746](https://github.com/seedcase-project/seedcase-sprout/pull/746)
  ([83ccba7](https://github.com/seedcase-project/seedcase-sprout/commit/83ccba743ff327538f82310575cf99981085556e))
- Add computed property `asdict`
  [#745](https://github.com/seedcase-project/seedcase-sprout/pull/745)
  ([f4e762b](https://github.com/seedcase-project/seedcase-sprout/commit/f4e762b7d66758d6c9dfff44798957c2698f2adb))
- Add sensible default values for package properties
  [#743](https://github.com/seedcase-project/seedcase-sprout/pull/743)
  ([d7fb08a](https://github.com/seedcase-project/seedcase-sprout/commit/d7fb08abf6d54dbf213abec7c148907caa7d61a5))
- Add `path_*()` functions (with their `verify_*()`'ers)
  [#730](https://github.com/seedcase-project/seedcase-sprout/pull/730)
  ([71d8a4b](https://github.com/seedcase-project/seedcase-sprout/commit/71d8a4bf20dca7546a62aac9d4a219ebb09ea352))
- Add `create_readme_text()`
  [#669](https://github.com/seedcase-project/seedcase-sprout/pull/669)
  ([ca2a388](https://github.com/seedcase-project/seedcase-sprout/commit/ca2a388c8dcc0cd0f63e29c21db05b9049602305))
- Add `create_package_structure()`
  [#754](https://github.com/seedcase-project/seedcase-sprout/pull/754)
  ([bfc8dc8](https://github.com/seedcase-project/seedcase-sprout/commit/bfc8dc8d6d002141b5c88bb0f851a436987a055f))
- Add default values to `ResourceProperties`
  [#769](https://github.com/seedcase-project/seedcase-sprout/pull/769)
  ([a7787ce](https://github.com/seedcase-project/seedcase-sprout/commit/a7787ceb4b68eabbb3cb9203f07542d7368606ef))
- Add `verify_package_properties()`
  [#744](https://github.com/seedcase-project/seedcase-sprout/pull/744)
  ([b1f7d5b](https://github.com/seedcase-project/seedcase-sprout/commit/b1f7d5bfc0451d72e646964e5aab6816efee7c9f))
- Add that `path_packages()` creates dir if it doesn't exist
  [#783](https://github.com/seedcase-project/seedcase-sprout/pull/783)
  ([3ae0992](https://github.com/seedcase-project/seedcase-sprout/commit/3ae099238bfda8989a69ae0fab356bd390acc59c))
- Update `verify_resource_properties()`
  [#773](https://github.com/seedcase-project/seedcase-sprout/pull/773)
  ([50801c3](https://github.com/seedcase-project/seedcase-sprout/commit/50801c35a36e1f2a998405eb900952557d3f464e))
- Add `edit_package_properties()`
  [#790](https://github.com/seedcase-project/seedcase-sprout/pull/790)
  ([3007f1f](https://github.com/seedcase-project/seedcase-sprout/commit/3007f1ffc56352cc5f03feff4a6f27b21c2942b7))
- Add `write_resource_properties()`
  [#784](https://github.com/seedcase-project/seedcase-sprout/pull/784)
  ([f27d8f5](https://github.com/seedcase-project/seedcase-sprout/commit/f27d8f582932daf8aecdbfbe15ec80aefa19df4f))
- Update `Properties` classes with default method and change behaviour of
  `compact_dict`
  [#808](https://github.com/seedcase-project/seedcase-sprout/pull/808)
  ([8b306cd](https://github.com/seedcase-project/seedcase-sprout/commit/8b306cdb354c33ca338998d7ebc01d2239c109be))
- Add `create_raw_file_name()`
  [#841](https://github.com/seedcase-project/seedcase-sprout/pull/841)
  ([4162506](https://github.com/seedcase-project/seedcase-sprout/commit/41625063be058b541ba93034c1cf946dcc4810cf))

### 🐛 Fixes

- *(typo)* Packagee -> package
  ([9c5723d](https://github.com/seedcase-project/seedcase-sprout/commit/9c5723de1cf3a8af8475d2260bd2f9c3c2d2b42e))
- Apply suggestions from code review
  ([f87a5aa](https://github.com/seedcase-project/seedcase-sprout/commit/f87a5aa58d662f88ae2007e936c34a064074454f))
- Remove "design" from path to login sequence png
  ([9e92e91](https://github.com/seedcase-project/seedcase-sprout/commit/9e92e91e44eec65551653cf42c8b8dae320f73d4))
- Add blank line before list so it renders correctly
  ([bdb4cb4](https://github.com/seedcase-project/seedcase-sprout/commit/bdb4cb49676bfcd370579815142db18b509ad93d))
- Remove ordering from yaml
  ([db227ab](https://github.com/seedcase-project/seedcase-sprout/commit/db227aba217753789128e84df36aa75ff21757cc))
- Remove files that are created when rendering
  ([4fe8b68](https://github.com/seedcase-project/seedcase-sprout/commit/4fe8b685413ad7961a89f08bed71dfc9c748908d))
- Minor text mods
  ([d88075f](https://github.com/seedcase-project/seedcase-sprout/commit/d88075f9e5d5ef542f19b40800572980026ff050))
- Add line from "continue" back validation check
  ([24e941a](https://github.com/seedcase-project/seedcase-sprout/commit/24e941a33e70dd2144ecb4cce10141e66a93424f))
- Minor fixes to user flow diagrams based on review from @lwjohnst86
  ([ff9a47e](https://github.com/seedcase-project/seedcase-sprout/commit/ff9a47e76459ddd49e69dc9e973931e406c49e43))
- Remove numbering from output file name
  ([c39e2c8](https://github.com/seedcase-project/seedcase-sprout/commit/c39e2c8243d73e0613ebb1c61481ac58b8945787))
- Remove "tricky part" png
  ([94c9abe](https://github.com/seedcase-project/seedcase-sprout/commit/94c9abe15013013bd10ae34acaaba45f3a573aa3))
- Delete outdated schema creation flow diagram
  ([0be5c77](https://github.com/seedcase-project/seedcase-sprout/commit/0be5c77cadf20ed4465a44cc5e53f463963094e1))
- Remove mention of "V2"
  ([56f70a0](https://github.com/seedcase-project/seedcase-sprout/commit/56f70a00a2fa34f0edc72ce6b77821a40471d210))
- Apply suggestions from code review
  ([106889a](https://github.com/seedcase-project/seedcase-sprout/commit/106889a47916e32beca6f50fd58e135cd0c21ddc))
- Replace "schema(s)" with "table(s)" in all files related to user flow
  ([4925440](https://github.com/seedcase-project/seedcase-sprout/commit/49254408aed656c2a9d4801cd13ef05b7b2869f9))
- Rerun pumls to change "schema(s)" to "table(s)"
  ([d9a2fe2](https://github.com/seedcase-project/seedcase-sprout/commit/d9a2fe25b45958686af77cd4e11261f247200593))
- Apply suggestions from code review
  ([31fd867](https://github.com/seedcase-project/seedcase-sprout/commit/31fd867592f78ab099458f34556d8514e6d4b566))
- Deploy to fly.io is fixed
  ([105152a](https://github.com/seedcase-project/seedcase-sprout/commit/105152a71c22aec5d986ae510ee85544b04040f2))
- Fixed poetry version
  ([2dbb6f4](https://github.com/seedcase-project/seedcase-sprout/commit/2dbb6f4b103d80dfac3d6cf0a7f6f58caef3f402))
- Reverting changes related to enforcing foreign key constraint in SQLite. This
  seems to be handled by Django
  ([610ae73](https://github.com/seedcase-project/seedcase-sprout/commit/610ae7388ea3ef1cb4e87f1e124180cc619f4075))
- Adding tests
  ([5559b3d](https://github.com/seedcase-project/seedcase-sprout/commit/5559b3db671464f524a6e8372b7a201520c953a1))
- Missing a just command
  ([8ce64f8](https://github.com/seedcase-project/seedcase-sprout/commit/8ce64f818a91900ae0e8df88d59601cf7afa3764))
- Indentation was wrong...
  ([3d956b8](https://github.com/seedcase-project/seedcase-sprout/commit/3d956b87c5a169e648819ead7a9147943818a76d))
- Change comment style from # to //
  ([9621049](https://github.com/seedcase-project/seedcase-sprout/commit/9621049d7453dd1678658a20147f60d01ab2b7e9))
- Semi colon -> comma
  ([a71b9fd](https://github.com/seedcase-project/seedcase-sprout/commit/a71b9fd630236a8ad8c4f83f0bf059f0d592e47c))
- Another fix to the test workflow
  ([7df506b](https://github.com/seedcase-project/seedcase-sprout/commit/7df506b06f8c828716354abf316f9513783c8fe6))
- -no-interaction --no-root
  ([ace8137](https://github.com/seedcase-project/seedcase-sprout/commit/ace8137a6b5607064d987f8746183542da5bd989))
- Apply suggestions from code review
  ([b26d987](https://github.com/seedcase-project/seedcase-sprout/commit/b26d987c642b3b822b1cdd3ad0afbee2e8cb21c6))
- Adjustments from review comments
  ([86077c7](https://github.com/seedcase-project/seedcase-sprout/commit/86077c79ad8d2caf5b781d45d14f28103a77676a))
- Seems like this code wasn't used, so removed it
  ([594e78e](https://github.com/seedcase-project/seedcase-sprout/commit/594e78e897ad75f5d569f9f9dbd89aff89d4494d))
- Move whitenoise up under securitymiddleware
  ([8c55215](https://github.com/seedcase-project/seedcase-sprout/commit/8c552157f21be184172fe5420ac64442e09d2e71))
- Small typo fix.
  ([3bdb95e](https://github.com/seedcase-project/seedcase-sprout/commit/3bdb95eb0236418ca2418580d7ad3cc8132618ba))
- Add migrations before loading sample
  ([6545af7](https://github.com/seedcase-project/seedcase-sprout/commit/6545af7aeb6289ed173f14fdac4865bde7e74036))
- Update-migrations creates and applies migrations
  ([532582a](https://github.com/seedcase-project/seedcase-sprout/commit/532582aaed8d70e4e6afb4041669f31b5e22ddd1))
- Using FLY_APP variable
  ([1fdc1c2](https://github.com/seedcase-project/seedcase-sprout/commit/1fdc1c2a8c5b6332827337d0b303fcd228f371a6))
- Hardcode seedcase-sprout-pr test
  ([649d74f](https://github.com/seedcase-project/seedcase-sprout/commit/649d74f9108701bd244b338e9783e5bf46507044))
- Only seedcase-sprout
  ([093ee8a](https://github.com/seedcase-project/seedcase-sprout/commit/093ee8a6c1dc0cd82ceae6bcfd6ea9d60f5c99d0))
- Rename to seedcase-sprout-preview which is more clear
  ([3f71509](https://github.com/seedcase-project/seedcase-sprout/commit/3f7150969f30f65cd0c089062e3c9bf78a5aae17))
- Ruff formatting added
  ([af4b03c](https://github.com/seedcase-project/seedcase-sprout/commit/af4b03ce7de777b3ac05059306c03ef6398e665d))
- Adjustments reviewed
  ([6a8ed20](https://github.com/seedcase-project/seedcase-sprout/commit/6a8ed2052b442f04622d8be9ffee948f6d44914f))
- Docstrings and type hints
  ([0371562](https://github.com/seedcase-project/seedcase-sprout/commit/0371562c2e170563e8219b94b8c098b1b77c9593))
- Apply suggestions from code review
  ([b24d65f](https://github.com/seedcase-project/seedcase-sprout/commit/b24d65fc245b348ee2140f0fcec575032a93e2ec))
- Apply suggestions from code review
  ([89f8573](https://github.com/seedcase-project/seedcase-sprout/commit/89f8573bcd8f865c7bf2f56ab986c13f46c1b140))
- Port 10000 -> 8000
  ([a0d3b8c](https://github.com/seedcase-project/seedcase-sprout/commit/a0d3b8c5c15218e19153835ce7c57d370afdbd46))
- Remove default=None from created_by
  ([ca00c1d](https://github.com/seedcase-project/seedcase-sprout/commit/ca00c1d1344d4af1772bc6372260303f750f90c4))
- Remove description text field - we use the form field now
  ([c71e0b4](https://github.com/seedcase-project/seedcase-sprout/commit/c71e0b4b7ef15ef5ba4848f968ac1ba871e90dfc))
- Remove data-ui from create button to avoid closing dialog when validation
  fails
  ([fcf0837](https://github.com/seedcase-project/seedcase-sprout/commit/fcf0837181e127f552ab45598951c8dd97c1efd6))
- Add button to cancel class
  ([9ce9e22](https://github.com/seedcase-project/seedcase-sprout/commit/9ce9e22e9302fe7be2bacf50bfe2285ad8b9c563))
- If errors in form, show dialog
  ([322cd31](https://github.com/seedcase-project/seedcase-sprout/commit/322cd31b0b88844f85a111f72e43cb4c3b452783))
- Trying to fix csrf
  ([90739f3](https://github.com/seedcase-project/seedcase-sprout/commit/90739f30656aa4cdd22da1fd8875e596f17ff5ef))
- Trying to fix csrf adding comment
  ([acea4c4](https://github.com/seedcase-project/seedcase-sprout/commit/acea4c4cf14619380e3fc2149d807faf56708506))
- Trying to fix csrf adding comment
  ([2a7052d](https://github.com/seedcase-project/seedcase-sprout/commit/2a7052de924db7206c050cf46f14f76900c50456))
- Missing file
  ([fe006b6](https://github.com/seedcase-project/seedcase-sprout/commit/fe006b692222d129bcb3b4d97ff5d2b44ecaf459))
- Trying CSRF_TRUSTED_ORIGINS
  ([fc1a8e8](https://github.com/seedcase-project/seedcase-sprout/commit/fc1a8e8cc0d1429b13a41e6be62cf0f089c02a6f))
- A function was forgotten to be renamed after it was changed.
  ([cd70708](https://github.com/seedcase-project/seedcase-sprout/commit/cd707087f6c69ebd0ad2377a9665f8c538b03ad2))
- The columns are updated after a migration
  ([0ecfb36](https://github.com/seedcase-project/seedcase-sprout/commit/0ecfb3659193503da41ffac442747670bdc60b07))
- Remove python_type and pandas_type
  ([668704e](https://github.com/seedcase-project/seedcase-sprout/commit/668704e94c7c1ce09fdeda936a7511b61d287468))
- Ruff adjustments
  ([16cd5f3](https://github.com/seedcase-project/seedcase-sprout/commit/16cd5f3fb9acad6fc882abcd1db1534d34924b17))
- Remove validtionerror from return typehint
  ([b185dd4](https://github.com/seedcase-project/seedcase-sprout/commit/b185dd48c204d42950fc142994e8bda69e9276a2))
- Remove validationerror from return typehint
  ([fc33b95](https://github.com/seedcase-project/seedcase-sprout/commit/fc33b95a69846be931d8a2d554a9a070f63cced0))
- Add bottom margin for name field when validation fails
  ([9ba4ef8](https://github.com/seedcase-project/seedcase-sprout/commit/9ba4ef8c64b0d5d404fc3cfd49ed4672f3ef6221))
- Apply suggestions from code review
  ([4947dfb](https://github.com/seedcase-project/seedcase-sprout/commit/4947dfbd71c2087fbe873f51c9162d068d5cd736))
- Resolve merge conflict
  ([550a47b](https://github.com/seedcase-project/seedcase-sprout/commit/550a47be1c1f782fa129cae52c235cd4194e44fd))
- Handle static assets when DEBUG=False
  ([35d5124](https://github.com/seedcase-project/seedcase-sprout/commit/35d5124f4351c3fdb48f7c8d528a05bf11de9bf0))
- Multiline comment
  ([7f2be6f](https://github.com/seedcase-project/seedcase-sprout/commit/7f2be6fffb6339c70c260b5862788f69561082fc))
- Apply suggestions from code review [skip ci]
  ([da8da21](https://github.com/seedcase-project/seedcase-sprout/commit/da8da215206586ec9ae0b9ae75ea1d0a05bf6a00))
- Centre align icon on it's own line
  ([80f72dd](https://github.com/seedcase-project/seedcase-sprout/commit/80f72dd8e65da3639106f0aaf51abe55c37104af))
- Update initial migration to include original_name in columnmetadata
  ([5a360ef](https://github.com/seedcase-project/seedcase-sprout/commit/5a360ef0459838c3d3273b7a88595078260c4d05))
- Ruff adjustments
  ([4a5a51d](https://github.com/seedcase-project/seedcase-sprout/commit/4a5a51d23965f9f6ad5fc10f57ba228d2421b02d))
- Ruff adjustments
  ([0dcc2b8](https://github.com/seedcase-project/seedcase-sprout/commit/0dcc2b8ad23be99621e3a71aa93cfba6a08ef463))
- Docstring adjustments
  ([937640c](https://github.com/seedcase-project/seedcase-sprout/commit/937640c0e9500fff80f74ff4a9f90338e6599162))
- Using selectors instead
  ([f6c4a62](https://github.com/seedcase-project/seedcase-sprout/commit/f6c4a6262a6ceb8ff53404fdcf67a645038dcc5d))
- Fixing if BytesIO instead of TextIO
  ([13a12f6](https://github.com/seedcase-project/seedcase-sprout/commit/13a12f66b3265642e3f2e8cd9fba79fad0bdc2b1))
- Reverting deploy-pr-preview.yml
  ([5a7505a](https://github.com/seedcase-project/seedcase-sprout/commit/5a7505acf7a3823e20ac71c0d12f8350819030b1))
- Why is preview deployment not triggered
  ([287bf08](https://github.com/seedcase-project/seedcase-sprout/commit/287bf086d6f605aa977e4da802eadf13e71b82e2))
- Ruff import order
  ([0b393a2](https://github.com/seedcase-project/seedcase-sprout/commit/0b393a29fb57508cbfd2099bcb8a304beb310aa8))
- Staticfiles needs to be present
  ([d714cc4](https://github.com/seedcase-project/seedcase-sprout/commit/d714cc447809bbb4ff7f2b6555bafc148045c1f2))
- Removed bad code
  ([ae708f6](https://github.com/seedcase-project/seedcase-sprout/commit/ae708f65316da572e306a8ff60946d5941736a99))
- Create dir if missing
  ([bd4a636](https://github.com/seedcase-project/seedcase-sprout/commit/bd4a6369ea0915c08f68c1b68920aaac67dcf15a))
- Extra / is removed in path
  ([817a492](https://github.com/seedcase-project/seedcase-sprout/commit/817a492e75e0de1fbde4b1217999ae2653176226))
- Ruff, unused import
  ([80f0814](https://github.com/seedcase-project/seedcase-sprout/commit/80f081433b5569065e9867f6ba9b9a842495d36b))
- After rename
  ([3a641b1](https://github.com/seedcase-project/seedcase-sprout/commit/3a641b1f717ed683e61e381682d66438d67e3eda))
- After rename
  ([ba70aba](https://github.com/seedcase-project/seedcase-sprout/commit/ba70abac53cf2cfc714208f1d0ecfa90956135ef))
- Status code changed
  ([6c7894e](https://github.com/seedcase-project/seedcase-sprout/commit/6c7894e708120101119ed0af7904f98ad81d0dd0))
- Add Ruff exemptions for a couple of D102 to see if that makes a difference for
  linting
  ([5453880](https://github.com/seedcase-project/seedcase-sprout/commit/5453880973af8229cc87f869d0b4bd1c85312e35))
- Update to docstrings and format of imports
  ([6c4e620](https://github.com/seedcase-project/seedcase-sprout/commit/6c4e6207ba0e2aad92f01463e7717c102aab1d8c))
- Add ruff exemptions to the last bits
  ([01a30b3](https://github.com/seedcase-project/seedcase-sprout/commit/01a30b3fda91fdba635226795a3eca59bde24acb))
- Remove data type from PR
  ([648fb9a](https://github.com/seedcase-project/seedcase-sprout/commit/648fb9af352b277918af0b056914986b2fc9f030))
- Sort out lint
  ([7f641fc](https://github.com/seedcase-project/seedcase-sprout/commit/7f641fcdeeb7da43b7499833ba5e3ae3ae671e59))
- Missed the init file first time
  ([9c7fbbe](https://github.com/seedcase-project/seedcase-sprout/commit/9c7fbbe84b9f376d1f0f1f4643d36373891f1503))
- Migration
  ([6b73e18](https://github.com/seedcase-project/seedcase-sprout/commit/6b73e18ac597c966ab129f68327b69b73abd9afd))
- Migrations are added in docker image and collectstatic is executed when the
  image is created (and not during startup)
  ([7747a82](https://github.com/seedcase-project/seedcase-sprout/commit/7747a82f976f0c60aa04c68b243693512b406bbf))
- Update href to match name of view-existing-tables
  ([8b8683b](https://github.com/seedcase-project/seedcase-sprout/commit/8b8683b39251ed1644843fc44215ebecd08f039f))
- Updated form test to use new field
  ([093a0e6](https://github.com/seedcase-project/seedcase-sprout/commit/093a0e638961dfc943cc2535e7e3aca6924c7438))
- Corrected a typo in the tests
  ([b2b1f85](https://github.com/seedcase-project/seedcase-sprout/commit/b2b1f8579a3b52377bf2d5e423263f5274e31d4f))
- Form validation error
  ([a35d865](https://github.com/seedcase-project/seedcase-sprout/commit/a35d865fdfc235c42d515f2d36307f4495d136cc))
- Change label from "name" to "table name"
  ([e7b8ae7](https://github.com/seedcase-project/seedcase-sprout/commit/e7b8ae75774e93348d6955b9c47cc6bd437d2933))
- Disable suggestions for table name
  ([3f02f49](https://github.com/seedcase-project/seedcase-sprout/commit/3f02f4915e4ee81049f2ceedc1e8f2d1e51436f3))
- Ruff format
  ([5c84dda](https://github.com/seedcase-project/seedcase-sprout/commit/5c84dda38461df4846d7a87b3681cfe81499a379))
- Naming and docstrings
  ([1c2b5e0](https://github.com/seedcase-project/seedcase-sprout/commit/1c2b5e05dd1155165a351432bc0a1f198983336d))
- Naming and docstrings
  ([0b15d1d](https://github.com/seedcase-project/seedcase-sprout/commit/0b15d1defa6046e5f316b2d9fde79b4c6980ac82))
- Merge-conflict
  ([17b4331](https://github.com/seedcase-project/seedcase-sprout/commit/17b4331a32a6f5bdae1dc719df1fde089cd95613))
- Ruff format
  ([12a598d](https://github.com/seedcase-project/seedcase-sprout/commit/12a598d8bcc000685948da31e886b873887550f8))
- Spelling mistake
  ([88e3ccd](https://github.com/seedcase-project/seedcase-sprout/commit/88e3ccd60fe4a7e2aa5a16a319e231a49685e8d0))
- Renamed test file for ColumnDataType
  ([2fd80dc](https://github.com/seedcase-project/seedcase-sprout/commit/2fd80dc43aeb096ea536eb593b6cbc4e4a4a6944))
- The folder staticfiles is automatically created to avoid the warning that the
  folder is missing
  ([c58982e](https://github.com/seedcase-project/seedcase-sprout/commit/c58982eaee37f498692ba28860a7a46b8233f763))
- Ruff adjustments
  ([a90dee6](https://github.com/seedcase-project/seedcase-sprout/commit/a90dee61824390fcc2c5be8fee223719c88601e1))
- Migration removed
  ([bb08abe](https://github.com/seedcase-project/seedcase-sprout/commit/bb08abecb64e4e2f405e8b86a716cc7cbc2bbd6b))
- Merge-conflict
  ([ed1dfd7](https://github.com/seedcase-project/seedcase-sprout/commit/ed1dfd7691ac0eb70d460ec6632098373e56aee6))
- Merge-conflict
  ([6f7f5cb](https://github.com/seedcase-project/seedcase-sprout/commit/6f7f5cb0abc703603c965bd0351172fafcc0fa60))
- Merge-conflict
  ([ac7a920](https://github.com/seedcase-project/seedcase-sprout/commit/ac7a920e206709a56eeb75d2fcabaf58b9991d5f))
- Based on review comments
  ([63db34f](https://github.com/seedcase-project/seedcase-sprout/commit/63db34fa140a33a8b4c71045b7e124ee298d197e))
- Fix missing ) in url.py
  ([6127921](https://github.com/seedcase-project/seedcase-sprout/commit/61279212253e64dc30449b1af7b6fb1c058749d1))
- Remove autocomplete
  ([3bd4d1c](https://github.com/seedcase-project/seedcase-sprout/commit/3bd4d1c13658071ea70fa145f000cbbb54238d8f))
- Removed space
  ([bee80eb](https://github.com/seedcase-project/seedcase-sprout/commit/bee80eb4fa9da6d245e4213d6de0c23fcb5d7bc9))
- Missing docstring
  ([e6982c8](https://github.com/seedcase-project/seedcase-sprout/commit/e6982c8104e7f331f1c6564d594bf03938ce45a8))
- Tests are moved to tests_csv_reader
  ([4cb03cb](https://github.com/seedcase-project/seedcase-sprout/commit/4cb03cb3d046405a0093d109694b83a87b0abf73))
- Save method is overridden and a test is added
  ([079162d](https://github.com/seedcase-project/seedcase-sprout/commit/079162dd4c83a0035844f3131707a8758c6b39a6))
- Ruff format
  ([f118e8a](https://github.com/seedcase-project/seedcase-sprout/commit/f118e8a9dd4b8e6bc82bd5a9b2aa9288d98eab17))
- Forgot to remove this import
  ([0e2798f](https://github.com/seedcase-project/seedcase-sprout/commit/0e2798f6db32579fcf57d138d36eb3b258aff5e3))
- Remove option for NULL in drop-down data-type
  ([e39940f](https://github.com/seedcase-project/seedcase-sprout/commit/e39940ff003d8d3b3b2317e5445d01bae0f916bd))
- Running tests told me datetime.UTC doesn't exist. Not sure why, so changed it
  to timezone.utc
  ([a5b3a21](https://github.com/seedcase-project/seedcase-sprout/commit/a5b3a21b7b2845ee66bda97c191bc67a76fb0cc9))
- Remove unused import: ColumnMetadata
  ([5346fff](https://github.com/seedcase-project/seedcase-sprout/commit/5346fff05c7b0aeba72349b493659a6f9ab849ad))
- Remove import of non-existing file-upload view
  ([1fb0331](https://github.com/seedcase-project/seedcase-sprout/commit/1fb03317be1d80eb123769658d5a96936d557604))
- Remove style ".expandable"
  ([b0ccf77](https://github.com/seedcase-project/seedcase-sprout/commit/b0ccf772ef70f18eafb83d0f7fa7640b3b441d68))
- Change table to div to enable the whole row being clickable/selectable
  ([48129c8](https://github.com/seedcase-project/seedcase-sprout/commit/48129c8ebc72cde939cee21bec87da9a95503d51))
- Change empty message to not include "sorry"
  ([3aad831](https://github.com/seedcase-project/seedcase-sprout/commit/3aad831a613398037ac6d0ee17c0155ee069f5fd))
- Remove unused import
  ([654529f](https://github.com/seedcase-project/seedcase-sprout/commit/654529f1aa0edaddbfa28d5bc5f4e3d8bedb81bb))
- Remove typo
  ([b2e99a7](https://github.com/seedcase-project/seedcase-sprout/commit/b2e99a74712305a2efc4fb19df033259a0e827d6))
- Merge-conflict solved
  ([a6d9650](https://github.com/seedcase-project/seedcase-sprout/commit/a6d965061dfb652a599782775c68818e458a9b18))
- Empty description field and home-made tabindex templatetag is removed
  ([2a9f5ef](https://github.com/seedcase-project/seedcase-sprout/commit/2a9f5ef0085a71344bf1e72ceaf32832997250a7))
- Add that selected_metadata_id should be equal to metadata.id to change url
  ([7390ed4](https://github.com/seedcase-project/seedcase-sprout/commit/7390ed42a83b4cf8750c057d6dab05f39eacf044))
- Add missing </a>
  ([186d1e0](https://github.com/seedcase-project/seedcase-sprout/commit/186d1e09480d06e718d4c1077593124ebe56f523))
- Remove old urls from merge with main
  ([82fc870](https://github.com/seedcase-project/seedcase-sprout/commit/82fc87032631b36f29d13c70e05959a290e140e9))
- Remove import of old view from merge with main
  ([e9253f7](https://github.com/seedcase-project/seedcase-sprout/commit/e9253f7cbc37964580583e54baac3a4cbb068756))
- Remove unused argument "table_id" from view
  ([33c3832](https://github.com/seedcase-project/seedcase-sprout/commit/33c38321a2ab642789ee5bfc9f487cf9e07ec1aa))
- Change referenced urls to kebab-case
  ([052b0ab](https://github.com/seedcase-project/seedcase-sprout/commit/052b0ab5045dabbca4d6beb8c724bcc52225fe10))
- Add that no spaces are allowed in error message
  ([493736f](https://github.com/seedcase-project/seedcase-sprout/commit/493736fc6056fb1ceae949727f0e2f37a0950dd5))
- Update data-import view in test to be minus instead of underscore
  ([512c222](https://github.com/seedcase-project/seedcase-sprout/commit/512c22276c5ec667e45e039ff9bd855dcb405670))
- Remove old template view_existing_tables
  ([70fc7b6](https://github.com/seedcase-project/seedcase-sprout/commit/70fc7b6b128270c90c45c389b3e07604925275eb))
- Ruff line too long error
  ([74dee05](https://github.com/seedcase-project/seedcase-sprout/commit/74dee05e510920d23f42e99a619bcd3c381e5bbd))
- Merge conflict
  ([dbf2209](https://github.com/seedcase-project/seedcase-sprout/commit/dbf22097f3c039266abb3a2975c0767b2788a478))
- Remove error msg from tests since it has been removed from view
  ([7a82c16](https://github.com/seedcase-project/seedcase-sprout/commit/7a82c16f0ae9996cea8c68493095dd6f5fb6d4db))
- Update tests to include new column names
  ([7ca7c94](https://github.com/seedcase-project/seedcase-sprout/commit/7ca7c94f5ce15471d461513346ee4be7fb34dcde))
- Resubmitting a file should delete previous file and columns
  ([6be6604](https://github.com/seedcase-project/seedcase-sprout/commit/6be6604a09a5f5d2927c7f1dbb6f8f6916769c46))
- Add a test
  ([22ec3ad](https://github.com/seedcase-project/seedcase-sprout/commit/22ec3ad4150c69b2932a407bfe47b4fad9328115))
- Name was renamed to extracted_name
  ([884b089](https://github.com/seedcase-project/seedcase-sprout/commit/884b089a33e6f488eb8c4c811e913856d3b27801))
- Thead background colour and remove bottom border
  ([c449fd2](https://github.com/seedcase-project/seedcase-sprout/commit/c449fd24e583da4c1c189171e8b37767411a57bb))
- Table -> metadata
  ([bad0b5d](https://github.com/seedcase-project/seedcase-sprout/commit/bad0b5de16a0d46ffacda2089c7525109c9bffb9))
- **init**.py is required in migrations folder otherwise the command
  makemigrations is not working
  ([d1936c4](https://github.com/seedcase-project/seedcase-sprout/commit/d1936c4ee64c46541568b851829616c588915a75))
- Add column metadata to view
  ([2b695af](https://github.com/seedcase-project/seedcase-sprout/commit/2b695afaa61c1be0c9c4233d89e1fbd0b25cb355))
- Remove wrongly merged variable
  ([de87be7](https://github.com/seedcase-project/seedcase-sprout/commit/de87be7d566b691c7e279c00484571f40fdc29d3))
- Variable rename fail is fixed
  ([f914a0f](https://github.com/seedcase-project/seedcase-sprout/commit/f914a0fad3fc391d5ded05bf17ab8b32c6c741ad))
- DataType and Excluded flag should also work when switching views
  ([0405c93](https://github.com/seedcase-project/seedcase-sprout/commit/0405c9381bfb225d8654da66840a807b6c1faa9f))
- Remove duplicate import
  ([c7c1c4a](https://github.com/seedcase-project/seedcase-sprout/commit/c7c1c4a09c6ba8cd0dad90f0fe589f04b1b404e9))
- Use hidden attribute instead of hide class
  ([b3a9d8a](https://github.com/seedcase-project/seedcase-sprout/commit/b3a9d8a3549e211becc774d1344a1de601611f3d))
- Machine readable name is also removed from table overview
  ([97b29f9](https://github.com/seedcase-project/seedcase-sprout/commit/97b29f9bbd705571ece3afebfc3565b6d8863e6f))
- Adjustments
  ([f6e9729](https://github.com/seedcase-project/seedcase-sprout/commit/f6e97299d2d7dfc8ef807553fa3fdaacc2e4365b))
- Redirect to data-import page after update
  ([1eafd64](https://github.com/seedcase-project/seedcase-sprout/commit/1eafd6487d2781afe542d2641e1a6214bed9c67a))
- Typos in the code introduced during the renaming
  ([82973ff](https://github.com/seedcase-project/seedcase-sprout/commit/82973ff89c9fd5dadb502bb73d460c51102e8fe1))
- Forgot to correct the `base.html` path after the change
  ([af5bb78](https://github.com/seedcase-project/seedcase-sprout/commit/af5bb784831232e90a909fa7826a96d9efc3bc9d))
- Fixing tests with small changes
  ([5e50f6e](https://github.com/seedcase-project/seedcase-sprout/commit/5e50f6e4f34af2090884de00f4cc87f85a7da8d2))
- Remove incorrect bracket
  ([cfdba78](https://github.com/seedcase-project/seedcase-sprout/commit/cfdba783e59596bd047437be007473c79ef86fd2))
- Typo, should be uppercase as a constant
  ([8591770](https://github.com/seedcase-project/seedcase-sprout/commit/859177098ea32652ec26329b4aeadbfca3f1ddca))
- Fix forgotten naming schemes for Models
  ([669611a](https://github.com/seedcase-project/seedcase-sprout/commit/669611a2edbe214ae5ea5d59324051db83a04842))
- Update upload URL in metadata view to direct to data update
  ([b5b8dd2](https://github.com/seedcase-project/seedcase-sprout/commit/b5b8dd21aabb2183c66308470623a4196648def4))
- Data-import and url
  ([c8990bb](https://github.com/seedcase-project/seedcase-sprout/commit/c8990bb3ba73b33a83518289953adc997d3068c9))
- Add missing docstrings to write() and path_raw_storage()
  ([62b1018](https://github.com/seedcase-project/seedcase-sprout/commit/62b101855f2669ee5787e5165fe8f988332f118d))
- Fix model names after renaming for naming scheme
  ([91a93ab](https://github.com/seedcase-project/seedcase-sprout/commit/91a93ab22e68fef5fc5bae84d24af429968dae80))
- This was changed to just `tables`
  ([935546a](https://github.com/seedcase-project/seedcase-sprout/commit/935546a75061d760b740c9b68df7f198354c8254))
- Wrong function name used.
  ([6e2c640](https://github.com/seedcase-project/seedcase-sprout/commit/6e2c64057edbf1b0999f23c43b6e3287bfcda161))
- Replace mentions of tables with metadata
  ([1cefb6b](https://github.com/seedcase-project/seedcase-sprout/commit/1cefb6b8d68645bc5a9bfdda967adf14795faa37))
- Change normal strings to raw strings for regex patterns
  ([61dfc1f](https://github.com/seedcase-project/seedcase-sprout/commit/61dfc1f5f7c6fac049f0d59a692f615281459bcf))
- Only include semibold and bold Rajdhani fonts
  ([0175f0b](https://github.com/seedcase-project/seedcase-sprout/commit/0175f0b83727bcf49479aeb495079bf234dea0a1))
- Data -> metadata
  ([e61ef94](https://github.com/seedcase-project/seedcase-sprout/commit/e61ef94ac117485c0b9dcc6a0182c33b7f4c1d2d))
- Change var name tables to table since it only contains one table
  ([f55b068](https://github.com/seedcase-project/seedcase-sprout/commit/f55b06848e8253a01685be7807b36718920dd355))
- Remove custom save method so modified_at is `None` before data upload
  ([6ea6650](https://github.com/seedcase-project/seedcase-sprout/commit/6ea6650a533c737ba646273973465d5e446304f2))
- Remove update to modified_at since it's not the metadata being updated here
  ([251e55d](https://github.com/seedcase-project/seedcase-sprout/commit/251e55dcb887d888f13bfceaba6923314948b411))
- Remove unused import of datetime
  ([b3bf0b4](https://github.com/seedcase-project/seedcase-sprout/commit/b3bf0b440372db9779de812f49134489de4ffd48))
- Add "rows" to successful upload message
  ([61a28c0](https://github.com/seedcase-project/seedcase-sprout/commit/61a28c0753e5fec981d4a13432e537c859ee24da))
- Apply suggestions from code review
  ([76be8aa](https://github.com/seedcase-project/seedcase-sprout/commit/76be8aaf1baf0c1a03ed298a7fd3a5cfd80cc328))
- Fix conflict
  ([5302c69](https://github.com/seedcase-project/seedcase-sprout/commit/5302c69f2dfe5b2471346c06772121da977d3d03))
- Fixing tests
  ([d81fe0f](https://github.com/seedcase-project/seedcase-sprout/commit/d81fe0f80244984d8776fc0beeacaab63e7e1892))
- Specify that only direct children of table-content should be grey
  ([bbd542a](https://github.com/seedcase-project/seedcase-sprout/commit/bbd542a1dd24547f587d687c98666b92f0fb8dec))
- Update and add more colours to fit ui wireframes
  ([5fdee1b](https://github.com/seedcase-project/seedcase-sprout/commit/5fdee1b74ca854e768e97739c32d55e6c16bd065))
- Update styles to use theme variables
  ([2d30e3d](https://github.com/seedcase-project/seedcase-sprout/commit/2d30e3ddbda2668607e6e1dc68093a94efaa8101))
- Modify css for .metadata_columns_table to be applied to correct elements
  ([edac3ae](https://github.com/seedcase-project/seedcase-sprout/commit/edac3ae01b9c7a85afe4c2b47a44023fb635e868))
- Remove unused/unseen style
  ([202704f](https://github.com/seedcase-project/seedcase-sprout/commit/202704f07f876b5b94c27f64a49482f41cf42d78))
- Remove beercss' default table borders
  ([7040994](https://github.com/seedcase-project/seedcase-sprout/commit/704099426ad304f84c08e050af2b9cb4de02fbc8))
- Don't include border-radius for any elements in metadata_columns_table
  elements
  ([2cf1148](https://github.com/seedcase-project/seedcase-sprout/commit/2cf1148e560304e9a4722343c7d327bcfcc419c1))
- To avoid having multiple tbodies, move <tbody> out of loop
  ([1360b42](https://github.com/seedcase-project/seedcase-sprout/commit/1360b4258072bf96ddd159f03a61737f25928176))
- For readability, add <tr> tag around column metadata tables
  ([e2be170](https://github.com/seedcase-project/seedcase-sprout/commit/e2be170b0d8c077b7cfa0dbfc4353ee62b4e1b75))
- Remove end of if-statement
  ([e0b1bfd](https://github.com/seedcase-project/seedcase-sprout/commit/e0b1bfd084a7677f5dbfd1b046b00b79a806b53b))
- Remove repeated dialog
  ([2d31ddd](https://github.com/seedcase-project/seedcase-sprout/commit/2d31ddd66b5e54c84694a2867a01778685cb8813))
- Remove border radius from navbar
  ([ba5e412](https://github.com/seedcase-project/seedcase-sprout/commit/ba5e412d20d1d21e9e4802d364995370b7f059cd))
- Specify styling to target <img> elements within a <nav> element
  ([d3e8c54](https://github.com/seedcase-project/seedcase-sprout/commit/d3e8c54cfb99bf6b5eaed94f95598babb19e16dc))
- Add background-size: cover to avoid "zoom in" on image
  ([45117f7](https://github.com/seedcase-project/seedcase-sprout/commit/45117f7673775619de8508a20d4de0aa8e7afaa7))
- Add quotes around class name
  ([45d2cc2](https://github.com/seedcase-project/seedcase-sprout/commit/45d2cc2a9340f440b9697b8dc41fcab5fdc504e8))
- Add card.css to base.html
  ([177fdcc](https://github.com/seedcase-project/seedcase-sprout/commit/177fdcc34280d591bb2815c9f4631708562489aa))
- Add missing s to url name
  ([8b0a4bc](https://github.com/seedcase-project/seedcase-sprout/commit/8b0a4bc1ce776aa85cb9f734417d3d0b535b61ea))
- Add missing s to url name
  [#410](https://github.com/seedcase-project/seedcase-sprout/pull/410)
  ([94a441b](https://github.com/seedcase-project/seedcase-sprout/commit/94a441bae3832841ba963bd4d78acb407d4db2f1))
- "gender" -> "sex"
  ([e78d73c](https://github.com/seedcase-project/seedcase-sprout/commit/e78d73cd0a008da69228a6617b762502b69d4b01))
- "gender" -> "sex"
  ([56d12a8](https://github.com/seedcase-project/seedcase-sprout/commit/56d12a8e9ff595fb1536bf63e0028626e55286be))
- Merge conflict
  ([7c40d9b](https://github.com/seedcase-project/seedcase-sprout/commit/7c40d9bc3725a18ed9b4bb3c22a79218f0a4cb57))
- Use columns_set
  ([6b7bc7e](https://github.com/seedcase-project/seedcase-sprout/commit/6b7bc7eac87eb56184ea1b7a6bb7fac057b08240))
- Expand icon and show more button is fixed
  ([57881aa](https://github.com/seedcase-project/seedcase-sprout/commit/57881aa42d1f26134d7ef420ce50244608ba799e))
- Comments added
  ([0c65456](https://github.com/seedcase-project/seedcase-sprout/commit/0c6545628b83c1d9a5e43062e7fe61a04358539e))
- Solve merge conflict
  ([e31c453](https://github.com/seedcase-project/seedcase-sprout/commit/e31c45348495e123cb3c53ee58f094dfd3eddeab))
- Make --surface-container-high white so it's not purple
  ([a5095d9](https://github.com/seedcase-project/seedcase-sprout/commit/a5095d9bff2200610d07f1e7ee836d5b3355386f))
- Make --surface-container-high white so it's not purple
  [#416](https://github.com/seedcase-project/seedcase-sprout/pull/416)
  ([1933469](https://github.com/seedcase-project/seedcase-sprout/commit/19334699b9cc4761abac19f9434dc33633fd109f))
- Update C4 container diagram
  ([69123dd](https://github.com/seedcase-project/seedcase-sprout/commit/69123ddda45da1b61c5ed861dc7d1eae012f3916))
- Update UI component diagram to be only about Sprout
  ([ce91d03](https://github.com/seedcase-project/seedcase-sprout/commit/ce91d03b1de6777dc3208373903a2ec0e5c53a31))
- Update C4 Context diagram to include only Sprout.
  ([87674f6](https://github.com/seedcase-project/seedcase-sprout/commit/87674f65abbe8f103a9cd8fe5d29d6f4b6a666b4))
- .venv is added to .dockerignore as it seems to break the docker build
  ([5315cc7](https://github.com/seedcase-project/seedcase-sprout/commit/5315cc791fe305f3917078a0005de05771e44275))
- A bit of styling is added
  ([15cbfac](https://github.com/seedcase-project/seedcase-sprout/commit/15cbfacd949394e493145bd30055514a3d991523))
- A bit of clean up
  ([78b5445](https://github.com/seedcase-project/seedcase-sprout/commit/78b5445a6f3047d554f7c56213c0519ce21386d2))
- Merge-conflict
  ([0f6db6f](https://github.com/seedcase-project/seedcase-sprout/commit/0f6db6f85e4af9b376aba77f5b47a00320cb429f))
- Changing existing table
  ([15ee617](https://github.com/seedcase-project/seedcase-sprout/commit/15ee6171e4160d845c3f3c562e46c57232e7cb27))
- Tests and linting is fixed
  ([5df5c2f](https://github.com/seedcase-project/seedcase-sprout/commit/5df5c2f1a6c0c4bee350badae1afbc56d22ae9da))
- Small adjustments
  ([dfd7b0c](https://github.com/seedcase-project/seedcase-sprout/commit/dfd7b0ccafa7dd55eacefee5cea52d004f7cec81))
- Small adjustments
  ([29652a1](https://github.com/seedcase-project/seedcase-sprout/commit/29652a1dabec8fff0f4c7fda28acd7cef5283235))
- Step file upload is added
  ([8e0bc7c](https://github.com/seedcase-project/seedcase-sprout/commit/8e0bc7ca59e9765bc84c0c63c90ce7cc16f00287))
- Is_draft=False when button is clicked
  ([9a093b8](https://github.com/seedcase-project/seedcase-sprout/commit/9a093b88e3c487d51e93ebc23b50572e538529d4))
- Format python
  ([7e6688c](https://github.com/seedcase-project/seedcase-sprout/commit/7e6688c92167183a055902a1e119ad74b418bfab))
- Make --surface-container-high white so it's not purple
  ([d5ad53e](https://github.com/seedcase-project/seedcase-sprout/commit/d5ad53e24bb83a4a3609fba9e73fffce9193ee3a))
- "headers" -> "columns" to fit current naming
  ([41805f4](https://github.com/seedcase-project/seedcase-sprout/commit/41805f47c8c8656cbc9dc97025981ef9a27d3b9a))
- Minor changes to wording in paragraphs
  ([6ebda20](https://github.com/seedcase-project/seedcase-sprout/commit/6ebda20c4c38427ff1cd2ac4ee231341a1f5baaf))
- Update helper dialog text and remove "machine-readable name"
  ([1e9c086](https://github.com/seedcase-project/seedcase-sprout/commit/1e9c08655d248370aec346106537323f5d88f4c8))
- Minor adjustments to step 3 of metadata creation for editing the metadata
  columns [#419](https://github.com/seedcase-project/seedcase-sprout/pull/419)
  ([057dae3](https://github.com/seedcase-project/seedcase-sprout/commit/057dae360ff3e848cbf3d01172f9e2eca75a7d41))
- Remove title from nacbar - not needed when sprout is in the navbar icon
  ([0d1d38e](https://github.com/seedcase-project/seedcase-sprout/commit/0d1d38e682e06f92f54aa6ca17849fa99f26c3a0))
- Elaborate on alt texts
  ([dd31131](https://github.com/seedcase-project/seedcase-sprout/commit/dd31131e63512ff0d8adaab7994555b2e5c037b7))
- Remove blank line
  ([96f4b74](https://github.com/seedcase-project/seedcase-sprout/commit/96f4b7443a2f7142066957fbc2721263dc7257cc))
- Remove old png
  ([49cef98](https://github.com/seedcase-project/seedcase-sprout/commit/49cef98d7d4e7ea532d912d4ab373e16af0c6386))
- Use url shortcode instead of urls inside a tags
  ([603cb17](https://github.com/seedcase-project/seedcase-sprout/commit/603cb172fd3c4d8d2e6b58570dc8d2acabea6061))
- Polars changed the name PolarsDataType to DataType
  ([87e7737](https://github.com/seedcase-project/seedcase-sprout/commit/87e7737cb8b68320ffbd9bbddb2eaa2014ae0a24))
- Fix check for whether tests are running
  ([a59eefa](https://github.com/seedcase-project/seedcase-sprout/commit/a59eefa6c8b5ac351ea63b756bb671b52a6840aa))
- Debug code depended on old unittest, updated for pytest
  [#529](https://github.com/seedcase-project/seedcase-sprout/pull/529)
  ([49e8f7a](https://github.com/seedcase-project/seedcase-sprout/commit/49e8f7a64120c488eecdd63eb70588d447b09801))
- Update c4 image links to svg
  ([8bc440c](https://github.com/seedcase-project/seedcase-sprout/commit/8bc440c8dbe1762da0e7eb00031ffb7fd656ab71))
- Update c4 image links to svg
  [#542](https://github.com/seedcase-project/seedcase-sprout/pull/542)
  ([deedffc](https://github.com/seedcase-project/seedcase-sprout/commit/deedffcb59a626a1a90f0a8b19cc2f3394a1a8d5))
- Path to svg
  ([7270ead](https://github.com/seedcase-project/seedcase-sprout/commit/7270eada13231cc14169484c37c8c8d1445cefaf))
- Use seedcase puml theme
  ([af96e35](https://github.com/seedcase-project/seedcase-sprout/commit/af96e359a04c3ffae9ea5c2ba2deb888352980fb))
- Image links and theme
  [#543](https://github.com/seedcase-project/seedcase-sprout/pull/543)
  ([8999a56](https://github.com/seedcase-project/seedcase-sprout/commit/8999a56e38246896507522b1494af873a2ff1353))
- Remove font colour and name from state diagrams
  [#583](https://github.com/seedcase-project/seedcase-sprout/pull/583)
  ([acaf25b](https://github.com/seedcase-project/seedcase-sprout/commit/acaf25baf31ac5e281bdde1b8fce4d7991608c11))
- Rename own csv folder to avoid clash with built-in csv
  [#593](https://github.com/seedcase-project/seedcase-sprout/pull/593)
  ([406b6f3](https://github.com/seedcase-project/seedcase-sprout/commit/406b6f3dd3e3d07d236b81affa2580d54f447b9f))
- Fix warnings from deprecated arguments
  ([7200f6a](https://github.com/seedcase-project/seedcase-sprout/commit/7200f6a5e7d49733236277f084f447174b56d20c))
- Fix import using old name
  [#670](https://github.com/seedcase-project/seedcase-sprout/pull/670)
  ([d9a15d5](https://github.com/seedcase-project/seedcase-sprout/commit/d9a15d5323d1e9110f0925abf7f593185aabfdfd))
- Remove space from filename
  [#687](https://github.com/seedcase-project/seedcase-sprout/pull/687)
  ([8d98200](https://github.com/seedcase-project/seedcase-sprout/commit/8d98200f081dfa5467f0dcb56d38e11deee57f54))
- Remove unnecessary id from `ResourceProperties`
  [#735](https://github.com/seedcase-project/seedcase-sprout/pull/735)
  ([c26e043](https://github.com/seedcase-project/seedcase-sprout/commit/c26e0438593a6956796a62aecf4b282c6c75d9bd))
- Add missing brackets
  [#750](https://github.com/seedcase-project/seedcase-sprout/pull/750)
  ([249822c](https://github.com/seedcase-project/seedcase-sprout/commit/249822c00094604a2376c46cc7a869bd10f7e669))
- Broken link to guide index file
  [#764](https://github.com/seedcase-project/seedcase-sprout/pull/764)
  ([7d4c09c](https://github.com/seedcase-project/seedcase-sprout/commit/7d4c09cdcdf17f9642dd76d5069cafcc90c22734))
- Sort ids before returning them
  [#767](https://github.com/seedcase-project/seedcase-sprout/pull/767)
  ([cede7a3](https://github.com/seedcase-project/seedcase-sprout/commit/cede7a34f635e67c45cbd4da2ff5ed69d4512a7e))
- Add UTC timezone to tests using timemachine
  [#851](https://github.com/seedcase-project/seedcase-sprout/pull/851)
  ([71c4985](https://github.com/seedcase-project/seedcase-sprout/commit/71c4985f14ae47b48f70347008027e7869d282be))

### ⏪ Revert

- Black formatting
  ([0ca773f](https://github.com/seedcase-project/seedcase-sprout/commit/0ca773fd77e0125001b68f1f9696da2f6d59d0b4))
- Remove irrelevant comment
  ([3bcc3f7](https://github.com/seedcase-project/seedcase-sprout/commit/3bcc3f733f2a4236606e238d62eca9dbfb21f4f2))
- Remove icon in create new table dialog
  ([7650118](https://github.com/seedcase-project/seedcase-sprout/commit/7650118834794da24c7a3f2abfa949b4ceb93543))
- "table name" -> "name" to test autocomplete="off"
  ([01ba59f](https://github.com/seedcase-project/seedcase-sprout/commit/01ba59f6d4a72c8edf4015adc35488cd77d48c6b))
- Reimplementing custom save method
  ([8b8a2f7](https://github.com/seedcase-project/seedcase-sprout/commit/8b8a2f79d93b27b8580403f470caa33d172e6cb7))
- Remove local experiments with removing create metadata dialog
  ([ac5d756](https://github.com/seedcase-project/seedcase-sprout/commit/ac5d75689938f10867e29474e4046e961c447490))
- Remove unused color
  ([76c6c1d](https://github.com/seedcase-project/seedcase-sprout/commit/76c6c1deb128b00b3d1940e6bb3192206599e1b5))

### ♻️ Refactor

- Update to match partial user flow diagrams
  ([1113441](https://github.com/seedcase-project/seedcase-sprout/commit/111344162d278a3f20a29fc996376d82775a0b2c))
- Rename val of no special characters
  ([d257eb9](https://github.com/seedcase-project/seedcase-sprout/commit/d257eb99df5366458f524145764271d0dd017171))
- Explicitly state that create is a submit button
  ([583dd3f](https://github.com/seedcase-project/seedcase-sprout/commit/583dd3fb116b0e00fc4c08fa710036d79072a0b6))
- Move val table already exists to form instead of model
  ([25ce14b](https://github.com/seedcase-project/seedcase-sprout/commit/25ce14b5f1340dacabaf62ce7af3a73c8a2032db))
- Use redirect instead of httpresponseredirect
  ([a2a9661](https://github.com/seedcase-project/seedcase-sprout/commit/a2a9661ad157cd47bfca16985aee9128db3ab966))
- Move validation of special character to validator
  ([9ee1517](https://github.com/seedcase-project/seedcase-sprout/commit/9ee1517875ccc791c9184c9e52bac5f3deedae0d))
- Add type hints for returns
  ([518be99](https://github.com/seedcase-project/seedcase-sprout/commit/518be99df1428719f30576051110dc97c196bcb8))
- Add typehints and docstring to clean_name
  ([0a3d86c](https://github.com/seedcase-project/seedcase-sprout/commit/0a3d86c7d4fa613bc48ca80d226019cd899226e8))
- Specify imports from django.forms
  ([c0f1c79](https://github.com/seedcase-project/seedcase-sprout/commit/c0f1c79c9199b897c208e59752b2d31f57d39eb2))
- Update error msg of no special characters validator
  ([6223308](https://github.com/seedcase-project/seedcase-sprout/commit/622330823fed8334d31e60534f2adf868b1bf8dd))
- Move const dialog to showDialog()
  ([8f9ef56](https://github.com/seedcase-project/seedcase-sprout/commit/8f9ef568756acd8d2204e89a6c1c9061a6c5602d))
- Method name change
  ([d87a14c](https://github.com/seedcase-project/seedcase-sprout/commit/d87a14c0f1aed63c351844476a33e16840e35fcd))
- Migration and FileMetaData renamed to FileMetadata
  ([ea86845](https://github.com/seedcase-project/seedcase-sprout/commit/ea8684553f9e3d4c4ef6e6d0d491c7ce3c341a78))
- Split up tests for views into separate files
  ([8acbd0c](https://github.com/seedcase-project/seedcase-sprout/commit/8acbd0c6d67316d6fe67b3cdf0f4b47f060fc248))
- Rename to specify which models are included in this file
  ([ec241d5](https://github.com/seedcase-project/seedcase-sprout/commit/ec241d50d3440dc297791fa097f5aa4009a3a8aa))
- Moved to csv folder
  ([29da12c](https://github.com/seedcase-project/seedcase-sprout/commit/29da12cd1f1a1bde43973167b39190356e05955a))
- Revise to indicate the upload is for creating metadata, not the final upload
  ([738263b](https://github.com/seedcase-project/seedcase-sprout/commit/738263bcd7a041356c20dbec134e1af0a861b7df))
- Rename files to match the `metadata/create` format
  ([6dda120](https://github.com/seedcase-project/seedcase-sprout/commit/6dda120feccb1908b7aa2b75551e2e3aeb4bca55))
- Move file storage code into its own function for more generic use later
  ([f3407a2](https://github.com/seedcase-project/seedcase-sprout/commit/f3407a219a8bd76e32a15cc72ab85d8129928928))
- Renamed function to describe what it does better, given changes to other
  functions
  ([7fb41a0](https://github.com/seedcase-project/seedcase-sprout/commit/7fb41a0433b68ef8d6089918bcae3166e13e301c))
- True/False seems more appropriate than Yes/No.
  ([42d4869](https://github.com/seedcase-project/seedcase-sprout/commit/42d48690d45b466dfd307fb829702f0b43a62c34))
- Convert to new naming scheme
  ([5b85ad2](https://github.com/seedcase-project/seedcase-sprout/commit/5b85ad2ff282688dd9503d003bc1ac6700cffc21))
- Remove duplicated/scatter code and consolidate into single `column-review`
  page
  ([b56486e](https://github.com/seedcase-project/seedcase-sprout/commit/b56486eee4a5a5d1ac3073c605b9e467c3c59cbb))
- Remove duplicated Django views and consolidated into `column_review.py`
  ([4a6ce62](https://github.com/seedcase-project/seedcase-sprout/commit/4a6ce62cbe7b1af30aafaa62b66fe2e2579e75bb))
- Update links after consolidation
  ([9ddd14c](https://github.com/seedcase-project/seedcase-sprout/commit/9ddd14cb1b5f443a5435d35bd75cfe41ccc2cb57))
- Restructure if statement to avoid writing error msg twice
  ([4a028a6](https://github.com/seedcase-project/seedcase-sprout/commit/4a028a6a9bc47ef52261d3f9fb26e21790933efc))
- Remove unused form name
  ([0cc1249](https://github.com/seedcase-project/seedcase-sprout/commit/0cc1249b0ed82627ac7356697336c6a8ad22d2aa))
- Handle redirect in template instead of view using js
  ([08e6010](https://github.com/seedcase-project/seedcase-sprout/commit/08e60104995aa43724b47d567e8f68d9f405dbb4))
- Move table selectable styles to static
  ([9270f8c](https://github.com/seedcase-project/seedcase-sprout/commit/9270f8c8a3f17d3471de318f336033919de11f9a))
- Change buttons to anchors to slightly simplify code
  ([a78d47e](https://github.com/seedcase-project/seedcase-sprout/commit/a78d47e6e1b678275410d93f5c681f181731832b))
- Simplified js and removed tests not valid with a js solution
  ([b95dbf8](https://github.com/seedcase-project/seedcase-sprout/commit/b95dbf8551d60ea315779fac6aad0b5df478568c))
- Separate create new metadata dialog
  ([a0ad204](https://github.com/seedcase-project/seedcase-sprout/commit/a0ad2048ee834a9557998c17164a056a149679e9))
- Merge expand feature into `project id metadata`
  ([ca0e848](https://github.com/seedcase-project/seedcase-sprout/commit/ca0e848c06752f002d4fc9933f60760f4152b8f1))
- URL should match naming scheme for URLs (minus project/id)
  ([5236b0c](https://github.com/seedcase-project/seedcase-sprout/commit/5236b0c80e01929cd763d6a4595bdd4b1645c25a))
- Rename HTML template file to match naming scheme
  ([29bcc64](https://github.com/seedcase-project/seedcase-sprout/commit/29bcc6482acae51ebaf1da6dc6d00777ebbd6ee7))
- Revise to match naming scheme
  ([df4bd4c](https://github.com/seedcase-project/seedcase-sprout/commit/df4bd4cd4c095450d4132ec998678f1c73367701))
- Use index.html instead in the Django view
  ([3a50a2e](https://github.com/seedcase-project/seedcase-sprout/commit/3a50a2e41c84dfa7548c0a8d55121ec8fc1dc751))
- Fix path to base.html, plus reformat
  ([5222d0b](https://github.com/seedcase-project/seedcase-sprout/commit/5222d0b6b86f45cc435a6fc3a2f99b90ca7c9b43))
- Use `project-id-view` html file path
  ([bec147d](https://github.com/seedcase-project/seedcase-sprout/commit/bec147dfdef83e0a4d32d3803c5fdf7a00e2c3b9))
- Change function names after renaming
  ([ba894b5](https://github.com/seedcase-project/seedcase-sprout/commit/ba894b57a986709c598a9da1ae79625794bd04e7))
- Fix names of URL in Python code
  ([f542327](https://github.com/seedcase-project/seedcase-sprout/commit/f5423274df0b799aab7ce935aa9cb960fbb62799))
- Rename functions to match scheme for metadata edit grid
  ([5a10f24](https://github.com/seedcase-project/seedcase-sprout/commit/5a10f24df0747e2a2605b72b98676686892b7c66))
- Match naming scheme for data/id/metadata/edit/table
  ([8bf617e](https://github.com/seedcase-project/seedcase-sprout/commit/8bf617e3cba8241ef9061ed5aa30c4540f6ba899))
- Match naming scheme for data/id/metadata/create
  ([19c9f83](https://github.com/seedcase-project/seedcase-sprout/commit/19c9f83ee7a26ad8a93366fa7cdef4d01569dc39))
- Match scheme for data/id/metadata/edit/table
  ([483637d](https://github.com/seedcase-project/seedcase-sprout/commit/483637d6d46b138187b41e04694ddee9f05a164a))
- Match scheme for data/id/metadata/create
  ([fbfe676](https://github.com/seedcase-project/seedcase-sprout/commit/fbfe6763542c877391cd78535dee9302d8e355b5))
- Match scheme for data/id/metadata/create
  ([82e0c65](https://github.com/seedcase-project/seedcase-sprout/commit/82e0c6588272eb26cfdd309703f1c9829af7ad9c))
- Fix paths to includes files, plus auto-reformat HTML
  ([5eb815a](https://github.com/seedcase-project/seedcase-sprout/commit/5eb815af8f2d463bec3f291631550483d9d8a51b))
- Update URLs and links to reflect name change, but leads to test issues
  ([642e6e9](https://github.com/seedcase-project/seedcase-sprout/commit/642e6e9942e7cdcda306dd97a50efdc94091d3c3))
- Projects-id instead of project-id (plural)
  ([c7e1472](https://github.com/seedcase-project/seedcase-sprout/commit/c7e1472a2ef3b339e795bd551e5e2fd6112afca7))
- Use correct url for create metadata, plus use reverse for url
  ([54d5083](https://github.com/seedcase-project/seedcase-sprout/commit/54d5083f58b53a5d85579a88dcb22c6e2c4e1107))
- Move to user-tests folder
  ([57713bf](https://github.com/seedcase-project/seedcase-sprout/commit/57713bf23d1b400f77dbac11755cec0e3a7afd12))
- Rename model class for DataTypes to match naming scheme
  ([b4499ad](https://github.com/seedcase-project/seedcase-sprout/commit/b4499adcad1f5bc43d24a3c5a59e6d10efd0c4b3))
- Rename to Columns (and columns) to match naming scheme of class
  ([424c43a](https://github.com/seedcase-project/seedcase-sprout/commit/424c43a1aeb978cb170e8d9a148bfa8d764047de))
- This should be capitalized as it is a constant
  ([9a2e127](https://github.com/seedcase-project/seedcase-sprout/commit/9a2e12705f7ff8b766ae72c944dcd1aec6fdf52a))
- Rename Files model to match naming scheme
  ([e4b4bdc](https://github.com/seedcase-project/seedcase-sprout/commit/e4b4bdcf1d295b7589126aa2d3f2525deb0da900))
- Rename Tables class to match naming scheme
  ([d2d2ad1](https://github.com/seedcase-project/seedcase-sprout/commit/d2d2ad11aa60955b44c04d2b337e3cb0868da43c))
- Convert URLs to use `reverse()` with full Django URL name (not path)
  ([4765967](https://github.com/seedcase-project/seedcase-sprout/commit/476596749dfa44cf9dc6159be6c98ee9e00a30bc))
- `projects id` not `project id`
  ([f857a83](https://github.com/seedcase-project/seedcase-sprout/commit/f857a837886a65740d0aa33952bb0021a8f23688))
- Follow naming scheme for classes
  ([337fe61](https://github.com/seedcase-project/seedcase-sprout/commit/337fe61cc28c072bb0fc5c54e78c0d47c5aeef7c))
- Include `includes` in path of these templates
  ([9feaae0](https://github.com/seedcase-project/seedcase-sprout/commit/9feaae055ce403666f58a38efa1c7aba7ca84d14))
- Make projects_id_metadata_view the home page
  ([342475e](https://github.com/seedcase-project/seedcase-sprout/commit/342475e7013d8e7ab2fa02a38b82e635cc30f6d5))
- Change redirects fit that projects_id_metadata_view is home
  ([13fc940](https://github.com/seedcase-project/seedcase-sprout/commit/13fc940812bf180fda7d2b6f0272b15da03a3fc2))
- Remove placeholder home
  ([9aa3da9](https://github.com/seedcase-project/seedcase-sprout/commit/9aa3da9a5c9f5cd60355fc340dbf0670d326e700))
- Use URL Django shortcode
  ([2c93522](https://github.com/seedcase-project/seedcase-sprout/commit/2c93522f3c7c90204e54dae0551f31fc53b1bfe2))
- Move table css styling into own file and initiate ui
  ([567564a](https://github.com/seedcase-project/seedcase-sprout/commit/567564a9d5c71645757f446bc1daab7d45d50ec9))
- Code is simplified
  ([86f72a2](https://github.com/seedcase-project/seedcase-sprout/commit/86f72a2a4659fe8846fb2b7d4f72797a24870dbd))
- Initiate the move of card styling to separate css file
  ([9eab924](https://github.com/seedcase-project/seedcase-sprout/commit/9eab924c8b6794f75440071ed4b7c3e0a80f88dc))
- Optimise the use of the innate theme variables
  ([3b3b0f8](https://github.com/seedcase-project/seedcase-sprout/commit/3b3b0f8201194e068e79ab952eff132aa16b6972))
- Move `background-image` into css to remove use of inline style
  ([a454c88](https://github.com/seedcase-project/seedcase-sprout/commit/a454c88e4b870fe775258898469b5eeba5149de7))
- Incompletely update/expand on the C4 component for API
  ([58454e5](https://github.com/seedcase-project/seedcase-sprout/commit/58454e5867c7b612a9a32e87ec470304ef659f2b))
- Renames based on PR review
  ([9a72e04](https://github.com/seedcase-project/seedcase-sprout/commit/9a72e0465a256354993f624d76517974b9c3cb5f))
- Switch to using HTML dd for each item, rather than a break between
  ([cb38bbe](https://github.com/seedcase-project/seedcase-sprout/commit/cb38bbeac8a6abd95583b2c9eca0a57a0917d6b2))
- Change label to "data type"
  [#519](https://github.com/seedcase-project/seedcase-sprout/pull/519)
  ([88a0fd3](https://github.com/seedcase-project/seedcase-sprout/commit/88a0fd3ad42493c83be0bfed418ff9207de13442))
- Reorganize Sprout into core and app components
  [#522](https://github.com/seedcase-project/seedcase-sprout/pull/522)
  ([d6f32c7](https://github.com/seedcase-project/seedcase-sprout/commit/d6f32c7429dd027a47dca17b311527abd38dd3e4))
- Add frictionless-style sample data and metadata
  [#530](https://github.com/seedcase-project/seedcase-sprout/pull/530)
  ([72d846a](https://github.com/seedcase-project/seedcase-sprout/commit/72d846a06059b5f318cac584eb5b80ad73134273))
- Move some string helper functions to core
  [#541](https://github.com/seedcase-project/seedcase-sprout/pull/541)
  ([c4d2e6d](https://github.com/seedcase-project/seedcase-sprout/commit/c4d2e6d9efc629de90aae343ea1893585d57b077))
- Divide tests into app and core folders
  [#545](https://github.com/seedcase-project/seedcase-sprout/pull/545)
  ([9a7465c](https://github.com/seedcase-project/seedcase-sprout/commit/9a7465c07d7b4db1d7785718f1e3f765537bd856))
- Rename to `edit_property_field()` to be more inclusive
  [#658](https://github.com/seedcase-project/seedcase-sprout/pull/658)
  ([b77ea6c](https://github.com/seedcase-project/seedcase-sprout/commit/b77ea6cec806a8c9f1c01baeb222b5f0528b94a2))
- Remove some functions in `create_properties_template()`
  [#685](https://github.com/seedcase-project/seedcase-sprout/pull/685)
  ([6f6a1e4](https://github.com/seedcase-project/seedcase-sprout/commit/6f6a1e468ccd59d73735deaf125b6ae6f301993c))
- Create resource dir when making package
  [#788](https://github.com/seedcase-project/seedcase-sprout/pull/788)
  ([b59dbff](https://github.com/seedcase-project/seedcase-sprout/commit/b59dbff0481a1a1556d0bed2f9006bab211c4f01))
- Rename "sprout" folder to "seedcase_sprout"
  [#844](https://github.com/seedcase-project/seedcase-sprout/pull/844)
  ([212b953](https://github.com/seedcase-project/seedcase-sprout/commit/212b9538cac7b93f6720410aa4c6ab7c329edfd2))
- Remove everything Django-related
  [#848](https://github.com/seedcase-project/seedcase-sprout/pull/848)
  ([ab0beff](https://github.com/seedcase-project/seedcase-sprout/commit/ab0beff9b00ce8eae0a1b5fcd4f4b06f49976307))

### 📝 Documentation

- *(diagrams)* Update svg for create_package_structure()
  ([0a4caa7](https://github.com/seedcase-project/seedcase-sprout/commit/0a4caa76dba00cd5c586d45ae6c66418ceef01e8))
- *(diagrams)* Add path as input for `create_id_path()`
  ([dec67a7](https://github.com/seedcase-project/seedcase-sprout/commit/dec67a77c6326a70e07daabc59c828eb4b7b5f4d))
- Content copy dump from seedcase-project repo
  ([58276fa](https://github.com/seedcase-project/seedcase-sprout/commit/58276faf295a5414600a1f7629b38750dc4bdf5d))
- Name file to be "users" to better reflect the contents
  ([8481bff](https://github.com/seedcase-project/seedcase-sprout/commit/8481bffdf8935a199e3d5e66b3d1c8c44e20070b))
- Update users and their uses of sprout
  ([bbf135f](https://github.com/seedcase-project/seedcase-sprout/commit/bbf135f3a6cb6f57117344759e077af50044e53f))
- Edits based on review comments
  ([ed5a388](https://github.com/seedcase-project/seedcase-sprout/commit/ed5a38806090d2185edc5a3ebd6c30e7b407def2))
- Transfer of text about runtime uploads
  ([1ef089f](https://github.com/seedcase-project/seedcase-sprout/commit/1ef089f94014d25f8a72762bf98e683bd86a4433))
- Small edits and proofreading to runtime view file
  ([0618575](https://github.com/seedcase-project/seedcase-sprout/commit/061857582c00cb8722003a59ce639f4e2e2167da))
- Add some basic details in the README
  ([22636ca](https://github.com/seedcase-project/seedcase-sprout/commit/22636ca6fdacc20d1d4287ab0b7b94608e5166f5))
- Add authors and maintainers to pyproject
  ([5997b55](https://github.com/seedcase-project/seedcase-sprout/commit/5997b553a668a6f3f41450f81d2e7ba385634df5))
- Rename flow diagram for upload prep + add footer
  ([9149eb0](https://github.com/seedcase-project/seedcase-sprout/commit/9149eb019242ae388cf4a9e6e95739ebae3dda29))
- Add initial draft of sequence diagram for upload prep
  ([1958f83](https://github.com/seedcase-project/seedcase-sprout/commit/1958f8388d90f8b0251e85a74879537650ce57ba))
- Rename "prepare for upload" diagrams to "schema creation"
  ([7af0162](https://github.com/seedcase-project/seedcase-sprout/commit/7af01623e185959d6fc0d0fafc817a3f59d88810))
- "Upload new data" -> "Create New Data Schema"
  ([aaa2afc](https://github.com/seedcase-project/seedcase-sprout/commit/aaa2afc041abdece9cea13a1eb7795be9b8dbeb0))
- Add initial draft of sequence diagram showing data upload from existing schema
  ([8871c0d](https://github.com/seedcase-project/seedcase-sprout/commit/8871c0dbc92c058ee93e74596a5d90884df70545))
- Add and move questions/comments to diagrams
  ([8eaecbc](https://github.com/seedcase-project/seedcase-sprout/commit/8eaecbcb93dcf4002ab9fbf755d05879870c1d0f))
- Minor text updates based on meeting with @hgo
  ([d9a0b87](https://github.com/seedcase-project/seedcase-sprout/commit/d9a0b87cfb48f10211d0b0476e205375a3a05e10))
- Minor text updates based on meeting with @henrik-goul
  ([6c454d3](https://github.com/seedcase-project/seedcase-sprout/commit/6c454d3075932b59a3c00f005b74ef290dff71e3))
- Update sequence diagrams based on talks with @henrik-goul and @K-Beicher
  ([4a7335d](https://github.com/seedcase-project/seedcase-sprout/commit/4a7335d803c3d8859fbf4d5a3e52572cc7293b76))
- Use snake_case for column names, more descriptive var names, and backticks for
  formatting
  ([c2d843e](https://github.com/seedcase-project/seedcase-sprout/commit/c2d843e8fccbff2c5af54b0a7e1c446dff5a404e))
- Text mods based on review by @lwjohnst86
  ([6ba6742](https://github.com/seedcase-project/seedcase-sprout/commit/6ba6742385580b7742dd9749b26305a3b373cc51))
- Minor text mods from readthrough
  ([c0ebf4a](https://github.com/seedcase-project/seedcase-sprout/commit/c0ebf4a7d4dfb457255cde1c1d9764fad259cce7))
- Add Data Access Administrator throughout text instead of user
  ([b98aefa](https://github.com/seedcase-project/seedcase-sprout/commit/b98aefa8ae2457dbc0f58571d0b0ac37ff3adaaf))
- Small edits, plus add a caption
  ([bb6eab4](https://github.com/seedcase-project/seedcase-sprout/commit/bb6eab47e4e0ad8c6b29d166526245f5483e4b12))
- Add a link to the fly.io demo app
  ([22ea7b3](https://github.com/seedcase-project/seedcase-sprout/commit/22ea7b3e1a6b11573cd64e4016e5e11712572c65))
- Add table naming and description to user flow
  ([ab48f34](https://github.com/seedcase-project/seedcase-sprout/commit/ab48f342ecf128840845e47ec00457a2db28d44e))
- Add validation check: does table already exist?
  ([88ba6d7](https://github.com/seedcase-project/seedcase-sprout/commit/88ba6d7c01a2b9a6dfac2008f12ada534c0955d6))
- Add validation check: is file a csv?
  ([99fe837](https://github.com/seedcase-project/seedcase-sprout/commit/99fe837bfc01c36ab83314dc5a0f0413e5b8d86c))
- Update with table description overlay and validation checks
  ([1bdefc3](https://github.com/seedcase-project/seedcase-sprout/commit/1bdefc3248c92ab0bef74f3d55b51f35e544f305))
- Add table creation diagram
  ([2a623f2](https://github.com/seedcase-project/seedcase-sprout/commit/2a623f25d00cdaa7c422653044be6d0ebe1b9b99))
- Minor update to comments
  ([fcf9a40](https://github.com/seedcase-project/seedcase-sprout/commit/fcf9a408b737cfb3a1a0d59131df48510f991350))
- Add comments describing sub-diagrams' start and end
  ([1a7756c](https://github.com/seedcase-project/seedcase-sprout/commit/1a7756cf36f1f8caba6335c0507e74dc603f8f5b))
- This text makes more sense in the team docs rather than in the readme
  ([560a665](https://github.com/seedcase-project/seedcase-sprout/commit/560a665c8fe49a6f30750b8975c6ca249347d68e))
- Edits to the data type table, simplify/shorten most fields, add link to
  ISO8601 format for dates
  ([2e9db7e](https://github.com/seedcase-project/seedcase-sprout/commit/2e9db7eddc2a453959c618e16859186b91eeb5e5))
- Decide about using JSON as data type later, commented it out
  ([a9d6b9b](https://github.com/seedcase-project/seedcase-sprout/commit/a9d6b9b0d1b03393eaf654af44417e6977cb2bfa))
- Stylistic choice for headers to simplify the document outline
  ([55176c4](https://github.com/seedcase-project/seedcase-sprout/commit/55176c47968ab3f320fce1e1ed2e9997fcee550e))
- Use yaml header for document title (what quarto expects)
  ([ac40a78](https://github.com/seedcase-project/seedcase-sprout/commit/ac40a78f6ef700a622d6dc3ca0fcadadc908abcf))
- Edits to text of data type sections
  ([271f719](https://github.com/seedcase-project/seedcase-sprout/commit/271f719b5268a155b6300d0fcc7c8d1ee34165cb))
- Comment out section about JSON data type, will return to this later
  ([f0e3952](https://github.com/seedcase-project/seedcase-sprout/commit/f0e3952e0ccae24deb2903f6b07246131645de44))
- Add table creation from file with table metadata
  ([5a14982](https://github.com/seedcase-project/seedcase-sprout/commit/5a149821b34dc22f2d265c24841bc57b07307388))
- Add option to download table metadata after table creation to user flow
  diagram
  ([f6abe49](https://github.com/seedcase-project/seedcase-sprout/commit/f6abe49345864ad60df71d07be01085c60b7df5e))
- Edits to follow wireframes more closely
  ([c59325a](https://github.com/seedcase-project/seedcase-sprout/commit/c59325a7c68000402be60c44602a2a5433c150b3))
- Update user flow subparts to follow main diagram
  ([d119526](https://github.com/seedcase-project/seedcase-sprout/commit/d119526f49d526fe96bbef9a682add1a2fd3060c))
- Minor text edits
  ([b30b875](https://github.com/seedcase-project/seedcase-sprout/commit/b30b875d351c8fbe537ba59a24076d85fbf7a3ac))
- Divide table creation into table and column metadata creation
  ([18de9bd](https://github.com/seedcase-project/seedcase-sprout/commit/18de9bd027975d7a2fc6f01d5fecf942ff4dffb7))
- Update table creation section
  ([e000b41](https://github.com/seedcase-project/seedcase-sprout/commit/e000b41b106723c784556fce89567e1f6eb7dc73))
- Docstrings and type hints
  ([9a50f17](https://github.com/seedcase-project/seedcase-sprout/commit/9a50f17dbe44f9beda5513be54e88e93c1f8494c))
- Remove old/irrelevant code comments
  ([541e555](https://github.com/seedcase-project/seedcase-sprout/commit/541e555367a75540ac23038250316ba8ce856998))
- Remove extra "upload"
  ([8225399](https://github.com/seedcase-project/seedcase-sprout/commit/82253994873b5fa510a2830378e9cde9624920dc))
- Minor edits to module headers
  ([73fac88](https://github.com/seedcase-project/seedcase-sprout/commit/73fac883029277412db2a4dce23f6aa4c1a197ed))
- Docstring edits
  ([f166b1e](https://github.com/seedcase-project/seedcase-sprout/commit/f166b1e0f8574d5047cf33b0764f455845ddfad4))
- Minor edit of docstring header
  ([e8d26e1](https://github.com/seedcase-project/seedcase-sprout/commit/e8d26e169208b7fffd505b87eab0feb6ef37e713))
- Remove "main application" from init docstring
  ([c046452](https://github.com/seedcase-project/seedcase-sprout/commit/c046452875231c84e2b61ed77efddc4fb196c572))
- Docstring wording changes
  ([63e2bc5](https://github.com/seedcase-project/seedcase-sprout/commit/63e2bc5e98db2d3049989c8e054d1ae93e2bb48c))
- Remove irrelevant comments
  ([9ab4065](https://github.com/seedcase-project/seedcase-sprout/commit/9ab4065bef7561d14d3ed2a968f0a72656a0df03))
- Fix two docstrings with line lengths longer than the max length
  ([fef253b](https://github.com/seedcase-project/seedcase-sprout/commit/fef253b20cd322c40c275b9617388a3efebcf817))
- Remove extra tabs
  ([8bbaf84](https://github.com/seedcase-project/seedcase-sprout/commit/8bbaf8494c72093931a23e367f3f81f89a4dc19d))
- Removed types on args
  ([168e5aa](https://github.com/seedcase-project/seedcase-sprout/commit/168e5aab86e36b45adc2ecf97e57ab569e004ee2))
- Edits and formatting fixes for the Markdown files
  ([f5b57a3](https://github.com/seedcase-project/seedcase-sprout/commit/f5b57a3cddd69337eee58f6da25e2c6f4177ab53))
- Small ruff change
  ([9afa81b](https://github.com/seedcase-project/seedcase-sprout/commit/9afa81bc300e583ccaf6e9f3257fc56517eedfab))
- Adding some documentation
  ([129b37d](https://github.com/seedcase-project/seedcase-sprout/commit/129b37d230557d40c16729faec4fcce720e14a9b))
- Remove option to add column during table completeness validation
  ([504bd61](https://github.com/seedcase-project/seedcase-sprout/commit/504bd61d5efb439cf4dd5e7ce65ee4a3d7d4e85d))
- Update pngs based on pumls
  ([d11d389](https://github.com/seedcase-project/seedcase-sprout/commit/d11d38902d6c3ea74c4970be5e75408ba85124e5))
- Add system converts original column name to snake case
  ([2b9284c](https://github.com/seedcase-project/seedcase-sprout/commit/2b9284c0212bcaef82414c7039a4fdcd106df721))
- Add initial table has been created in green box
  ([dddc9c4](https://github.com/seedcase-project/seedcase-sprout/commit/dddc9c435871dbf08aba9e55309e82e772f4455a))
- Fix typo: use -> user
  ([9201f33](https://github.com/seedcase-project/seedcase-sprout/commit/9201f33c0a405dd3b11821fcf7a0f5fc927f5ea5))
- Move comment on table completeness val down
  ([ed692e0](https://github.com/seedcase-project/seedcase-sprout/commit/ed692e01c334af41ed1aaf03d830989123878450))
- Layout - move to one line
  ([1de7328](https://github.com/seedcase-project/seedcase-sprout/commit/1de73281ab935a73c4193120453090d9965383dd))
- Remove actual error message text and describe error instead
  ([ccfb732](https://github.com/seedcase-project/seedcase-sprout/commit/ccfb73247bfbe240d8a01b4a3b5888268d1fbf4e))
- Add edits from user flow.puml
  ([31a610a](https://github.com/seedcase-project/seedcase-sprout/commit/31a610a5bbdb2855c978baba5a8cedee15341215))
- Add edits to val table completeness from user flow.puml
  ([48d2637](https://github.com/seedcase-project/seedcase-sprout/commit/48d263746b6f60edd98fc7ad96c6326ad17b493b))
- Add todo to do overall introduction of sprout flow
  ([4ab5df6](https://github.com/seedcase-project/seedcase-sprout/commit/4ab5df63c7b36ebfb6defe9cb266b9684c21ede0))
- Fix mistake of having "second" twice
  ([841d37d](https://github.com/seedcase-project/seedcase-sprout/commit/841d37ddac06b267c6be1bd93825c86f35d4957d))
- Add updated user-flow png
  ([f5b56fd](https://github.com/seedcase-project/seedcase-sprout/commit/f5b56fdff05ef8e6a2afe7ac4a7e9c0b2b695cb5))
- Add fork to contain "create column metadata from file"
  ([979bea0](https://github.com/seedcase-project/seedcase-sprout/commit/979bea03db92495302ef75ac0b1a8800d60ee01d))
- Move column metadata extraction and original column name to snakecase to end
  of fork
  ([9f4fa5c](https://github.com/seedcase-project/seedcase-sprout/commit/9f4fa5c6bf8b94082278a29171ae6323b404fecf))
- Table -> column metadata
  ([315cbaf](https://github.com/seedcase-project/seedcase-sprout/commit/315cbafc31e29b8e5344a288048e5f162451f26f))
- Update based on user-flow.puml
  ([51f380e](https://github.com/seedcase-project/seedcase-sprout/commit/51f380e2119df28d292c5f14017fbdd9f192a04c))
- Update pngs based on changes in their pumls
  ([f913284](https://github.com/seedcase-project/seedcase-sprout/commit/f91328419386f7464a7f2c9b99910339ec494d00))
- Add "with data" to header
  ([4ebc19c](https://github.com/seedcase-project/seedcase-sprout/commit/4ebc19c41494470a7d0c8786105f7c8f72f90725))
- Add column name creation from original column names in text
  ([1319f58](https://github.com/seedcase-project/seedcase-sprout/commit/1319f58424abb0e732ba94d64f6e39e8cb10b9fa))
- Remove last instance of "option to add column"
  ([28a4be1](https://github.com/seedcase-project/seedcase-sprout/commit/28a4be10488d990f4a513dd8e4a971f3c41babd0))
- A draft of the naming scheme
  ([61f9e9a](https://github.com/seedcase-project/seedcase-sprout/commit/61f9e9a8743a3ec733cbb545146075f1bc4c5109))
- Add another potential equivalent naming pair
  ([a438232](https://github.com/seedcase-project/seedcase-sprout/commit/a438232828e120c6d0290638a30e7a792d5e96ae))
- Small edits to naming scheme
  ([e052704](https://github.com/seedcase-project/seedcase-sprout/commit/e0527044dab265534ff2f3317548658b72ebdf35))
- Apply suggestions from code review
  ([bd1ba96](https://github.com/seedcase-project/seedcase-sprout/commit/bd1ba9694057c28846aec8d781ddb7beaec22b52))
- Update naming scheme docs based on comments from PR
  ([5faf3d2](https://github.com/seedcase-project/seedcase-sprout/commit/5faf3d2a08be914514ff73b7780a24b1d5771cd3))
- Update usage of Yes/No to True/False in documentation
  ([2792bf2](https://github.com/seedcase-project/seedcase-sprout/commit/2792bf27ed0cb7e29f5671f7cd33af15120ac480))
- Minor edit for clarification
  ([6615d12](https://github.com/seedcase-project/seedcase-sprout/commit/6615d12ed069d393f00de8ed03a4e6e81f89e190))
- Make docstring clearer
  ([52c8ac3](https://github.com/seedcase-project/seedcase-sprout/commit/52c8ac378931fbe64e9c31a3755c2a9963720482))
- Update naming scheme after extensive discussions about it
  ([a04fe8e](https://github.com/seedcase-project/seedcase-sprout/commit/a04fe8e6bb942e4515e9912083856bbda8ae2954))
- Naming scheme for internal Python code
  ([56a4656](https://github.com/seedcase-project/seedcase-sprout/commit/56a46565d2ef4cd7505a152c3ed5c5237c1b568c))
- Apply suggestions from code review
  ([980b22d](https://github.com/seedcase-project/seedcase-sprout/commit/980b22d62a7b02b27429d8567d67a8a919d168af))
- Apply suggestions from code review
  ([3840ad7](https://github.com/seedcase-project/seedcase-sprout/commit/3840ad76068d600057995cf6d968da9eaaf502c5))
- Fix file docstring
  ([0e14b2b](https://github.com/seedcase-project/seedcase-sprout/commit/0e14b2b98aeaa95ba3f0e32db245dce5d9bc7be3))
- Remove removed variable (error msg) from test docstring
  ([752a5bd](https://github.com/seedcase-project/seedcase-sprout/commit/752a5bd8975ab896e7b18cd213c48de557fc9f5a))
- Change button texts to sentence case
  ([e98962e](https://github.com/seedcase-project/seedcase-sprout/commit/e98962e04cc773c663663c521525f105014bab89))
- Added comments to some tricky code
  ([2331b36](https://github.com/seedcase-project/seedcase-sprout/commit/2331b365be847cf4ee56e26dd434df72fc49e4dd))
- Finish writing the docstrings
  ([c386528](https://github.com/seedcase-project/seedcase-sprout/commit/c38652818ab105bceaccaa7754fe88d262f440ba))
- Rename edit to update
  ([1a0a44c](https://github.com/seedcase-project/seedcase-sprout/commit/1a0a44cde4c7678600fe049bdbcff6607bbade2e))
- Add draft for user test context
  ([4a2e0da](https://github.com/seedcase-project/seedcase-sprout/commit/4a2e0da7807b73b14e5901744f67d6247f105c71))
- Update introduction with clearer sentences
  ([7f358d1](https://github.com/seedcase-project/seedcase-sprout/commit/7f358d10811ae8119beec28b58e4d8e4a07278f2))
- Add a short intro to the Seedcase ecosystem as a whole
  ([179f225](https://github.com/seedcase-project/seedcase-sprout/commit/179f2256170747a29ce18845470a592ffee86473))
- Add comment on potentially removing the definitions of data and metadata
  ([3a15a65](https://github.com/seedcase-project/seedcase-sprout/commit/3a15a655dcd66c9b40617c996e6d3e4ba13d7a4a))
- Fix date error in example data
  ([80168db](https://github.com/seedcase-project/seedcase-sprout/commit/80168dbc80fbfe0d0cd0f246b3c5cb897c6d6f67))
- Remove definitions of data and metadata
  ([d9715aa](https://github.com/seedcase-project/seedcase-sprout/commit/d9715aa6b53b262bd546debe190a9c50d7d1f715))
- Added link to the data repo
  ([9935f38](https://github.com/seedcase-project/seedcase-sprout/commit/9935f38c1be5f22eaef5903a4ca9d0b1eb599c53))
- Fix docstring related to change in naming scheme of models
  ([d5d3183](https://github.com/seedcase-project/seedcase-sprout/commit/d5d3183466231b96eddefeb57d91b3701518d3d4))
- Minor changes to save docstring
  ([2f84dcc](https://github.com/seedcase-project/seedcase-sprout/commit/2f84dcc1b0c386defd1511784e1ed3c8ab61b517))
- Create a diagram of the flow for the functionalit/pages
  ([f16aa9c](https://github.com/seedcase-project/seedcase-sprout/commit/f16aa9c3a84778213651d530d3524865e646945f))
- Start including a glossary of terms
  ([9af122c](https://github.com/seedcase-project/seedcase-sprout/commit/9af122ca985a973bc597e7a32018cc41ac5a44d6))
- Add CCBY license for docs
  ([93fe788](https://github.com/seedcase-project/seedcase-sprout/commit/93fe7882c5291b4fc45342a6cb50166917e3ce98))
- Update all C4 model plantuml diagrams
  ([11ccf44](https://github.com/seedcase-project/seedcase-sprout/commit/11ccf442b561294f74b9f8bb38918a9a121138a2))
- Apply suggestions from code review
  ([a43c16f](https://github.com/seedcase-project/seedcase-sprout/commit/a43c16ff9f8e7f5baa36133f5583b7abbf85e9b2))
- Revisions based on PR comments and feedback
  ([38a7d03](https://github.com/seedcase-project/seedcase-sprout/commit/38a7d03f9c218c4b308cb866261a36a67f838442))
- Document listing and describing the C4 model diagrams
  ([ba2421f](https://github.com/seedcase-project/seedcase-sprout/commit/ba2421f43234c478f30dc411e1c556d2a9822c5e))
- Apply suggestions from code review
  ([4f9c25b](https://github.com/seedcase-project/seedcase-sprout/commit/4f9c25b9402b4ed40848bed8dd992c63bb334b64))
- Update based on PR comments
  ([aa8ea63](https://github.com/seedcase-project/seedcase-sprout/commit/aa8ea635c0b64517867215a3838b8e2cf3a0c824))
- Update with desc of data
  ([8984202](https://github.com/seedcase-project/seedcase-sprout/commit/898420227d205d978c71d5bd64b8d93c62d98f18))
- New user type and data description
  ([a3f1d4e](https://github.com/seedcase-project/seedcase-sprout/commit/a3f1d4ef371f3c84b97394159577397f9b2aa3ea))
- Update based on Luke's comments
  ([c6c1259](https://github.com/seedcase-project/seedcase-sprout/commit/c6c1259ed2fb4de5b3875d5813e505df462d1e52))
- Update first batch of comments
  ([7525551](https://github.com/seedcase-project/seedcase-sprout/commit/7525551b617fc6f8678426a29e53240f019e4ec2))
- Formating
  ([26dbba1](https://github.com/seedcase-project/seedcase-sprout/commit/26dbba1512ca7665d0b38a33d392925332dec2cd))
- Revise and reorganize user roles doc
  ([47a4d61](https://github.com/seedcase-project/seedcase-sprout/commit/47a4d6125c11f5f1efcc0410d0a41723dbff09ba))
- Fix broken links users.qmd -> user-roles.qmd
  ([e7ac6f3](https://github.com/seedcase-project/seedcase-sprout/commit/e7ac6f3efc9c5f89248b3c635dddbf38e3ab19f5))
- Move login-, authentication- and authorisation-related sections to Sprout
  ([7b88127](https://github.com/seedcase-project/seedcase-sprout/commit/7b88127128953e749ec8dc525928f65964004d17))
- Format markdown files
  ([2fd8927](https://github.com/seedcase-project/seedcase-sprout/commit/2fd89276791a3aeeda894949a8456d0778a3d5de))
- Wrong url for users, fixed.
  ([a8a553c](https://github.com/seedcase-project/seedcase-sprout/commit/a8a553c0ae6a975aca9d285e13870248b10a681d))
- This sentence hadn't been finished
  ([01da305](https://github.com/seedcase-project/seedcase-sprout/commit/01da305ab91dbdf12f3b2f3569b3e85b89000a5c))
- Fix path to the wip include file
  ([41895a8](https://github.com/seedcase-project/seedcase-sprout/commit/41895a8494408d7b84b3c48effee906fa03927ed))
- Remove text about terms, better to refer to central location
  ([0216719](https://github.com/seedcase-project/seedcase-sprout/commit/0216719d7cce0b63a1bbf1911b165e1a35cdb149))
- Need an index landing page
  ([861a77b](https://github.com/seedcase-project/seedcase-sprout/commit/861a77b09688d24d535fa4d88e4fd381d559075b))
- Png -> svg
  ([5544c31](https://github.com/seedcase-project/seedcase-sprout/commit/5544c31280fd1d2910a62e7ebb44bbf750addbe4))
- Small edits to the license file
  ([05d7947](https://github.com/seedcase-project/seedcase-sprout/commit/05d7947263553340cb2af7915dee0bd8b34952f2))
- Add to sprout readme file
  ([885a52f](https://github.com/seedcase-project/seedcase-sprout/commit/885a52fb9bdeada1e4ee6926ffa0d782cb7be3c2))
- Add a description of the app
  ([63f0f60](https://github.com/seedcase-project/seedcase-sprout/commit/63f0f60deb9b20a89f4f833e68ab9fdae8269568))
- Move authentication, authorisation and login to Sprout
  [#467](https://github.com/seedcase-project/seedcase-sprout/pull/467)
  ([571bc95](https://github.com/seedcase-project/seedcase-sprout/commit/571bc95a1baa1af8d92ca031d50bef3704340bf6))
- Remove general naming style guide content, move to design repo
  ([792096d](https://github.com/seedcase-project/seedcase-sprout/commit/792096da793217a60aee60f39c501cd46ae3fcad))
- Small edits to intro section of naming scheme
  ([bc5091a](https://github.com/seedcase-project/seedcase-sprout/commit/bc5091ad3c38796a9b13ba20d02f2321cb67a371))
- Add naming scheme for output files/folders
  ([bcf7e0f](https://github.com/seedcase-project/seedcase-sprout/commit/bcf7e0f55233526a67351bba353f1808acb6fc33))
- Apply suggestions from review
  ([39b1d8a](https://github.com/seedcase-project/seedcase-sprout/commit/39b1d8acfcd250104d216b5f9a8342d5e4a44b89))
- Diagram of internal flow of creating a resource structure
  [#549](https://github.com/seedcase-project/seedcase-sprout/pull/549)
  ([2ffb1a6](https://github.com/seedcase-project/seedcase-sprout/commit/2ffb1a6ecb5c91dd4b7ecebbecf99a4731c303df))
- Description of core, external Python functions
  [#553](https://github.com/seedcase-project/seedcase-sprout/pull/553)
  ([f0ec298](https://github.com/seedcase-project/seedcase-sprout/commit/f0ec2984eac1e32d0b011f4e2c7ccd82267b9247))
- Diagram for flow of create resource properties
  [#556](https://github.com/seedcase-project/seedcase-sprout/pull/556)
  ([5759f49](https://github.com/seedcase-project/seedcase-sprout/commit/5759f49865103ac5da5ca8256bbe209e19663ddb))
- Major rewrite of the naming scheme to match frictionless
  [#546](https://github.com/seedcase-project/seedcase-sprout/pull/546)
  ([00ce79f](https://github.com/seedcase-project/seedcase-sprout/commit/00ce79f5946f80732cea00aa263666e20cfdc8df))
- Description of the app URLs and functionality
  [#555](https://github.com/seedcase-project/seedcase-sprout/pull/555)
  ([56e1556](https://github.com/seedcase-project/seedcase-sprout/commit/56e1556c30e5fae6c4d7ab5b50bb76ae4ff5f647))
- Sprout's output files and structure
  [#554](https://github.com/seedcase-project/seedcase-sprout/pull/554)
  ([9b24b68](https://github.com/seedcase-project/seedcase-sprout/commit/9b24b68c5837127147ea339412a1694b5fccae22))
- Get_resource_ids -> get_ids
  [#584](https://github.com/seedcase-project/seedcase-sprout/pull/584)
  ([2a8bd25](https://github.com/seedcase-project/seedcase-sprout/commit/2a8bd256009d09e20e3f6dc9f5467ca38d417356))
- Internal flow for `create_package_structure()`
  [#552](https://github.com/seedcase-project/seedcase-sprout/pull/552)
  ([ee800cd](https://github.com/seedcase-project/seedcase-sprout/commit/ee800cd7b2be9c6bd77b82842d813f0cd9639869))
- Update `create_resource_structure()` function diagram
  [#589](https://github.com/seedcase-project/seedcase-sprout/pull/589)
  ([75a4053](https://github.com/seedcase-project/seedcase-sprout/commit/75a4053f93ce2f9f6f02b07b13ad53353caf6344))
- Add extract action to naming scheme
  [#602](https://github.com/seedcase-project/seedcase-sprout/pull/602)
  ([9c0a8f7](https://github.com/seedcase-project/seedcase-sprout/commit/9c0a8f769c149e2110eccf8392e6a938594de92d))
- Description of the function to create the properties template
  [#599](https://github.com/seedcase-project/seedcase-sprout/pull/599)
  ([60fa11d](https://github.com/seedcase-project/seedcase-sprout/commit/60fa11d3e05a5f85166b3f5e1b49c982a53f8933))
- Restructure and reformat the function doc
  [#601](https://github.com/seedcase-project/seedcase-sprout/pull/601)
  ([c04dc6f](https://github.com/seedcase-project/seedcase-sprout/commit/c04dc6fb8e06ebc7ffd9619a5e1564a0783520ef))
- Include descriptions and details for the `path` functions
  [#606](https://github.com/seedcase-project/seedcase-sprout/pull/606)
  ([bcd701c](https://github.com/seedcase-project/seedcase-sprout/commit/bcd701c5fd1d79fe23d3695aaefb35e7b945c3ff))
- Diagram of internal code for `extract_resource_properties()`
  [#605](https://github.com/seedcase-project/seedcase-sprout/pull/605)
  ([71bee50](https://github.com/seedcase-project/seedcase-sprout/commit/71bee50af38a4449b3818fbb8f223dd06413dcac))
- Function diagram for `create_properties_template()`
  [#600](https://github.com/seedcase-project/seedcase-sprout/pull/600)
  ([85a3e29](https://github.com/seedcase-project/seedcase-sprout/commit/85a3e29329240d0c0bf066b17a5d33e27e6d97d5))
- Add description of `extract_resource_properties()`
  [#603](https://github.com/seedcase-project/seedcase-sprout/pull/603)
  ([497a42b](https://github.com/seedcase-project/seedcase-sprout/commit/497a42bfc7634d34eebf899be21d1a8801c84ff0))
- Add `extract_resources_properties()` diagram to post
  [#612](https://github.com/seedcase-project/seedcase-sprout/pull/612)
  ([7cb71c0](https://github.com/seedcase-project/seedcase-sprout/commit/7cb71c0945295dc81d18800e191a82fed8aca330))
- Start of guide to creating a package
  [#557](https://github.com/seedcase-project/seedcase-sprout/pull/557)
  ([68b20dd](https://github.com/seedcase-project/seedcase-sprout/commit/68b20dd884a47cd95cbd337b01050ba210ad4b3d))
- Update `create-resource-properties` diagram
  [#598](https://github.com/seedcase-project/seedcase-sprout/pull/598)
  ([f8a017c](https://github.com/seedcase-project/seedcase-sprout/commit/f8a017cfda437b4151d9fe62e770c80e8ca90f61))
- Update function name to `create_package_properties()`
  [#624](https://github.com/seedcase-project/seedcase-sprout/pull/624)
  ([1de9a79](https://github.com/seedcase-project/seedcase-sprout/commit/1de9a7999fee902cc286c65daa7a459ac56ccfe4))
- Fixed new paths for links in the docs
  ([b2a9e34](https://github.com/seedcase-project/seedcase-sprout/commit/b2a9e34580ba155c39e6074ada90c258dbb7d4e8))
- Add landing pages for each section
  ([f0deb27](https://github.com/seedcase-project/seedcase-sprout/commit/f0deb27a7a31616633e02867ded5022a287d495a))
- Make the function descriptions more compact and navigable
  [#666](https://github.com/seedcase-project/seedcase-sprout/pull/666)
  ([ee9a709](https://github.com/seedcase-project/seedcase-sprout/commit/ee9a709636fa4792c4aae9b1fe457a3358c36121))
- Ensure WIP callout is always default appearance
  [#668](https://github.com/seedcase-project/seedcase-sprout/pull/668)
  ([8c2e50f](https://github.com/seedcase-project/seedcase-sprout/commit/8c2e50f7a04b08a832d3b106af85f7bdf7a1636a))
- Split design docs up into two parts
  [#667](https://github.com/seedcase-project/seedcase-sprout/pull/667)
  ([262e5ad](https://github.com/seedcase-project/seedcase-sprout/commit/262e5ad46da3063ca0e556f3c842bfb71b9e3755))
- Functions to help create correct properties object
  [#665](https://github.com/seedcase-project/seedcase-sprout/pull/665)
  ([affc349](https://github.com/seedcase-project/seedcase-sprout/commit/affc3499c53fd3519788cf500b3116265477c445))
- Diagrams of internals for `path_sprout_root()`
  [#672](https://github.com/seedcase-project/seedcase-sprout/pull/672)
  ([3833e4e](https://github.com/seedcase-project/seedcase-sprout/commit/3833e4e80c5a311d4eb92edda7c1c8b5c50131de))
- Clarify the difference between descriptor and properties
  [#677](https://github.com/seedcase-project/seedcase-sprout/pull/677)
  ([b21a48c](https://github.com/seedcase-project/seedcase-sprout/commit/b21a48c6de7f5de66bc3793601cb211570a5fe2b))
- Internal flow for `create_package_properties()`
  [#664](https://github.com/seedcase-project/seedcase-sprout/pull/664)
  ([0ba7501](https://github.com/seedcase-project/seedcase-sprout/commit/0ba7501a20db703c4ca947081634b6fd459a3798))
- Remove `create_properties_template()`
  [#684](https://github.com/seedcase-project/seedcase-sprout/pull/684)
  ([b3efc97](https://github.com/seedcase-project/seedcase-sprout/commit/b3efc977b43b43040af6e08cb0a9e5a122e9e88f))
- Diagram of code flow for `path_*()` functions
  [#696](https://github.com/seedcase-project/seedcase-sprout/pull/696)
  ([dc35f2c](https://github.com/seedcase-project/seedcase-sprout/commit/dc35f2c8a2a8ffb898325dccc815cef94915fe0f))
- Replace with `create_properties_object()`
  [#686](https://github.com/seedcase-project/seedcase-sprout/pull/686)
  ([76f43fc](https://github.com/seedcase-project/seedcase-sprout/commit/76f43fc1fde333d3fb41ecdf45ff320776277a67))
- Expand on descriptions of path functions
  [#697](https://github.com/seedcase-project/seedcase-sprout/pull/697)
  ([c6bfb91](https://github.com/seedcase-project/seedcase-sprout/commit/c6bfb91847db170846b9259c767639709b0bc9c3))
- Revised section on properties to be only about the class
  [#691](https://github.com/seedcase-project/seedcase-sprout/pull/691)
  ([e8e1e63](https://github.com/seedcase-project/seedcase-sprout/commit/e8e1e63f9a6957ed9213a6c519b30c4ca3d452ba))
- Replace `view_*_template()` with `*Properties`
  [#702](https://github.com/seedcase-project/seedcase-sprout/pull/702)
  ([340c5f9](https://github.com/seedcase-project/seedcase-sprout/commit/340c5f92fe44db9b95e83370164892e2d1e8c016))
- Expand on usage guide for Properties class
  [#690](https://github.com/seedcase-project/seedcase-sprout/pull/690)
  ([517fb4b](https://github.com/seedcase-project/seedcase-sprout/commit/517fb4bbb8a59411732e72b2fd16ed0fa7d61560))
- Remove `create_package_properties()`, use `edit_*()` instead
  [#701](https://github.com/seedcase-project/seedcase-sprout/pull/701)
  ([32e1bfb](https://github.com/seedcase-project/seedcase-sprout/commit/32e1bfb50e593e1134705ec1754e8c4068eb3612))
- Internal flow diagram for `write_package_properties()`
  [#720](https://github.com/seedcase-project/seedcase-sprout/pull/720)
  ([1ae3d6f](https://github.com/seedcase-project/seedcase-sprout/commit/1ae3d6f7690ac02c09022266cc178aaee23902ed))
- Rename to `create_default_package_properties()`
  [#733](https://github.com/seedcase-project/seedcase-sprout/pull/733)
  ([342f415](https://github.com/seedcase-project/seedcase-sprout/commit/342f41595b0a9275cb551b08f95774be00b17fcf))
- Improve on the docstrings in `*Properties` classes
  [#718](https://github.com/seedcase-project/seedcase-sprout/pull/718)
  ([72a32b8](https://github.com/seedcase-project/seedcase-sprout/commit/72a32b803e42e09f776dc658c10deed49cd17a84))
- Diagram for `write_resource_data_to_raw()`
  [#721](https://github.com/seedcase-project/seedcase-sprout/pull/721)
  ([bec4fba](https://github.com/seedcase-project/seedcase-sprout/commit/bec4fba5777625577cbdb67bdee7cf380d305ce7))
- Description of split between core, cli, and app
  [#753](https://github.com/seedcase-project/seedcase-sprout/pull/753)
  ([c59ec5a](https://github.com/seedcase-project/seedcase-sprout/commit/c59ec5a57a74f4237615bfb854a5b03e6e821210))
- Internal diagram for `write_resource_properties()`
  [#751](https://github.com/seedcase-project/seedcase-sprout/pull/751)
  ([11d9f99](https://github.com/seedcase-project/seedcase-sprout/commit/11d9f99072a0a792ba60ebf0691cc05d6c0a0931))
- Add content to landing page
  [#772](https://github.com/seedcase-project/seedcase-sprout/pull/772)
  ([dcc98e7](https://github.com/seedcase-project/seedcase-sprout/commit/dcc98e7009883fa1f76f8e233b23a744de2a683d))
- Update readme
  [#778](https://github.com/seedcase-project/seedcase-sprout/pull/778)
  ([d303f4c](https://github.com/seedcase-project/seedcase-sprout/commit/d303f4c49d72b0c1195991af582c2501aaa15f7d))
- Installation guide on Sprout with pip
  [#765](https://github.com/seedcase-project/seedcase-sprout/pull/765)
  ([e3e6d27](https://github.com/seedcase-project/seedcase-sprout/commit/e3e6d2743d3d434e39cb7c32f2b9fc230f378923))
- Run Python code chunks in docs
  [#789](https://github.com/seedcase-project/seedcase-sprout/pull/789)
  ([1aa027c](https://github.com/seedcase-project/seedcase-sprout/commit/1aa027c4626fc569e76bf5a8359ad518a471a90a))
- Add logo and update header to match website
  [#799](https://github.com/seedcase-project/seedcase-sprout/pull/799)
  ([afa51de](https://github.com/seedcase-project/seedcase-sprout/commit/afa51dea94b99662ce4ef6805355aca12dffca82))
- Update code blocks in `packages` guide
  [#809](https://github.com/seedcase-project/seedcase-sprout/pull/809)
  ([3fcd3c0](https://github.com/seedcase-project/seedcase-sprout/commit/3fcd3c07ad9b99097f4925eb9843181f0973eeef))
- Update landing page with an image
  [#836](https://github.com/seedcase-project/seedcase-sprout/pull/836)
  ([05d9836](https://github.com/seedcase-project/seedcase-sprout/commit/05d98362036eb851ed075c0c3c230cea51b1e12c))
- Convert chunk to execute `edit_package_properties()`
  [#865](https://github.com/seedcase-project/seedcase-sprout/pull/865)
  ([09ff64e](https://github.com/seedcase-project/seedcase-sprout/commit/09ff64e70c171c4bc960f6cbfd9d0160faab3b30))

### 💄 Style

- Title-case headers
  ([d0b5ec8](https://github.com/seedcase-project/seedcase-sprout/commit/d0b5ec874965fe1f5d94d59b4a271bb9ed773413))
- Change variable names in footer to lower case
  ([0059ded](https://github.com/seedcase-project/seedcase-sprout/commit/0059ded4569f57198dba8f800c11b2bcfbc8e268))
- Ran Ruff styling
  ([5c7503e](https://github.com/seedcase-project/seedcase-sprout/commit/5c7503e44824e52b342790d4fa9fc33eb66641bc))
- Rearrange tables to be one table, summarized at the top
  ([0772f5b](https://github.com/seedcase-project/seedcase-sprout/commit/0772f5bfd71d71d81cb38cca272f5d4e2b9b250a))
- Format with ruff
  ([6927b0a](https://github.com/seedcase-project/seedcase-sprout/commit/6927b0ac93f95e47fb91c5a431303fe4157d7206))
- Remove blank line
  ([83ab38e](https://github.com/seedcase-project/seedcase-sprout/commit/83ab38ea3026b24e88fc354d4b9f8bf188452060))
- Add and remove blank lines
  ([51d8bbd](https://github.com/seedcase-project/seedcase-sprout/commit/51d8bbdceb3ec73b8d0a63a06e4b41eccfed70d8))
- Add comments
  ([0e795ae](https://github.com/seedcase-project/seedcase-sprout/commit/0e795aee761a54be5aacbbf037136134ba642d87))
- Add whitespace before table dialog
  ([a76ecf5](https://github.com/seedcase-project/seedcase-sprout/commit/a76ecf59231dc34e94ce33f9c607ec8a53d0addf))
- Change hyperlink colour to blue
  ([f9b1cec](https://github.com/seedcase-project/seedcase-sprout/commit/f9b1cec39651ac12e588c7225bef8531932dd030))
- Simplify comments
  ([5a5a286](https://github.com/seedcase-project/seedcase-sprout/commit/5a5a286c79145a0ce3856ec5c81e6240005babce))
- Rename val_table_does_not_exist to include *not*
  ([54051ac](https://github.com/seedcase-project/seedcase-sprout/commit/54051acfaa92cdf5af1bc5e997cff54553e506ff))
- Typehints, comments, and format
  ([8823183](https://github.com/seedcase-project/seedcase-sprout/commit/8823183f21aecb6f305e4651202b663cf4d9ac3f))
- Rename variable "name" to "name_value"
  ([2b9e57c](https://github.com/seedcase-project/seedcase-sprout/commit/2b9e57c064139fa5d5fcbbb9a31c5600de8c097a))
- Add whitespace
  ([027a034](https://github.com/seedcase-project/seedcase-sprout/commit/027a034cd0be40355140e6828a47ff2885543a85))
- Add empty line after docstrings
  ([d72823d](https://github.com/seedcase-project/seedcase-sprout/commit/d72823d8961d4a4e2922fc69e6013ccdc6fffa1a))
- Formatting and style of docstrings, ran ruff
  ([2a96e4a](https://github.com/seedcase-project/seedcase-sprout/commit/2a96e4acc5377e50c41a7520842769cdcff008c6))
- Use edit icon, not mobile icon
  ([c1fa659](https://github.com/seedcase-project/seedcase-sprout/commit/c1fa6597797fcdd2313919f2b35eb4e3803972e0))
- Small edits and styling to docstrings
  ([ac8f9ee](https://github.com/seedcase-project/seedcase-sprout/commit/ac8f9ee9503fdbceb455f087c50b203d73647bf4))
- Add . to docstring
  ([6f7790e](https://github.com/seedcase-project/seedcase-sprout/commit/6f7790e3d509d65d8acee317ef718b02684249f2))
- Use more natural language to describe error message.
  ([8156bd4](https://github.com/seedcase-project/seedcase-sprout/commit/8156bd4a5ec870da958814eff10c540e6216e843))
- Ran ruff formatting
  ([bf63159](https://github.com/seedcase-project/seedcase-sprout/commit/bf631595cb85a4c062f9eb51487591dc8f396cfe))
- Add max line length of 88
  ([b3eec10](https://github.com/seedcase-project/seedcase-sprout/commit/b3eec10adb9a5641b22d46995a3234c163d5ba6d))
- Double quotes around staticfiles to follow black formatting
  ([b0283d6](https://github.com/seedcase-project/seedcase-sprout/commit/b0283d6c4d89dfe6b5ed981323f70811d0262f04))
- Change icon from "edit" to "new_window"
  ([2d680e7](https://github.com/seedcase-project/seedcase-sprout/commit/2d680e7c4fafbcf941c2bed184b7551c7167cc40))
- Ruff adjustments
  ([5883179](https://github.com/seedcase-project/seedcase-sprout/commit/5883179bfe459cc6eeafb678ac7a01751a4767aa))
- Ruff format
  ([69568d7](https://github.com/seedcase-project/seedcase-sprout/commit/69568d7143eedb8af684e936d80d28defad876ee))
- Fix linter error
  ([f3d5670](https://github.com/seedcase-project/seedcase-sprout/commit/f3d5670d6cbf5985b084311333374b0652cc78d3))
- Use definition list HTML tags rather than "big" and "p"
  ([b233b22](https://github.com/seedcase-project/seedcase-sprout/commit/b233b22efccce02d0601478c52ab3e2227aa019f))
- Tried to change style of definition lists, but doesn't work
  ([48b7df1](https://github.com/seedcase-project/seedcase-sprout/commit/48b7df11254e3e614bc5c0853de427982a331dbb))
- Shorten msg variable name so ruff line length passes
  ([f02a690](https://github.com/seedcase-project/seedcase-sprout/commit/f02a6902ba4d78a80854f27fc934bc54b52972fe))
- Align variable naming: metadata -> existing_metadata
  ([17fda76](https://github.com/seedcase-project/seedcase-sprout/commit/17fda76ccc0081d9049980e47972226ca3fbe4ee))
- Add comments for clarity
  ([c9f0b3c](https://github.com/seedcase-project/seedcase-sprout/commit/c9f0b3c30015b51acca6cbd9f435c56310acf1c7))
- Ran Quarto reformatter on text
  ([9d3df37](https://github.com/seedcase-project/seedcase-sprout/commit/9d3df370749bbad5669beefd974e2b5578e1970f))
- Rename template, view, url to `project id metadata view`
  ([a3b89e1](https://github.com/seedcase-project/seedcase-sprout/commit/a3b89e11211a1221819b43df7e7f4876e21fce72))
- Align naming of urls to kebab case
  ([fb4a7ca](https://github.com/seedcase-project/seedcase-sprout/commit/fb4a7ca7dd15d4a2e55e84f07adc082b17b02413))
- Enforce column width in docs
  ([9cef9df](https://github.com/seedcase-project/seedcase-sprout/commit/9cef9dfd3c0ab6d77b08121d80f486a3dc5a0385))
- .. along with some changes to the wording in the help dialog in column-review
  ([bf954b6](https://github.com/seedcase-project/seedcase-sprout/commit/bf954b6ee49a4af6f41b48c621a06f0fdf19606a))
- For longer header's, include a `...` to keep it on the card
  ([522bc8e](https://github.com/seedcase-project/seedcase-sprout/commit/522bc8eb040bbc26908bb76683c491ec7febc889))
- Reformat changes
  ([7abe481](https://github.com/seedcase-project/seedcase-sprout/commit/7abe481de37e52d2a18594da02323d2065250e9d))
- Align to use querySelector at all relevent lines
  ([80a729e](https://github.com/seedcase-project/seedcase-sprout/commit/80a729eaf1301673cf913965d0a877dd6d81fe36))
- Format
  ([a2803a6](https://github.com/seedcase-project/seedcase-sprout/commit/a2803a69f6786a53f9658596ae511cdc1159a9b0))
- Update comments and change single quotes to double quotes
  ([7b5f37b](https://github.com/seedcase-project/seedcase-sprout/commit/7b5f37bcc630c3797dd822d915d0dee7b9d829ff))
- Add whitespace around django variables to follow Django conventions
  ([78355cc](https://github.com/seedcase-project/seedcase-sprout/commit/78355cca83aca56ef9abad159873faa30265c967))
- For clarity, change JS variable name from col_no to column_number
  ([5fabf5c](https://github.com/seedcase-project/seedcase-sprout/commit/5fabf5c151b8bee8b6cc542af23c45ec32741666))
- Use more generic text for file zone button, ie "upload"
  ([16c3919](https://github.com/seedcase-project/seedcase-sprout/commit/16c391937458b4a373ac4a8a67a17c9ab880832c))
- Use lowercase for file-zone text and use code text for .csv text
  ([aa8d7d9](https://github.com/seedcase-project/seedcase-sprout/commit/aa8d7d900ed851612bae34d2e0206f7e4a9fa40b))
- Ran HTML formatter
  ([7b863c4](https://github.com/seedcase-project/seedcase-sprout/commit/7b863c4fb0b4f3f9146ba23d74e525f686c0ac52))
- Reformat html filess
  ([f9d0ab2](https://github.com/seedcase-project/seedcase-sprout/commit/f9d0ab2019b00be2dbeb218cf6d7c163828bae7a))
- Reformat using Django Template Support extension
  ([b51d68a](https://github.com/seedcase-project/seedcase-sprout/commit/b51d68a317374b7f0281d39864a68c2a0f101444))
- Move navigation bar content into base
  ([0adb6a9](https://github.com/seedcase-project/seedcase-sprout/commit/0adb6a96285cc88ccf508c9143df5a842a82b51a))
- Small renaming of object to match it's purpose
  ([c89591b](https://github.com/seedcase-project/seedcase-sprout/commit/c89591b988f949ecb3300e8ff81c9ae84af137ec))
- Format column width
  ([ef3550d](https://github.com/seedcase-project/seedcase-sprout/commit/ef3550dfe5152a981656b62d91678de51a490d96))
- Add theme colours based on ui wireframes and homepage look
  ([0844030](https://github.com/seedcase-project/seedcase-sprout/commit/0844030798356987f40f7c23ec86dd9509004834))
- Remove extra blank line
  ([9e89e62](https://github.com/seedcase-project/seedcase-sprout/commit/9e89e622d4a11b1536fe12b240373a4150f0f442))
- Apply styled table-content class to view with tables
  ([2120370](https://github.com/seedcase-project/seedcase-sprout/commit/212037095a8cdc074096e3aaffa3be5e417d0520))
- Add tertiary color to use as border of column metadata table
  ([e797b90](https://github.com/seedcase-project/seedcase-sprout/commit/e797b90ba0dea45f758a8e38be72aa53bad3f980))
- Style column metadata table background colour to be white
  ([6b0ea7a](https://github.com/seedcase-project/seedcase-sprout/commit/6b0ea7aceb4d361e3e2e6ec400d9dd7ea94032c1))
- Add solid border to buttons
  ([83b36d4](https://github.com/seedcase-project/seedcase-sprout/commit/83b36d487737c7ff934967eb6dd041db211921f4))
- Add theme background colour to columns table
  ([c991f80](https://github.com/seedcase-project/seedcase-sprout/commit/c991f80ffe83743314e9803f4c9a45009279cc0a))
- Add rounded corners of first and last td in table rows
  ([cc78865](https://github.com/seedcase-project/seedcase-sprout/commit/cc78865afc1c55344ef66f868a894bad51c531be))
- Adding background to navigation bar
  ([3c74355](https://github.com/seedcase-project/seedcase-sprout/commit/3c7435589c24b2eedf15b81992b8c94b508c8101))
- Rename "table-content" to "primary-table"
  ([288f647](https://github.com/seedcase-project/seedcase-sprout/commit/288f6477c99b4bda05a8feed997e4355ae2371d1))
- Add "secondary-table" class and add styling to this class'
  ([7a97b94](https://github.com/seedcase-project/seedcase-sprout/commit/7a97b9464e5add89c22f2cecb99d7905630b399a))
- For clarify, update dict tag function name to include "dict"
  ([a7b3bc7](https://github.com/seedcase-project/seedcase-sprout/commit/a7b3bc7ee7946e8c8851bb55258219fd9238a86d))
- Align to use queryselector in js
  ([677f672](https://github.com/seedcase-project/seedcase-sprout/commit/677f6726dab3e64643875109a3d898aa1284ecf0))
- Add whitespaces in js
  ([a056054](https://github.com/seedcase-project/seedcase-sprout/commit/a0560549a79861b4932aaeb59fe06d2e862f8fdd))
- Remove border from transparent buttons
  ([7fd7614](https://github.com/seedcase-project/seedcase-sprout/commit/7fd76144b623c39f7f9885456588936cfe48de9c))
- Change navbar icon colours to match logo
  ([b3109b5](https://github.com/seedcase-project/seedcase-sprout/commit/b3109b56d25e11a52111a269be553137b054e3d2))
- Add padding around img tags to create space around logo in navbar
  ([ec2e331](https://github.com/seedcase-project/seedcase-sprout/commit/ec2e33128a101a77c22b5e728e5478799c68466f))
- Remove transparent style from dialog buttons
  ([af72f15](https://github.com/seedcase-project/seedcase-sprout/commit/af72f15e87e7b99e3ef880409822a33fb11adb85))
- Fix sizing of the logo, it was a bit too big
  ([154d202](https://github.com/seedcase-project/seedcase-sprout/commit/154d202e43be1e59c94f9732f58c8840238dd192))
- Set a lighter background colour for dialog boxes
  ([b2ab87e](https://github.com/seedcase-project/seedcase-sprout/commit/b2ab87e99a358bfbfb964c5264a3d0971fac2c93))
- Remove "fill" class from ? button to fit with new colour theme
  ([f095cee](https://github.com/seedcase-project/seedcase-sprout/commit/f095cee2a197dd2b04e7b79f49cc57b04af34982))
- Fix sizing of the logo and small nav bar fixes
  [#412](https://github.com/seedcase-project/seedcase-sprout/pull/412)
  ([05fb1b2](https://github.com/seedcase-project/seedcase-sprout/commit/05fb1b20c7e5d0d0156f9b096818272a4aeaa0f8))
- Reformat HTML only, added newline to end of file
  ([61f691d](https://github.com/seedcase-project/seedcase-sprout/commit/61f691daa08bebf80a5b6762b987fe230e67a720))
- Add seedcase-theme website style
  ([1ebede9](https://github.com/seedcase-project/seedcase-sprout/commit/1ebede90ef3953f1adf1957e4bc3b924f06f6fe9))
- Add theme colours based on ui wireframes and homepage look
  [#398](https://github.com/seedcase-project/seedcase-sprout/pull/398)
  ([d93443d](https://github.com/seedcase-project/seedcase-sprout/commit/d93443dc9263948e2324cd805f0f3d777428b704))
- Using divs instead of table to allow more flexibility in design
  ([56828e7](https://github.com/seedcase-project/seedcase-sprout/commit/56828e7bf8601bd098c72d3643488482930d6bf4))
- Using divs instead of table to allow more flexibility in design
  [#408](https://github.com/seedcase-project/seedcase-sprout/pull/408)
  ([694232d](https://github.com/seedcase-project/seedcase-sprout/commit/694232d49483a803fe392fcfa7a330d0eb951f6d))
- Small stylistic edits and to be consistent across diagrams
  ([3c633b4](https://github.com/seedcase-project/seedcase-sprout/commit/3c633b45ce27e32396a082b26d814778cce4fc50))
- Add vars secondary-container and on-secondary-container in sprout colours
  ([48dfe2c](https://github.com/seedcase-project/seedcase-sprout/commit/48dfe2c05ea3857ef3fceffc4aac6756d44db779))
- Add green outline to segmentated buttons
  ([cb84f66](https://github.com/seedcase-project/seedcase-sprout/commit/cb84f6652e151ea67a0be31f8661592d2449ac05))
- Remove inline styling and decrease header size
  ([4e8cd4a](https://github.com/seedcase-project/seedcase-sprout/commit/4e8cd4a99611795394dadc330d8ec36af3f3f8ff))
- Add spacing for dl tags
  ([9b4c372](https://github.com/seedcase-project/seedcase-sprout/commit/9b4c3729c9f5334b602693d6002bf0ac230bdbef))
- Move dd HTML items to the right a bit, so the dt hangs over them
  ([62c1c04](https://github.com/seedcase-project/seedcase-sprout/commit/62c1c04300ebe1c9700d60e59b8793e4a0a4e6e0))
- This line was too long
  ([b1b20da](https://github.com/seedcase-project/seedcase-sprout/commit/b1b20dadea85f1d3634768e9d073a43d85c18039))
- Ran ruff formatter
  ([4294fb0](https://github.com/seedcase-project/seedcase-sprout/commit/4294fb06fa66dcae318e4cbbf7d856d32a3a3c5b))
- Run just format-python
  [#608](https://github.com/seedcase-project/seedcase-sprout/pull/608)
  ([c894119](https://github.com/seedcase-project/seedcase-sprout/commit/c8941199ec93d2cd488cba03c113dead1fa63434))
- Ran ruff formatter
  ([85283c9](https://github.com/seedcase-project/seedcase-sprout/commit/85283c9b4b9e811c5550b2db65aac647a5dfb5cb))
- Indent multiline class attribute docstrings correctly
  [#737](https://github.com/seedcase-project/seedcase-sprout/pull/737)
  ([c38afad](https://github.com/seedcase-project/seedcase-sprout/commit/c38afadc04146f71530dd703ba71a93efa3c600a))
- Remove unused import
  [#747](https://github.com/seedcase-project/seedcase-sprout/pull/747)
  ([7044fd4](https://github.com/seedcase-project/seedcase-sprout/commit/7044fd4bb92549e2c27baeca2ebfefb215cee3c0))
- Move WIP header into Quarto config, rather than as own file
  [#760](https://github.com/seedcase-project/seedcase-sprout/pull/760)
  ([8b53832](https://github.com/seedcase-project/seedcase-sprout/commit/8b538324d2d535708e7bc7f8ec6fea341f057b1d))
- Use updated theme divs in landing page
  [#787](https://github.com/seedcase-project/seedcase-sprout/pull/787)
  ([e381541](https://github.com/seedcase-project/seedcase-sprout/commit/e381541c930c0ba378d79147f3701b6e1a8545c5))
- Ran pre-commit, only fixes trailing whitespaces and end of file newlines
  [#828](https://github.com/seedcase-project/seedcase-sprout/pull/828)
  ([0f45ab1](https://github.com/seedcase-project/seedcase-sprout/commit/0f45ab143116ac0f544a04a9b66ed67a63303c4a))

### 🧪 Tests

- Adding fixture sample
  ([a23be6a](https://github.com/seedcase-project/seedcase-sprout/commit/a23be6a903df39e3894f12cfd0d7db555d134c8b))
- Tablemetadataform validation tests
  ([27045f0](https://github.com/seedcase-project/seedcase-sprout/commit/27045f02d9507fd15ad7f5b00386aea3adf2b541))
- Add for validators special character and table exists
  ([cd12f3e](https://github.com/seedcase-project/seedcase-sprout/commit/cd12f3ed1f5e3cdc5c1042c404362f81500ed9d6))
- Update tests with new error message for no_special_characters validator
  ([ae759be](https://github.com/seedcase-project/seedcase-sprout/commit/ae759be8f473944098cacbda6edd0b36d6b670d5))
- Add a test that checks for an invalid form
  ([db8cdc0](https://github.com/seedcase-project/seedcase-sprout/commit/db8cdc0066458efc75fd3c7b7c91d07e0ef4fd1c))
- Added test that already existed
  ([8598015](https://github.com/seedcase-project/seedcase-sprout/commit/8598015bcae32952045dd7b458ec3ac2ee9d24a6))
- Tests are updated
  ([852a011](https://github.com/seedcase-project/seedcase-sprout/commit/852a01159f4509fe5593bbe0c124215ec258f422))
- Tests was not committed
  ([669d933](https://github.com/seedcase-project/seedcase-sprout/commit/669d9336f98d76bb51e672bd0921b0557ad6c9d3))
- Add tests for \_convert_to_snake_case
  ([5fce586](https://github.com/seedcase-project/seedcase-sprout/commit/5fce586df2207a74d50b09570fe957668d6fd485))
- A test was added
  ([e45ce55](https://github.com/seedcase-project/seedcase-sprout/commit/e45ce554d20104668342e53fd8f4e722f7a0affa))
- Updated the tests with the URL to the correct location
  ([541b044](https://github.com/seedcase-project/seedcase-sprout/commit/541b0445a496bf93cab5d77cbd9b12c9a6a3da27))
- Test for `upload_raw_file()` function.
  ([f8116a2](https://github.com/seedcase-project/seedcase-sprout/commit/f8116a296fda836804894b634c7e2e9f88401eac))
- Test is added for happy path
  ([c5b1b15](https://github.com/seedcase-project/seedcase-sprout/commit/c5b1b158e8fe2d602105621a16729f5789babdd4))
- Adding test for another csv format
  ([045c950](https://github.com/seedcase-project/seedcase-sprout/commit/045c950c3fd2239d8da9e81a28e118d7b02df64b))
- Update tests to use True/False instead
  ([d9aeb71](https://github.com/seedcase-project/seedcase-sprout/commit/d9aeb71deed3b2099df5850ab6b073d383d00262))
- Add basic tests of rendering and all tables shown in view
  ([488e2ce](https://github.com/seedcase-project/seedcase-sprout/commit/488e2cec6ad0ed9a2e7f55d894664836d3c8f8a4))
- Add failing tests supposed to check whether page redirects correctly
  ([70dc49c](https://github.com/seedcase-project/seedcase-sprout/commit/70dc49cbedcc3b4d9eb460f1f78583c18c75442b))
- Update button upload and selected row test - still fails
  ([7a53245](https://github.com/seedcase-project/seedcase-sprout/commit/7a5324575610c698de2afcb93be690aafb3f029d))
- Add setUp
  ([44ccb71](https://github.com/seedcase-project/seedcase-sprout/commit/44ccb71590cf66929465e0ec823c1843df0d9395))
- Fix and format redirects_with_button_upload_and_selected_row
  ([7184dee](https://github.com/seedcase-project/seedcase-sprout/commit/7184deec2147d9d39587fd2fae8e4a6b76ce31ed))
- Rename to `metadata_view` to fix failing tests
  ([42849ee](https://github.com/seedcase-project/seedcase-sprout/commit/42849ee6dc3866ec8febbe05af6093d3730105fe))
- Bad name is_not_running_unit_tests
  ([2bc1cac](https://github.com/seedcase-project/seedcase-sprout/commit/2bc1cacda862e2f8b54f7ed15e870c9c2ff298f1))
- Test is adjusted to ensure the correct file and columns are uploaded
  ([ddfbb80](https://github.com/seedcase-project/seedcase-sprout/commit/ddfbb805700604f5229a74ca8db48fdf25850eb7))
- Add tests of dialog from data-import to metadata-view
  ([4d4e168](https://github.com/seedcase-project/seedcase-sprout/commit/4d4e1689372577953eab00135819ed76801ee23b))
- Ensure column names are actually converted
  ([45341c5](https://github.com/seedcase-project/seedcase-sprout/commit/45341c5841af8810e334205d4e9738cbe9d76ff8))
- Used wrong url for tests, should match the name in Django's `path()`
  ([b9735c0](https://github.com/seedcase-project/seedcase-sprout/commit/b9735c0db3a1b882516bc2830147a9977bef61a9))
- Updated test
  ([b3effe4](https://github.com/seedcase-project/seedcase-sprout/commit/b3effe449bcdd625cb570d259c65bc248c651cc9))
- Used wrong URL in tests.
  ([1222d60](https://github.com/seedcase-project/seedcase-sprout/commit/1222d60e1589ad62c75dcd0c1881a4e2d05be8f6))
- Fix issues with URLs and paths in tests after renaming
  ([4c06221](https://github.com/seedcase-project/seedcase-sprout/commit/4c0622123ad6127a02c248e548f6276def39d12d))
- This should have been lowercase, previous change capitalized it.
  ([487a8ef](https://github.com/seedcase-project/seedcase-sprout/commit/487a8efb8d536c7cf98f5996726b2e2b221b3bbe))
- Update test with new redirect to projects-id-metadata-view
  ([e255da4](https://github.com/seedcase-project/seedcase-sprout/commit/e255da40dd11dc4d75c2f4450272a8e30cf04ee1))
- Split modified_at test on creation and save into two tests
  ([7a74a1e](https://github.com/seedcase-project/seedcase-sprout/commit/7a74a1ed32bc7606aeded8d0139823a6e45e4b10))
- Add test of data rows count on creation
  ([31a827d](https://github.com/seedcase-project/seedcase-sprout/commit/31a827d5806d360f27021d4bcf5b67aade3b2d4c))
- Add tests of data upload on creation and update to data rows
  ([bce3f7a](https://github.com/seedcase-project/seedcase-sprout/commit/bce3f7a3abd459363a0669ed4ab989a4020093b4))
- Comment out failing test, since we might delete this HTML form anyway
  ([1ac67ca](https://github.com/seedcase-project/seedcase-sprout/commit/1ac67ca20a17ea4748976ad1adf3af7b214f8122))
- Remove left over Django test file
  ([d70647a](https://github.com/seedcase-project/seedcase-sprout/commit/d70647ade40c27218fbcab8df5de2e2ea13aa4c7))
- Fix test failures after Django removal
  [#870](https://github.com/seedcase-project/seedcase-sprout/pull/870)
  ([ece4bb4](https://github.com/seedcase-project/seedcase-sprout/commit/ece4bb4f7ea9bbdf66c274d6ab795a3a4f185285))

### 👷 CI/CD

- Resolve merge integration with fly.io's deployment, plus add some items from
  review
  ([8c98945](https://github.com/seedcase-project/seedcase-sprout/commit/8c9894595a6066c9ea6314be73f6a678d2e0c5de))
- Small edits to testing action
  ([7543463](https://github.com/seedcase-project/seedcase-sprout/commit/7543463a381d12e15d64e9bf526b9a90d35203ea))
- Add some extra steps to test CI
  ([7ab6874](https://github.com/seedcase-project/seedcase-sprout/commit/7ab68745bf81b8838af1520da50fd536b2a4eccc))
- Deploy pull-requests to seedcase-sprout-pr
  ([d5b8025](https://github.com/seedcase-project/seedcase-sprout/commit/d5b802501646ec3145759ffe093046c9658d1338))
- Use fly preview-pr-apps action
  ([c9f4266](https://github.com/seedcase-project/seedcase-sprout/commit/c9f42664ddddac877ff6afabf756200df3ed281d))
- Set the default name to the fly preview
  ([8adfbc5](https://github.com/seedcase-project/seedcase-sprout/commit/8adfbc5bdcb07a34a6436ae02b77914bfa9faeaf))
- Using the flyio preview action, so reverting to previous action
  ([5d5a377](https://github.com/seedcase-project/seedcase-sprout/commit/5d5a3778f34b364ab5bf9796558c07d75478f1fe))
- Remove these duplicate files, since they were renamed in central .github repo
  ([c425c59](https://github.com/seedcase-project/seedcase-sprout/commit/c425c59c6ed26c20335cecb000b8b8c090907003))
- These are now reusable actions, so don't need them in this repo anymore
  ([b6b5e04](https://github.com/seedcase-project/seedcase-sprout/commit/b6b5e04c4f37cd125a69983318eeb035896d9790))
- Add token that gives permission to write (delete) environments
  ([38818e5](https://github.com/seedcase-project/seedcase-sprout/commit/38818e574b1f414e57ebe45b6498e1193497ca85))
- Add Action to build and deploy the docs website
  ([cb209e4](https://github.com/seedcase-project/seedcase-sprout/commit/cb209e4119e1c9e468ffad6a7c8d4a0e50320108))
- Use the reusable action instead
  ([3e1739b](https://github.com/seedcase-project/seedcase-sprout/commit/3e1739b1a17dc0b325f91c7d3521fe9f6155d775))
- No longer need this workflow
  ([13b8e97](https://github.com/seedcase-project/seedcase-sprout/commit/13b8e97b0aefb1385622683a5d3d545f7d156d27))

### 🧱 Build system

- *(deps)* Bump ruff from 0.4.10 to 0.5.0
  [#492](https://github.com/seedcase-project/seedcase-sprout/pull/492)
  ([c0ed6bc](https://github.com/seedcase-project/seedcase-sprout/commit/c0ed6bc94c0cf26a44c83eaea10a7c82f86c37a2))
- Start using poetry
  ([801f784](https://github.com/seedcase-project/seedcase-sprout/commit/801f7840ad0b64a86a5a007cdbb54d0389791c17))
- Set up basic files for Django project.
  ([824192b](https://github.com/seedcase-project/seedcase-sprout/commit/824192b6bef3c35ae595284cceb9d86c2a83c312))
- Set up start of a Django app
  ([de34208](https://github.com/seedcase-project/seedcase-sprout/commit/de3420886945c1bf2bc83f3c762a005a18b82b61))
- Mostly updates to pyproject to configure Poetry more.
  ([ef7d04c](https://github.com/seedcase-project/seedcase-sprout/commit/ef7d04c694ffc1624dfdec02849511d20be48fc1))
- Add Ruff to poetry lock file
  ([a9c1dde](https://github.com/seedcase-project/seedcase-sprout/commit/a9c1ddeaf84e58c149bf4affff3da0deb2c84eca))
- Setup Fly.io settings and configuration files
  ([9a682b7](https://github.com/seedcase-project/seedcase-sprout/commit/9a682b77e1e7eb94cb36fbbf730947be2dd340b8))
- Be consistent with port, use 8000 in docker compose
  ([1b92408](https://github.com/seedcase-project/seedcase-sprout/commit/1b92408f799937a881af642af536aff09e24ccf3))
- Have a lint (no-fix) just recipe, and include lint (fix) in format recipe
  ([7896628](https://github.com/seedcase-project/seedcase-sprout/commit/7896628e48bbad811c01865609ea95f6325e7765))
- Add just recipe to install dependencies with poetry
  ([36fa9b5](https://github.com/seedcase-project/seedcase-sprout/commit/36fa9b5ef63dd9a6d30343d8e0d42be5cd4945e6))
- I accidentally changed this to the wrong value, should be app
  ([4269412](https://github.com/seedcase-project/seedcase-sprout/commit/42694122f6b291d838d62f12725370c97e74a097))
- Setup Quarto website build for the docs
  ([8269ebd](https://github.com/seedcase-project/seedcase-sprout/commit/8269ebd89ea057a5c43f22507c16965560e3e823))
- Extension to incorporate a glossary to the website
  ([32edacb](https://github.com/seedcase-project/seedcase-sprout/commit/32edacb8082b24b4f3b35c28d8a9751bea80e71e))
- Set Fly option so it doesn't turn off too fast
  ([c5ae0d6](https://github.com/seedcase-project/seedcase-sprout/commit/c5ae0d6b9a5f8039bb5f8d7e2203527b4196b13b))
- Add pytest as a dependency via poetry
  ([45ccc3a](https://github.com/seedcase-project/seedcase-sprout/commit/45ccc3a54414ca19e42fd6bfec2a9861b14d2f28))
- Upgrade ruff and move it as a dev dependency
  ([4c50d81](https://github.com/seedcase-project/seedcase-sprout/commit/4c50d8112b18765e274079efc357225c3c678302))
- Make pytest aware of django settings
  ([a3ab770](https://github.com/seedcase-project/seedcase-sprout/commit/a3ab770785ac9dc06bfa218b4d7dcc484fc82fa1))
- Switch just recipe to use pytest
  ([e42ac78](https://github.com/seedcase-project/seedcase-sprout/commit/e42ac781c6acc379c196de7dee0800e31864d952))
- Install packages in 'edit' mode so it is easier to test and develop
  ([17c1018](https://github.com/seedcase-project/seedcase-sprout/commit/17c1018ff542be0296f9afad77373c16c75589a8))
- Fix link to fixtures after moving things around
  ([eebaacc](https://github.com/seedcase-project/seedcase-sprout/commit/eebaacc4f28f98e1b6ff5e2eb94f83d297e9a8d9))
- Add pytest and rearrange tests to make use of pytest
  [#524](https://github.com/seedcase-project/seedcase-sprout/pull/524)
  ([7abfb53](https://github.com/seedcase-project/seedcase-sprout/commit/7abfb53f2296a61c7e42657327e1933c796043f2))
- Add frictionless with sql to dependencies
  [#544](https://github.com/seedcase-project/seedcase-sprout/pull/544)
  ([6787b54](https://github.com/seedcase-project/seedcase-sprout/commit/6787b549ccf7f9a0fdf038b18e8f0da8e39cd734))
- Major restructure of deps plus upgrade to python3.12
  ([a7dae0d](https://github.com/seedcase-project/seedcase-sprout/commit/a7dae0d3f93e12103b4cc1b9057a9fd5de80f303))
- Bump Python version to 3.12 in Dockerfile
  ([d5974f1](https://github.com/seedcase-project/seedcase-sprout/commit/d5974f17681723242ebcfe69b87e38b4aa6873a5))
- Add django dependencies to poetry install
  ([c343fb2](https://github.com/seedcase-project/seedcase-sprout/commit/c343fb29eefe91c350c861fa59da571ea876bd6f))
- Major restructure of deps plus upgrade to python3.12
  [#611](https://github.com/seedcase-project/seedcase-sprout/pull/611)
  ([d013ac4](https://github.com/seedcase-project/seedcase-sprout/commit/d013ac4681f42835edc124af0513e1061670c55b))
- Add quartodoc infrastructure
  [#818](https://github.com/seedcase-project/seedcase-sprout/pull/818)
  ([aecd5dc](https://github.com/seedcase-project/seedcase-sprout/commit/aecd5dc86a9bb95a9c8e5b5317ae209f826f8b24))
- Update poetry lock file
  ([3c5c162](https://github.com/seedcase-project/seedcase-sprout/commit/3c5c162dcb6657e457cb9d577b9bc4b5c5c694f7))

### 🧹 Chores

- *(sync)* Synced local '.github/pull_request_template.md' with remote
  '.github/pull_request_template.md'
  ([a520c3d](https://github.com/seedcase-project/seedcase-sprout/commit/a520c3df546890b6a13b407e3ca56ad7cbddd466))
- *(sync)* Synced local '.github/pull_request_template.md' with remote
  'common/templates/software-pull-request.md'
  ([331f4fe](https://github.com/seedcase-project/seedcase-sprout/commit/331f4fe66c04f7691b66c95a9f6ee6285dff109b))
- *(sync)* Synced file(s) with seedcase-project/.github
  [#496](https://github.com/seedcase-project/seedcase-sprout/pull/496)
  ([61f7c42](https://github.com/seedcase-project/seedcase-sprout/commit/61f7c4284c14d041e78f74b6006c02e063092766))
- *(sync)* Synced local '.github/pull_request_template.md' with remote
  '.github/pull_request_template.md'
  ([d74c1e4](https://github.com/seedcase-project/seedcase-sprout/commit/d74c1e48338797d30204f2ee79f214ddc3e3e762))
- *(sync)* Synced local '.github/dependabot.yml' with remote
  'common/actions/dependabot.yml'
  ([6cb11a5](https://github.com/seedcase-project/seedcase-sprout/commit/6cb11a5e5410d247dcce467445ce84cfa0766326))
- *(sync)* Synced local '.github/workflows/deploy-pr-preview.yml' with remote
  'common/actions/deploy-pr-preview.yml'
  ([2098376](https://github.com/seedcase-project/seedcase-sprout/commit/20983765aa2b49ee6a39a30ff59789db4e988f56))
- *(sync)* Synced local '.github/pull_request_template.md' with remote
  'common/templates/software-pull-request.md'
  ([04f693e](https://github.com/seedcase-project/seedcase-sprout/commit/04f693e4073fb5c016d3bdef492e41b04838cab0))
- *(sync)* Synced local '.github/pull_request_template.md' with remote
  '.github/pull_request_template.md'
  ([2f24654](https://github.com/seedcase-project/seedcase-sprout/commit/2f24654eea97478fe4e3e5ffc4d6f6fd023111d9))
- *(sync)* Synced local 'justfile' with remote 'common/justfile/django'
  ([7bfc346](https://github.com/seedcase-project/seedcase-sprout/commit/7bfc34631b56087495438d5d04841c31918f9716))
- *(sync)* Synced local '.github/pull_request_template.md' with remote
  'common/templates/software-pull-request.md'
  ([f3e6a80](https://github.com/seedcase-project/seedcase-sprout/commit/f3e6a80d37276b59956215721089cd27d575c76e))
- *(sync)* Synced file(s) with seedcase-project/.github
  [#525](https://github.com/seedcase-project/seedcase-sprout/pull/525)
  ([c6492ac](https://github.com/seedcase-project/seedcase-sprout/commit/c6492ace11cfe860147ed24b9e244640061b38b8))
- *(sync)* Synced local '.vscode/settings.json' with remote
  '.vscode/settings.json'
  ([7eacb15](https://github.com/seedcase-project/seedcase-sprout/commit/7eacb1573aadb2b2e9c75303ef2cb499cbeb1233))
- *(sync)* Synced local '.github/pull_request_template.md' with remote
  '.github/pull_request_template.md'
  ([a14ec08](https://github.com/seedcase-project/seedcase-sprout/commit/a14ec08f140c978258bffd5306243b9087b1ea06))
- *(sync)* Synced local '.github/pull_request_template.md' with remote
  'common/templates/software-pull-request.md'
  ([be82c6a](https://github.com/seedcase-project/seedcase-sprout/commit/be82c6add17a9c57f326aad064b445e4f65510ef))
- *(sync)* Synced local '.vscode/google-notypes.mustache' with remote
  '.vscode/google-notypes.mustache'
  ([dfd8d8f](https://github.com/seedcase-project/seedcase-sprout/commit/dfd8d8ffec4288cc2a59d4855d56257b65fdb377))
- *(sync)* Synced local '.vscode/extensions.json' with remote
  '.vscode/extensions.json'
  ([e68ed12](https://github.com/seedcase-project/seedcase-sprout/commit/e68ed12af246db30e0da253c3138af70c6da4f37))
- *(sync)* Synced local '.gitignore' with remote '.gitignore'
  ([51afdb1](https://github.com/seedcase-project/seedcase-sprout/commit/51afdb17ebb62e8f117507ef5fb9da9cc565e30f))
- *(sync)* Synced local '.github/pull_request_template.md' with remote
  '.github/pull_request_template.md'
  ([df776c1](https://github.com/seedcase-project/seedcase-sprout/commit/df776c1d3bddce71b3a8e471c402faa54db2dea7))
- *(sync)* Synced local '.github/workflows/' with remote '.github/workflows/'
  ([b749f26](https://github.com/seedcase-project/seedcase-sprout/commit/b749f2650c6708bf054c94bca071756330be5b64))
- *(sync)* Synced local '.vscode/' with remote '.vscode/'
  ([3d3b99c](https://github.com/seedcase-project/seedcase-sprout/commit/3d3b99cdc62376e7a7f37def4970edd17f545b97))
- *(sync)* Synced file(s) with seedcase-project/template-python-project
  [#693](https://github.com/seedcase-project/seedcase-sprout/pull/693)
  ([900a087](https://github.com/seedcase-project/seedcase-sprout/commit/900a087cbacb07150e712ea1920f8edcfc10e5ad))
- *(sync)* Synced local 'justfile' with remote 'justfile'
  ([61541f3](https://github.com/seedcase-project/seedcase-sprout/commit/61541f31a7daa6610c0271872e67988ddb291206))
- *(sync)* Synced local '.gitignore' with remote '.gitignore'
  ([d4e7740](https://github.com/seedcase-project/seedcase-sprout/commit/d4e77400ad56ba8b21d9fa240ce5a2ac1704df8e))
- *(sync)* Synced local '.github/workflows/' with remote '.github/workflows/'
  ([1094acf](https://github.com/seedcase-project/seedcase-sprout/commit/1094acfa35e230dcfd541b50031519481fa39eeb))
- *(sync)* Synced file(s) with seedcase-project/template-python-project
  [#749](https://github.com/seedcase-project/seedcase-sprout/pull/749)
  ([954ec59](https://github.com/seedcase-project/seedcase-sprout/commit/954ec59141b0ff9ce2e2bbe9843dccb1d5cdb266))
- *(sync)* Synced file(s) with seedcase-project/seedcase-theme
  ([d47b72f](https://github.com/seedcase-project/seedcase-sprout/commit/d47b72fc9613cf61d2b56fec2a9aef97dd96cd7f))
- *(sync)* Synced file(s) with seedcase-project/seedcase-theme
  [#771](https://github.com/seedcase-project/seedcase-sprout/pull/771)
  ([e62355d](https://github.com/seedcase-project/seedcase-sprout/commit/e62355daf50d5823aa703ed56e9c2fd1c5f50dd7))
- *(sync)* Synced local '\_extensions/seedcase-project/seedcase-theme/' with
  remote '\_extensions/seedcase-theme/'
  ([e47fc52](https://github.com/seedcase-project/seedcase-sprout/commit/e47fc52d18796a35e79eef37a2e47e3c9ed29c77))
- *(sync)* Synced file(s) with seedcase-project/template-python-project
  [#779](https://github.com/seedcase-project/seedcase-sprout/pull/779)
  ([a48f5cb](https://github.com/seedcase-project/seedcase-sprout/commit/a48f5cbf67e45e3a49fd9d5b03ee0a4260660343))
- *(sync)* Synced local '\_extensions/seedcase-project/seedcase-theme/' with
  remote '\_extensions/seedcase-theme/'
  ([f0fa4d0](https://github.com/seedcase-project/seedcase-sprout/commit/f0fa4d04a20b7e5f9fdda53e674608171e01d64d))
- *(sync)* Created local '404.qmd' from remote '404.qmd'
  ([1a4165c](https://github.com/seedcase-project/seedcase-sprout/commit/1a4165c78752681bc7062e1f22613d6c3549d751))
- *(sync)* Synced local '\_extensions/seedcase-project/seedcase-theme/' with
  remote '\_extensions/seedcase-theme/'
  ([259f04f](https://github.com/seedcase-project/seedcase-sprout/commit/259f04f273979655ff49318d54c622737607dab1))
- *(sync)* Synced local 'justfile' with remote 'justfile'
  ([be757fb](https://github.com/seedcase-project/seedcase-sprout/commit/be757fb3097d97841c46f3f0d53009d39d878c59))
- *(sync)* Synced local '.github/workflows/' with remote '.github/workflows/'
  ([2012ccd](https://github.com/seedcase-project/seedcase-sprout/commit/2012ccd8a211258304eed1310d3ec87956e60f8f))
- *(sync)* Synced local '.gitignore' with remote '.gitignore'
  ([9e310d8](https://github.com/seedcase-project/seedcase-sprout/commit/9e310d86bddcac5dc788d7cd129f35ba38414910))
- *(sync)* Synced local '.vscode/' with remote '.vscode/'
  ([d93f836](https://github.com/seedcase-project/seedcase-sprout/commit/d93f836d7ab349ccaa63201a985dedc3c4b9234e))
- *(sync)* Synced local '\_extensions/seedcase-project/seedcase-theme/' with
  remote '\_extensions/seedcase-theme/'
  ([7fe96d0](https://github.com/seedcase-project/seedcase-sprout/commit/7fe96d03069c0deffe1dbb6c38a077c5907c6234))
- *(sync)* Synced local '\_extensions/seedcase-project/seedcase-theme/' with
  remote '\_extensions/seedcase-theme/'
  ([5a7beed](https://github.com/seedcase-project/seedcase-sprout/commit/5a7beed39b86a407828b4a3f199da38b15f7cb5a))
- *(sync)* Synced local '.gitignore' with remote '.gitignore'
  ([0b6db14](https://github.com/seedcase-project/seedcase-sprout/commit/0b6db14709040a849fddf1189d026278d7bd871e))
- *(sync)* Synced local 'justfile' with remote 'justfile'
  ([46775c0](https://github.com/seedcase-project/seedcase-sprout/commit/46775c07931b5406c92663688f19f500115e4638))
- *(sync)* Synced local '.gitignore' with remote '.gitignore'
  ([b2501ba](https://github.com/seedcase-project/seedcase-sprout/commit/b2501baefd2263471249427ad0fe920180a2df03))
- *(sync)* Synced local 'justfile' with remote 'justfile'
  ([d3ac2bc](https://github.com/seedcase-project/seedcase-sprout/commit/d3ac2bcabe992aefa1f86b766946d823d2c21944))
- *(sync)* Synced local '\_extensions/seedcase-project/seedcase-theme/' with
  remote '\_extensions/seedcase-theme/'
  ([ea3a703](https://github.com/seedcase-project/seedcase-sprout/commit/ea3a703f4fa69fd05774ba02a9814fb196087653))
- *(sync)* Created local '\_extensions/debruine/' from remote
  '\_extensions/debruine/'
  ([177972c](https://github.com/seedcase-project/seedcase-sprout/commit/177972cf2c79c9831ba6411d53f545793d4c50a9))
- *(sync)* Synced local '.pre-commit-config.yaml' with remote
  '.pre-commit-config.yaml'
  ([9218dc3](https://github.com/seedcase-project/seedcase-sprout/commit/9218dc3ae8c8f5eb0a315074ffe5ac5af9edfb5a))
- *(sync)* Synced local '.vscode/' with remote '.vscode/'
  ([f4f4eba](https://github.com/seedcase-project/seedcase-sprout/commit/f4f4ebae33e2cac9deff7a5fd21ede4e8807c4e8))
- *(sync)* Synced local '.gitignore' with remote '.gitignore'
  ([234206b](https://github.com/seedcase-project/seedcase-sprout/commit/234206be403398eac1028e4048355d4c0423b70d))
- *(sync)* Synced local 'justfile' with remote 'justfile'
  ([fcbeddc](https://github.com/seedcase-project/seedcase-sprout/commit/fcbeddcb64e8d713e5b1cdab57b708113b0e6225))
- *(sync)* Created local '.cz.toml' from remote '.cz.toml'
  ([6ab287e](https://github.com/seedcase-project/seedcase-sprout/commit/6ab287e1202c4642528a7eac2bbff335fc047453))
- *(sync)* Synced local 'ruff.toml' with remote 'ruff.toml'
  ([79a1e23](https://github.com/seedcase-project/seedcase-sprout/commit/79a1e23649f08a8099680358aae2e6156dffb02b))
- *(sync)* Synced local '.github/workflows/' with remote '.github/workflows/'
  ([1fef859](https://github.com/seedcase-project/seedcase-sprout/commit/1fef859ed522e4cb22aec34040ae40116db38969))
- *(sync)* Synced local '.vscode/' with remote '.vscode/'
  ([8013dd3](https://github.com/seedcase-project/seedcase-sprout/commit/8013dd3fc8bfb49571a622da029faba6a09c61da))
- *(sync)* Synced local '.github/workflows/' with remote '.github/workflows/'
  ([b16c3ba](https://github.com/seedcase-project/seedcase-sprout/commit/b16c3bae1022ea96f4218f3c95d24ea872c5278b))
- *(sync)* Synced local '.github/workflows/' with remote '.github/workflows/'
  ([ecf476d](https://github.com/seedcase-project/seedcase-sprout/commit/ecf476d386f62f3f5c6562b2a5fe789640a26cab))
- Create custom conventional branch names to use.
  ([605c4a8](https://github.com/seedcase-project/seedcase-sprout/commit/605c4a89de41f20589852c1f91503d0ba9344277))
- Don't need sprout nor v1 in filename
  ([c24e0b6](https://github.com/seedcase-project/seedcase-sprout/commit/c24e0b6ffef8208623e6d4f42470ef1b8d67d19d))
- Remove spout and v1 from text inside files
  ([b5134ce](https://github.com/seedcase-project/seedcase-sprout/commit/b5134ceeb2cbada9033ac2719eeea5dde9d10c83))
- Small edits to text
  ([2cd0e72](https://github.com/seedcase-project/seedcase-sprout/commit/2cd0e72dd56af74ea16dfdaf9044e37022bbefb8))
- Add pngs of sequence diagrams so @henrik-goul can access them more easily
  ([78284c9](https://github.com/seedcase-project/seedcase-sprout/commit/78284c9fa1ddee7ed87470f698114dd30058581f))
- Update user flow diagram after discussion with @K-Beicher
  ([90fe212](https://github.com/seedcase-project/seedcase-sprout/commit/90fe21235812bef9bc15cb090c1d3d3870f4e345))
- Update user flow diagram based on discussions with @K-Beicher
  ([c6ee607](https://github.com/seedcase-project/seedcase-sprout/commit/c6ee6078239b844bd3c4e914e63a596233ca8a08))
- Renmae user flow files and minor edits based on review from @lwjohnst86
  ([dce11d0](https://github.com/seedcase-project/seedcase-sprout/commit/dce11d03f64a47f4f5775cd61ded39e390bc0081))
- Redo title to avoid /
  ([5e8d647](https://github.com/seedcase-project/seedcase-sprout/commit/5e8d6472e90294b19ab707ede7731630ac909797))
- Add pngs from updated pumls
  ([e7a5b3f](https://github.com/seedcase-project/seedcase-sprout/commit/e7a5b3f61acb22888fd5ee5944a2c13c28b3ebc6))
- Add TODO tags to these files so we know to fix them later.
  ([025cdc6](https://github.com/seedcase-project/seedcase-sprout/commit/025cdc6b66c31212e574f823871d9a1fd3feaab1))
- Remove leftover file, not needed anymore
  ([6370f28](https://github.com/seedcase-project/seedcase-sprout/commit/6370f28d7e3ad4b21fc6f2ab3cb7f497576e76b3))
- Remove obsolete noqa F401 comments
  ([48cfac1](https://github.com/seedcase-project/seedcase-sprout/commit/48cfac1dcc8c06ab14fb40405f352347a1cf8b00))
- Renamed folder to the more accurate name 'config'
  ([c90d57d](https://github.com/seedcase-project/seedcase-sprout/commit/c90d57d2c9bc23337f4c75b4db7d7ef24762563f))
- Update links to use config instead
  ([a890de0](https://github.com/seedcase-project/seedcase-sprout/commit/a890de0c1dbd86b311dc813eb9e7afe2d27eaa04))
- Renamed app folder to sprout, which is clearer on the purpose of it
  ([5f40231](https://github.com/seedcase-project/seedcase-sprout/commit/5f40231b02d8733e7d92d7861d29aa0992bf92a8))
- Small TODO item to look into later.
  ([b439346](https://github.com/seedcase-project/seedcase-sprout/commit/b4393461b3c08367ba8fcc3cb5d7f60763d1992e))
- Fix name of test file to match function name change
  ([fe6dc27](https://github.com/seedcase-project/seedcase-sprout/commit/fe6dc279e654affa1114a064eaa6dd4d4989c5d7))
- VS Code doesn't pick up venv of Poetry, so set it to the repo
  ([464949f](https://github.com/seedcase-project/seedcase-sprout/commit/464949f9c49f89b1af3404e8d60f004e9da985ef))
- Add MIT license keyword to `pyproject.toml` file
  ([4717c75](https://github.com/seedcase-project/seedcase-sprout/commit/4717c75eb59cbc7e5fde896c8526f9d9d02db218))
- Keep css style within it's own file
  ([27f6661](https://github.com/seedcase-project/seedcase-sprout/commit/27f666176f665c95d93efd433cb35b174e3d81c9))
- Don't need this file anymore
  ([5119849](https://github.com/seedcase-project/seedcase-sprout/commit/5119849d2a325cbe6c8299d3b816d20484649690))
- Revise file name to match naming scheme
  ([df932d2](https://github.com/seedcase-project/seedcase-sprout/commit/df932d2494b43ce40300f1fc76be8302372ff5af))
- Rename files and functions to match naming scheme
  ([d2af536](https://github.com/seedcase-project/seedcase-sprout/commit/d2af53698168d7a2e95f819654cbd9bd026bbdfc))
- Silly typo in file name, oops
  ([8ec19b9](https://github.com/seedcase-project/seedcase-sprout/commit/8ec19b9d5c8b2bd41a58a9db140f6976d020df56))
- Fix paths in URLs
  ([ffb5670](https://github.com/seedcase-project/seedcase-sprout/commit/ffb5670f46091f370ce91fe11946e5000231532b))
- Move base.html to includes folder
  ([e118767](https://github.com/seedcase-project/seedcase-sprout/commit/e118767d443184e56437525361a1ca1622c8e2cd))
- Rename home to index
  ([5ba7e58](https://github.com/seedcase-project/seedcase-sprout/commit/5ba7e58e2864b161e8326406fd4298f6fc068cec))
- Rename file to match naming scheme (project-id-view)
  ([7a162e5](https://github.com/seedcase-project/seedcase-sprout/commit/7a162e51869f228096baf73d9e87b6164e613b14))
- Rename Python view file to `project_id_view`
  ([c16b9e6](https://github.com/seedcase-project/seedcase-sprout/commit/c16b9e67b1ba012178c67fab9bc969fc74cf6a7f))
- Rename HTML template file to `project-id-data-id-metadata-edit-grid`
  ([3900762](https://github.com/seedcase-project/seedcase-sprout/commit/390076206fcd34cf34e53856f3cb237413b0e297))
- Rename view to match template
  ([bc2fb5d](https://github.com/seedcase-project/seedcase-sprout/commit/bc2fb5d30db9978c742e26fe6c8d1d14dfbc9bad))
- Matching naming scheme, metadata edit (table style)
  ([398731b](https://github.com/seedcase-project/seedcase-sprout/commit/398731b870bef3dba2f9c21ffd9855b71a6850ec))
- Move includes into own includes folder
  ([2b61980](https://github.com/seedcase-project/seedcase-sprout/commit/2b61980e59945c05bf1abcafddfa501c35683332))
- Rename to naming scheme for data/id/metadata/create
  ([4171db9](https://github.com/seedcase-project/seedcase-sprout/commit/4171db9f4dc4e9417bd0567d0b9a96e7ac4d1b9f))
- Rename file to match scheme for data/id/metadata/edit/table
  ([d8128b1](https://github.com/seedcase-project/seedcase-sprout/commit/d8128b1f8f86b81846b5f7022764776f6a7c0994))
- Match scheme for Python view file, for data/id/metadata/create
  ([3edf97b](https://github.com/seedcase-project/seedcase-sprout/commit/3edf97b9951c89155313d970b57725a7e9ecca4f))
- Project to projects naming, typo
  ([6b1b3e3](https://github.com/seedcase-project/seedcase-sprout/commit/6b1b3e3ccf2a39af82044a02f7692440b0ee74bb))
- Projects from project, typo
  ([e4c659a](https://github.com/seedcase-project/seedcase-sprout/commit/e4c659accb191e6e660652b2181d23b8dcb204d0))
- Rename tests to match naming scheme
  ([b0a473e](https://github.com/seedcase-project/seedcase-sprout/commit/b0a473efa469da72e539a491fc2125f75bce92f9))
- Accidentally committed this WIP file, append with `_` to indicate WIP status
  ([3002e30](https://github.com/seedcase-project/seedcase-sprout/commit/3002e30cd70779fbc834b3b4137dae7dfde2d0fe))
- Rename based on using metadata first
  ([893e0c4](https://github.com/seedcase-project/seedcase-sprout/commit/893e0c42753b96ec12b89b2da5f66576a80f0ef4))
- Remove this leftover file
  ([6fdbf9d](https://github.com/seedcase-project/seedcase-sprout/commit/6fdbf9d8f0f5361d96422dfc75b741adcc581c86))
- Fix link to base.html
  ([fe2ae9d](https://github.com/seedcase-project/seedcase-sprout/commit/fe2ae9d3f4fe85303bb03094b9ae486d94fcaec6))
- Fix links based on naming scheme
  ([a13f1ad](https://github.com/seedcase-project/seedcase-sprout/commit/a13f1adcb10a32a661a92b9e8d0d4068822164df))
- Forgot to rename this file
  ([3c33681](https://github.com/seedcase-project/seedcase-sprout/commit/3c3368124011d581ae02ed9d73bd1814fadbc76e))
- Fix naming of URLs in tests
  ([b23d421](https://github.com/seedcase-project/seedcase-sprout/commit/b23d421cc6920f43a35f60529a1879186750f537))
- Rename file to use plural projects
  ([2eb1e76](https://github.com/seedcase-project/seedcase-sprout/commit/2eb1e76ca442c06b5052ff98a35a6d751db09115))
- Moved data files into data repo
  ([31150e3](https://github.com/seedcase-project/seedcase-sprout/commit/31150e3beeeb0c3563184e32a46be83f7bbe5789))
- Rename data type files to match naming scheme
  ([9a2e21e](https://github.com/seedcase-project/seedcase-sprout/commit/9a2e21e07b64ec59b5e5add418e52d89f63ed841))
- Rename files to match naming scheme for the Columns model
  ([ecd9a89](https://github.com/seedcase-project/seedcase-sprout/commit/ecd9a8952ab250953ed405f4e9eb74188d839f07))
- Rename files for Files model to match naming scheme
  ([24164ee](https://github.com/seedcase-project/seedcase-sprout/commit/24164ee7127c5079862a9c9fd184ac3b639eca14))
- Rename files related to Tables model based on naming scheme
  ([bf32f1b](https://github.com/seedcase-project/seedcase-sprout/commit/bf32f1b857bda857393fe684c0091f61be7c8767))
- Changed project_id to projects_id in file paths
  ([e471635](https://github.com/seedcase-project/seedcase-sprout/commit/e471635462975d2e6da02199e05a909f55436e9f))
- Generated puml images
  ([1043669](https://github.com/seedcase-project/seedcase-sprout/commit/104366929d3295937aff64d181bd0f11ee910b0b))
- Regenerated puml images
  ([e5b7ac1](https://github.com/seedcase-project/seedcase-sprout/commit/e5b7ac10a5952662a01eb12757f00e871c6c629e))
- Regenerate the puml images
  ([171d4c4](https://github.com/seedcase-project/seedcase-sprout/commit/171d4c448ae023985ef84f2a54cf83c41172be16))
- Rename file to better reflect content
  ([252707a](https://github.com/seedcase-project/seedcase-sprout/commit/252707af51f7f50fdd7021cfa289bf8b5ab4759c))
- Don't include title in navbar
  ([0f454f1](https://github.com/seedcase-project/seedcase-sprout/commit/0f454f1e87cffd9590fb7108a244e1d3b74abe34))
- Keep title in website html header, but not navbar.
  ([5bca58d](https://github.com/seedcase-project/seedcase-sprout/commit/5bca58dc28066a6db291d9e1cebfd25c466c2e84))
- Move wip note to includes folder
  ([8244444](https://github.com/seedcase-project/seedcase-sprout/commit/82444441db536a11ffa7ac665b07441b0b25177c))
- This file is in the teams repo now
  ([168149a](https://github.com/seedcase-project/seedcase-sprout/commit/168149a791dc3f8fef9a25f55fdf9bc57a9bac2e))
- Follow Quarto's assumed Git root is website root, so we don't fight their
  config
  ([ebb76be](https://github.com/seedcase-project/seedcase-sprout/commit/ebb76bec6d59838d79c41d3aa51ef9aafe21f709))
- Don't need this gitignore file anymore
  ([1316227](https://github.com/seedcase-project/seedcase-sprout/commit/1316227efa204d5f4edd3de2f3105fdfea8b0f5f))
- Add Quarto files to docker ignore file
  ([054b3ff](https://github.com/seedcase-project/seedcase-sprout/commit/054b3ffbff76d3ca251c45ef31ebfe211058bc89))
- Don't need this extension (yet?)
  ([e5c9c92](https://github.com/seedcase-project/seedcase-sprout/commit/e5c9c929538ea60a1b219fab4aedb88cbcf851e9))
- These are duplicates already in the favicon folder
  ([8972ac8](https://github.com/seedcase-project/seedcase-sprout/commit/8972ac8ad2180171ba787872c15fd68c6e2fcf01))
- Footer is now in the extension theme
  ([65c2c3c](https://github.com/seedcase-project/seedcase-sprout/commit/65c2c3c5307fc9c3d04c39eeef96a835fe17a34d))
- Move tests to root folder and follow pytest `test_` prefix requirement
  ([99c2ff8](https://github.com/seedcase-project/seedcase-sprout/commit/99c2ff8ade83e46b514af88b0c0a7f0a0f673c4a))
- Make VSCode aware of using pytest to be able to run integrated testing tools
  ([b5c5a5d](https://github.com/seedcase-project/seedcase-sprout/commit/b5c5a5d9220e3c20a3199dd69e74a1f358ab6c66))
- Add test debug config that allows debugging external files
  ([c752bf3](https://github.com/seedcase-project/seedcase-sprout/commit/c752bf3c8790d0bf1934653f0cf03dd9fdc3397a))
- Add sprout to included packages in `pyproject.toml`
  [#538](https://github.com/seedcase-project/seedcase-sprout/pull/538)
  ([db519ee](https://github.com/seedcase-project/seedcase-sprout/commit/db519ee2c01bc912d8c6d47eb7f6d307c0447576))
- Keep only relevant design docs on website
  [#547](https://github.com/seedcase-project/seedcase-sprout/pull/547)
  ([e41a69a](https://github.com/seedcase-project/seedcase-sprout/commit/e41a69a5c603b91baa9fbb6f9aba6607bc436ae2))
- This describes the app pages, not functions, so renamed them
  [#548](https://github.com/seedcase-project/seedcase-sprout/pull/548)
  ([1b954bd](https://github.com/seedcase-project/seedcase-sprout/commit/1b954bd200e064b0f3273aba562de4bda1df5ed2))
- Organize images into their own folders
  [#604](https://github.com/seedcase-project/seedcase-sprout/pull/604)
  ([d12e468](https://github.com/seedcase-project/seedcase-sprout/commit/d12e468592ecb807e8916208c8ca77d0ff73d654))
- Add Marton to the `pyproject.toml` file
  ([a4cdbae](https://github.com/seedcase-project/seedcase-sprout/commit/a4cdbaec6806e6cae1c3c203e56cea7a3e2858bc))
- Limit functions accessible when importing all
  [#626](https://github.com/seedcase-project/seedcase-sprout/pull/626)
  ([64b7241](https://github.com/seedcase-project/seedcase-sprout/commit/64b724141907bbb592406553566e4a751549425b))
- Moved files into architecture vs implementation
  ([7ac54e8](https://github.com/seedcase-project/seedcase-sprout/commit/7ac54e84f10dcba8f9bc95fbbd9247a14e317eb9))
- Split design content into two sections with sidebar
  ([51cd804](https://github.com/seedcase-project/seedcase-sprout/commit/51cd804ac5e539cafe17187456c155313af5984a))
- Convert guide landing page to listing with each guide entry
  [#763](https://github.com/seedcase-project/seedcase-sprout/pull/763)
  ([3199259](https://github.com/seedcase-project/seedcase-sprout/commit/3199259d85bd2988a3cd4686b540045ca7547b9e))
- Move callout block to own file and use include instead
  [#762](https://github.com/seedcase-project/seedcase-sprout/pull/762)
  ([6f1c6d0](https://github.com/seedcase-project/seedcase-sprout/commit/6f1c6d0b871a3df4ad9bd19ae0e5a03f7275988f))
- Add sprout logo as landing page image
  [#775](https://github.com/seedcase-project/seedcase-sprout/pull/775)
  ([1c12764](https://github.com/seedcase-project/seedcase-sprout/commit/1c127646795922fe509688f34c53ac9ff4ab0e4e))
- Add glossary path and set pop-up settings
  [#829](https://github.com/seedcase-project/seedcase-sprout/pull/829)
  ([36e6e65](https://github.com/seedcase-project/seedcase-sprout/commit/36e6e65ec53711fcdd18233aa6184b98e9f85de0))
- Add pre-commit config with commit linting
  [#827](https://github.com/seedcase-project/seedcase-sprout/pull/827)
  ([7503462](https://github.com/seedcase-project/seedcase-sprout/commit/75034624335b647417eb6677e4b673ba646e0b28))
- Update link to glossary
  [#840](https://github.com/seedcase-project/seedcase-sprout/pull/840)
  ([b84ba4b](https://github.com/seedcase-project/seedcase-sprout/commit/b84ba4bb764ac31c3f58d5375e56c6b0ba08ddd6))
- Need to end in semicolon
  [#842](https://github.com/seedcase-project/seedcase-sprout/pull/842)
  ([8ec8252](https://github.com/seedcase-project/seedcase-sprout/commit/8ec825298fc8d524fdb08c65353eee76add7917e))
- Remove left over app storage folder
  ([52e3f51](https://github.com/seedcase-project/seedcase-sprout/commit/52e3f51a6719f0871a8d9e75d72456ed8fbf76b4))
