## Supported Versions

- Only the latest version on `master` receives fixes.
- Sample JSON datasets are considered fixtures; security fixes target the sorting utilities themselves.

## Ecosystem & Compatibility

| Component     | Version(s) / Tooling               | Notes                                                                                    |
| ------------- | ---------------------------------- | ---------------------------------------------------------------------------------------- |
| OS baseline   | WSL (Ubuntu 25.10)                 | Shared environment across tracks.                                                        |
| Ruby sorter   | Ruby 4.0.3 (`.ruby-version`)       | Uses Ruby stdlib (`JSON`, `FileUtils`). Declare extra gems if introduced.                |
| Python sorter | CPython 3.14.4 (`.python-version`) | Uses Python stdlib (`json`, `argparse`). Add `requirements.txt` for third-party modules. |

## Backward Compatibility

- Sorting behavior and CLI options remain stable for Ruby 4.0.x / Python 3.14.x environments. Any key-order changes will be communicated via release notes.
- Earlier interpreter majors or alternative JSON engines are not supported and will not receive security fixes.

## Reporting a Vulnerability

## Reporting a Vulnerability

Please report issues privately via **GitHub Security Advisory** (preferred) — open through the repository’s **Security → Report a vulnerability** workflow.

Acknowledgement occurs and status updates follow as soon as possible.  
After remediation we publish guidance alongside required dependency updates.
