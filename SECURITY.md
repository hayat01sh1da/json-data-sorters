# Security Policy

## Supported Versions

- Only the latest version on `master` receives fixes.
- Sample JSON datasets are considered fixtures; security fixes target the
	sorting utilities themselves.

## Ecosystem & Compatibility

| Component            | Version(s) / Tooling            | Notes |
| -------------------- | ------------------------------ | ----- |
| OS baseline          | WSL (Ubuntu 24.04.3 LTS)       | Shared across Ruby and Python implementations. |
| Ruby sorter          | Ruby 4.0.1 (`.ruby-version`)   | Uses Ruby stdlib (`JSON`, `FileUtils`). Declare extra gems if introduced. |
| Python sorter        | CPython 3.14.2 (`.python-version`) | Uses Python stdlib (`json`, `argparse`). Add `requirements.txt` for third-party modules. |

## Backward Compatibility

- Sorting behavior and CLI options remain stable for Ruby 4.0.x / Python 3.14.x
	environments. Any key-order changes will be communicated via release notes.
- Earlier interpreter majors or alternative JSON engines are not supported and
	will not receive security fixes.

## Reporting a Vulnerability

Please disclose vulnerabilities privately:

1. Use GitHub’s **Security → Report a vulnerability** flow (preferred).
2. Alternatively, email `security@project.org` with sample payloads, sort order
	 (`asc`/`desc`), and reproduction steps.

We acknowledge within **3 business days** and provide updates at least every
**7 business days** until remediation or closure.
