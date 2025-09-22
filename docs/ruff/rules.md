[Skip to content](https://docs.astral.sh/ruff/rules/#rules)

# [Rules](https://docs.astral.sh/ruff/rules/\#rules)

**Ruff supports over 800 lint rules**, many of which are inspired by popular tools like Flake8,
isort, pyupgrade, and others. Regardless of the rule's origin, Ruff re-implements every rule in
Rust as a first-party feature.

By default, Ruff enables Flake8's `F` rules, along with a subset of the `E` rules, omitting any
stylistic rules that overlap with the use of a formatter, like `ruff format` or
[Black](https://github.com/psf/black).

If you're just getting started with Ruff, **the default rule set is a great place to start**: it
catches a wide variety of common errors (like unused imports) with zero configuration.

## [Legend](https://docs.astral.sh/ruff/rules/\#legend)

    🧪     The rule is unstable and is in ["preview"](https://docs.astral.sh/ruff/faq/#what-is-preview).

    ⚠️     The rule has been deprecated and will be removed in a future release.

    ❌     The rule has been removed only the documentation is available.

    🛠️     The rule is automatically fixable by the `--fix` command-line option.

All rules not marked as preview, deprecated or removed are stable.

## [Airflow (AIR)](https://docs.astral.sh/ruff/rules/\#airflow-air)

For more, see [Airflow](https://pypi.org/project/apache-airflow/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| AIR001 | [airflow-variable-name-task-id-mismatch](https://docs.astral.sh/ruff/rules/airflow-variable-name-task-id-mismatch/) | Task variable name should match the `task_id`: "{task\_id}" |  |
| AIR002 | [airflow-dag-no-schedule-argument](https://docs.astral.sh/ruff/rules/airflow-dag-no-schedule-argument/) | DAG should have an explicit `schedule` argument | 🧪 |
| AIR301 | [airflow3-removal](https://docs.astral.sh/ruff/rules/airflow3-removal/) | `{deprecated}` is removed in Airflow 3.0 | 🧪🛠️ |
| AIR302 | [airflow3-moved-to-provider](https://docs.astral.sh/ruff/rules/airflow3-moved-to-provider/) | `{deprecated}` is removed in Airflow 3.0 | 🧪🛠️ |
| AIR311 | [airflow3-suggested-update](https://docs.astral.sh/ruff/rules/airflow3-suggested-update/) | `{deprecated}` is removed in Airflow 3.0; It still works in Airflow 3.0 but is expected to be removed in a future version. | 🧪🛠️ |
| AIR312 | [airflow3-suggested-to-move-to-provider](https://docs.astral.sh/ruff/rules/airflow3-suggested-to-move-to-provider/) | `{deprecated}` is removed in Airflow 3.0 | 🧪🛠️ |

## [eradicate (ERA)](https://docs.astral.sh/ruff/rules/\#eradicate-era)

For more, see [eradicate](https://pypi.org/project/eradicate/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| ERA001 | [commented-out-code](https://docs.astral.sh/ruff/rules/commented-out-code/) | Found commented-out code |  |

## [FastAPI (FAST)](https://docs.astral.sh/ruff/rules/\#fastapi-fast)

For more, see [FastAPI](https://pypi.org/project/fastapi/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| FAST001 | [fast-api-redundant-response-model](https://docs.astral.sh/ruff/rules/fast-api-redundant-response-model/) | FastAPI route with redundant `response_model` argument | 🛠️ |
| FAST002 | [fast-api-non-annotated-dependency](https://docs.astral.sh/ruff/rules/fast-api-non-annotated-dependency/) | FastAPI dependency without `Annotated` | 🛠️ |
| FAST003 | [fast-api-unused-path-parameter](https://docs.astral.sh/ruff/rules/fast-api-unused-path-parameter/) | Parameter `{arg_name}` appears in route path, but not in `{function_name}` signature | 🛠️ |

## [flake8-2020 (YTT)](https://docs.astral.sh/ruff/rules/\#flake8-2020-ytt)

For more, see [flake8-2020](https://pypi.org/project/flake8-2020/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| YTT101 | [sys-version-slice3](https://docs.astral.sh/ruff/rules/sys-version-slice3/) | `sys.version[:3]` referenced (python3.10), use `sys.version_info` |  |
| YTT102 | [sys-version2](https://docs.astral.sh/ruff/rules/sys-version2/) | `sys.version[2]` referenced (python3.10), use `sys.version_info` |  |
| YTT103 | [sys-version-cmp-str3](https://docs.astral.sh/ruff/rules/sys-version-cmp-str3/) | `sys.version` compared to string (python3.10), use `sys.version_info` |  |
| YTT201 | [sys-version-info0-eq3](https://docs.astral.sh/ruff/rules/sys-version-info0-eq3/) | `sys.version_info[0] == 3` referenced (python4), use `>=` |  |
| YTT202 | [six-py3](https://docs.astral.sh/ruff/rules/six-py3/) | `six.PY3` referenced (python4), use `not six.PY2` |  |
| YTT203 | [sys-version-info1-cmp-int](https://docs.astral.sh/ruff/rules/sys-version-info1-cmp-int/) | `sys.version_info[1]` compared to integer (python4), compare `sys.version_info` to tuple |  |
| YTT204 | [sys-version-info-minor-cmp-int](https://docs.astral.sh/ruff/rules/sys-version-info-minor-cmp-int/) | `sys.version_info.minor` compared to integer (python4), compare `sys.version_info` to tuple |  |
| YTT301 | [sys-version0](https://docs.astral.sh/ruff/rules/sys-version0/) | `sys.version[0]` referenced (python10), use `sys.version_info` |  |
| YTT302 | [sys-version-cmp-str10](https://docs.astral.sh/ruff/rules/sys-version-cmp-str10/) | `sys.version` compared to string (python10), use `sys.version_info` |  |
| YTT303 | [sys-version-slice1](https://docs.astral.sh/ruff/rules/sys-version-slice1/) | `sys.version[:1]` referenced (python10), use `sys.version_info` |  |

## [flake8-annotations (ANN)](https://docs.astral.sh/ruff/rules/\#flake8-annotations-ann)

For more, see [flake8-annotations](https://pypi.org/project/flake8-annotations/) on PyPI.

For related settings, see [flake8-annotations](https://docs.astral.sh/ruff/settings/#lintflake8-annotations).

| Code | Name | Message |  |
| --- | --- | --- | --- |
| ANN001 | [missing-type-function-argument](https://docs.astral.sh/ruff/rules/missing-type-function-argument/) | Missing type annotation for function argument `{name}` |  |
| ANN002 | [missing-type-args](https://docs.astral.sh/ruff/rules/missing-type-args/) | Missing type annotation for `*{name}` |  |
| ANN003 | [missing-type-kwargs](https://docs.astral.sh/ruff/rules/missing-type-kwargs/) | Missing type annotation for `**{name}` |  |
| ANN101 | [missing-type-self](https://docs.astral.sh/ruff/rules/missing-type-self/) | Missing type annotation for `{name}` in method | ❌ |
| ANN102 | [missing-type-cls](https://docs.astral.sh/ruff/rules/missing-type-cls/) | Missing type annotation for `{name}` in classmethod | ❌ |
| ANN201 | [missing-return-type-undocumented-public-function](https://docs.astral.sh/ruff/rules/missing-return-type-undocumented-public-function/) | Missing return type annotation for public function `{name}` | 🛠️ |
| ANN202 | [missing-return-type-private-function](https://docs.astral.sh/ruff/rules/missing-return-type-private-function/) | Missing return type annotation for private function `{name}` | 🛠️ |
| ANN204 | [missing-return-type-special-method](https://docs.astral.sh/ruff/rules/missing-return-type-special-method/) | Missing return type annotation for special method `{name}` | 🛠️ |
| ANN205 | [missing-return-type-static-method](https://docs.astral.sh/ruff/rules/missing-return-type-static-method/) | Missing return type annotation for staticmethod `{name}` | 🛠️ |
| ANN206 | [missing-return-type-class-method](https://docs.astral.sh/ruff/rules/missing-return-type-class-method/) | Missing return type annotation for classmethod `{name}` | 🛠️ |
| ANN401 | [any-type](https://docs.astral.sh/ruff/rules/any-type/) | Dynamically typed expressions (typing.Any) are disallowed in `{name}` |  |

## [flake8-async (ASYNC)](https://docs.astral.sh/ruff/rules/\#flake8-async-async)

For more, see [flake8-async](https://pypi.org/project/flake8-async/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| ASYNC100 | [cancel-scope-no-checkpoint](https://docs.astral.sh/ruff/rules/cancel-scope-no-checkpoint/) | A `with {method_name}(...):` context does not contain any `await` statements. This makes it pointless, as the timeout can only be triggered by a checkpoint. |  |
| ASYNC105 | [trio-sync-call](https://docs.astral.sh/ruff/rules/trio-sync-call/) | Call to `{method_name}` is not immediately awaited | 🛠️ |
| ASYNC109 | [async-function-with-timeout](https://docs.astral.sh/ruff/rules/async-function-with-timeout/) | Async function definition with a `timeout` parameter |  |
| ASYNC110 | [async-busy-wait](https://docs.astral.sh/ruff/rules/async-busy-wait/) | Use `{module}.Event` instead of awaiting `{module}.sleep` in a `while` loop |  |
| ASYNC115 | [async-zero-sleep](https://docs.astral.sh/ruff/rules/async-zero-sleep/) | Use `{module}.lowlevel.checkpoint()` instead of `{module}.sleep(0)` | 🛠️ |
| ASYNC116 | [long-sleep-not-forever](https://docs.astral.sh/ruff/rules/long-sleep-not-forever/) | `{module}.sleep()` with >24 hour interval should usually be `{module}.sleep_forever()` | 🧪🛠️ |
| ASYNC210 | [blocking-http-call-in-async-function](https://docs.astral.sh/ruff/rules/blocking-http-call-in-async-function/) | Async functions should not call blocking HTTP methods |  |
| ASYNC220 | [create-subprocess-in-async-function](https://docs.astral.sh/ruff/rules/create-subprocess-in-async-function/) | Async functions should not create subprocesses with blocking methods |  |
| ASYNC221 | [run-process-in-async-function](https://docs.astral.sh/ruff/rules/run-process-in-async-function/) | Async functions should not run processes with blocking methods |  |
| ASYNC222 | [wait-for-process-in-async-function](https://docs.astral.sh/ruff/rules/wait-for-process-in-async-function/) | Async functions should not wait on processes with blocking methods |  |
| ASYNC230 | [blocking-open-call-in-async-function](https://docs.astral.sh/ruff/rules/blocking-open-call-in-async-function/) | Async functions should not open files with blocking methods like `open` |  |
| ASYNC251 | [blocking-sleep-in-async-function](https://docs.astral.sh/ruff/rules/blocking-sleep-in-async-function/) | Async functions should not call `time.sleep` |  |

## [flake8-bandit (S)](https://docs.astral.sh/ruff/rules/\#flake8-bandit-s)

For more, see [flake8-bandit](https://pypi.org/project/flake8-bandit/) on PyPI.

For related settings, see [flake8-bandit](https://docs.astral.sh/ruff/settings/#lintflake8-bandit).

| Code | Name | Message |  |
| --- | --- | --- | --- |
| S101 | [assert](https://docs.astral.sh/ruff/rules/assert/) | Use of `assert` detected |  |
| S102 | [exec-builtin](https://docs.astral.sh/ruff/rules/exec-builtin/) | Use of `exec` detected |  |
| S103 | [bad-file-permissions](https://docs.astral.sh/ruff/rules/bad-file-permissions/) | `os.chmod` setting a permissive mask `{mask:#o}` on file or directory |  |
| S104 | [hardcoded-bind-all-interfaces](https://docs.astral.sh/ruff/rules/hardcoded-bind-all-interfaces/) | Possible binding to all interfaces |  |
| S105 | [hardcoded-password-string](https://docs.astral.sh/ruff/rules/hardcoded-password-string/) | Possible hardcoded password assigned to: "{}" |  |
| S106 | [hardcoded-password-func-arg](https://docs.astral.sh/ruff/rules/hardcoded-password-func-arg/) | Possible hardcoded password assigned to argument: "{}" |  |
| S107 | [hardcoded-password-default](https://docs.astral.sh/ruff/rules/hardcoded-password-default/) | Possible hardcoded password assigned to function default: "{}" |  |
| S108 | [hardcoded-temp-file](https://docs.astral.sh/ruff/rules/hardcoded-temp-file/) | Probable insecure usage of temporary file or directory: "{}" |  |
| S110 | [try-except-pass](https://docs.astral.sh/ruff/rules/try-except-pass/) | `try`- `except`- `pass` detected, consider logging the exception |  |
| S112 | [try-except-continue](https://docs.astral.sh/ruff/rules/try-except-continue/) | `try`- `except`- `continue` detected, consider logging the exception |  |
| S113 | [request-without-timeout](https://docs.astral.sh/ruff/rules/request-without-timeout/) | Probable use of `{module}` call without timeout |  |
| S201 | [flask-debug-true](https://docs.astral.sh/ruff/rules/flask-debug-true/) | Use of `debug=True` in Flask app detected |  |
| S202 | [tarfile-unsafe-members](https://docs.astral.sh/ruff/rules/tarfile-unsafe-members/) | Uses of `tarfile.extractall()` |  |
| S301 | [suspicious-pickle-usage](https://docs.astral.sh/ruff/rules/suspicious-pickle-usage/) | `pickle` and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue |  |
| S302 | [suspicious-marshal-usage](https://docs.astral.sh/ruff/rules/suspicious-marshal-usage/) | Deserialization with the `marshal` module is possibly dangerous |  |
| S303 | [suspicious-insecure-hash-usage](https://docs.astral.sh/ruff/rules/suspicious-insecure-hash-usage/) | Use of insecure MD2, MD4, MD5, or SHA1 hash function |  |
| S304 | [suspicious-insecure-cipher-usage](https://docs.astral.sh/ruff/rules/suspicious-insecure-cipher-usage/) | Use of insecure cipher, replace with a known secure cipher such as AES |  |
| S305 | [suspicious-insecure-cipher-mode-usage](https://docs.astral.sh/ruff/rules/suspicious-insecure-cipher-mode-usage/) | Use of insecure block cipher mode, replace with a known secure mode such as CBC or CTR |  |
| S306 | [suspicious-mktemp-usage](https://docs.astral.sh/ruff/rules/suspicious-mktemp-usage/) | Use of insecure and deprecated function ( `mktemp`) |  |
| S307 | [suspicious-eval-usage](https://docs.astral.sh/ruff/rules/suspicious-eval-usage/) | Use of possibly insecure function; consider using `ast.literal_eval` |  |
| S308 | [suspicious-mark-safe-usage](https://docs.astral.sh/ruff/rules/suspicious-mark-safe-usage/) | Use of `mark_safe` may expose cross-site scripting vulnerabilities |  |
| S310 | [suspicious-url-open-usage](https://docs.astral.sh/ruff/rules/suspicious-url-open-usage/) | Audit URL open for permitted schemes. Allowing use of `file:` or custom schemes is often unexpected. |  |
| S311 | [suspicious-non-cryptographic-random-usage](https://docs.astral.sh/ruff/rules/suspicious-non-cryptographic-random-usage/) | Standard pseudo-random generators are not suitable for cryptographic purposes |  |
| S312 | [suspicious-telnet-usage](https://docs.astral.sh/ruff/rules/suspicious-telnet-usage/) | Telnet is considered insecure. Use SSH or some other encrypted protocol. |  |
| S313 | [suspicious-xmlc-element-tree-usage](https://docs.astral.sh/ruff/rules/suspicious-xmlc-element-tree-usage/) | Using `xml` to parse untrusted data is known to be vulnerable to XML attacks; use `defusedxml` equivalents |  |
| S314 | [suspicious-xml-element-tree-usage](https://docs.astral.sh/ruff/rules/suspicious-xml-element-tree-usage/) | Using `xml` to parse untrusted data is known to be vulnerable to XML attacks; use `defusedxml` equivalents |  |
| S315 | [suspicious-xml-expat-reader-usage](https://docs.astral.sh/ruff/rules/suspicious-xml-expat-reader-usage/) | Using `xml` to parse untrusted data is known to be vulnerable to XML attacks; use `defusedxml` equivalents |  |
| S316 | [suspicious-xml-expat-builder-usage](https://docs.astral.sh/ruff/rules/suspicious-xml-expat-builder-usage/) | Using `xml` to parse untrusted data is known to be vulnerable to XML attacks; use `defusedxml` equivalents |  |
| S317 | [suspicious-xml-sax-usage](https://docs.astral.sh/ruff/rules/suspicious-xml-sax-usage/) | Using `xml` to parse untrusted data is known to be vulnerable to XML attacks; use `defusedxml` equivalents |  |
| S318 | [suspicious-xml-mini-dom-usage](https://docs.astral.sh/ruff/rules/suspicious-xml-mini-dom-usage/) | Using `xml` to parse untrusted data is known to be vulnerable to XML attacks; use `defusedxml` equivalents |  |
| S319 | [suspicious-xml-pull-dom-usage](https://docs.astral.sh/ruff/rules/suspicious-xml-pull-dom-usage/) | Using `xml` to parse untrusted data is known to be vulnerable to XML attacks; use `defusedxml` equivalents |  |
| S320 | [suspicious-xmle-tree-usage](https://docs.astral.sh/ruff/rules/suspicious-xmle-tree-usage/) | Using `lxml` to parse untrusted data is known to be vulnerable to XML attacks | ❌ |
| S321 | [suspicious-ftp-lib-usage](https://docs.astral.sh/ruff/rules/suspicious-ftp-lib-usage/) | FTP-related functions are being called. FTP is considered insecure. Use SSH/SFTP/SCP or some other encrypted protocol. |  |
| S323 | [suspicious-unverified-context-usage](https://docs.astral.sh/ruff/rules/suspicious-unverified-context-usage/) | Python allows using an insecure context via the `_create_unverified_context` that reverts to the previous behavior that does not validate certificates or perform hostname checks. |  |
| S324 | [hashlib-insecure-hash-function](https://docs.astral.sh/ruff/rules/hashlib-insecure-hash-function/) | Probable use of insecure hash functions in `{library}`: `{string}` |  |
| S401 | [suspicious-telnetlib-import](https://docs.astral.sh/ruff/rules/suspicious-telnetlib-import/) | `telnetlib` and related modules are considered insecure. Use SSH or another encrypted protocol. | 🧪 |
| S402 | [suspicious-ftplib-import](https://docs.astral.sh/ruff/rules/suspicious-ftplib-import/) | `ftplib` and related modules are considered insecure. Use SSH, SFTP, SCP, or another encrypted protocol. | 🧪 |
| S403 | [suspicious-pickle-import](https://docs.astral.sh/ruff/rules/suspicious-pickle-import/) | `pickle`, `cPickle`, `dill`, and `shelve` modules are possibly insecure | 🧪 |
| S404 | [suspicious-subprocess-import](https://docs.astral.sh/ruff/rules/suspicious-subprocess-import/) | `subprocess` module is possibly insecure | 🧪 |
| S405 | [suspicious-xml-etree-import](https://docs.astral.sh/ruff/rules/suspicious-xml-etree-import/) | `xml.etree` methods are vulnerable to XML attacks | 🧪 |
| S406 | [suspicious-xml-sax-import](https://docs.astral.sh/ruff/rules/suspicious-xml-sax-import/) | `xml.sax` methods are vulnerable to XML attacks | 🧪 |
| S407 | [suspicious-xml-expat-import](https://docs.astral.sh/ruff/rules/suspicious-xml-expat-import/) | `xml.dom.expatbuilder` is vulnerable to XML attacks | 🧪 |
| S408 | [suspicious-xml-minidom-import](https://docs.astral.sh/ruff/rules/suspicious-xml-minidom-import/) | `xml.dom.minidom` is vulnerable to XML attacks | 🧪 |
| S409 | [suspicious-xml-pulldom-import](https://docs.astral.sh/ruff/rules/suspicious-xml-pulldom-import/) | `xml.dom.pulldom` is vulnerable to XML attacks | 🧪 |
| S410 | [suspicious-lxml-import](https://docs.astral.sh/ruff/rules/suspicious-lxml-import/) | `lxml` is vulnerable to XML attacks | ❌ |
| S411 | [suspicious-xmlrpc-import](https://docs.astral.sh/ruff/rules/suspicious-xmlrpc-import/) | XMLRPC is vulnerable to remote XML attacks | 🧪 |
| S412 | [suspicious-httpoxy-import](https://docs.astral.sh/ruff/rules/suspicious-httpoxy-import/) | `httpoxy` is a set of vulnerabilities that affect application code running inCGI, or CGI-like environments. The use of CGI for web applications should be avoided | 🧪 |
| S413 | [suspicious-pycrypto-import](https://docs.astral.sh/ruff/rules/suspicious-pycrypto-import/) | `pycrypto` library is known to have publicly disclosed buffer overflow vulnerability | 🧪 |
| S415 | [suspicious-pyghmi-import](https://docs.astral.sh/ruff/rules/suspicious-pyghmi-import/) | An IPMI-related module is being imported. Prefer an encrypted protocol over IPMI. | 🧪 |
| S501 | [request-with-no-cert-validation](https://docs.astral.sh/ruff/rules/request-with-no-cert-validation/) | Probable use of `{string}` call with `verify=False` disabling SSL certificate checks |  |
| S502 | [ssl-insecure-version](https://docs.astral.sh/ruff/rules/ssl-insecure-version/) | Call made with insecure SSL protocol: `{protocol}` |  |
| S503 | [ssl-with-bad-defaults](https://docs.astral.sh/ruff/rules/ssl-with-bad-defaults/) | Argument default set to insecure SSL protocol: `{protocol}` |  |
| S504 | [ssl-with-no-version](https://docs.astral.sh/ruff/rules/ssl-with-no-version/) | `ssl.wrap_socket` called without an \`ssl\_version\`\` |  |
| S505 | [weak-cryptographic-key](https://docs.astral.sh/ruff/rules/weak-cryptographic-key/) | {cryptographic\_key} key sizes below {minimum\_key\_size} bits are considered breakable |  |
| S506 | [unsafe-yaml-load](https://docs.astral.sh/ruff/rules/unsafe-yaml-load/) | Probable use of unsafe loader `{name}` with `yaml.load`. Allows instantiation of arbitrary objects. Consider `yaml.safe_load`. |  |
| S507 | [ssh-no-host-key-verification](https://docs.astral.sh/ruff/rules/ssh-no-host-key-verification/) | Paramiko call with policy set to automatically trust the unknown host key |  |
| S508 | [snmp-insecure-version](https://docs.astral.sh/ruff/rules/snmp-insecure-version/) | The use of SNMPv1 and SNMPv2 is insecure. Use SNMPv3 if able. |  |
| S509 | [snmp-weak-cryptography](https://docs.astral.sh/ruff/rules/snmp-weak-cryptography/) | You should not use SNMPv3 without encryption. `noAuthNoPriv` & `authNoPriv` is insecure. |  |
| S601 | [paramiko-call](https://docs.astral.sh/ruff/rules/paramiko-call/) | Possible shell injection via Paramiko call; check inputs are properly sanitized |  |
| S602 | [subprocess-popen-with-shell-equals-true](https://docs.astral.sh/ruff/rules/subprocess-popen-with-shell-equals-true/) | `subprocess` call with `shell=True` seems safe, but may be changed in the future; consider rewriting without `shell` |  |
| S603 | [subprocess-without-shell-equals-true](https://docs.astral.sh/ruff/rules/subprocess-without-shell-equals-true/) | `subprocess` call: check for execution of untrusted input |  |
| S604 | [call-with-shell-equals-true](https://docs.astral.sh/ruff/rules/call-with-shell-equals-true/) | Function call with `shell=True` parameter identified, security issue |  |
| S605 | [start-process-with-a-shell](https://docs.astral.sh/ruff/rules/start-process-with-a-shell/) | Starting a process with a shell: seems safe, but may be changed in the future; consider rewriting without `shell` |  |
| S606 | [start-process-with-no-shell](https://docs.astral.sh/ruff/rules/start-process-with-no-shell/) | Starting a process without a shell |  |
| S607 | [start-process-with-partial-path](https://docs.astral.sh/ruff/rules/start-process-with-partial-path/) | Starting a process with a partial executable path |  |
| S608 | [hardcoded-sql-expression](https://docs.astral.sh/ruff/rules/hardcoded-sql-expression/) | Possible SQL injection vector through string-based query construction |  |
| S609 | [unix-command-wildcard-injection](https://docs.astral.sh/ruff/rules/unix-command-wildcard-injection/) | Possible wildcard injection in call due to `*` usage |  |
| S610 | [django-extra](https://docs.astral.sh/ruff/rules/django-extra/) | Use of Django `extra` can lead to SQL injection vulnerabilities |  |
| S611 | [django-raw-sql](https://docs.astral.sh/ruff/rules/django-raw-sql/) | Use of `RawSQL` can lead to SQL injection vulnerabilities |  |
| S612 | [logging-config-insecure-listen](https://docs.astral.sh/ruff/rules/logging-config-insecure-listen/) | Use of insecure `logging.config.listen` detected |  |
| S701 | [jinja2-autoescape-false](https://docs.astral.sh/ruff/rules/jinja2-autoescape-false/) | Using jinja2 templates with `autoescape=False` is dangerous and can lead to XSS. Ensure `autoescape=True` or use the `select_autoescape` function. |  |
| S702 | [mako-templates](https://docs.astral.sh/ruff/rules/mako-templates/) | Mako templates allow HTML and JavaScript rendering by default and are inherently open to XSS attacks |  |
| S704 | [unsafe-markup-use](https://docs.astral.sh/ruff/rules/unsafe-markup-use/) | Unsafe use of `{name}` detected |  |

## [flake8-blind-except (BLE)](https://docs.astral.sh/ruff/rules/\#flake8-blind-except-ble)

For more, see [flake8-blind-except](https://pypi.org/project/flake8-blind-except/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| BLE001 | [blind-except](https://docs.astral.sh/ruff/rules/blind-except/) | Do not catch blind exception: `{name}` |  |

## [flake8-boolean-trap (FBT)](https://docs.astral.sh/ruff/rules/\#flake8-boolean-trap-fbt)

For more, see [flake8-boolean-trap](https://pypi.org/project/flake8-boolean-trap/) on PyPI.

For related settings, see [flake8-boolean-trap](https://docs.astral.sh/ruff/settings/#lintflake8-boolean-trap).

| Code | Name | Message |  |
| --- | --- | --- | --- |
| FBT001 | [boolean-type-hint-positional-argument](https://docs.astral.sh/ruff/rules/boolean-type-hint-positional-argument/) | Boolean-typed positional argument in function definition |  |
| FBT002 | [boolean-default-value-positional-argument](https://docs.astral.sh/ruff/rules/boolean-default-value-positional-argument/) | Boolean default positional argument in function definition |  |
| FBT003 | [boolean-positional-value-in-call](https://docs.astral.sh/ruff/rules/boolean-positional-value-in-call/) | Boolean positional value in function call |  |

## [flake8-bugbear (B)](https://docs.astral.sh/ruff/rules/\#flake8-bugbear-b)

For more, see [flake8-bugbear](https://pypi.org/project/flake8-bugbear/) on PyPI.

For related settings, see [flake8-bugbear](https://docs.astral.sh/ruff/settings/#lintflake8-bugbear).

| Code | Name | Message |  |
| --- | --- | --- | --- |
| B002 | [unary-prefix-increment-decrement](https://docs.astral.sh/ruff/rules/unary-prefix-increment-decrement/) | Python does not support the unary prefix increment operator ( `++`) |  |
| B003 | [assignment-to-os-environ](https://docs.astral.sh/ruff/rules/assignment-to-os-environ/) | Assigning to `os.environ` doesn't clear the environment |  |
| B004 | [unreliable-callable-check](https://docs.astral.sh/ruff/rules/unreliable-callable-check/) | Using `hasattr(x, "__call__")` to test if x is callable is unreliable. Use `callable(x)` for consistent results. | 🛠️ |
| B005 | [strip-with-multi-characters](https://docs.astral.sh/ruff/rules/strip-with-multi-characters/) | Using `.strip()` with multi-character strings is misleading |  |
| B006 | [mutable-argument-default](https://docs.astral.sh/ruff/rules/mutable-argument-default/) | Do not use mutable data structures for argument defaults | 🛠️ |
| B007 | [unused-loop-control-variable](https://docs.astral.sh/ruff/rules/unused-loop-control-variable/) | Loop control variable `{name}` not used within loop body | 🛠️ |
| B008 | [function-call-in-default-argument](https://docs.astral.sh/ruff/rules/function-call-in-default-argument/) | Do not perform function call `{name}` in argument defaults; instead, perform the call within the function, or read the default from a module-level singleton variable |  |
| B009 | [get-attr-with-constant](https://docs.astral.sh/ruff/rules/get-attr-with-constant/) | Do not call `getattr` with a constant attribute value. It is not any safer than normal property access. | 🛠️ |
| B010 | [set-attr-with-constant](https://docs.astral.sh/ruff/rules/set-attr-with-constant/) | Do not call `setattr` with a constant attribute value. It is not any safer than normal property access. | 🛠️ |
| B011 | [assert-false](https://docs.astral.sh/ruff/rules/assert-false/) | Do not `assert False` ( `python -O` removes these calls), raise `AssertionError()` | 🛠️ |
| B012 | [jump-statement-in-finally](https://docs.astral.sh/ruff/rules/jump-statement-in-finally/) | `{name}` inside `finally` blocks cause exceptions to be silenced |  |
| B013 | [redundant-tuple-in-exception-handler](https://docs.astral.sh/ruff/rules/redundant-tuple-in-exception-handler/) | A length-one tuple literal is redundant in exception handlers | 🛠️ |
| B014 | [duplicate-handler-exception](https://docs.astral.sh/ruff/rules/duplicate-handler-exception/) | Exception handler with duplicate exception: `{name}` | 🛠️ |
| B015 | [useless-comparison](https://docs.astral.sh/ruff/rules/useless-comparison/) | Pointless comparison. Did you mean to assign a value? Otherwise, prepend `assert` or remove it. |  |
| B016 | [raise-literal](https://docs.astral.sh/ruff/rules/raise-literal/) | Cannot raise a literal. Did you intend to return it or raise an Exception? |  |
| B017 | [assert-raises-exception](https://docs.astral.sh/ruff/rules/assert-raises-exception/) | Do not assert blind exception: `{exception}` |  |
| B018 | [useless-expression](https://docs.astral.sh/ruff/rules/useless-expression/) | Found useless expression. Either assign it to a variable or remove it. |  |
| B019 | [cached-instance-method](https://docs.astral.sh/ruff/rules/cached-instance-method/) | Use of `functools.lru_cache` or `functools.cache` on methods can lead to memory leaks |  |
| B020 | [loop-variable-overrides-iterator](https://docs.astral.sh/ruff/rules/loop-variable-overrides-iterator/) | Loop control variable `{name}` overrides iterable it iterates |  |
| B021 | [f-string-docstring](https://docs.astral.sh/ruff/rules/f-string-docstring/) | f-string used as docstring. Python will interpret this as a joined string, rather than a docstring. |  |
| B022 | [useless-contextlib-suppress](https://docs.astral.sh/ruff/rules/useless-contextlib-suppress/) | No arguments passed to `contextlib.suppress`. No exceptions will be suppressed and therefore this context manager is redundant |  |
| B023 | [function-uses-loop-variable](https://docs.astral.sh/ruff/rules/function-uses-loop-variable/) | Function definition does not bind loop variable `{name}` |  |
| B024 | [abstract-base-class-without-abstract-method](https://docs.astral.sh/ruff/rules/abstract-base-class-without-abstract-method/) | `{name}` is an abstract base class, but it has no abstract methods or properties |  |
| B025 | [duplicate-try-block-exception](https://docs.astral.sh/ruff/rules/duplicate-try-block-exception/) | try-except\* block with duplicate exception `{name}` |  |
| B026 | [star-arg-unpacking-after-keyword-arg](https://docs.astral.sh/ruff/rules/star-arg-unpacking-after-keyword-arg/) | Star-arg unpacking after a keyword argument is strongly discouraged |  |
| B027 | [empty-method-without-abstract-decorator](https://docs.astral.sh/ruff/rules/empty-method-without-abstract-decorator/) | `{name}` is an empty method in an abstract base class, but has no abstract decorator |  |
| B028 | [no-explicit-stacklevel](https://docs.astral.sh/ruff/rules/no-explicit-stacklevel/) | No explicit `stacklevel` keyword argument found | 🛠️ |
| B029 | [except-with-empty-tuple](https://docs.astral.sh/ruff/rules/except-with-empty-tuple/) | Using `except* ():` with an empty tuple does not catch anything; add exceptions to handle |  |
| B030 | [except-with-non-exception-classes](https://docs.astral.sh/ruff/rules/except-with-non-exception-classes/) | `except*` handlers should only be exception classes or tuples of exception classes |  |
| B031 | [reuse-of-groupby-generator](https://docs.astral.sh/ruff/rules/reuse-of-groupby-generator/) | Using the generator returned from `itertools.groupby()` more than once will do nothing on the second usage |  |
| B032 | [unintentional-type-annotation](https://docs.astral.sh/ruff/rules/unintentional-type-annotation/) | Possible unintentional type annotation (using `:`). Did you mean to assign (using `=`)? |  |
| B033 | [duplicate-value](https://docs.astral.sh/ruff/rules/duplicate-value/) | Sets should not contain duplicate item `{value}` | 🛠️ |
| B034 | [re-sub-positional-args](https://docs.astral.sh/ruff/rules/re-sub-positional-args/) | `{method}` should pass `{param_name}` and `flags` as keyword arguments to avoid confusion due to unintuitive argument positions |  |
| B035 | [static-key-dict-comprehension](https://docs.astral.sh/ruff/rules/static-key-dict-comprehension/) | Dictionary comprehension uses static key: `{key}` |  |
| B039 | [mutable-contextvar-default](https://docs.astral.sh/ruff/rules/mutable-contextvar-default/) | Do not use mutable data structures for `ContextVar` defaults |  |
| B901 | [return-in-generator](https://docs.astral.sh/ruff/rules/return-in-generator/) | Using `yield` and `return {value}` in a generator function can lead to confusing behavior | 🧪 |
| B903 | [class-as-data-structure](https://docs.astral.sh/ruff/rules/class-as-data-structure/) | Class could be dataclass or namedtuple | 🧪 |
| B904 | [raise-without-from-inside-except](https://docs.astral.sh/ruff/rules/raise-without-from-inside-except/) | Within an `except*` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling |  |
| B905 | [zip-without-explicit-strict](https://docs.astral.sh/ruff/rules/zip-without-explicit-strict/) | `zip()` without an explicit `strict=` parameter | 🛠️ |
| B909 | [loop-iterator-mutation](https://docs.astral.sh/ruff/rules/loop-iterator-mutation/) | Mutation to loop iterable `{name}` during iteration | 🧪 |
| B911 | [batched-without-explicit-strict](https://docs.astral.sh/ruff/rules/batched-without-explicit-strict/) | `itertools.batched()` without an explicit `strict` parameter |  |

## [flake8-builtins (A)](https://docs.astral.sh/ruff/rules/\#flake8-builtins-a)

For more, see [flake8-builtins](https://pypi.org/project/flake8-builtins/) on PyPI.

For related settings, see [flake8-builtins](https://docs.astral.sh/ruff/settings/#lintflake8-builtins).

| Code | Name | Message |  |
| --- | --- | --- | --- |
| A001 | [builtin-variable-shadowing](https://docs.astral.sh/ruff/rules/builtin-variable-shadowing/) | Variable `{name}` is shadowing a Python builtin |  |
| A002 | [builtin-argument-shadowing](https://docs.astral.sh/ruff/rules/builtin-argument-shadowing/) | Function argument `{name}` is shadowing a Python builtin |  |
| A003 | [builtin-attribute-shadowing](https://docs.astral.sh/ruff/rules/builtin-attribute-shadowing/) | Python builtin is shadowed by class attribute `{name}` from {row} |  |
| A004 | [builtin-import-shadowing](https://docs.astral.sh/ruff/rules/builtin-import-shadowing/) | Import `{name}` is shadowing a Python builtin |  |
| A005 | [stdlib-module-shadowing](https://docs.astral.sh/ruff/rules/stdlib-module-shadowing/) | Module `{name}` shadows a Python standard-library module |  |
| A006 | [builtin-lambda-argument-shadowing](https://docs.astral.sh/ruff/rules/builtin-lambda-argument-shadowing/) | Lambda argument `{name}` is shadowing a Python builtin |  |

## [flake8-commas (COM)](https://docs.astral.sh/ruff/rules/\#flake8-commas-com)

For more, see [flake8-commas](https://pypi.org/project/flake8-commas/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| COM812 | [missing-trailing-comma](https://docs.astral.sh/ruff/rules/missing-trailing-comma/) | Trailing comma missing | 🛠️ |
| COM818 | [trailing-comma-on-bare-tuple](https://docs.astral.sh/ruff/rules/trailing-comma-on-bare-tuple/) | Trailing comma on bare tuple prohibited |  |
| COM819 | [prohibited-trailing-comma](https://docs.astral.sh/ruff/rules/prohibited-trailing-comma/) | Trailing comma prohibited | 🛠️ |

## [flake8-comprehensions (C4)](https://docs.astral.sh/ruff/rules/\#flake8-comprehensions-c4)

For more, see [flake8-comprehensions](https://pypi.org/project/flake8-comprehensions/) on PyPI.

For related settings, see [flake8-comprehensions](https://docs.astral.sh/ruff/settings/#lintflake8-comprehensions).

| Code | Name | Message |  |
| --- | --- | --- | --- |
| C400 | [unnecessary-generator-list](https://docs.astral.sh/ruff/rules/unnecessary-generator-list/) | Unnecessary generator (rewrite using `list()`) | 🛠️ |
| C401 | [unnecessary-generator-set](https://docs.astral.sh/ruff/rules/unnecessary-generator-set/) | Unnecessary generator (rewrite using `set()`) | 🛠️ |
| C402 | [unnecessary-generator-dict](https://docs.astral.sh/ruff/rules/unnecessary-generator-dict/) | Unnecessary generator (rewrite as a dict comprehension) | 🛠️ |
| C403 | [unnecessary-list-comprehension-set](https://docs.astral.sh/ruff/rules/unnecessary-list-comprehension-set/) | Unnecessary list comprehension (rewrite as a set comprehension) | 🛠️ |
| C404 | [unnecessary-list-comprehension-dict](https://docs.astral.sh/ruff/rules/unnecessary-list-comprehension-dict/) | Unnecessary list comprehension (rewrite as a dict comprehension) | 🛠️ |
| C405 | [unnecessary-literal-set](https://docs.astral.sh/ruff/rules/unnecessary-literal-set/) | Unnecessary {kind} literal (rewrite as a set literal) | 🛠️ |
| C406 | [unnecessary-literal-dict](https://docs.astral.sh/ruff/rules/unnecessary-literal-dict/) | Unnecessary {obj\_type} literal (rewrite as a dict literal) | 🛠️ |
| C408 | [unnecessary-collection-call](https://docs.astral.sh/ruff/rules/unnecessary-collection-call/) | Unnecessary `{kind}()` call (rewrite as a literal) | 🛠️ |
| C409 | [unnecessary-literal-within-tuple-call](https://docs.astral.sh/ruff/rules/unnecessary-literal-within-tuple-call/) | Unnecessary list literal passed to `tuple()` (rewrite as a tuple literal) | 🛠️ |
| C410 | [unnecessary-literal-within-list-call](https://docs.astral.sh/ruff/rules/unnecessary-literal-within-list-call/) | Unnecessary list literal passed to `list()` (remove the outer call to `list()`) | 🛠️ |
| C411 | [unnecessary-list-call](https://docs.astral.sh/ruff/rules/unnecessary-list-call/) | Unnecessary `list()` call (remove the outer call to `list()`) | 🛠️ |
| C413 | [unnecessary-call-around-sorted](https://docs.astral.sh/ruff/rules/unnecessary-call-around-sorted/) | Unnecessary `{func}()` call around `sorted()` | 🛠️ |
| C414 | [unnecessary-double-cast-or-process](https://docs.astral.sh/ruff/rules/unnecessary-double-cast-or-process/) | Unnecessary `{inner}()` call within `{outer}()` | 🛠️ |
| C415 | [unnecessary-subscript-reversal](https://docs.astral.sh/ruff/rules/unnecessary-subscript-reversal/) | Unnecessary subscript reversal of iterable within `{func}()` |  |
| C416 | [unnecessary-comprehension](https://docs.astral.sh/ruff/rules/unnecessary-comprehension/) | Unnecessary {kind} comprehension (rewrite using `{kind}()`) | 🛠️ |
| C417 | [unnecessary-map](https://docs.astral.sh/ruff/rules/unnecessary-map/) | Unnecessary `map()` usage (rewrite using a {object\_type}) | 🛠️ |
| C418 | [unnecessary-literal-within-dict-call](https://docs.astral.sh/ruff/rules/unnecessary-literal-within-dict-call/) | Unnecessary dict {kind} passed to `dict()` (remove the outer call to `dict()`) | 🛠️ |
| C419 | [unnecessary-comprehension-in-call](https://docs.astral.sh/ruff/rules/unnecessary-comprehension-in-call/) | Unnecessary list comprehension | 🛠️ |
| C420 | [unnecessary-dict-comprehension-for-iterable](https://docs.astral.sh/ruff/rules/unnecessary-dict-comprehension-for-iterable/) | Unnecessary dict comprehension for iterable; use `dict.fromkeys` instead | 🛠️ |

## [flake8-copyright (CPY)](https://docs.astral.sh/ruff/rules/\#flake8-copyright-cpy)

For more, see [flake8-copyright](https://pypi.org/project/flake8-copyright/) on PyPI.

For related settings, see [flake8-copyright](https://docs.astral.sh/ruff/settings/#lintflake8-copyright).

| Code | Name | Message |  |
| --- | --- | --- | --- |
| CPY001 | [missing-copyright-notice](https://docs.astral.sh/ruff/rules/missing-copyright-notice/) | Missing copyright notice at top of file | 🧪 |

## [flake8-datetimez (DTZ)](https://docs.astral.sh/ruff/rules/\#flake8-datetimez-dtz)

For more, see [flake8-datetimez](https://pypi.org/project/flake8-datetimez/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| DTZ001 | [call-datetime-without-tzinfo](https://docs.astral.sh/ruff/rules/call-datetime-without-tzinfo/) | `datetime.datetime()` called without a `tzinfo` argument |  |
| DTZ002 | [call-datetime-today](https://docs.astral.sh/ruff/rules/call-datetime-today/) | `datetime.datetime.today()` used |  |
| DTZ003 | [call-datetime-utcnow](https://docs.astral.sh/ruff/rules/call-datetime-utcnow/) | `datetime.datetime.utcnow()` used |  |
| DTZ004 | [call-datetime-utcfromtimestamp](https://docs.astral.sh/ruff/rules/call-datetime-utcfromtimestamp/) | `datetime.datetime.utcfromtimestamp()` used |  |
| DTZ005 | [call-datetime-now-without-tzinfo](https://docs.astral.sh/ruff/rules/call-datetime-now-without-tzinfo/) | `datetime.datetime.now()` called without a `tz` argument |  |
| DTZ006 | [call-datetime-fromtimestamp](https://docs.astral.sh/ruff/rules/call-datetime-fromtimestamp/) | `datetime.datetime.fromtimestamp()` called without a `tz` argument |  |
| DTZ007 | [call-datetime-strptime-without-zone](https://docs.astral.sh/ruff/rules/call-datetime-strptime-without-zone/) | Naive datetime constructed using `datetime.datetime.strptime()` without %z |  |
| DTZ011 | [call-date-today](https://docs.astral.sh/ruff/rules/call-date-today/) | `datetime.date.today()` used |  |
| DTZ012 | [call-date-fromtimestamp](https://docs.astral.sh/ruff/rules/call-date-fromtimestamp/) | `datetime.date.fromtimestamp()` used |  |
| DTZ901 | [datetime-min-max](https://docs.astral.sh/ruff/rules/datetime-min-max/) | Use of `datetime.datetime.{min_max}` without timezone information |  |

## [flake8-debugger (T10)](https://docs.astral.sh/ruff/rules/\#flake8-debugger-t10)

For more, see [flake8-debugger](https://pypi.org/project/flake8-debugger/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| T100 | [debugger](https://docs.astral.sh/ruff/rules/debugger/) | Trace found: `{name}` used |  |

## [flake8-django (DJ)](https://docs.astral.sh/ruff/rules/\#flake8-django-dj)

For more, see [flake8-django](https://pypi.org/project/flake8-django/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| DJ001 | [django-nullable-model-string-field](https://docs.astral.sh/ruff/rules/django-nullable-model-string-field/) | Avoid using `null=True` on string-based fields such as `{field_name}` |  |
| DJ003 | [django-locals-in-render-function](https://docs.astral.sh/ruff/rules/django-locals-in-render-function/) | Avoid passing `locals()` as context to a `render` function |  |
| DJ006 | [django-exclude-with-model-form](https://docs.astral.sh/ruff/rules/django-exclude-with-model-form/) | Do not use `exclude` with `ModelForm`, use `fields` instead |  |
| DJ007 | [django-all-with-model-form](https://docs.astral.sh/ruff/rules/django-all-with-model-form/) | Do not use `__all__` with `ModelForm`, use `fields` instead |  |
| DJ008 | [django-model-without-dunder-str](https://docs.astral.sh/ruff/rules/django-model-without-dunder-str/) | Model does not define `__str__` method |  |
| DJ012 | [django-unordered-body-content-in-model](https://docs.astral.sh/ruff/rules/django-unordered-body-content-in-model/) | Order of model's inner classes, methods, and fields does not follow the Django Style Guide: {element\_type} should come before {prev\_element\_type} |  |
| DJ013 | [django-non-leading-receiver-decorator](https://docs.astral.sh/ruff/rules/django-non-leading-receiver-decorator/) | `@receiver` decorator must be on top of all the other decorators |  |

## [flake8-errmsg (EM)](https://docs.astral.sh/ruff/rules/\#flake8-errmsg-em)

For more, see [flake8-errmsg](https://pypi.org/project/flake8-errmsg/) on PyPI.

For related settings, see [flake8-errmsg](https://docs.astral.sh/ruff/settings/#lintflake8-errmsg).

| Code | Name | Message |  |
| --- | --- | --- | --- |
| EM101 | [raw-string-in-exception](https://docs.astral.sh/ruff/rules/raw-string-in-exception/) | Exception must not use a string literal, assign to variable first | 🛠️ |
| EM102 | [f-string-in-exception](https://docs.astral.sh/ruff/rules/f-string-in-exception/) | Exception must not use an f-string literal, assign to variable first | 🛠️ |
| EM103 | [dot-format-in-exception](https://docs.astral.sh/ruff/rules/dot-format-in-exception/) | Exception must not use a `.format()` string directly, assign to variable first | 🛠️ |

## [flake8-executable (EXE)](https://docs.astral.sh/ruff/rules/\#flake8-executable-exe)

For more, see [flake8-executable](https://pypi.org/project/flake8-executable/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| EXE001 | [shebang-not-executable](https://docs.astral.sh/ruff/rules/shebang-not-executable/) | Shebang is present but file is not executable |  |
| EXE002 | [shebang-missing-executable-file](https://docs.astral.sh/ruff/rules/shebang-missing-executable-file/) | The file is executable but no shebang is present |  |
| EXE003 | [shebang-missing-python](https://docs.astral.sh/ruff/rules/shebang-missing-python/) | Shebang should contain `python`, `pytest`, or `uv run` |  |
| EXE004 | [shebang-leading-whitespace](https://docs.astral.sh/ruff/rules/shebang-leading-whitespace/) | Avoid whitespace before shebang | 🛠️ |
| EXE005 | [shebang-not-first-line](https://docs.astral.sh/ruff/rules/shebang-not-first-line/) | Shebang should be at the beginning of the file |  |

## [flake8-fixme (FIX)](https://docs.astral.sh/ruff/rules/\#flake8-fixme-fix)

For more, see [flake8-fixme](https://github.com/tommilligan/flake8-fixme) on GitHub.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| FIX001 | [line-contains-fixme](https://docs.astral.sh/ruff/rules/line-contains-fixme/) | Line contains FIXME, consider resolving the issue |  |
| FIX002 | [line-contains-todo](https://docs.astral.sh/ruff/rules/line-contains-todo/) | Line contains TODO, consider resolving the issue |  |
| FIX003 | [line-contains-xxx](https://docs.astral.sh/ruff/rules/line-contains-xxx/) | Line contains XXX, consider resolving the issue |  |
| FIX004 | [line-contains-hack](https://docs.astral.sh/ruff/rules/line-contains-hack/) | Line contains HACK, consider resolving the issue |  |

## [flake8-future-annotations (FA)](https://docs.astral.sh/ruff/rules/\#flake8-future-annotations-fa)

For more, see [flake8-future-annotations](https://pypi.org/project/flake8-future-annotations/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| FA100 | [future-rewritable-type-annotation](https://docs.astral.sh/ruff/rules/future-rewritable-type-annotation/) | Add `from __future__ import annotations` to simplify `{name}` | 🛠️ |
| FA102 | [future-required-type-annotation](https://docs.astral.sh/ruff/rules/future-required-type-annotation/) | Missing `from __future__ import annotations`, but uses {reason} | 🛠️ |

## [flake8-gettext (INT)](https://docs.astral.sh/ruff/rules/\#flake8-gettext-int)

For more, see [flake8-gettext](https://pypi.org/project/flake8-gettext/) on PyPI.

For related settings, see [flake8-gettext](https://docs.astral.sh/ruff/settings/#lintflake8-gettext).

| Code | Name | Message |  |
| --- | --- | --- | --- |
| INT001 | [f-string-in-get-text-func-call](https://docs.astral.sh/ruff/rules/f-string-in-get-text-func-call/) | f-string is resolved before function call; consider `_("string %s") % arg` |  |
| INT002 | [format-in-get-text-func-call](https://docs.astral.sh/ruff/rules/format-in-get-text-func-call/) | `format` method argument is resolved before function call; consider `_("string %s") % arg` |  |
| INT003 | [printf-in-get-text-func-call](https://docs.astral.sh/ruff/rules/printf-in-get-text-func-call/) | printf-style format is resolved before function call; consider `_("string %s") % arg` |  |

## [flake8-implicit-str-concat (ISC)](https://docs.astral.sh/ruff/rules/\#flake8-implicit-str-concat-isc)

For more, see [flake8-implicit-str-concat](https://pypi.org/project/flake8-implicit-str-concat/) on PyPI.

For related settings, see [flake8-implicit-str-concat](https://docs.astral.sh/ruff/settings/#lintflake8-implicit-str-concat).

| Code | Name | Message |  |
| --- | --- | --- | --- |
| ISC001 | [single-line-implicit-string-concatenation](https://docs.astral.sh/ruff/rules/single-line-implicit-string-concatenation/) | Implicitly concatenated string literals on one line | 🛠️ |
| ISC002 | [multi-line-implicit-string-concatenation](https://docs.astral.sh/ruff/rules/multi-line-implicit-string-concatenation/) | Implicitly concatenated string literals over multiple lines |  |
| ISC003 | [explicit-string-concatenation](https://docs.astral.sh/ruff/rules/explicit-string-concatenation/) | Explicitly concatenated string should be implicitly concatenated | 🛠️ |

## [flake8-import-conventions (ICN)](https://docs.astral.sh/ruff/rules/\#flake8-import-conventions-icn)

For more, see [flake8-import-conventions](https://github.com/joaopalmeiro/flake8-import-conventions) on GitHub.

For related settings, see [flake8-import-conventions](https://docs.astral.sh/ruff/settings/#lintflake8-import-conventions).

| Code | Name | Message |  |
| --- | --- | --- | --- |
| ICN001 | [unconventional-import-alias](https://docs.astral.sh/ruff/rules/unconventional-import-alias/) | `{name}` should be imported as `{asname}` | 🛠️ |
| ICN002 | [banned-import-alias](https://docs.astral.sh/ruff/rules/banned-import-alias/) | `{name}` should not be imported as `{asname}` |  |
| ICN003 | [banned-import-from](https://docs.astral.sh/ruff/rules/banned-import-from/) | Members of `{name}` should not be imported explicitly |  |

## [flake8-logging (LOG)](https://docs.astral.sh/ruff/rules/\#flake8-logging-log)

For more, see [flake8-logging](https://pypi.org/project/flake8-logging/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| LOG001 | [direct-logger-instantiation](https://docs.astral.sh/ruff/rules/direct-logger-instantiation/) | Use `logging.getLogger()` to instantiate loggers | 🛠️ |
| LOG002 | [invalid-get-logger-argument](https://docs.astral.sh/ruff/rules/invalid-get-logger-argument/) | Use `__name__` with `logging.getLogger()` | 🛠️ |
| LOG004 | [log-exception-outside-except-handler](https://docs.astral.sh/ruff/rules/log-exception-outside-except-handler/) | `.exception()` call outside exception handlers | 🧪🛠️ |
| LOG007 | [exception-without-exc-info](https://docs.astral.sh/ruff/rules/exception-without-exc-info/) | Use of `logging.exception` with falsy `exc_info` |  |
| LOG009 | [undocumented-warn](https://docs.astral.sh/ruff/rules/undocumented-warn/) | Use of undocumented `logging.WARN` constant | 🛠️ |
| LOG014 | [exc-info-outside-except-handler](https://docs.astral.sh/ruff/rules/exc-info-outside-except-handler/) | `exc_info=` outside exception handlers | 🛠️ |
| LOG015 | [root-logger-call](https://docs.astral.sh/ruff/rules/root-logger-call/) | `{}()` call on root logger |  |

## [flake8-logging-format (G)](https://docs.astral.sh/ruff/rules/\#flake8-logging-format-g)

For more, see [flake8-logging-format](https://pypi.org/project/flake8-logging-format/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| G001 | [logging-string-format](https://docs.astral.sh/ruff/rules/logging-string-format/) | Logging statement uses `str.format` |  |
| G002 | [logging-percent-format](https://docs.astral.sh/ruff/rules/logging-percent-format/) | Logging statement uses `%` |  |
| G003 | [logging-string-concat](https://docs.astral.sh/ruff/rules/logging-string-concat/) | Logging statement uses `+` |  |
| G004 | [logging-f-string](https://docs.astral.sh/ruff/rules/logging-f-string/) | Logging statement uses f-string |  |
| G010 | [logging-warn](https://docs.astral.sh/ruff/rules/logging-warn/) | Logging statement uses `warn` instead of `warning` | 🛠️ |
| G101 | [logging-extra-attr-clash](https://docs.astral.sh/ruff/rules/logging-extra-attr-clash/) | Logging statement uses an `extra` field that clashes with a `LogRecord` field: `{key}` |  |
| G201 | [logging-exc-info](https://docs.astral.sh/ruff/rules/logging-exc-info/) | Logging `.exception(...)` should be used instead of `.error(..., exc_info=True)` |  |
| G202 | [logging-redundant-exc-info](https://docs.astral.sh/ruff/rules/logging-redundant-exc-info/) | Logging statement has redundant `exc_info` |  |

## [flake8-no-pep420 (INP)](https://docs.astral.sh/ruff/rules/\#flake8-no-pep420-inp)

For more, see [flake8-no-pep420](https://pypi.org/project/flake8-no-pep420/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| INP001 | [implicit-namespace-package](https://docs.astral.sh/ruff/rules/implicit-namespace-package/) | File `{filename}` is part of an implicit namespace package. Add an `__init__.py`. |  |

## [flake8-pie (PIE)](https://docs.astral.sh/ruff/rules/\#flake8-pie-pie)

For more, see [flake8-pie](https://pypi.org/project/flake8-pie/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| PIE790 | [unnecessary-placeholder](https://docs.astral.sh/ruff/rules/unnecessary-placeholder/) | Unnecessary `pass` statement | 🛠️ |
| PIE794 | [duplicate-class-field-definition](https://docs.astral.sh/ruff/rules/duplicate-class-field-definition/) | Class field `{name}` is defined multiple times | 🛠️ |
| PIE796 | [non-unique-enums](https://docs.astral.sh/ruff/rules/non-unique-enums/) | Enum contains duplicate value: `{value}` |  |
| PIE800 | [unnecessary-spread](https://docs.astral.sh/ruff/rules/unnecessary-spread/) | Unnecessary spread `**` | 🛠️ |
| PIE804 | [unnecessary-dict-kwargs](https://docs.astral.sh/ruff/rules/unnecessary-dict-kwargs/) | Unnecessary `dict` kwargs | 🛠️ |
| PIE807 | [reimplemented-container-builtin](https://docs.astral.sh/ruff/rules/reimplemented-container-builtin/) | Prefer `{container}` over useless lambda | 🛠️ |
| PIE808 | [unnecessary-range-start](https://docs.astral.sh/ruff/rules/unnecessary-range-start/) | Unnecessary `start` argument in `range` | 🛠️ |
| PIE810 | [multiple-starts-ends-with](https://docs.astral.sh/ruff/rules/multiple-starts-ends-with/) | Call `{attr}` once with a `tuple` | 🛠️ |

## [flake8-print (T20)](https://docs.astral.sh/ruff/rules/\#flake8-print-t20)

For more, see [flake8-print](https://pypi.org/project/flake8-print/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| T201 | [print](https://docs.astral.sh/ruff/rules/print/) | `print` found | 🛠️ |
| T203 | [p-print](https://docs.astral.sh/ruff/rules/p-print/) | `pprint` found | 🛠️ |

## [flake8-pyi (PYI)](https://docs.astral.sh/ruff/rules/\#flake8-pyi-pyi)

For more, see [flake8-pyi](https://pypi.org/project/flake8-pyi/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| PYI001 | [unprefixed-type-param](https://docs.astral.sh/ruff/rules/unprefixed-type-param/) | Name of private `{kind}` must start with `_` |  |
| PYI002 | [complex-if-statement-in-stub](https://docs.astral.sh/ruff/rules/complex-if-statement-in-stub/) | `if` test must be a simple comparison against `sys.platform` or `sys.version_info` |  |
| PYI003 | [unrecognized-version-info-check](https://docs.astral.sh/ruff/rules/unrecognized-version-info-check/) | Unrecognized `sys.version_info` check |  |
| PYI004 | [patch-version-comparison](https://docs.astral.sh/ruff/rules/patch-version-comparison/) | Version comparison must use only major and minor version |  |
| PYI005 | [wrong-tuple-length-version-comparison](https://docs.astral.sh/ruff/rules/wrong-tuple-length-version-comparison/) | Version comparison must be against a length-{expected\_length} tuple |  |
| PYI006 | [bad-version-info-comparison](https://docs.astral.sh/ruff/rules/bad-version-info-comparison/) | Use `<` or `>=` for `sys.version_info` comparisons |  |
| PYI007 | [unrecognized-platform-check](https://docs.astral.sh/ruff/rules/unrecognized-platform-check/) | Unrecognized `sys.platform` check |  |
| PYI008 | [unrecognized-platform-name](https://docs.astral.sh/ruff/rules/unrecognized-platform-name/) | Unrecognized platform `{platform}` |  |
| PYI009 | [pass-statement-stub-body](https://docs.astral.sh/ruff/rules/pass-statement-stub-body/) | Empty body should contain `...`, not `pass` | 🛠️ |
| PYI010 | [non-empty-stub-body](https://docs.astral.sh/ruff/rules/non-empty-stub-body/) | Function body must contain only `...` | 🛠️ |
| PYI011 | [typed-argument-default-in-stub](https://docs.astral.sh/ruff/rules/typed-argument-default-in-stub/) | Only simple default values allowed for typed arguments | 🛠️ |
| PYI012 | [pass-in-class-body](https://docs.astral.sh/ruff/rules/pass-in-class-body/) | Class body must not contain `pass` | 🛠️ |
| PYI013 | [ellipsis-in-non-empty-class-body](https://docs.astral.sh/ruff/rules/ellipsis-in-non-empty-class-body/) | Non-empty class body must not contain `...` | 🛠️ |
| PYI014 | [argument-default-in-stub](https://docs.astral.sh/ruff/rules/argument-default-in-stub/) | Only simple default values allowed for arguments | 🛠️ |
| PYI015 | [assignment-default-in-stub](https://docs.astral.sh/ruff/rules/assignment-default-in-stub/) | Only simple default values allowed for assignments | 🛠️ |
| PYI016 | [duplicate-union-member](https://docs.astral.sh/ruff/rules/duplicate-union-member/) | Duplicate union member `{}` | 🛠️ |
| PYI017 | [complex-assignment-in-stub](https://docs.astral.sh/ruff/rules/complex-assignment-in-stub/) | Stubs should not contain assignments to attributes or multiple targets |  |
| PYI018 | [unused-private-type-var](https://docs.astral.sh/ruff/rules/unused-private-type-var/) | Private {type\_var\_like\_kind} `{type_var_like_name}` is never used | 🛠️ |
| PYI019 | [custom-type-var-for-self](https://docs.astral.sh/ruff/rules/custom-type-var-for-self/) | Use `Self` instead of custom TypeVar `{}` | 🛠️ |
| PYI020 | [quoted-annotation-in-stub](https://docs.astral.sh/ruff/rules/quoted-annotation-in-stub/) | Quoted annotations should not be included in stubs | 🛠️ |
| PYI021 | [docstring-in-stub](https://docs.astral.sh/ruff/rules/docstring-in-stub/) | Docstrings should not be included in stubs | 🛠️ |
| PYI024 | [collections-named-tuple](https://docs.astral.sh/ruff/rules/collections-named-tuple/) | Use `typing.NamedTuple` instead of `collections.namedtuple` |  |
| PYI025 | [unaliased-collections-abc-set-import](https://docs.astral.sh/ruff/rules/unaliased-collections-abc-set-import/) | Use `from collections.abc import Set as AbstractSet` to avoid confusion with the `set` builtin | 🛠️ |
| PYI026 | [type-alias-without-annotation](https://docs.astral.sh/ruff/rules/type-alias-without-annotation/) | Use `{module}.TypeAlias` for type alias, e.g., `{name}: TypeAlias = {value}` | 🛠️ |
| PYI029 | [str-or-repr-defined-in-stub](https://docs.astral.sh/ruff/rules/str-or-repr-defined-in-stub/) | Defining `{name}` in a stub is almost always redundant | 🛠️ |
| PYI030 | [unnecessary-literal-union](https://docs.astral.sh/ruff/rules/unnecessary-literal-union/) | Multiple literal members in a union. Use a single literal, e.g. `Literal[{}]` | 🛠️ |
| PYI032 | [any-eq-ne-annotation](https://docs.astral.sh/ruff/rules/any-eq-ne-annotation/) | Prefer `object` to `Any` for the second parameter to `{method_name}` | 🛠️ |
| PYI033 | [type-comment-in-stub](https://docs.astral.sh/ruff/rules/type-comment-in-stub/) | Don't use type comments in stub file |  |
| PYI034 | [non-self-return-type](https://docs.astral.sh/ruff/rules/non-self-return-type/) | `__new__` methods usually return `self` at runtime | 🛠️ |
| PYI035 | [unassigned-special-variable-in-stub](https://docs.astral.sh/ruff/rules/unassigned-special-variable-in-stub/) | `{name}` in a stub file must have a value, as it has the same semantics as `{name}` at runtime |  |
| PYI036 | [bad-exit-annotation](https://docs.astral.sh/ruff/rules/bad-exit-annotation/) | Star-args in `{method_name}` should be annotated with `object` | 🛠️ |
| PYI041 | [redundant-numeric-union](https://docs.astral.sh/ruff/rules/redundant-numeric-union/) | Use `{supertype}` instead of `{subtype} | {supertype}` | 🛠️ |
| PYI042 | [snake-case-type-alias](https://docs.astral.sh/ruff/rules/snake-case-type-alias/) | Type alias `{name}` should be CamelCase |  |
| PYI043 | [t-suffixed-type-alias](https://docs.astral.sh/ruff/rules/t-suffixed-type-alias/) | Private type alias `{name}` should not be suffixed with `T` (the `T` suffix implies that an object is a `TypeVar`) |  |
| PYI044 | [future-annotations-in-stub](https://docs.astral.sh/ruff/rules/future-annotations-in-stub/) | `from __future__ import annotations` has no effect in stub files, since type checkers automatically treat stubs as having those semantics | 🛠️ |
| PYI045 | [iter-method-return-iterable](https://docs.astral.sh/ruff/rules/iter-method-return-iterable/) | `__aiter__` methods should return an `AsyncIterator`, not an `AsyncIterable` |  |
| PYI046 | [unused-private-protocol](https://docs.astral.sh/ruff/rules/unused-private-protocol/) | Private protocol `{name}` is never used |  |
| PYI047 | [unused-private-type-alias](https://docs.astral.sh/ruff/rules/unused-private-type-alias/) | Private TypeAlias `{name}` is never used |  |
| PYI048 | [stub-body-multiple-statements](https://docs.astral.sh/ruff/rules/stub-body-multiple-statements/) | Function body must contain exactly one statement |  |
| PYI049 | [unused-private-typed-dict](https://docs.astral.sh/ruff/rules/unused-private-typed-dict/) | Private TypedDict `{name}` is never used |  |
| PYI050 | [no-return-argument-annotation-in-stub](https://docs.astral.sh/ruff/rules/no-return-argument-annotation-in-stub/) | Prefer `{module}.Never` over `NoReturn` for argument annotations |  |
| PYI051 | [redundant-literal-union](https://docs.astral.sh/ruff/rules/redundant-literal-union/) | `Literal[{literal}]` is redundant in a union with `{builtin_type}` |  |
| PYI052 | [unannotated-assignment-in-stub](https://docs.astral.sh/ruff/rules/unannotated-assignment-in-stub/) | Need type annotation for `{name}` |  |
| PYI053 | [string-or-bytes-too-long](https://docs.astral.sh/ruff/rules/string-or-bytes-too-long/) | String and bytes literals longer than 50 characters are not permitted | 🛠️ |
| PYI054 | [numeric-literal-too-long](https://docs.astral.sh/ruff/rules/numeric-literal-too-long/) | Numeric literals with a string representation longer than ten characters are not permitted | 🛠️ |
| PYI055 | [unnecessary-type-union](https://docs.astral.sh/ruff/rules/unnecessary-type-union/) | Multiple `type` members in a union. Combine them into one, e.g., `type[{union_str}]`. | 🛠️ |
| PYI056 | [unsupported-method-call-on-all](https://docs.astral.sh/ruff/rules/unsupported-method-call-on-all/) | Calling `.{name}()` on `__all__` may not be supported by all type checkers (use `+=` instead) |  |
| PYI057 | [byte-string-usage](https://docs.astral.sh/ruff/rules/byte-string-usage/) | Do not use `{origin}.ByteString`, which has unclear semantics and is deprecated |  |
| PYI058 | [generator-return-from-iter-method](https://docs.astral.sh/ruff/rules/generator-return-from-iter-method/) | Use `{return_type}` as the return value for simple `{method}` methods | 🛠️ |
| PYI059 | [generic-not-last-base-class](https://docs.astral.sh/ruff/rules/generic-not-last-base-class/) | `Generic[]` should always be the last base class | 🧪🛠️ |
| PYI061 | [redundant-none-literal](https://docs.astral.sh/ruff/rules/redundant-none-literal/) | Use `None` rather than `Literal[None]` | 🧪🛠️ |
| PYI062 | [duplicate-literal-member](https://docs.astral.sh/ruff/rules/duplicate-literal-member/) | Duplicate literal member `{}` | 🛠️ |
| PYI063 | [pep484-style-positional-only-parameter](https://docs.astral.sh/ruff/rules/pep484-style-positional-only-parameter/) | Use PEP 570 syntax for positional-only parameters |  |
| PYI064 | [redundant-final-literal](https://docs.astral.sh/ruff/rules/redundant-final-literal/) | `Final[Literal[{literal}]]` can be replaced with a bare `Final` | 🛠️ |
| PYI066 | [bad-version-info-order](https://docs.astral.sh/ruff/rules/bad-version-info-order/) | Put branches for newer Python versions first when branching on `sys.version_info` comparisons |  |

## [flake8-pytest-style (PT)](https://docs.astral.sh/ruff/rules/\#flake8-pytest-style-pt)

For more, see [flake8-pytest-style](https://pypi.org/project/flake8-pytest-style/) on PyPI.

For related settings, see [flake8-pytest-style](https://docs.astral.sh/ruff/settings/#lintflake8-pytest-style).

| Code | Name | Message |  |
| --- | --- | --- | --- |
| PT001 | [pytest-fixture-incorrect-parentheses-style](https://docs.astral.sh/ruff/rules/pytest-fixture-incorrect-parentheses-style/) | Use `@pytest.fixture{expected}` over `@pytest.fixture{actual}` | 🛠️ |
| PT002 | [pytest-fixture-positional-args](https://docs.astral.sh/ruff/rules/pytest-fixture-positional-args/) | Configuration for fixture `{function}` specified via positional args, use kwargs |  |
| PT003 | [pytest-extraneous-scope-function](https://docs.astral.sh/ruff/rules/pytest-extraneous-scope-function/) | `scope='function'` is implied in `@pytest.fixture()` | 🛠️ |
| PT004 | [pytest-missing-fixture-name-underscore](https://docs.astral.sh/ruff/rules/pytest-missing-fixture-name-underscore/) | Fixture `{function}` does not return anything, add leading underscore | ❌ |
| PT005 | [pytest-incorrect-fixture-name-underscore](https://docs.astral.sh/ruff/rules/pytest-incorrect-fixture-name-underscore/) | Fixture `{function}` returns a value, remove leading underscore | ❌ |
| PT006 | [pytest-parametrize-names-wrong-type](https://docs.astral.sh/ruff/rules/pytest-parametrize-names-wrong-type/) | Wrong type passed to first argument of `pytest.mark.parametrize`; expected {expected\_string} | 🛠️ |
| PT007 | [pytest-parametrize-values-wrong-type](https://docs.astral.sh/ruff/rules/pytest-parametrize-values-wrong-type/) | Wrong values type in `pytest.mark.parametrize` expected `{values}` of `{row}` | 🛠️ |
| PT008 | [pytest-patch-with-lambda](https://docs.astral.sh/ruff/rules/pytest-patch-with-lambda/) | Use `return_value=` instead of patching with `lambda` |  |
| PT009 | [pytest-unittest-assertion](https://docs.astral.sh/ruff/rules/pytest-unittest-assertion/) | Use a regular `assert` instead of unittest-style `{assertion}` | 🛠️ |
| PT010 | [pytest-raises-without-exception](https://docs.astral.sh/ruff/rules/pytest-raises-without-exception/) | Set the expected exception in `pytest.raises()` |  |
| PT011 | [pytest-raises-too-broad](https://docs.astral.sh/ruff/rules/pytest-raises-too-broad/) | `pytest.raises({exception})` is too broad, set the `match` parameter or use a more specific exception |  |
| PT012 | [pytest-raises-with-multiple-statements](https://docs.astral.sh/ruff/rules/pytest-raises-with-multiple-statements/) | `pytest.raises()` block should contain a single simple statement |  |
| PT013 | [pytest-incorrect-pytest-import](https://docs.astral.sh/ruff/rules/pytest-incorrect-pytest-import/) | Incorrect import of `pytest`; use `import pytest` instead |  |
| PT014 | [pytest-duplicate-parametrize-test-cases](https://docs.astral.sh/ruff/rules/pytest-duplicate-parametrize-test-cases/) | Duplicate of test case at index {index} in `pytest.mark.parametrize` | 🛠️ |
| PT015 | [pytest-assert-always-false](https://docs.astral.sh/ruff/rules/pytest-assert-always-false/) | Assertion always fails, replace with `pytest.fail()` |  |
| PT016 | [pytest-fail-without-message](https://docs.astral.sh/ruff/rules/pytest-fail-without-message/) | No message passed to `pytest.fail()` |  |
| PT017 | [pytest-assert-in-except](https://docs.astral.sh/ruff/rules/pytest-assert-in-except/) | Found assertion on exception `{name}` in `except` block, use `pytest.raises()` instead |  |
| PT018 | [pytest-composite-assertion](https://docs.astral.sh/ruff/rules/pytest-composite-assertion/) | Assertion should be broken down into multiple parts | 🛠️ |
| PT019 | [pytest-fixture-param-without-value](https://docs.astral.sh/ruff/rules/pytest-fixture-param-without-value/) | Fixture `{name}` without value is injected as parameter, use `@pytest.mark.usefixtures` instead |  |
| PT020 | [pytest-deprecated-yield-fixture](https://docs.astral.sh/ruff/rules/pytest-deprecated-yield-fixture/) | `@pytest.yield_fixture` is deprecated, use `@pytest.fixture` |  |
| PT021 | [pytest-fixture-finalizer-callback](https://docs.astral.sh/ruff/rules/pytest-fixture-finalizer-callback/) | Use `yield` instead of `request.addfinalizer` |  |
| PT022 | [pytest-useless-yield-fixture](https://docs.astral.sh/ruff/rules/pytest-useless-yield-fixture/) | No teardown in fixture `{name}`, use `return` instead of `yield` | 🛠️ |
| PT023 | [pytest-incorrect-mark-parentheses-style](https://docs.astral.sh/ruff/rules/pytest-incorrect-mark-parentheses-style/) | Use `@pytest.mark.{mark_name}{expected_parens}` over `@pytest.mark.{mark_name}{actual_parens}` | 🛠️ |
| PT024 | [pytest-unnecessary-asyncio-mark-on-fixture](https://docs.astral.sh/ruff/rules/pytest-unnecessary-asyncio-mark-on-fixture/) | `pytest.mark.asyncio` is unnecessary for fixtures | 🛠️ |
| PT025 | [pytest-erroneous-use-fixtures-on-fixture](https://docs.astral.sh/ruff/rules/pytest-erroneous-use-fixtures-on-fixture/) | `pytest.mark.usefixtures` has no effect on fixtures | 🛠️ |
| PT026 | [pytest-use-fixtures-without-parameters](https://docs.astral.sh/ruff/rules/pytest-use-fixtures-without-parameters/) | Useless `pytest.mark.usefixtures` without parameters | 🛠️ |
| PT027 | [pytest-unittest-raises-assertion](https://docs.astral.sh/ruff/rules/pytest-unittest-raises-assertion/) | Use `pytest.raises` instead of unittest-style `{assertion}` | 🛠️ |
| PT028 | [pytest-parameter-with-default-argument](https://docs.astral.sh/ruff/rules/pytest-parameter-with-default-argument/) | Test function parameter `{}` has default argument |  |
| PT029 | [pytest-warns-without-warning](https://docs.astral.sh/ruff/rules/pytest-warns-without-warning/) | Set the expected warning in `pytest.warns()` | 🧪 |
| PT030 | [pytest-warns-too-broad](https://docs.astral.sh/ruff/rules/pytest-warns-too-broad/) | `pytest.warns({warning})` is too broad, set the `match` parameter or use a more specific warning |  |
| PT031 | [pytest-warns-with-multiple-statements](https://docs.astral.sh/ruff/rules/pytest-warns-with-multiple-statements/) | `pytest.warns()` block should contain a single simple statement |  |

## [flake8-quotes (Q)](https://docs.astral.sh/ruff/rules/\#flake8-quotes-q)

For more, see [flake8-quotes](https://pypi.org/project/flake8-quotes/) on PyPI.

For related settings, see [flake8-quotes](https://docs.astral.sh/ruff/settings/#lintflake8-quotes).

| Code | Name | Message |  |
| --- | --- | --- | --- |
| Q000 | [bad-quotes-inline-string](https://docs.astral.sh/ruff/rules/bad-quotes-inline-string/) | Single quotes found but double quotes preferred | 🛠️ |
| Q001 | [bad-quotes-multiline-string](https://docs.astral.sh/ruff/rules/bad-quotes-multiline-string/) | Single quote multiline found but double quotes preferred | 🛠️ |
| Q002 | [bad-quotes-docstring](https://docs.astral.sh/ruff/rules/bad-quotes-docstring/) | Single quote docstring found but double quotes preferred | 🛠️ |
| Q003 | [avoidable-escaped-quote](https://docs.astral.sh/ruff/rules/avoidable-escaped-quote/) | Change outer quotes to avoid escaping inner quotes | 🛠️ |
| Q004 | [unnecessary-escaped-quote](https://docs.astral.sh/ruff/rules/unnecessary-escaped-quote/) | Unnecessary escape on inner quote character | 🛠️ |

## [flake8-raise (RSE)](https://docs.astral.sh/ruff/rules/\#flake8-raise-rse)

For more, see [flake8-raise](https://pypi.org/project/flake8-raise/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| RSE102 | [unnecessary-paren-on-raise-exception](https://docs.astral.sh/ruff/rules/unnecessary-paren-on-raise-exception/) | Unnecessary parentheses on raised exception | 🛠️ |

## [flake8-return (RET)](https://docs.astral.sh/ruff/rules/\#flake8-return-ret)

For more, see [flake8-return](https://pypi.org/project/flake8-return/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| RET501 | [unnecessary-return-none](https://docs.astral.sh/ruff/rules/unnecessary-return-none/) | Do not explicitly `return None` in function if it is the only possible return value | 🛠️ |
| RET502 | [implicit-return-value](https://docs.astral.sh/ruff/rules/implicit-return-value/) | Do not implicitly `return None` in function able to return non- `None` value | 🛠️ |
| RET503 | [implicit-return](https://docs.astral.sh/ruff/rules/implicit-return/) | Missing explicit `return` at the end of function able to return non- `None` value | 🛠️ |
| RET504 | [unnecessary-assign](https://docs.astral.sh/ruff/rules/unnecessary-assign/) | Unnecessary assignment to `{name}` before `return` statement | 🛠️ |
| RET505 | [superfluous-else-return](https://docs.astral.sh/ruff/rules/superfluous-else-return/) | Unnecessary `{branch}` after `return` statement | 🛠️ |
| RET506 | [superfluous-else-raise](https://docs.astral.sh/ruff/rules/superfluous-else-raise/) | Unnecessary `{branch}` after `raise` statement | 🛠️ |
| RET507 | [superfluous-else-continue](https://docs.astral.sh/ruff/rules/superfluous-else-continue/) | Unnecessary `{branch}` after `continue` statement | 🛠️ |
| RET508 | [superfluous-else-break](https://docs.astral.sh/ruff/rules/superfluous-else-break/) | Unnecessary `{branch}` after `break` statement | 🛠️ |

## [flake8-self (SLF)](https://docs.astral.sh/ruff/rules/\#flake8-self-slf)

For more, see [flake8-self](https://pypi.org/project/flake8-self/) on PyPI.

For related settings, see [flake8-self](https://docs.astral.sh/ruff/settings/#lintflake8-self).

| Code | Name | Message |  |
| --- | --- | --- | --- |
| SLF001 | [private-member-access](https://docs.astral.sh/ruff/rules/private-member-access/) | Private member accessed: `{access}` |  |

## [flake8-simplify (SIM)](https://docs.astral.sh/ruff/rules/\#flake8-simplify-sim)

For more, see [flake8-simplify](https://pypi.org/project/flake8-simplify/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| SIM101 | [duplicate-isinstance-call](https://docs.astral.sh/ruff/rules/duplicate-isinstance-call/) | Multiple `isinstance` calls for `{name}`, merge into a single call | 🛠️ |
| SIM102 | [collapsible-if](https://docs.astral.sh/ruff/rules/collapsible-if/) | Use a single `if` statement instead of nested `if` statements | 🛠️ |
| SIM103 | [needless-bool](https://docs.astral.sh/ruff/rules/needless-bool/) | Return the condition `{condition}` directly | 🛠️ |
| SIM105 | [suppressible-exception](https://docs.astral.sh/ruff/rules/suppressible-exception/) | Use `contextlib.suppress({exception})` instead of `try`- `except`- `pass` | 🛠️ |
| SIM107 | [return-in-try-except-finally](https://docs.astral.sh/ruff/rules/return-in-try-except-finally/) | Don't use `return` in `try`- `except` and `finally` |  |
| SIM108 | [if-else-block-instead-of-if-exp](https://docs.astral.sh/ruff/rules/if-else-block-instead-of-if-exp/) | Use ternary operator `{contents}` instead of `if`- `else`-block | 🛠️ |
| SIM109 | [compare-with-tuple](https://docs.astral.sh/ruff/rules/compare-with-tuple/) | Use `{replacement}` instead of multiple equality comparisons | 🛠️ |
| SIM110 | [reimplemented-builtin](https://docs.astral.sh/ruff/rules/reimplemented-builtin/) | Use `{replacement}` instead of `for` loop | 🛠️ |
| SIM112 | [uncapitalized-environment-variables](https://docs.astral.sh/ruff/rules/uncapitalized-environment-variables/) | Use capitalized environment variable `{expected}` instead of `{actual}` | 🛠️ |
| SIM113 | [enumerate-for-loop](https://docs.astral.sh/ruff/rules/enumerate-for-loop/) | Use `enumerate()` for index variable `{index}` in `for` loop |  |
| SIM114 | [if-with-same-arms](https://docs.astral.sh/ruff/rules/if-with-same-arms/) | Combine `if` branches using logical `or` operator | 🛠️ |
| SIM115 | [open-file-with-context-handler](https://docs.astral.sh/ruff/rules/open-file-with-context-handler/) | Use a context manager for opening files |  |
| SIM116 | [if-else-block-instead-of-dict-lookup](https://docs.astral.sh/ruff/rules/if-else-block-instead-of-dict-lookup/) | Use a dictionary instead of consecutive `if` statements |  |
| SIM117 | [multiple-with-statements](https://docs.astral.sh/ruff/rules/multiple-with-statements/) | Use a single `with` statement with multiple contexts instead of nested `with` statements | 🛠️ |
| SIM118 | [in-dict-keys](https://docs.astral.sh/ruff/rules/in-dict-keys/) | Use `key {operator} dict` instead of `key {operator} dict.keys()` | 🛠️ |
| SIM201 | [negate-equal-op](https://docs.astral.sh/ruff/rules/negate-equal-op/) | Use `{left} != {right}` instead of `not {left} == {right}` | 🛠️ |
| SIM202 | [negate-not-equal-op](https://docs.astral.sh/ruff/rules/negate-not-equal-op/) | Use `{left} == {right}` instead of `not {left} != {right}` | 🛠️ |
| SIM208 | [double-negation](https://docs.astral.sh/ruff/rules/double-negation/) | Use `{expr}` instead of `not (not {expr})` | 🛠️ |
| SIM210 | [if-expr-with-true-false](https://docs.astral.sh/ruff/rules/if-expr-with-true-false/) | Remove unnecessary `True if ... else False` | 🛠️ |
| SIM211 | [if-expr-with-false-true](https://docs.astral.sh/ruff/rules/if-expr-with-false-true/) | Use `not ...` instead of `False if ... else True` | 🛠️ |
| SIM212 | [if-expr-with-twisted-arms](https://docs.astral.sh/ruff/rules/if-expr-with-twisted-arms/) | Use `{expr_else} if {expr_else} else {expr_body}` instead of `{expr_body} if not {expr_else} else {expr_else}` | 🛠️ |
| SIM220 | [expr-and-not-expr](https://docs.astral.sh/ruff/rules/expr-and-not-expr/) | Use `False` instead of `{name} and not {name}` | 🛠️ |
| SIM221 | [expr-or-not-expr](https://docs.astral.sh/ruff/rules/expr-or-not-expr/) | Use `True` instead of `{name} or not {name}` | 🛠️ |
| SIM222 | [expr-or-true](https://docs.astral.sh/ruff/rules/expr-or-true/) | Use `{expr}` instead of `{replaced}` | 🛠️ |
| SIM223 | [expr-and-false](https://docs.astral.sh/ruff/rules/expr-and-false/) | Use `{expr}` instead of `{replaced}` | 🛠️ |
| SIM300 | [yoda-conditions](https://docs.astral.sh/ruff/rules/yoda-conditions/) | Yoda condition detected | 🛠️ |
| SIM401 | [if-else-block-instead-of-dict-get](https://docs.astral.sh/ruff/rules/if-else-block-instead-of-dict-get/) | Use `{contents}` instead of an `if` block | 🛠️ |
| SIM905 | [split-static-string](https://docs.astral.sh/ruff/rules/split-static-string/) | Consider using a list literal instead of `str.split` | 🛠️ |
| SIM910 | [dict-get-with-none-default](https://docs.astral.sh/ruff/rules/dict-get-with-none-default/) | Use `{expected}` instead of `{actual}` | 🛠️ |
| SIM911 | [zip-dict-keys-and-values](https://docs.astral.sh/ruff/rules/zip-dict-keys-and-values/) | Use `{expected}` instead of `{actual}` | 🛠️ |

## [flake8-slots (SLOT)](https://docs.astral.sh/ruff/rules/\#flake8-slots-slot)

For more, see [flake8-slots](https://pypi.org/project/flake8-slots/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| SLOT000 | [no-slots-in-str-subclass](https://docs.astral.sh/ruff/rules/no-slots-in-str-subclass/) | Subclasses of `str` should define `__slots__` |  |
| SLOT001 | [no-slots-in-tuple-subclass](https://docs.astral.sh/ruff/rules/no-slots-in-tuple-subclass/) | Subclasses of `tuple` should define `__slots__` |  |
| SLOT002 | [no-slots-in-namedtuple-subclass](https://docs.astral.sh/ruff/rules/no-slots-in-namedtuple-subclass/) | Subclasses of {namedtuple\_kind} should define `__slots__` |  |

## [flake8-tidy-imports (TID)](https://docs.astral.sh/ruff/rules/\#flake8-tidy-imports-tid)

For more, see [flake8-tidy-imports](https://pypi.org/project/flake8-tidy-imports/) on PyPI.

For related settings, see [flake8-tidy-imports](https://docs.astral.sh/ruff/settings/#lintflake8-tidy-imports).

| Code | Name | Message |  |
| --- | --- | --- | --- |
| TID251 | [banned-api](https://docs.astral.sh/ruff/rules/banned-api/) | `{name}` is banned: {message} |  |
| TID252 | [relative-imports](https://docs.astral.sh/ruff/rules/relative-imports/) | Prefer absolute imports over relative imports from parent modules | 🛠️ |
| TID253 | [banned-module-level-imports](https://docs.astral.sh/ruff/rules/banned-module-level-imports/) | `{name}` is banned at the module level |  |

## [flake8-todos (TD)](https://docs.astral.sh/ruff/rules/\#flake8-todos-td)

For more, see [flake8-todos](https://github.com/orsinium-labs/flake8-todos/) on GitHub.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| TD001 | [invalid-todo-tag](https://docs.astral.sh/ruff/rules/invalid-todo-tag/) | Invalid TODO tag: `{tag}` |  |
| TD002 | [missing-todo-author](https://docs.astral.sh/ruff/rules/missing-todo-author/) | Missing author in TODO; try: `# TODO(<author_name>): ...` or `# TODO @<author_name>: ...` |  |
| TD003 | [missing-todo-link](https://docs.astral.sh/ruff/rules/missing-todo-link/) | Missing issue link for this TODO |  |
| TD004 | [missing-todo-colon](https://docs.astral.sh/ruff/rules/missing-todo-colon/) | Missing colon in TODO |  |
| TD005 | [missing-todo-description](https://docs.astral.sh/ruff/rules/missing-todo-description/) | Missing issue description after `TODO` |  |
| TD006 | [invalid-todo-capitalization](https://docs.astral.sh/ruff/rules/invalid-todo-capitalization/) | Invalid TODO capitalization: `{tag}` should be `TODO` | 🛠️ |
| TD007 | [missing-space-after-todo-colon](https://docs.astral.sh/ruff/rules/missing-space-after-todo-colon/) | Missing space after colon in TODO |  |

## [flake8-type-checking (TC)](https://docs.astral.sh/ruff/rules/\#flake8-type-checking-tc)

For more, see [flake8-type-checking](https://pypi.org/project/flake8-type-checking/) on PyPI.

For related settings, see [flake8-type-checking](https://docs.astral.sh/ruff/settings/#lintflake8-type-checking).

| Code | Name | Message |  |
| --- | --- | --- | --- |
| TC001 | [typing-only-first-party-import](https://docs.astral.sh/ruff/rules/typing-only-first-party-import/) | Move application import `{}` into a type-checking block | 🛠️ |
| TC002 | [typing-only-third-party-import](https://docs.astral.sh/ruff/rules/typing-only-third-party-import/) | Move third-party import `{}` into a type-checking block | 🛠️ |
| TC003 | [typing-only-standard-library-import](https://docs.astral.sh/ruff/rules/typing-only-standard-library-import/) | Move standard library import `{}` into a type-checking block | 🛠️ |
| TC004 | [runtime-import-in-type-checking-block](https://docs.astral.sh/ruff/rules/runtime-import-in-type-checking-block/) | Move import `{qualified_name}` out of type-checking block. Import is used for more than type hinting. | 🛠️ |
| TC005 | [empty-type-checking-block](https://docs.astral.sh/ruff/rules/empty-type-checking-block/) | Found empty type-checking block | 🛠️ |
| TC006 | [runtime-cast-value](https://docs.astral.sh/ruff/rules/runtime-cast-value/) | Add quotes to type expression in `typing.cast()` | 🛠️ |
| TC007 | [unquoted-type-alias](https://docs.astral.sh/ruff/rules/unquoted-type-alias/) | Add quotes to type alias | 🛠️ |
| TC008 | [quoted-type-alias](https://docs.astral.sh/ruff/rules/quoted-type-alias/) | Remove quotes from type alias | 🧪🛠️ |
| TC010 | [runtime-string-union](https://docs.astral.sh/ruff/rules/runtime-string-union/) | Invalid string member in `X | Y`-style union type |  |

## [flake8-unused-arguments (ARG)](https://docs.astral.sh/ruff/rules/\#flake8-unused-arguments-arg)

For more, see [flake8-unused-arguments](https://pypi.org/project/flake8-unused-arguments/) on PyPI.

For related settings, see [flake8-unused-arguments](https://docs.astral.sh/ruff/settings/#lintflake8-unused-arguments).

| Code | Name | Message |  |
| --- | --- | --- | --- |
| ARG001 | [unused-function-argument](https://docs.astral.sh/ruff/rules/unused-function-argument/) | Unused function argument: `{name}` |  |
| ARG002 | [unused-method-argument](https://docs.astral.sh/ruff/rules/unused-method-argument/) | Unused method argument: `{name}` |  |
| ARG003 | [unused-class-method-argument](https://docs.astral.sh/ruff/rules/unused-class-method-argument/) | Unused class method argument: `{name}` |  |
| ARG004 | [unused-static-method-argument](https://docs.astral.sh/ruff/rules/unused-static-method-argument/) | Unused static method argument: `{name}` |  |
| ARG005 | [unused-lambda-argument](https://docs.astral.sh/ruff/rules/unused-lambda-argument/) | Unused lambda argument: `{name}` |  |

## [flake8-use-pathlib (PTH)](https://docs.astral.sh/ruff/rules/\#flake8-use-pathlib-pth)

For more, see [flake8-use-pathlib](https://pypi.org/project/flake8-use-pathlib/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| PTH100 | [os-path-abspath](https://docs.astral.sh/ruff/rules/os-path-abspath/) | `os.path.abspath()` should be replaced by `Path.resolve()` | 🛠️ |
| PTH101 | [os-chmod](https://docs.astral.sh/ruff/rules/os-chmod/) | `os.chmod()` should be replaced by `Path.chmod()` | 🛠️ |
| PTH102 | [os-mkdir](https://docs.astral.sh/ruff/rules/os-mkdir/) | `os.mkdir()` should be replaced by `Path.mkdir()` | 🛠️ |
| PTH103 | [os-makedirs](https://docs.astral.sh/ruff/rules/os-makedirs/) | `os.makedirs()` should be replaced by `Path.mkdir(parents=True)` | 🛠️ |
| PTH104 | [os-rename](https://docs.astral.sh/ruff/rules/os-rename/) | `os.rename()` should be replaced by `Path.rename()` | 🛠️ |
| PTH105 | [os-replace](https://docs.astral.sh/ruff/rules/os-replace/) | `os.replace()` should be replaced by `Path.replace()` | 🛠️ |
| PTH106 | [os-rmdir](https://docs.astral.sh/ruff/rules/os-rmdir/) | `os.rmdir()` should be replaced by `Path.rmdir()` | 🛠️ |
| PTH107 | [os-remove](https://docs.astral.sh/ruff/rules/os-remove/) | `os.remove()` should be replaced by `Path.unlink()` | 🛠️ |
| PTH108 | [os-unlink](https://docs.astral.sh/ruff/rules/os-unlink/) | `os.unlink()` should be replaced by `Path.unlink()` | 🛠️ |
| PTH109 | [os-getcwd](https://docs.astral.sh/ruff/rules/os-getcwd/) | `os.getcwd()` should be replaced by `Path.cwd()` | 🛠️ |
| PTH110 | [os-path-exists](https://docs.astral.sh/ruff/rules/os-path-exists/) | `os.path.exists()` should be replaced by `Path.exists()` | 🛠️ |
| PTH111 | [os-path-expanduser](https://docs.astral.sh/ruff/rules/os-path-expanduser/) | `os.path.expanduser()` should be replaced by `Path.expanduser()` | 🛠️ |
| PTH112 | [os-path-isdir](https://docs.astral.sh/ruff/rules/os-path-isdir/) | `os.path.isdir()` should be replaced by `Path.is_dir()` | 🛠️ |
| PTH113 | [os-path-isfile](https://docs.astral.sh/ruff/rules/os-path-isfile/) | `os.path.isfile()` should be replaced by `Path.is_file()` | 🛠️ |
| PTH114 | [os-path-islink](https://docs.astral.sh/ruff/rules/os-path-islink/) | `os.path.islink()` should be replaced by `Path.is_symlink()` | 🛠️ |
| PTH115 | [os-readlink](https://docs.astral.sh/ruff/rules/os-readlink/) | `os.readlink()` should be replaced by `Path.readlink()` | 🛠️ |
| PTH116 | [os-stat](https://docs.astral.sh/ruff/rules/os-stat/) | `os.stat()` should be replaced by `Path.stat()`, `Path.owner()`, or `Path.group()` |  |
| PTH117 | [os-path-isabs](https://docs.astral.sh/ruff/rules/os-path-isabs/) | `os.path.isabs()` should be replaced by `Path.is_absolute()` | 🛠️ |
| PTH118 | [os-path-join](https://docs.astral.sh/ruff/rules/os-path-join/) | `os.{module}.join()` should be replaced by `Path` with `/` operator |  |
| PTH119 | [os-path-basename](https://docs.astral.sh/ruff/rules/os-path-basename/) | `os.path.basename()` should be replaced by `Path.name` | 🛠️ |
| PTH120 | [os-path-dirname](https://docs.astral.sh/ruff/rules/os-path-dirname/) | `os.path.dirname()` should be replaced by `Path.parent` | 🛠️ |
| PTH121 | [os-path-samefile](https://docs.astral.sh/ruff/rules/os-path-samefile/) | `os.path.samefile()` should be replaced by `Path.samefile()` | 🛠️ |
| PTH122 | [os-path-splitext](https://docs.astral.sh/ruff/rules/os-path-splitext/) | `os.path.splitext()` should be replaced by `Path.suffix`, `Path.stem`, and `Path.parent` |  |
| PTH123 | [builtin-open](https://docs.astral.sh/ruff/rules/builtin-open/) | `open()` should be replaced by `Path.open()` |  |
| PTH124 | [py-path](https://docs.astral.sh/ruff/rules/py-path/) | `py.path` is in maintenance mode, use `pathlib` instead |  |
| PTH201 | [path-constructor-current-directory](https://docs.astral.sh/ruff/rules/path-constructor-current-directory/) | Do not pass the current directory explicitly to `Path` | 🛠️ |
| PTH202 | [os-path-getsize](https://docs.astral.sh/ruff/rules/os-path-getsize/) | `os.path.getsize` should be replaced by `Path.stat().st_size` | 🛠️ |
| PTH203 | [os-path-getatime](https://docs.astral.sh/ruff/rules/os-path-getatime/) | `os.path.getatime` should be replaced by `Path.stat().st_atime` | 🛠️ |
| PTH204 | [os-path-getmtime](https://docs.astral.sh/ruff/rules/os-path-getmtime/) | `os.path.getmtime` should be replaced by `Path.stat().st_mtime` | 🛠️ |
| PTH205 | [os-path-getctime](https://docs.astral.sh/ruff/rules/os-path-getctime/) | `os.path.getctime` should be replaced by `Path.stat().st_ctime` | 🛠️ |
| PTH206 | [os-sep-split](https://docs.astral.sh/ruff/rules/os-sep-split/) | Replace `.split(os.sep)` with `Path.parts` |  |
| PTH207 | [glob](https://docs.astral.sh/ruff/rules/glob/) | Replace `{function}` with `Path.glob` or `Path.rglob` |  |
| PTH208 | [os-listdir](https://docs.astral.sh/ruff/rules/os-listdir/) | Use `pathlib.Path.iterdir()` instead. |  |
| PTH210 | [invalid-pathlib-with-suffix](https://docs.astral.sh/ruff/rules/invalid-pathlib-with-suffix/) | Invalid suffix passed to `.with_suffix()` | 🛠️ |
| PTH211 | [os-symlink](https://docs.astral.sh/ruff/rules/os-symlink/) | `os.symlink` should be replaced by `Path.symlink_to` | 🧪 |

## [flynt (FLY)](https://docs.astral.sh/ruff/rules/\#flynt-fly)

For more, see [flynt](https://pypi.org/project/flynt/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| FLY002 | [static-join-to-f-string](https://docs.astral.sh/ruff/rules/static-join-to-f-string/) | Consider `{expression}` instead of string join | 🛠️ |

## [isort (I)](https://docs.astral.sh/ruff/rules/\#isort-i)

For more, see [isort](https://pypi.org/project/isort/) on PyPI.

For related settings, see [isort](https://docs.astral.sh/ruff/settings/#lintisort).

| Code | Name | Message |  |
| --- | --- | --- | --- |
| I001 | [unsorted-imports](https://docs.astral.sh/ruff/rules/unsorted-imports/) | Import block is un-sorted or un-formatted | 🛠️ |
| I002 | [missing-required-import](https://docs.astral.sh/ruff/rules/missing-required-import/) | Missing required import: `{name}` | 🛠️ |

## [mccabe (C90)](https://docs.astral.sh/ruff/rules/\#mccabe-c90)

For more, see [mccabe](https://pypi.org/project/mccabe/) on PyPI.

For related settings, see [mccabe](https://docs.astral.sh/ruff/settings/#lintmccabe).

| Code | Name | Message |  |
| --- | --- | --- | --- |
| C901 | [complex-structure](https://docs.astral.sh/ruff/rules/complex-structure/) | `{name}` is too complex ({complexity} > {max\_complexity}) |  |

## [NumPy-specific rules (NPY)](https://docs.astral.sh/ruff/rules/\#numpy-specific-rules-npy)

| Code | Name | Message |  |
| --- | --- | --- | --- |
| NPY001 | [numpy-deprecated-type-alias](https://docs.astral.sh/ruff/rules/numpy-deprecated-type-alias/) | Type alias `np.{type_name}` is deprecated, replace with builtin type | 🛠️ |
| NPY002 | [numpy-legacy-random](https://docs.astral.sh/ruff/rules/numpy-legacy-random/) | Replace legacy `np.random.{method_name}` call with `np.random.Generator` |  |
| NPY003 | [numpy-deprecated-function](https://docs.astral.sh/ruff/rules/numpy-deprecated-function/) | `np.{existing}` is deprecated; use `np.{replacement}` instead | 🛠️ |
| NPY201 | [numpy2-deprecation](https://docs.astral.sh/ruff/rules/numpy2-deprecation/) | `np.{existing}` will be removed in NumPy 2.0. {migration\_guide} | 🛠️ |

## [pandas-vet (PD)](https://docs.astral.sh/ruff/rules/\#pandas-vet-pd)

For more, see [pandas-vet](https://pypi.org/project/pandas-vet/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| PD002 | [pandas-use-of-inplace-argument](https://docs.astral.sh/ruff/rules/pandas-use-of-inplace-argument/) | `inplace=True` should be avoided; it has inconsistent behavior | 🛠️ |
| PD003 | [pandas-use-of-dot-is-null](https://docs.astral.sh/ruff/rules/pandas-use-of-dot-is-null/) | `.isna` is preferred to `.isnull`; functionality is equivalent |  |
| PD004 | [pandas-use-of-dot-not-null](https://docs.astral.sh/ruff/rules/pandas-use-of-dot-not-null/) | `.notna` is preferred to `.notnull`; functionality is equivalent |  |
| PD007 | [pandas-use-of-dot-ix](https://docs.astral.sh/ruff/rules/pandas-use-of-dot-ix/) | `.ix` is deprecated; use more explicit `.loc` or `.iloc` |  |
| PD008 | [pandas-use-of-dot-at](https://docs.astral.sh/ruff/rules/pandas-use-of-dot-at/) | Use `.loc` instead of `.at`. If speed is important, use NumPy. |  |
| PD009 | [pandas-use-of-dot-iat](https://docs.astral.sh/ruff/rules/pandas-use-of-dot-iat/) | Use `.iloc` instead of `.iat`. If speed is important, use NumPy. |  |
| PD010 | [pandas-use-of-dot-pivot-or-unstack](https://docs.astral.sh/ruff/rules/pandas-use-of-dot-pivot-or-unstack/) | `.pivot_table` is preferred to `.pivot` or `.unstack`; provides same functionality |  |
| PD011 | [pandas-use-of-dot-values](https://docs.astral.sh/ruff/rules/pandas-use-of-dot-values/) | Use `.to_numpy()` instead of `.values` |  |
| PD012 | [pandas-use-of-dot-read-table](https://docs.astral.sh/ruff/rules/pandas-use-of-dot-read-table/) | Use `.read_csv` instead of `.read_table` to read CSV files |  |
| PD013 | [pandas-use-of-dot-stack](https://docs.astral.sh/ruff/rules/pandas-use-of-dot-stack/) | `.melt` is preferred to `.stack`; provides same functionality |  |
| PD015 | [pandas-use-of-pd-merge](https://docs.astral.sh/ruff/rules/pandas-use-of-pd-merge/) | Use `.merge` method instead of `pd.merge` function. They have equivalent functionality. |  |
| PD101 | [pandas-nunique-constant-series-check](https://docs.astral.sh/ruff/rules/pandas-nunique-constant-series-check/) | Using `series.nunique()` for checking that a series is constant is inefficient |  |
| PD901 | [pandas-df-variable-name](https://docs.astral.sh/ruff/rules/pandas-df-variable-name/) | Avoid using the generic variable name `df` for DataFrames | ⚠️ |

## [pep8-naming (N)](https://docs.astral.sh/ruff/rules/\#pep8-naming-n)

For more, see [pep8-naming](https://pypi.org/project/pep8-naming/) on PyPI.

For related settings, see [pep8-naming](https://docs.astral.sh/ruff/settings/#lintpep8-naming).

| Code | Name | Message |  |
| --- | --- | --- | --- |
| N801 | [invalid-class-name](https://docs.astral.sh/ruff/rules/invalid-class-name/) | Class name `{name}` should use CapWords convention |  |
| N802 | [invalid-function-name](https://docs.astral.sh/ruff/rules/invalid-function-name/) | Function name `{name}` should be lowercase |  |
| N803 | [invalid-argument-name](https://docs.astral.sh/ruff/rules/invalid-argument-name/) | Argument name `{name}` should be lowercase |  |
| N804 | [invalid-first-argument-name-for-class-method](https://docs.astral.sh/ruff/rules/invalid-first-argument-name-for-class-method/) | First argument of a class method should be named `cls` | 🛠️ |
| N805 | [invalid-first-argument-name-for-method](https://docs.astral.sh/ruff/rules/invalid-first-argument-name-for-method/) | First argument of a method should be named `self` | 🛠️ |
| N806 | [non-lowercase-variable-in-function](https://docs.astral.sh/ruff/rules/non-lowercase-variable-in-function/) | Variable `{name}` in function should be lowercase |  |
| N807 | [dunder-function-name](https://docs.astral.sh/ruff/rules/dunder-function-name/) | Function name should not start and end with `__` |  |
| N811 | [constant-imported-as-non-constant](https://docs.astral.sh/ruff/rules/constant-imported-as-non-constant/) | Constant `{name}` imported as non-constant `{asname}` |  |
| N812 | [lowercase-imported-as-non-lowercase](https://docs.astral.sh/ruff/rules/lowercase-imported-as-non-lowercase/) | Lowercase `{name}` imported as non-lowercase `{asname}` |  |
| N813 | [camelcase-imported-as-lowercase](https://docs.astral.sh/ruff/rules/camelcase-imported-as-lowercase/) | Camelcase `{name}` imported as lowercase `{asname}` |  |
| N814 | [camelcase-imported-as-constant](https://docs.astral.sh/ruff/rules/camelcase-imported-as-constant/) | Camelcase `{name}` imported as constant `{asname}` |  |
| N815 | [mixed-case-variable-in-class-scope](https://docs.astral.sh/ruff/rules/mixed-case-variable-in-class-scope/) | Variable `{name}` in class scope should not be mixedCase |  |
| N816 | [mixed-case-variable-in-global-scope](https://docs.astral.sh/ruff/rules/mixed-case-variable-in-global-scope/) | Variable `{name}` in global scope should not be mixedCase |  |
| N817 | [camelcase-imported-as-acronym](https://docs.astral.sh/ruff/rules/camelcase-imported-as-acronym/) | CamelCase `{name}` imported as acronym `{asname}` |  |
| N818 | [error-suffix-on-exception-name](https://docs.astral.sh/ruff/rules/error-suffix-on-exception-name/) | Exception name `{name}` should be named with an Error suffix |  |
| N999 | [invalid-module-name](https://docs.astral.sh/ruff/rules/invalid-module-name/) | Invalid module name: '{name}' |  |

## [Perflint (PERF)](https://docs.astral.sh/ruff/rules/\#perflint-perf)

For more, see [Perflint](https://pypi.org/project/perflint/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| PERF101 | [unnecessary-list-cast](https://docs.astral.sh/ruff/rules/unnecessary-list-cast/) | Do not cast an iterable to `list` before iterating over it | 🛠️ |
| PERF102 | [incorrect-dict-iterator](https://docs.astral.sh/ruff/rules/incorrect-dict-iterator/) | When using only the {subset} of a dict use the `{subset}()` method | 🛠️ |
| PERF203 | [try-except-in-loop](https://docs.astral.sh/ruff/rules/try-except-in-loop/) | `try`- `except` within a loop incurs performance overhead |  |
| PERF401 | [manual-list-comprehension](https://docs.astral.sh/ruff/rules/manual-list-comprehension/) | Use {message\_str} to create a transformed list | 🛠️ |
| PERF402 | [manual-list-copy](https://docs.astral.sh/ruff/rules/manual-list-copy/) | Use `list` or `list.copy` to create a copy of a list |  |
| PERF403 | [manual-dict-comprehension](https://docs.astral.sh/ruff/rules/manual-dict-comprehension/) | Use a dictionary comprehension instead of {modifier} for-loop | 🛠️ |

## [pycodestyle (E, W)](https://docs.astral.sh/ruff/rules/\#pycodestyle-e-w)

For more, see [pycodestyle](https://pypi.org/project/pycodestyle/) on PyPI.

For related settings, see [pycodestyle](https://docs.astral.sh/ruff/settings/#lintpycodestyle).

### [Error (E)](https://docs.astral.sh/ruff/rules/\#error-e)

| Code | Name | Message |  |
| --- | --- | --- | --- |
| E101 | [mixed-spaces-and-tabs](https://docs.astral.sh/ruff/rules/mixed-spaces-and-tabs/) | Indentation contains mixed spaces and tabs |  |
| E111 | [indentation-with-invalid-multiple](https://docs.astral.sh/ruff/rules/indentation-with-invalid-multiple/) | Indentation is not a multiple of {indent\_width} | 🧪 |
| E112 | [no-indented-block](https://docs.astral.sh/ruff/rules/no-indented-block/) | Expected an indented block | 🧪 |
| E113 | [unexpected-indentation](https://docs.astral.sh/ruff/rules/unexpected-indentation/) | Unexpected indentation | 🧪 |
| E114 | [indentation-with-invalid-multiple-comment](https://docs.astral.sh/ruff/rules/indentation-with-invalid-multiple-comment/) | Indentation is not a multiple of {indent\_width} (comment) | 🧪 |
| E115 | [no-indented-block-comment](https://docs.astral.sh/ruff/rules/no-indented-block-comment/) | Expected an indented block (comment) | 🧪 |
| E116 | [unexpected-indentation-comment](https://docs.astral.sh/ruff/rules/unexpected-indentation-comment/) | Unexpected indentation (comment) | 🧪 |
| E117 | [over-indented](https://docs.astral.sh/ruff/rules/over-indented/) | Over-indented (comment) | 🧪 |
| E201 | [whitespace-after-open-bracket](https://docs.astral.sh/ruff/rules/whitespace-after-open-bracket/) | Whitespace after '{symbol}' | 🧪🛠️ |
| E202 | [whitespace-before-close-bracket](https://docs.astral.sh/ruff/rules/whitespace-before-close-bracket/) | Whitespace before '{symbol}' | 🧪🛠️ |
| E203 | [whitespace-before-punctuation](https://docs.astral.sh/ruff/rules/whitespace-before-punctuation/) | Whitespace before '{symbol}' | 🧪🛠️ |
| E204 | [whitespace-after-decorator](https://docs.astral.sh/ruff/rules/whitespace-after-decorator/) | Whitespace after decorator | 🧪🛠️ |
| E211 | [whitespace-before-parameters](https://docs.astral.sh/ruff/rules/whitespace-before-parameters/) | Whitespace before '{bracket}' | 🧪🛠️ |
| E221 | [multiple-spaces-before-operator](https://docs.astral.sh/ruff/rules/multiple-spaces-before-operator/) | Multiple spaces before operator | 🧪🛠️ |
| E222 | [multiple-spaces-after-operator](https://docs.astral.sh/ruff/rules/multiple-spaces-after-operator/) | Multiple spaces after operator | 🧪🛠️ |
| E223 | [tab-before-operator](https://docs.astral.sh/ruff/rules/tab-before-operator/) | Tab before operator | 🧪🛠️ |
| E224 | [tab-after-operator](https://docs.astral.sh/ruff/rules/tab-after-operator/) | Tab after operator | 🧪🛠️ |
| E225 | [missing-whitespace-around-operator](https://docs.astral.sh/ruff/rules/missing-whitespace-around-operator/) | Missing whitespace around operator | 🧪🛠️ |
| E226 | [missing-whitespace-around-arithmetic-operator](https://docs.astral.sh/ruff/rules/missing-whitespace-around-arithmetic-operator/) | Missing whitespace around arithmetic operator | 🧪🛠️ |
| E227 | [missing-whitespace-around-bitwise-or-shift-operator](https://docs.astral.sh/ruff/rules/missing-whitespace-around-bitwise-or-shift-operator/) | Missing whitespace around bitwise or shift operator | 🧪🛠️ |
| E228 | [missing-whitespace-around-modulo-operator](https://docs.astral.sh/ruff/rules/missing-whitespace-around-modulo-operator/) | Missing whitespace around modulo operator | 🧪🛠️ |
| E231 | [missing-whitespace](https://docs.astral.sh/ruff/rules/missing-whitespace/) | Missing whitespace after {} | 🧪🛠️ |
| E241 | [multiple-spaces-after-comma](https://docs.astral.sh/ruff/rules/multiple-spaces-after-comma/) | Multiple spaces after comma | 🧪🛠️ |
| E242 | [tab-after-comma](https://docs.astral.sh/ruff/rules/tab-after-comma/) | Tab after comma | 🧪🛠️ |
| E251 | [unexpected-spaces-around-keyword-parameter-equals](https://docs.astral.sh/ruff/rules/unexpected-spaces-around-keyword-parameter-equals/) | Unexpected spaces around keyword / parameter equals | 🧪🛠️ |
| E252 | [missing-whitespace-around-parameter-equals](https://docs.astral.sh/ruff/rules/missing-whitespace-around-parameter-equals/) | Missing whitespace around parameter equals | 🧪🛠️ |
| E261 | [too-few-spaces-before-inline-comment](https://docs.astral.sh/ruff/rules/too-few-spaces-before-inline-comment/) | Insert at least two spaces before an inline comment | 🧪🛠️ |
| E262 | [no-space-after-inline-comment](https://docs.astral.sh/ruff/rules/no-space-after-inline-comment/) | Inline comment should start with `#` | 🧪🛠️ |
| E265 | [no-space-after-block-comment](https://docs.astral.sh/ruff/rules/no-space-after-block-comment/) | Block comment should start with `#` | 🧪🛠️ |
| E266 | [multiple-leading-hashes-for-block-comment](https://docs.astral.sh/ruff/rules/multiple-leading-hashes-for-block-comment/) | Too many leading `#` before block comment | 🧪🛠️ |
| E271 | [multiple-spaces-after-keyword](https://docs.astral.sh/ruff/rules/multiple-spaces-after-keyword/) | Multiple spaces after keyword | 🧪🛠️ |
| E272 | [multiple-spaces-before-keyword](https://docs.astral.sh/ruff/rules/multiple-spaces-before-keyword/) | Multiple spaces before keyword | 🧪🛠️ |
| E273 | [tab-after-keyword](https://docs.astral.sh/ruff/rules/tab-after-keyword/) | Tab after keyword | 🧪🛠️ |
| E274 | [tab-before-keyword](https://docs.astral.sh/ruff/rules/tab-before-keyword/) | Tab before keyword | 🧪🛠️ |
| E275 | [missing-whitespace-after-keyword](https://docs.astral.sh/ruff/rules/missing-whitespace-after-keyword/) | Missing whitespace after keyword | 🧪🛠️ |
| E301 | [blank-line-between-methods](https://docs.astral.sh/ruff/rules/blank-line-between-methods/) | Expected {BLANK\_LINES\_NESTED\_LEVEL:?} blank line, found 0 | 🧪🛠️ |
| E302 | [blank-lines-top-level](https://docs.astral.sh/ruff/rules/blank-lines-top-level/) | Expected {expected\_blank\_lines:?} blank lines, found {actual\_blank\_lines} | 🧪🛠️ |
| E303 | [too-many-blank-lines](https://docs.astral.sh/ruff/rules/too-many-blank-lines/) | Too many blank lines ({actual\_blank\_lines}) | 🧪🛠️ |
| E304 | [blank-line-after-decorator](https://docs.astral.sh/ruff/rules/blank-line-after-decorator/) | Blank lines found after function decorator ({lines}) | 🧪🛠️ |
| E305 | [blank-lines-after-function-or-class](https://docs.astral.sh/ruff/rules/blank-lines-after-function-or-class/) | Expected 2 blank lines after class or function definition, found ({blank\_lines}) | 🧪🛠️ |
| E306 | [blank-lines-before-nested-definition](https://docs.astral.sh/ruff/rules/blank-lines-before-nested-definition/) | Expected 1 blank line before a nested definition, found 0 | 🧪🛠️ |
| E401 | [multiple-imports-on-one-line](https://docs.astral.sh/ruff/rules/multiple-imports-on-one-line/) | Multiple imports on one line | 🛠️ |
| E402 | [module-import-not-at-top-of-file](https://docs.astral.sh/ruff/rules/module-import-not-at-top-of-file/) | Module level import not at top of cell |  |
| E501 | [line-too-long](https://docs.astral.sh/ruff/rules/line-too-long/) | Line too long ({width} > {limit}) |  |
| E502 | [redundant-backslash](https://docs.astral.sh/ruff/rules/redundant-backslash/) | Redundant backslash | 🧪🛠️ |
| E701 | [multiple-statements-on-one-line-colon](https://docs.astral.sh/ruff/rules/multiple-statements-on-one-line-colon/) | Multiple statements on one line (colon) |  |
| E702 | [multiple-statements-on-one-line-semicolon](https://docs.astral.sh/ruff/rules/multiple-statements-on-one-line-semicolon/) | Multiple statements on one line (semicolon) |  |
| E703 | [useless-semicolon](https://docs.astral.sh/ruff/rules/useless-semicolon/) | Statement ends with an unnecessary semicolon | 🛠️ |
| E711 | [none-comparison](https://docs.astral.sh/ruff/rules/none-comparison/) | Comparison to `None` should be `cond is None` | 🛠️ |
| E712 | [true-false-comparison](https://docs.astral.sh/ruff/rules/true-false-comparison/) | Avoid equality comparisons to `True`; use `{cond}:` for truth checks | 🛠️ |
| E713 | [not-in-test](https://docs.astral.sh/ruff/rules/not-in-test/) | Test for membership should be `not in` | 🛠️ |
| E714 | [not-is-test](https://docs.astral.sh/ruff/rules/not-is-test/) | Test for object identity should be `is not` | 🛠️ |
| E721 | [type-comparison](https://docs.astral.sh/ruff/rules/type-comparison/) | Use `is` and `is not` for type comparisons, or `isinstance()` for isinstance checks |  |
| E722 | [bare-except](https://docs.astral.sh/ruff/rules/bare-except/) | Do not use bare `except` |  |
| E731 | [lambda-assignment](https://docs.astral.sh/ruff/rules/lambda-assignment/) | Do not assign a `lambda` expression, use a `def` | 🛠️ |
| E741 | [ambiguous-variable-name](https://docs.astral.sh/ruff/rules/ambiguous-variable-name/) | Ambiguous variable name: `{name}` |  |
| E742 | [ambiguous-class-name](https://docs.astral.sh/ruff/rules/ambiguous-class-name/) | Ambiguous class name: `{name}` |  |
| E743 | [ambiguous-function-name](https://docs.astral.sh/ruff/rules/ambiguous-function-name/) | Ambiguous function name: `{name}` |  |
| E902 | [io-error](https://docs.astral.sh/ruff/rules/io-error/) | {message} |  |
| E999 | [syntax-error](https://docs.astral.sh/ruff/rules/syntax-error/) | SyntaxError | ❌ |

### [Warning (W)](https://docs.astral.sh/ruff/rules/\#warning-w)

| Code | Name | Message |  |
| --- | --- | --- | --- |
| W191 | [tab-indentation](https://docs.astral.sh/ruff/rules/tab-indentation/) | Indentation contains tabs |  |
| W291 | [trailing-whitespace](https://docs.astral.sh/ruff/rules/trailing-whitespace/) | Trailing whitespace | 🛠️ |
| W292 | [missing-newline-at-end-of-file](https://docs.astral.sh/ruff/rules/missing-newline-at-end-of-file/) | No newline at end of file | 🛠️ |
| W293 | [blank-line-with-whitespace](https://docs.astral.sh/ruff/rules/blank-line-with-whitespace/) | Blank line contains whitespace | 🛠️ |
| W391 | [too-many-newlines-at-end-of-file](https://docs.astral.sh/ruff/rules/too-many-newlines-at-end-of-file/) | Too many newlines at end of {domain} | 🧪🛠️ |
| W505 | [doc-line-too-long](https://docs.astral.sh/ruff/rules/doc-line-too-long/) | Doc line too long ({width} > {limit}) |  |
| W605 | [invalid-escape-sequence](https://docs.astral.sh/ruff/rules/invalid-escape-sequence/) | Invalid escape sequence: `\{ch}` | 🛠️ |

## [pydoclint (DOC)](https://docs.astral.sh/ruff/rules/\#pydoclint-doc)

For more, see [pydoclint](https://pypi.org/project/pydoclint/) on PyPI.

For related settings, see [pydoclint](https://docs.astral.sh/ruff/settings/#lintpydoclint).

| Code | Name | Message |  |
| --- | --- | --- | --- |
| DOC201 | [docstring-missing-returns](https://docs.astral.sh/ruff/rules/docstring-missing-returns/) | `return` is not documented in docstring | 🧪 |
| DOC202 | [docstring-extraneous-returns](https://docs.astral.sh/ruff/rules/docstring-extraneous-returns/) | Docstring should not have a returns section because the function doesn't return anything | 🧪 |
| DOC402 | [docstring-missing-yields](https://docs.astral.sh/ruff/rules/docstring-missing-yields/) | `yield` is not documented in docstring | 🧪 |
| DOC403 | [docstring-extraneous-yields](https://docs.astral.sh/ruff/rules/docstring-extraneous-yields/) | Docstring has a "Yields" section but the function doesn't yield anything | 🧪 |
| DOC501 | [docstring-missing-exception](https://docs.astral.sh/ruff/rules/docstring-missing-exception/) | Raised exception `{id}` missing from docstring | 🧪 |
| DOC502 | [docstring-extraneous-exception](https://docs.astral.sh/ruff/rules/docstring-extraneous-exception/) | Raised exception is not explicitly raised: `{id}` | 🧪 |

## [pydocstyle (D)](https://docs.astral.sh/ruff/rules/\#pydocstyle-d)

For more, see [pydocstyle](https://pypi.org/project/pydocstyle/) on PyPI.

For related settings, see [pydocstyle](https://docs.astral.sh/ruff/settings/#lintpydocstyle).

| Code | Name | Message |  |
| --- | --- | --- | --- |
| D100 | [undocumented-public-module](https://docs.astral.sh/ruff/rules/undocumented-public-module/) | Missing docstring in public module |  |
| D101 | [undocumented-public-class](https://docs.astral.sh/ruff/rules/undocumented-public-class/) | Missing docstring in public class |  |
| D102 | [undocumented-public-method](https://docs.astral.sh/ruff/rules/undocumented-public-method/) | Missing docstring in public method |  |
| D103 | [undocumented-public-function](https://docs.astral.sh/ruff/rules/undocumented-public-function/) | Missing docstring in public function |  |
| D104 | [undocumented-public-package](https://docs.astral.sh/ruff/rules/undocumented-public-package/) | Missing docstring in public package |  |
| D105 | [undocumented-magic-method](https://docs.astral.sh/ruff/rules/undocumented-magic-method/) | Missing docstring in magic method |  |
| D106 | [undocumented-public-nested-class](https://docs.astral.sh/ruff/rules/undocumented-public-nested-class/) | Missing docstring in public nested class |  |
| D107 | [undocumented-public-init](https://docs.astral.sh/ruff/rules/undocumented-public-init/) | Missing docstring in `__init__` |  |
| D200 | [unnecessary-multiline-docstring](https://docs.astral.sh/ruff/rules/unnecessary-multiline-docstring/) | One-line docstring should fit on one line | 🛠️ |
| D201 | [blank-line-before-function](https://docs.astral.sh/ruff/rules/blank-line-before-function/) | No blank lines allowed before function docstring (found {num\_lines}) | 🛠️ |
| D202 | [blank-line-after-function](https://docs.astral.sh/ruff/rules/blank-line-after-function/) | No blank lines allowed after function docstring (found {num\_lines}) | 🛠️ |
| D203 | [incorrect-blank-line-before-class](https://docs.astral.sh/ruff/rules/incorrect-blank-line-before-class/) | 1 blank line required before class docstring | 🛠️ |
| D204 | [incorrect-blank-line-after-class](https://docs.astral.sh/ruff/rules/incorrect-blank-line-after-class/) | 1 blank line required after class docstring | 🛠️ |
| D205 | [missing-blank-line-after-summary](https://docs.astral.sh/ruff/rules/missing-blank-line-after-summary/) | 1 blank line required between summary line and description | 🛠️ |
| D206 | [docstring-tab-indentation](https://docs.astral.sh/ruff/rules/docstring-tab-indentation/) | Docstring should be indented with spaces, not tabs |  |
| D207 | [under-indentation](https://docs.astral.sh/ruff/rules/under-indentation/) | Docstring is under-indented | 🛠️ |
| D208 | [over-indentation](https://docs.astral.sh/ruff/rules/over-indentation/) | Docstring is over-indented | 🛠️ |
| D209 | [new-line-after-last-paragraph](https://docs.astral.sh/ruff/rules/new-line-after-last-paragraph/) | Multi-line docstring closing quotes should be on a separate line | 🛠️ |
| D210 | [surrounding-whitespace](https://docs.astral.sh/ruff/rules/surrounding-whitespace/) | No whitespaces allowed surrounding docstring text | 🛠️ |
| D211 | [blank-line-before-class](https://docs.astral.sh/ruff/rules/blank-line-before-class/) | No blank lines allowed before class docstring | 🛠️ |
| D212 | [multi-line-summary-first-line](https://docs.astral.sh/ruff/rules/multi-line-summary-first-line/) | Multi-line docstring summary should start at the first line | 🛠️ |
| D213 | [multi-line-summary-second-line](https://docs.astral.sh/ruff/rules/multi-line-summary-second-line/) | Multi-line docstring summary should start at the second line | 🛠️ |
| D214 | [overindented-section](https://docs.astral.sh/ruff/rules/overindented-section/) | Section is over-indented ("{name}") | 🛠️ |
| D215 | [overindented-section-underline](https://docs.astral.sh/ruff/rules/overindented-section-underline/) | Section underline is over-indented ("{name}") | 🛠️ |
| D300 | [triple-single-quotes](https://docs.astral.sh/ruff/rules/triple-single-quotes/) | Use triple double quotes `"""` | 🛠️ |
| D301 | [escape-sequence-in-docstring](https://docs.astral.sh/ruff/rules/escape-sequence-in-docstring/) | Use `r"""` if any backslashes in a docstring | 🛠️ |
| D400 | [missing-trailing-period](https://docs.astral.sh/ruff/rules/missing-trailing-period/) | First line should end with a period | 🛠️ |
| D401 | [non-imperative-mood](https://docs.astral.sh/ruff/rules/non-imperative-mood/) | First line of docstring should be in imperative mood: "{first\_line}" |  |
| D402 | [signature-in-docstring](https://docs.astral.sh/ruff/rules/signature-in-docstring/) | First line should not be the function's signature |  |
| D403 | [first-word-uncapitalized](https://docs.astral.sh/ruff/rules/first-word-uncapitalized/) | First word of the docstring should be capitalized: `{}` -\> `{}` | 🛠️ |
| D404 | [docstring-starts-with-this](https://docs.astral.sh/ruff/rules/docstring-starts-with-this/) | First word of the docstring should not be "This" |  |
| D405 | [non-capitalized-section-name](https://docs.astral.sh/ruff/rules/non-capitalized-section-name/) | Section name should be properly capitalized ("{name}") | 🛠️ |
| D406 | [missing-new-line-after-section-name](https://docs.astral.sh/ruff/rules/missing-new-line-after-section-name/) | Section name should end with a newline ("{name}") | 🛠️ |
| D407 | [missing-dashed-underline-after-section](https://docs.astral.sh/ruff/rules/missing-dashed-underline-after-section/) | Missing dashed underline after section ("{name}") | 🛠️ |
| D408 | [missing-section-underline-after-name](https://docs.astral.sh/ruff/rules/missing-section-underline-after-name/) | Section underline should be in the line following the section's name ("{name}") | 🛠️ |
| D409 | [mismatched-section-underline-length](https://docs.astral.sh/ruff/rules/mismatched-section-underline-length/) | Section underline should match the length of its name ("{name}") | 🛠️ |
| D410 | [no-blank-line-after-section](https://docs.astral.sh/ruff/rules/no-blank-line-after-section/) | Missing blank line after section ("{name}") | 🛠️ |
| D411 | [no-blank-line-before-section](https://docs.astral.sh/ruff/rules/no-blank-line-before-section/) | Missing blank line before section ("{name}") | 🛠️ |
| D412 | [blank-lines-between-header-and-content](https://docs.astral.sh/ruff/rules/blank-lines-between-header-and-content/) | No blank lines allowed between a section header and its content ("{name}") | 🛠️ |
| D413 | [missing-blank-line-after-last-section](https://docs.astral.sh/ruff/rules/missing-blank-line-after-last-section/) | Missing blank line after last section ("{name}") | 🛠️ |
| D414 | [empty-docstring-section](https://docs.astral.sh/ruff/rules/empty-docstring-section/) | Section has no content ("{name}") |  |
| D415 | [missing-terminal-punctuation](https://docs.astral.sh/ruff/rules/missing-terminal-punctuation/) | First line should end with a period, question mark, or exclamation point | 🛠️ |
| D416 | [missing-section-name-colon](https://docs.astral.sh/ruff/rules/missing-section-name-colon/) | Section name should end with a colon ("{name}") | 🛠️ |
| D417 | [undocumented-param](https://docs.astral.sh/ruff/rules/undocumented-param/) | Missing argument description in the docstring for `{definition}`: `{name}` |  |
| D418 | [overload-with-docstring](https://docs.astral.sh/ruff/rules/overload-with-docstring/) | Function decorated with `@overload` shouldn't contain a docstring |  |
| D419 | [empty-docstring](https://docs.astral.sh/ruff/rules/empty-docstring/) | Docstring is empty |  |

## [Pyflakes (F)](https://docs.astral.sh/ruff/rules/\#pyflakes-f)

For more, see [Pyflakes](https://pypi.org/project/pyflakes/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| F401 | [unused-import](https://docs.astral.sh/ruff/rules/unused-import/) | `{name}` imported but unused; consider using `importlib.util.find_spec` to test for availability | 🛠️ |
| F402 | [import-shadowed-by-loop-var](https://docs.astral.sh/ruff/rules/import-shadowed-by-loop-var/) | Import `{name}` from {row} shadowed by loop variable |  |
| F403 | [undefined-local-with-import-star](https://docs.astral.sh/ruff/rules/undefined-local-with-import-star/) | `from {name} import *` used; unable to detect undefined names |  |
| F404 | [late-future-import](https://docs.astral.sh/ruff/rules/late-future-import/) | `from __future__` imports must occur at the beginning of the file |  |
| F405 | [undefined-local-with-import-star-usage](https://docs.astral.sh/ruff/rules/undefined-local-with-import-star-usage/) | `{name}` may be undefined, or defined from star imports |  |
| F406 | [undefined-local-with-nested-import-star-usage](https://docs.astral.sh/ruff/rules/undefined-local-with-nested-import-star-usage/) | `from {name} import *` only allowed at module level |  |
| F407 | [future-feature-not-defined](https://docs.astral.sh/ruff/rules/future-feature-not-defined/) | Future feature `{name}` is not defined |  |
| F501 | [percent-format-invalid-format](https://docs.astral.sh/ruff/rules/percent-format-invalid-format/) | `%`-format string has invalid format string: {message} |  |
| F502 | [percent-format-expected-mapping](https://docs.astral.sh/ruff/rules/percent-format-expected-mapping/) | `%`-format string expected mapping but got sequence |  |
| F503 | [percent-format-expected-sequence](https://docs.astral.sh/ruff/rules/percent-format-expected-sequence/) | `%`-format string expected sequence but got mapping |  |
| F504 | [percent-format-extra-named-arguments](https://docs.astral.sh/ruff/rules/percent-format-extra-named-arguments/) | `%`-format string has unused named argument(s): {message} | 🛠️ |
| F505 | [percent-format-missing-argument](https://docs.astral.sh/ruff/rules/percent-format-missing-argument/) | `%`-format string is missing argument(s) for placeholder(s): {message} |  |
| F506 | [percent-format-mixed-positional-and-named](https://docs.astral.sh/ruff/rules/percent-format-mixed-positional-and-named/) | `%`-format string has mixed positional and named placeholders |  |
| F507 | [percent-format-positional-count-mismatch](https://docs.astral.sh/ruff/rules/percent-format-positional-count-mismatch/) | `%`-format string has {wanted} placeholder(s) but {got} substitution(s) |  |
| F508 | [percent-format-star-requires-sequence](https://docs.astral.sh/ruff/rules/percent-format-star-requires-sequence/) | `%`-format string `*` specifier requires sequence |  |
| F509 | [percent-format-unsupported-format-character](https://docs.astral.sh/ruff/rules/percent-format-unsupported-format-character/) | `%`-format string has unsupported format character `{char}` |  |
| F521 | [string-dot-format-invalid-format](https://docs.astral.sh/ruff/rules/string-dot-format-invalid-format/) | `.format` call has invalid format string: {message} |  |
| F522 | [string-dot-format-extra-named-arguments](https://docs.astral.sh/ruff/rules/string-dot-format-extra-named-arguments/) | `.format` call has unused named argument(s): {message} | 🛠️ |
| F523 | [string-dot-format-extra-positional-arguments](https://docs.astral.sh/ruff/rules/string-dot-format-extra-positional-arguments/) | `.format` call has unused arguments at position(s): {message} | 🛠️ |
| F524 | [string-dot-format-missing-arguments](https://docs.astral.sh/ruff/rules/string-dot-format-missing-arguments/) | `.format` call is missing argument(s) for placeholder(s): {message} |  |
| F525 | [string-dot-format-mixing-automatic](https://docs.astral.sh/ruff/rules/string-dot-format-mixing-automatic/) | `.format` string mixes automatic and manual numbering |  |
| F541 | [f-string-missing-placeholders](https://docs.astral.sh/ruff/rules/f-string-missing-placeholders/) | f-string without any placeholders | 🛠️ |
| F601 | [multi-value-repeated-key-literal](https://docs.astral.sh/ruff/rules/multi-value-repeated-key-literal/) | Dictionary key literal `{name}` repeated | 🛠️ |
| F602 | [multi-value-repeated-key-variable](https://docs.astral.sh/ruff/rules/multi-value-repeated-key-variable/) | Dictionary key `{name}` repeated | 🛠️ |
| F621 | [expressions-in-star-assignment](https://docs.astral.sh/ruff/rules/expressions-in-star-assignment/) | Too many expressions in star-unpacking assignment |  |
| F622 | [multiple-starred-expressions](https://docs.astral.sh/ruff/rules/multiple-starred-expressions/) | Two starred expressions in assignment |  |
| F631 | [assert-tuple](https://docs.astral.sh/ruff/rules/assert-tuple/) | Assert test is a non-empty tuple, which is always `True` |  |
| F632 | [is-literal](https://docs.astral.sh/ruff/rules/is-literal/) | Use `==` to compare constant literals | 🛠️ |
| F633 | [invalid-print-syntax](https://docs.astral.sh/ruff/rules/invalid-print-syntax/) | Use of `>>` is invalid with `print` function |  |
| F634 | [if-tuple](https://docs.astral.sh/ruff/rules/if-tuple/) | If test is a tuple, which is always `True` |  |
| F701 | [break-outside-loop](https://docs.astral.sh/ruff/rules/break-outside-loop/) | `break` outside loop |  |
| F702 | [continue-outside-loop](https://docs.astral.sh/ruff/rules/continue-outside-loop/) | `continue` not properly in loop |  |
| F704 | [yield-outside-function](https://docs.astral.sh/ruff/rules/yield-outside-function/) | `{keyword}` statement outside of a function |  |
| F706 | [return-outside-function](https://docs.astral.sh/ruff/rules/return-outside-function/) | `return` statement outside of a function/method |  |
| F707 | [default-except-not-last](https://docs.astral.sh/ruff/rules/default-except-not-last/) | An `except` block as not the last exception handler |  |
| F722 | [forward-annotation-syntax-error](https://docs.astral.sh/ruff/rules/forward-annotation-syntax-error/) | Syntax error in forward annotation: {parse\_error} |  |
| F811 | [redefined-while-unused](https://docs.astral.sh/ruff/rules/redefined-while-unused/) | Redefinition of unused `{name}` from {row} | 🛠️ |
| F821 | [undefined-name](https://docs.astral.sh/ruff/rules/undefined-name/) | Undefined name `{name}`. {tip} |  |
| F822 | [undefined-export](https://docs.astral.sh/ruff/rules/undefined-export/) | Undefined name `{name}` in `__all__` |  |
| F823 | [undefined-local](https://docs.astral.sh/ruff/rules/undefined-local/) | Local variable `{name}` referenced before assignment |  |
| F841 | [unused-variable](https://docs.astral.sh/ruff/rules/unused-variable/) | Local variable `{name}` is assigned to but never used | 🛠️ |
| F842 | [unused-annotation](https://docs.astral.sh/ruff/rules/unused-annotation/) | Local variable `{name}` is annotated but never used |  |
| F901 | [raise-not-implemented](https://docs.astral.sh/ruff/rules/raise-not-implemented/) | `raise NotImplemented` should be `raise NotImplementedError` | 🛠️ |

## [pygrep-hooks (PGH)](https://docs.astral.sh/ruff/rules/\#pygrep-hooks-pgh)

For more, see [pygrep-hooks](https://github.com/pre-commit/pygrep-hooks) on GitHub.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| PGH001 | [eval](https://docs.astral.sh/ruff/rules/eval/) | No builtin `eval()` allowed | ❌ |
| PGH002 | [deprecated-log-warn](https://docs.astral.sh/ruff/rules/deprecated-log-warn/) | `warn` is deprecated in favor of `warning` | ❌🛠️ |
| PGH003 | [blanket-type-ignore](https://docs.astral.sh/ruff/rules/blanket-type-ignore/) | Use specific rule codes when ignoring type issues |  |
| PGH004 | [blanket-noqa](https://docs.astral.sh/ruff/rules/blanket-noqa/) | Use specific rule codes when using `noqa` | 🛠️ |
| PGH005 | [invalid-mock-access](https://docs.astral.sh/ruff/rules/invalid-mock-access/) | Mock method should be called: `{name}` |  |

## [Pylint (PL)](https://docs.astral.sh/ruff/rules/\#pylint-pl)

For more, see [Pylint](https://pypi.org/project/pylint/) on PyPI.

### [Convention (PLC)](https://docs.astral.sh/ruff/rules/\#convention-plc)

| Code | Name | Message |  |
| --- | --- | --- | --- |
| PLC0105 | [type-name-incorrect-variance](https://docs.astral.sh/ruff/rules/type-name-incorrect-variance/) | `{kind}` name "{param\_name}" does not reflect its {variance}; consider renaming it to "{replacement\_name}" |  |
| PLC0131 | [type-bivariance](https://docs.astral.sh/ruff/rules/type-bivariance/) | `{kind}` cannot be both covariant and contravariant |  |
| PLC0132 | [type-param-name-mismatch](https://docs.astral.sh/ruff/rules/type-param-name-mismatch/) | `{kind}` name `{param_name}` does not match assigned variable name `{var_name}` |  |
| PLC0205 | [single-string-slots](https://docs.astral.sh/ruff/rules/single-string-slots/) | Class `__slots__` should be a non-string iterable |  |
| PLC0206 | [dict-index-missing-items](https://docs.astral.sh/ruff/rules/dict-index-missing-items/) | Extracting value from dictionary without calling `.items()` |  |
| PLC0207 | [missing-maxsplit-arg](https://docs.astral.sh/ruff/rules/missing-maxsplit-arg/) | Replace with `{suggested_split_type}(..., maxsplit=1)`. | 🧪🛠️ |
| PLC0208 | [iteration-over-set](https://docs.astral.sh/ruff/rules/iteration-over-set/) | Use a sequence type instead of a `set` when iterating over values | 🛠️ |
| PLC0414 | [useless-import-alias](https://docs.astral.sh/ruff/rules/useless-import-alias/) | Import alias does not rename original package | 🛠️ |
| PLC0415 | [import-outside-top-level](https://docs.astral.sh/ruff/rules/import-outside-top-level/) | `import` should be at the top-level of a file |  |
| PLC1802 | [len-test](https://docs.astral.sh/ruff/rules/len-test/) | `len({expression})` used as condition without comparison | 🛠️ |
| PLC1901 | [compare-to-empty-string](https://docs.astral.sh/ruff/rules/compare-to-empty-string/) | `{existing}` can be simplified to `{replacement}` as an empty string is falsey | 🧪 |
| PLC2401 | [non-ascii-name](https://docs.astral.sh/ruff/rules/non-ascii-name/) | {kind} name `{name}` contains a non-ASCII character |  |
| PLC2403 | [non-ascii-import-name](https://docs.astral.sh/ruff/rules/non-ascii-import-name/) | Module alias `{name}` contains a non-ASCII character |  |
| PLC2701 | [import-private-name](https://docs.astral.sh/ruff/rules/import-private-name/) | Private name import `{name}` from external module `{module}` | 🧪 |
| PLC2801 | [unnecessary-dunder-call](https://docs.astral.sh/ruff/rules/unnecessary-dunder-call/) | Unnecessary dunder call to `{method}`. {replacement}. | 🧪🛠️ |
| PLC3002 | [unnecessary-direct-lambda-call](https://docs.astral.sh/ruff/rules/unnecessary-direct-lambda-call/) | Lambda expression called directly. Execute the expression inline instead. |  |

### [Error (PLE)](https://docs.astral.sh/ruff/rules/\#error-ple)

| Code | Name | Message |  |
| --- | --- | --- | --- |
| PLE0100 | [yield-in-init](https://docs.astral.sh/ruff/rules/yield-in-init/) | `__init__` method is a generator |  |
| PLE0101 | [return-in-init](https://docs.astral.sh/ruff/rules/return-in-init/) | Explicit return in `__init__` |  |
| PLE0115 | [nonlocal-and-global](https://docs.astral.sh/ruff/rules/nonlocal-and-global/) | Name `{name}` is both `nonlocal` and `global` |  |
| PLE0116 | [continue-in-finally](https://docs.astral.sh/ruff/rules/continue-in-finally/) | `continue` not supported inside `finally` clause |  |
| PLE0117 | [nonlocal-without-binding](https://docs.astral.sh/ruff/rules/nonlocal-without-binding/) | Nonlocal name `{name}` found without binding |  |
| PLE0118 | [load-before-global-declaration](https://docs.astral.sh/ruff/rules/load-before-global-declaration/) | Name `{name}` is used prior to global declaration on {row} |  |
| PLE0237 | [non-slot-assignment](https://docs.astral.sh/ruff/rules/non-slot-assignment/) | Attribute `{name}` is not defined in class's `__slots__` |  |
| PLE0241 | [duplicate-bases](https://docs.astral.sh/ruff/rules/duplicate-bases/) | Duplicate base `{base}` for class `{class}` | 🛠️ |
| PLE0302 | [unexpected-special-method-signature](https://docs.astral.sh/ruff/rules/unexpected-special-method-signature/) | The special method `{}` expects {}, {} {} given |  |
| PLE0303 | [invalid-length-return-type](https://docs.astral.sh/ruff/rules/invalid-length-return-type/) | `__len__` does not return a non-negative integer |  |
| PLE0304 | [invalid-bool-return-type](https://docs.astral.sh/ruff/rules/invalid-bool-return-type/) | `__bool__` does not return `bool` | 🧪 |
| PLE0305 | [invalid-index-return-type](https://docs.astral.sh/ruff/rules/invalid-index-return-type/) | `__index__` does not return an integer |  |
| PLE0307 | [invalid-str-return-type](https://docs.astral.sh/ruff/rules/invalid-str-return-type/) | `__str__` does not return `str` |  |
| PLE0308 | [invalid-bytes-return-type](https://docs.astral.sh/ruff/rules/invalid-bytes-return-type/) | `__bytes__` does not return `bytes` |  |
| PLE0309 | [invalid-hash-return-type](https://docs.astral.sh/ruff/rules/invalid-hash-return-type/) | `__hash__` does not return an integer |  |
| PLE0604 | [invalid-all-object](https://docs.astral.sh/ruff/rules/invalid-all-object/) | Invalid object in `__all__`, must contain only strings |  |
| PLE0605 | [invalid-all-format](https://docs.astral.sh/ruff/rules/invalid-all-format/) | Invalid format for `__all__`, must be `tuple` or `list` |  |
| PLE0643 | [potential-index-error](https://docs.astral.sh/ruff/rules/potential-index-error/) | Expression is likely to raise `IndexError` |  |
| PLE0704 | [misplaced-bare-raise](https://docs.astral.sh/ruff/rules/misplaced-bare-raise/) | Bare `raise` statement is not inside an exception handler |  |
| PLE1132 | [repeated-keyword-argument](https://docs.astral.sh/ruff/rules/repeated-keyword-argument/) | Repeated keyword argument: `{duplicate_keyword}` |  |
| PLE1141 | [dict-iter-missing-items](https://docs.astral.sh/ruff/rules/dict-iter-missing-items/) | Unpacking a dictionary in iteration without calling `.items()` | 🧪🛠️ |
| PLE1142 | [await-outside-async](https://docs.astral.sh/ruff/rules/await-outside-async/) | `await` should be used within an async function |  |
| PLE1205 | [logging-too-many-args](https://docs.astral.sh/ruff/rules/logging-too-many-args/) | Too many arguments for `logging` format string |  |
| PLE1206 | [logging-too-few-args](https://docs.astral.sh/ruff/rules/logging-too-few-args/) | Not enough arguments for `logging` format string |  |
| PLE1300 | [bad-string-format-character](https://docs.astral.sh/ruff/rules/bad-string-format-character/) | Unsupported format character '{format\_char}' |  |
| PLE1307 | [bad-string-format-type](https://docs.astral.sh/ruff/rules/bad-string-format-type/) | Format type does not match argument type |  |
| PLE1310 | [bad-str-strip-call](https://docs.astral.sh/ruff/rules/bad-str-strip-call/) | String `{strip}` call contains duplicate characters (did you mean `{removal}`?) |  |
| PLE1507 | [invalid-envvar-value](https://docs.astral.sh/ruff/rules/invalid-envvar-value/) | Invalid type for initial `os.getenv` argument; expected `str` |  |
| PLE1519 | [singledispatch-method](https://docs.astral.sh/ruff/rules/singledispatch-method/) | `@singledispatch` decorator should not be used on methods | 🛠️ |
| PLE1520 | [singledispatchmethod-function](https://docs.astral.sh/ruff/rules/singledispatchmethod-function/) | `@singledispatchmethod` decorator should not be used on non-method functions | 🛠️ |
| PLE1700 | [yield-from-in-async-function](https://docs.astral.sh/ruff/rules/yield-from-in-async-function/) | `yield from` statement in async function; use `async for` instead |  |
| PLE2502 | [bidirectional-unicode](https://docs.astral.sh/ruff/rules/bidirectional-unicode/) | Contains control characters that can permit obfuscated code |  |
| PLE2510 | [invalid-character-backspace](https://docs.astral.sh/ruff/rules/invalid-character-backspace/) | Invalid unescaped character backspace, use "\\b" instead | 🛠️ |
| PLE2512 | [invalid-character-sub](https://docs.astral.sh/ruff/rules/invalid-character-sub/) | Invalid unescaped character SUB, use "\\x1a" instead | 🛠️ |
| PLE2513 | [invalid-character-esc](https://docs.astral.sh/ruff/rules/invalid-character-esc/) | Invalid unescaped character ESC, use "\\x1b" instead | 🛠️ |
| PLE2514 | [invalid-character-nul](https://docs.astral.sh/ruff/rules/invalid-character-nul/) | Invalid unescaped character NUL, use "\\0" instead | 🛠️ |
| PLE2515 | [invalid-character-zero-width-space](https://docs.astral.sh/ruff/rules/invalid-character-zero-width-space/) | Invalid unescaped character zero-width-space, use "\\u200B" instead | 🛠️ |
| PLE4703 | [modified-iterating-set](https://docs.astral.sh/ruff/rules/modified-iterating-set/) | Iterated set `{name}` is modified within the `for` loop | 🧪🛠️ |

### [Refactor (PLR)](https://docs.astral.sh/ruff/rules/\#refactor-plr)

| Code | Name | Message |  |
| --- | --- | --- | --- |
| PLR0124 | [comparison-with-itself](https://docs.astral.sh/ruff/rules/comparison-with-itself/) | Name compared with itself, consider replacing `{actual}` |  |
| PLR0133 | [comparison-of-constant](https://docs.astral.sh/ruff/rules/comparison-of-constant/) | Two constants compared in a comparison, consider replacing `{left_constant} {op} {right_constant}` |  |
| PLR0202 | [no-classmethod-decorator](https://docs.astral.sh/ruff/rules/no-classmethod-decorator/) | Class method defined without decorator | 🧪🛠️ |
| PLR0203 | [no-staticmethod-decorator](https://docs.astral.sh/ruff/rules/no-staticmethod-decorator/) | Static method defined without decorator | 🧪🛠️ |
| PLR0206 | [property-with-parameters](https://docs.astral.sh/ruff/rules/property-with-parameters/) | Cannot have defined parameters for properties |  |
| PLR0402 | [manual-from-import](https://docs.astral.sh/ruff/rules/manual-from-import/) | Use `from {module} import {name}` in lieu of alias | 🛠️ |
| PLR0904 | [too-many-public-methods](https://docs.astral.sh/ruff/rules/too-many-public-methods/) | Too many public methods ({methods} > {max\_methods}) | 🧪 |
| PLR0911 | [too-many-return-statements](https://docs.astral.sh/ruff/rules/too-many-return-statements/) | Too many return statements ({returns} > {max\_returns}) |  |
| PLR0912 | [too-many-branches](https://docs.astral.sh/ruff/rules/too-many-branches/) | Too many branches ({branches} > {max\_branches}) |  |
| PLR0913 | [too-many-arguments](https://docs.astral.sh/ruff/rules/too-many-arguments/) | Too many arguments in function definition ({c\_args} > {max\_args}) |  |
| PLR0914 | [too-many-locals](https://docs.astral.sh/ruff/rules/too-many-locals/) | Too many local variables ({current\_amount}/{max\_amount}) | 🧪 |
| PLR0915 | [too-many-statements](https://docs.astral.sh/ruff/rules/too-many-statements/) | Too many statements ({statements} > {max\_statements}) |  |
| PLR0916 | [too-many-boolean-expressions](https://docs.astral.sh/ruff/rules/too-many-boolean-expressions/) | Too many Boolean expressions ({expressions} > {max\_expressions}) | 🧪 |
| PLR0917 | [too-many-positional-arguments](https://docs.astral.sh/ruff/rules/too-many-positional-arguments/) | Too many positional arguments ({c\_pos}/{max\_pos}) | 🧪 |
| PLR1701 | [repeated-isinstance-calls](https://docs.astral.sh/ruff/rules/repeated-isinstance-calls/) | Merge `isinstance` calls: `{expression}` | ❌🛠️ |
| PLR1702 | [too-many-nested-blocks](https://docs.astral.sh/ruff/rules/too-many-nested-blocks/) | Too many nested blocks ({nested\_blocks} > {max\_nested\_blocks}) | 🧪 |
| PLR1704 | [redefined-argument-from-local](https://docs.astral.sh/ruff/rules/redefined-argument-from-local/) | Redefining argument with the local name `{name}` |  |
| PLR1706 | [and-or-ternary](https://docs.astral.sh/ruff/rules/and-or-ternary/) | Consider using if-else expression | ❌ |
| PLR1711 | [useless-return](https://docs.astral.sh/ruff/rules/useless-return/) | Useless `return` statement at end of function | 🛠️ |
| PLR1714 | [repeated-equality-comparison](https://docs.astral.sh/ruff/rules/repeated-equality-comparison/) | Consider merging multiple comparisons: `{expression}`. Use a `set` if the elements are hashable. | 🛠️ |
| PLR1716 | [boolean-chained-comparison](https://docs.astral.sh/ruff/rules/boolean-chained-comparison/) | Contains chained boolean comparison that can be simplified | 🛠️ |
| PLR1722 | [sys-exit-alias](https://docs.astral.sh/ruff/rules/sys-exit-alias/) | Use `sys.exit()` instead of `{name}` | 🛠️ |
| PLR1730 | [if-stmt-min-max](https://docs.astral.sh/ruff/rules/if-stmt-min-max/) | Replace `if` statement with `{replacement}` | 🛠️ |
| PLR1733 | [unnecessary-dict-index-lookup](https://docs.astral.sh/ruff/rules/unnecessary-dict-index-lookup/) | Unnecessary lookup of dictionary value by key | 🛠️ |
| PLR1736 | [unnecessary-list-index-lookup](https://docs.astral.sh/ruff/rules/unnecessary-list-index-lookup/) | List index lookup in `enumerate()` loop | 🛠️ |
| PLR2004 | [magic-value-comparison](https://docs.astral.sh/ruff/rules/magic-value-comparison/) | Magic value used in comparison, consider replacing `{value}` with a constant variable |  |
| PLR2044 | [empty-comment](https://docs.astral.sh/ruff/rules/empty-comment/) | Line with empty comment | 🛠️ |
| PLR5501 | [collapsible-else-if](https://docs.astral.sh/ruff/rules/collapsible-else-if/) | Use `elif` instead of `else` then `if`, to reduce indentation | 🛠️ |
| PLR6104 | [non-augmented-assignment](https://docs.astral.sh/ruff/rules/non-augmented-assignment/) | Use `{operator}` to perform an augmented assignment directly | 🧪🛠️ |
| PLR6201 | [literal-membership](https://docs.astral.sh/ruff/rules/literal-membership/) | Use a set literal when testing for membership | 🧪🛠️ |
| PLR6301 | [no-self-use](https://docs.astral.sh/ruff/rules/no-self-use/) | Method `{method_name}` could be a function, class method, or static method | 🧪 |

### [Warning (PLW)](https://docs.astral.sh/ruff/rules/\#warning-plw)

| Code | Name | Message |  |
| --- | --- | --- | --- |
| PLW0108 | [unnecessary-lambda](https://docs.astral.sh/ruff/rules/unnecessary-lambda/) | Lambda may be unnecessary; consider inlining inner function | 🧪🛠️ |
| PLW0120 | [useless-else-on-loop](https://docs.astral.sh/ruff/rules/useless-else-on-loop/) | `else` clause on loop without a `break` statement; remove the `else` and dedent its contents | 🛠️ |
| PLW0127 | [self-assigning-variable](https://docs.astral.sh/ruff/rules/self-assigning-variable/) | Self-assignment of variable `{name}` |  |
| PLW0128 | [redeclared-assigned-name](https://docs.astral.sh/ruff/rules/redeclared-assigned-name/) | Redeclared variable `{name}` in assignment |  |
| PLW0129 | [assert-on-string-literal](https://docs.astral.sh/ruff/rules/assert-on-string-literal/) | Asserting on an empty string literal will never pass |  |
| PLW0131 | [named-expr-without-context](https://docs.astral.sh/ruff/rules/named-expr-without-context/) | Named expression used without context |  |
| PLW0133 | [useless-exception-statement](https://docs.astral.sh/ruff/rules/useless-exception-statement/) | Missing `raise` statement on exception | 🛠️ |
| PLW0177 | [nan-comparison](https://docs.astral.sh/ruff/rules/nan-comparison/) | Comparing against a NaN value; use `math.isnan` instead |  |
| PLW0211 | [bad-staticmethod-argument](https://docs.astral.sh/ruff/rules/bad-staticmethod-argument/) | First argument of a static method should not be named `{argument_name}` |  |
| PLW0244 | [redefined-slots-in-subclass](https://docs.astral.sh/ruff/rules/redefined-slots-in-subclass/) | Slot `{slot_name}` redefined from base class `{base}` | 🧪 |
| PLW0245 | [super-without-brackets](https://docs.astral.sh/ruff/rules/super-without-brackets/) | `super` call is missing parentheses | 🛠️ |
| PLW0406 | [import-self](https://docs.astral.sh/ruff/rules/import-self/) | Module `{name}` imports itself |  |
| PLW0602 | [global-variable-not-assigned](https://docs.astral.sh/ruff/rules/global-variable-not-assigned/) | Using global for `{name}` but no assignment is done |  |
| PLW0603 | [global-statement](https://docs.astral.sh/ruff/rules/global-statement/) | Using the global statement to update `{name}` is discouraged |  |
| PLW0604 | [global-at-module-level](https://docs.astral.sh/ruff/rules/global-at-module-level/) | `global` at module level is redundant |  |
| PLW0642 | [self-or-cls-assignment](https://docs.astral.sh/ruff/rules/self-or-cls-assignment/) | Reassigned `{}` variable in {method\_type} method |  |
| PLW0711 | [binary-op-exception](https://docs.astral.sh/ruff/rules/binary-op-exception/) | Exception to catch is the result of a binary `and` operation |  |
| PLW1501 | [bad-open-mode](https://docs.astral.sh/ruff/rules/bad-open-mode/) | `{mode}` is not a valid mode for `open` |  |
| PLW1507 | [shallow-copy-environ](https://docs.astral.sh/ruff/rules/shallow-copy-environ/) | Shallow copy of `os.environ` via `copy.copy(os.environ)` | 🛠️ |
| PLW1508 | [invalid-envvar-default](https://docs.astral.sh/ruff/rules/invalid-envvar-default/) | Invalid type for environment variable default; expected `str` or `None` |  |
| PLW1509 | [subprocess-popen-preexec-fn](https://docs.astral.sh/ruff/rules/subprocess-popen-preexec-fn/) | `preexec_fn` argument is unsafe when using threads |  |
| PLW1510 | [subprocess-run-without-check](https://docs.astral.sh/ruff/rules/subprocess-run-without-check/) | `subprocess.run` without explicit `check` argument | 🛠️ |
| PLW1514 | [unspecified-encoding](https://docs.astral.sh/ruff/rules/unspecified-encoding/) | `{function_name}` in text mode without explicit `encoding` argument | 🧪🛠️ |
| PLW1641 | [eq-without-hash](https://docs.astral.sh/ruff/rules/eq-without-hash/) | Object does not implement `__hash__` method |  |
| PLW2101 | [useless-with-lock](https://docs.astral.sh/ruff/rules/useless-with-lock/) | Threading lock directly created in `with` statement has no effect |  |
| PLW2901 | [redefined-loop-name](https://docs.astral.sh/ruff/rules/redefined-loop-name/) | Outer {outer\_kind} variable `{name}` overwritten by inner {inner\_kind} target |  |
| PLW3201 | [bad-dunder-method-name](https://docs.astral.sh/ruff/rules/bad-dunder-method-name/) | Dunder method `{name}` has no special meaning in Python 3 | 🧪 |
| PLW3301 | [nested-min-max](https://docs.astral.sh/ruff/rules/nested-min-max/) | Nested `{func}` calls can be flattened | 🛠️ |

## [pyupgrade (UP)](https://docs.astral.sh/ruff/rules/\#pyupgrade-up)

For more, see [pyupgrade](https://pypi.org/project/pyupgrade/) on PyPI.

For related settings, see [pyupgrade](https://docs.astral.sh/ruff/settings/#lintpyupgrade).

| Code | Name | Message |  |
| --- | --- | --- | --- |
| UP001 | [useless-metaclass-type](https://docs.astral.sh/ruff/rules/useless-metaclass-type/) | `__metaclass__ = type` is implied | 🛠️ |
| UP003 | [type-of-primitive](https://docs.astral.sh/ruff/rules/type-of-primitive/) | Use `{}` instead of `type(...)` | 🛠️ |
| UP004 | [useless-object-inheritance](https://docs.astral.sh/ruff/rules/useless-object-inheritance/) | Class `{name}` inherits from `object` | 🛠️ |
| UP005 | [deprecated-unittest-alias](https://docs.astral.sh/ruff/rules/deprecated-unittest-alias/) | `{alias}` is deprecated, use `{target}` | 🛠️ |
| UP006 | [non-pep585-annotation](https://docs.astral.sh/ruff/rules/non-pep585-annotation/) | Use `{to}` instead of `{from}` for type annotation | 🛠️ |
| UP007 | [non-pep604-annotation-union](https://docs.astral.sh/ruff/rules/non-pep604-annotation-union/) | Use `X | Y` for type annotations | 🛠️ |
| UP008 | [super-call-with-parameters](https://docs.astral.sh/ruff/rules/super-call-with-parameters/) | Use `super()` instead of `super(__class__, self)` | 🛠️ |
| UP009 | [utf8-encoding-declaration](https://docs.astral.sh/ruff/rules/utf8-encoding-declaration/) | UTF-8 encoding declaration is unnecessary | 🛠️ |
| UP010 | [unnecessary-future-import](https://docs.astral.sh/ruff/rules/unnecessary-future-import/) | Unnecessary `__future__` import `{import}` for target Python version | 🛠️ |
| UP011 | [lru-cache-without-parameters](https://docs.astral.sh/ruff/rules/lru-cache-without-parameters/) | Unnecessary parentheses to `functools.lru_cache` | 🛠️ |
| UP012 | [unnecessary-encode-utf8](https://docs.astral.sh/ruff/rules/unnecessary-encode-utf8/) | Unnecessary call to `encode` as UTF-8 | 🛠️ |
| UP013 | [convert-typed-dict-functional-to-class](https://docs.astral.sh/ruff/rules/convert-typed-dict-functional-to-class/) | Convert `{name}` from `TypedDict` functional to class syntax | 🛠️ |
| UP014 | [convert-named-tuple-functional-to-class](https://docs.astral.sh/ruff/rules/convert-named-tuple-functional-to-class/) | Convert `{name}` from `NamedTuple` functional to class syntax | 🛠️ |
| UP015 | [redundant-open-modes](https://docs.astral.sh/ruff/rules/redundant-open-modes/) | Unnecessary mode argument | 🛠️ |
| UP017 | [datetime-timezone-utc](https://docs.astral.sh/ruff/rules/datetime-timezone-utc/) | Use `datetime.UTC` alias | 🛠️ |
| UP018 | [native-literals](https://docs.astral.sh/ruff/rules/native-literals/) | Unnecessary `{literal_type}` call (rewrite as a literal) | 🛠️ |
| UP019 | [typing-text-str-alias](https://docs.astral.sh/ruff/rules/typing-text-str-alias/) | `typing.Text` is deprecated, use `str` | 🛠️ |
| UP020 | [open-alias](https://docs.astral.sh/ruff/rules/open-alias/) | Use builtin `open` | 🛠️ |
| UP021 | [replace-universal-newlines](https://docs.astral.sh/ruff/rules/replace-universal-newlines/) | `universal_newlines` is deprecated, use `text` | 🛠️ |
| UP022 | [replace-stdout-stderr](https://docs.astral.sh/ruff/rules/replace-stdout-stderr/) | Prefer `capture_output` over sending `stdout` and `stderr` to `PIPE` | 🛠️ |
| UP023 | [deprecated-c-element-tree](https://docs.astral.sh/ruff/rules/deprecated-c-element-tree/) | `cElementTree` is deprecated, use `ElementTree` | 🛠️ |
| UP024 | [os-error-alias](https://docs.astral.sh/ruff/rules/os-error-alias/) | Replace aliased errors with `OSError` | 🛠️ |
| UP025 | [unicode-kind-prefix](https://docs.astral.sh/ruff/rules/unicode-kind-prefix/) | Remove unicode literals from strings | 🛠️ |
| UP026 | [deprecated-mock-import](https://docs.astral.sh/ruff/rules/deprecated-mock-import/) | `mock` is deprecated, use `unittest.mock` | 🛠️ |
| UP027 | [unpacked-list-comprehension](https://docs.astral.sh/ruff/rules/unpacked-list-comprehension/) | Replace unpacked list comprehension with a generator expression | ❌ |
| UP028 | [yield-in-for-loop](https://docs.astral.sh/ruff/rules/yield-in-for-loop/) | Replace `yield` over `for` loop with `yield from` | 🛠️ |
| UP029 | [unnecessary-builtin-import](https://docs.astral.sh/ruff/rules/unnecessary-builtin-import/) | Unnecessary builtin import: `{import}` | 🛠️ |
| UP030 | [format-literals](https://docs.astral.sh/ruff/rules/format-literals/) | Use implicit references for positional format fields | 🛠️ |
| UP031 | [printf-string-formatting](https://docs.astral.sh/ruff/rules/printf-string-formatting/) | Use format specifiers instead of percent format | 🛠️ |
| UP032 | [f-string](https://docs.astral.sh/ruff/rules/f-string/) | Use f-string instead of `format` call | 🛠️ |
| UP033 | [lru-cache-with-maxsize-none](https://docs.astral.sh/ruff/rules/lru-cache-with-maxsize-none/) | Use `@functools.cache` instead of `@functools.lru_cache(maxsize=None)` | 🛠️ |
| UP034 | [extraneous-parentheses](https://docs.astral.sh/ruff/rules/extraneous-parentheses/) | Avoid extraneous parentheses | 🛠️ |
| UP035 | [deprecated-import](https://docs.astral.sh/ruff/rules/deprecated-import/) | Import from `{target}` instead: {names} | 🛠️ |
| UP036 | [outdated-version-block](https://docs.astral.sh/ruff/rules/outdated-version-block/) | Version block is outdated for minimum Python version | 🛠️ |
| UP037 | [quoted-annotation](https://docs.astral.sh/ruff/rules/quoted-annotation/) | Remove quotes from type annotation | 🛠️ |
| UP038 | [non-pep604-isinstance](https://docs.astral.sh/ruff/rules/non-pep604-isinstance/) | Use `X | Y` in `{}` call instead of `(X, Y)` | ⚠️🛠️ |
| UP039 | [unnecessary-class-parentheses](https://docs.astral.sh/ruff/rules/unnecessary-class-parentheses/) | Unnecessary parentheses after class definition | 🛠️ |
| UP040 | [non-pep695-type-alias](https://docs.astral.sh/ruff/rules/non-pep695-type-alias/) | Type alias `{name}` uses {type\_alias\_method} instead of the `type` keyword | 🛠️ |
| UP041 | [timeout-error-alias](https://docs.astral.sh/ruff/rules/timeout-error-alias/) | Replace aliased errors with `TimeoutError` | 🛠️ |
| UP042 | [replace-str-enum](https://docs.astral.sh/ruff/rules/replace-str-enum/) | Class {name} inherits from both `str` and `enum.Enum` | 🧪🛠️ |
| UP043 | [unnecessary-default-type-args](https://docs.astral.sh/ruff/rules/unnecessary-default-type-args/) | Unnecessary default type arguments | 🛠️ |
| UP044 | [non-pep646-unpack](https://docs.astral.sh/ruff/rules/non-pep646-unpack/) | Use `*` for unpacking | 🛠️ |
| UP045 | [non-pep604-annotation-optional](https://docs.astral.sh/ruff/rules/non-pep604-annotation-optional/) | Use `X | None` for type annotations | 🛠️ |
| UP046 | [non-pep695-generic-class](https://docs.astral.sh/ruff/rules/non-pep695-generic-class/) | Generic class `{name}` uses `Generic` subclass instead of type parameters | 🛠️ |
| UP047 | [non-pep695-generic-function](https://docs.astral.sh/ruff/rules/non-pep695-generic-function/) | Generic function `{name}` should use type parameters | 🛠️ |
| UP049 | [private-type-parameter](https://docs.astral.sh/ruff/rules/private-type-parameter/) | Generic {} uses private type parameters | 🛠️ |
| UP050 | [useless-class-metaclass-type](https://docs.astral.sh/ruff/rules/useless-class-metaclass-type/) | Class `{name}` uses `metaclass=type`, which is redundant | 🧪🛠️ |

## [refurb (FURB)](https://docs.astral.sh/ruff/rules/\#refurb-furb)

For more, see [refurb](https://pypi.org/project/refurb/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| FURB101 | [read-whole-file](https://docs.astral.sh/ruff/rules/read-whole-file/) | `open` and `read` should be replaced by `Path({filename}).{suggestion}` | 🧪 |
| FURB103 | [write-whole-file](https://docs.astral.sh/ruff/rules/write-whole-file/) | `open` and `write` should be replaced by `Path({filename}).{suggestion}` | 🧪 |
| FURB105 | [print-empty-string](https://docs.astral.sh/ruff/rules/print-empty-string/) | Unnecessary empty string passed to `print` | 🛠️ |
| FURB110 | [if-exp-instead-of-or-operator](https://docs.astral.sh/ruff/rules/if-exp-instead-of-or-operator/) | Replace ternary `if` expression with `or` operator | 🧪🛠️ |
| FURB113 | [repeated-append](https://docs.astral.sh/ruff/rules/repeated-append/) | Use `{suggestion}` instead of repeatedly calling `{name}.append()` | 🧪🛠️ |
| FURB116 | [f-string-number-format](https://docs.astral.sh/ruff/rules/f-string-number-format/) | Replace `{function_name}` call with `{display}` | 🧪🛠️ |
| FURB118 | [reimplemented-operator](https://docs.astral.sh/ruff/rules/reimplemented-operator/) | Use `operator.{operator}` instead of defining a {target} | 🧪🛠️ |
| FURB122 | [for-loop-writes](https://docs.astral.sh/ruff/rules/for-loop-writes/) | Use of `{}.write` in a for loop | 🛠️ |
| FURB129 | [readlines-in-for](https://docs.astral.sh/ruff/rules/readlines-in-for/) | Instead of calling `readlines()`, iterate over file object directly | 🛠️ |
| FURB131 | [delete-full-slice](https://docs.astral.sh/ruff/rules/delete-full-slice/) | Prefer `clear` over deleting a full slice | 🧪🛠️ |
| FURB132 | [check-and-remove-from-set](https://docs.astral.sh/ruff/rules/check-and-remove-from-set/) | Use `{suggestion}` instead of check and `remove` | 🛠️ |
| FURB136 | [if-expr-min-max](https://docs.astral.sh/ruff/rules/if-expr-min-max/) | Replace `if` expression with `{min_max}` call | 🛠️ |
| FURB140 | [reimplemented-starmap](https://docs.astral.sh/ruff/rules/reimplemented-starmap/) | Use `itertools.starmap` instead of the generator | 🧪🛠️ |
| FURB142 | [for-loop-set-mutations](https://docs.astral.sh/ruff/rules/for-loop-set-mutations/) | Use of `set.{}()` in a for loop | 🧪🛠️ |
| FURB145 | [slice-copy](https://docs.astral.sh/ruff/rules/slice-copy/) | Prefer `copy` method over slicing | 🧪🛠️ |
| FURB148 | [unnecessary-enumerate](https://docs.astral.sh/ruff/rules/unnecessary-enumerate/) | `enumerate` value is unused, use `for x in range(len(y))` instead | 🧪🛠️ |
| FURB152 | [math-constant](https://docs.astral.sh/ruff/rules/math-constant/) | Replace `{literal}` with `math.{constant}` | 🧪🛠️ |
| FURB154 | [repeated-global](https://docs.astral.sh/ruff/rules/repeated-global/) | Use of repeated consecutive `{}` | 🧪🛠️ |
| FURB156 | [hardcoded-string-charset](https://docs.astral.sh/ruff/rules/hardcoded-string-charset/) | Use of hardcoded string charset | 🧪🛠️ |
| FURB157 | [verbose-decimal-constructor](https://docs.astral.sh/ruff/rules/verbose-decimal-constructor/) | Verbose expression in `Decimal` constructor | 🛠️ |
| FURB161 | [bit-count](https://docs.astral.sh/ruff/rules/bit-count/) | Use of `bin({existing}).count('1')` | 🛠️ |
| FURB162 | [fromisoformat-replace-z](https://docs.astral.sh/ruff/rules/fromisoformat-replace-z/) | Unnecessary timezone replacement with zero offset | 🛠️ |
| FURB163 | [redundant-log-base](https://docs.astral.sh/ruff/rules/redundant-log-base/) | Prefer `math.{log_function}({arg})` over `math.log` with a redundant base | 🛠️ |
| FURB164 | [unnecessary-from-float](https://docs.astral.sh/ruff/rules/unnecessary-from-float/) | Verbose method `{method_name}` in `{constructor}` construction | 🧪🛠️ |
| FURB166 | [int-on-sliced-str](https://docs.astral.sh/ruff/rules/int-on-sliced-str/) | Use of `int` with explicit `base={base}` after removing prefix | 🛠️ |
| FURB167 | [regex-flag-alias](https://docs.astral.sh/ruff/rules/regex-flag-alias/) | Use of regular expression alias `re.{}` | 🛠️ |
| FURB168 | [isinstance-type-none](https://docs.astral.sh/ruff/rules/isinstance-type-none/) | Prefer `is` operator over `isinstance` to check if an object is `None` | 🛠️ |
| FURB169 | [type-none-comparison](https://docs.astral.sh/ruff/rules/type-none-comparison/) | When checking against `None`, use `{}` instead of comparison with `type(None)` | 🛠️ |
| FURB171 | [single-item-membership-test](https://docs.astral.sh/ruff/rules/single-item-membership-test/) | Membership test against single-item container | 🧪🛠️ |
| FURB177 | [implicit-cwd](https://docs.astral.sh/ruff/rules/implicit-cwd/) | Prefer `Path.cwd()` over `Path().resolve()` for current-directory lookups | 🛠️ |
| FURB180 | [meta-class-abc-meta](https://docs.astral.sh/ruff/rules/meta-class-abc-meta/) | Use of `metaclass=abc.ABCMeta` to define abstract base class | 🧪🛠️ |
| FURB181 | [hashlib-digest-hex](https://docs.astral.sh/ruff/rules/hashlib-digest-hex/) | Use of hashlib's `.digest().hex()` | 🛠️ |
| FURB187 | [list-reverse-copy](https://docs.astral.sh/ruff/rules/list-reverse-copy/) | Use of assignment of `reversed` on list `{name}` | 🛠️ |
| FURB188 | [slice-to-remove-prefix-or-suffix](https://docs.astral.sh/ruff/rules/slice-to-remove-prefix-or-suffix/) | Prefer `str.removeprefix()` over conditionally replacing with slice. | 🛠️ |
| FURB189 | [subclass-builtin](https://docs.astral.sh/ruff/rules/subclass-builtin/) | Subclassing `{subclass}` can be error prone, use `collections.{replacement}` instead | 🧪🛠️ |
| FURB192 | [sorted-min-max](https://docs.astral.sh/ruff/rules/sorted-min-max/) | Prefer `min` over `sorted()` to compute the minimum value in a sequence | 🧪🛠️ |

## [Ruff-specific rules (RUF)](https://docs.astral.sh/ruff/rules/\#ruff-specific-rules-ruf)

| Code | Name | Message |  |
| --- | --- | --- | --- |
| RUF001 | [ambiguous-unicode-character-string](https://docs.astral.sh/ruff/rules/ambiguous-unicode-character-string/) | String contains ambiguous {}. Did you mean {}? |  |
| RUF002 | [ambiguous-unicode-character-docstring](https://docs.astral.sh/ruff/rules/ambiguous-unicode-character-docstring/) | Docstring contains ambiguous {}. Did you mean {}? |  |
| RUF003 | [ambiguous-unicode-character-comment](https://docs.astral.sh/ruff/rules/ambiguous-unicode-character-comment/) | Comment contains ambiguous {}. Did you mean {}? |  |
| RUF005 | [collection-literal-concatenation](https://docs.astral.sh/ruff/rules/collection-literal-concatenation/) | Consider `{expression}` instead of concatenation | 🛠️ |
| RUF006 | [asyncio-dangling-task](https://docs.astral.sh/ruff/rules/asyncio-dangling-task/) | Store a reference to the return value of `{expr}.{method}` |  |
| RUF007 | [zip-instead-of-pairwise](https://docs.astral.sh/ruff/rules/zip-instead-of-pairwise/) | Prefer `itertools.pairwise()` over `zip()` when iterating over successive pairs | 🛠️ |
| RUF008 | [mutable-dataclass-default](https://docs.astral.sh/ruff/rules/mutable-dataclass-default/) | Do not use mutable default values for dataclass attributes |  |
| RUF009 | [function-call-in-dataclass-default-argument](https://docs.astral.sh/ruff/rules/function-call-in-dataclass-default-argument/) | Do not perform function call `{name}` in dataclass defaults |  |
| RUF010 | [explicit-f-string-type-conversion](https://docs.astral.sh/ruff/rules/explicit-f-string-type-conversion/) | Use explicit conversion flag | 🛠️ |
| RUF011 | [ruff-static-key-dict-comprehension](https://docs.astral.sh/ruff/rules/ruff-static-key-dict-comprehension/) | Dictionary comprehension uses static key | ❌ |
| RUF012 | [mutable-class-default](https://docs.astral.sh/ruff/rules/mutable-class-default/) | Mutable class attributes should be annotated with `typing.ClassVar` |  |
| RUF013 | [implicit-optional](https://docs.astral.sh/ruff/rules/implicit-optional/) | PEP 484 prohibits implicit `Optional` | 🛠️ |
| RUF015 | [unnecessary-iterable-allocation-for-first-element](https://docs.astral.sh/ruff/rules/unnecessary-iterable-allocation-for-first-element/) | Prefer `next({iterable})` over single element slice | 🛠️ |
| RUF016 | [invalid-index-type](https://docs.astral.sh/ruff/rules/invalid-index-type/) | Slice in indexed access to type `{value_type}` uses type `{index_type}` instead of an integer |  |
| RUF017 | [quadratic-list-summation](https://docs.astral.sh/ruff/rules/quadratic-list-summation/) | Avoid quadratic list summation | 🛠️ |
| RUF018 | [assignment-in-assert](https://docs.astral.sh/ruff/rules/assignment-in-assert/) | Avoid assignment expressions in `assert` statements |  |
| RUF019 | [unnecessary-key-check](https://docs.astral.sh/ruff/rules/unnecessary-key-check/) | Unnecessary key check before dictionary access | 🛠️ |
| RUF020 | [never-union](https://docs.astral.sh/ruff/rules/never-union/) | `{never_like} | T` is equivalent to `T` | 🛠️ |
| RUF021 | [parenthesize-chained-operators](https://docs.astral.sh/ruff/rules/parenthesize-chained-operators/) | Parenthesize `a and b` expressions when chaining `and` and `or` together, to make the precedence clear | 🛠️ |
| RUF022 | [unsorted-dunder-all](https://docs.astral.sh/ruff/rules/unsorted-dunder-all/) | `__all__` is not sorted | 🛠️ |
| RUF023 | [unsorted-dunder-slots](https://docs.astral.sh/ruff/rules/unsorted-dunder-slots/) | `{}.__slots__` is not sorted | 🛠️ |
| RUF024 | [mutable-fromkeys-value](https://docs.astral.sh/ruff/rules/mutable-fromkeys-value/) | Do not pass mutable objects as values to `dict.fromkeys` | 🛠️ |
| RUF026 | [default-factory-kwarg](https://docs.astral.sh/ruff/rules/default-factory-kwarg/) | `default_factory` is a positional-only argument to `defaultdict` | 🛠️ |
| RUF027 | [missing-f-string-syntax](https://docs.astral.sh/ruff/rules/missing-f-string-syntax/) | Possible f-string without an `f` prefix | 🧪🛠️ |
| RUF028 | [invalid-formatter-suppression-comment](https://docs.astral.sh/ruff/rules/invalid-formatter-suppression-comment/) | This suppression comment is invalid because {} | 🛠️ |
| RUF029 | [unused-async](https://docs.astral.sh/ruff/rules/unused-async/) | Function `{name}` is declared `async`, but doesn't `await` or use `async` features. | 🧪 |
| RUF030 | [assert-with-print-message](https://docs.astral.sh/ruff/rules/assert-with-print-message/) | `print()` call in `assert` statement is likely unintentional | 🛠️ |
| RUF031 | [incorrectly-parenthesized-tuple-in-subscript](https://docs.astral.sh/ruff/rules/incorrectly-parenthesized-tuple-in-subscript/) | Use parentheses for tuples in subscripts | 🧪🛠️ |
| RUF032 | [decimal-from-float-literal](https://docs.astral.sh/ruff/rules/decimal-from-float-literal/) | `Decimal()` called with float literal argument | 🛠️ |
| RUF033 | [post-init-default](https://docs.astral.sh/ruff/rules/post-init-default/) | `__post_init__` method with argument defaults | 🛠️ |
| RUF034 | [useless-if-else](https://docs.astral.sh/ruff/rules/useless-if-else/) | Useless `if`- `else` condition |  |
| RUF035 | [ruff-unsafe-markup-use](https://docs.astral.sh/ruff/rules/ruff-unsafe-markup-use/) | Unsafe use of `{name}` detected | ❌ |
| RUF036 | [none-not-at-end-of-union](https://docs.astral.sh/ruff/rules/none-not-at-end-of-union/) | `None` not at the end of the type annotation. | 🧪 |
| RUF037 | [unnecessary-empty-iterable-within-deque-call](https://docs.astral.sh/ruff/rules/unnecessary-empty-iterable-within-deque-call/) | Unnecessary empty iterable within a deque call | 🧪🛠️ |
| RUF038 | [redundant-bool-literal](https://docs.astral.sh/ruff/rules/redundant-bool-literal/) | `Literal[True, False, ...]` can be replaced with `Literal[...] | bool` | 🧪🛠️ |
| RUF039 | [unraw-re-pattern](https://docs.astral.sh/ruff/rules/unraw-re-pattern/) | First argument to {call} is not raw string | 🧪🛠️ |
| RUF040 | [invalid-assert-message-literal-argument](https://docs.astral.sh/ruff/rules/invalid-assert-message-literal-argument/) | Non-string literal used as assert message |  |
| RUF041 | [unnecessary-nested-literal](https://docs.astral.sh/ruff/rules/unnecessary-nested-literal/) | Unnecessary nested `Literal` | 🛠️ |
| RUF043 | [pytest-raises-ambiguous-pattern](https://docs.astral.sh/ruff/rules/pytest-raises-ambiguous-pattern/) | Pattern passed to `match=` contains metacharacters but is neither escaped nor raw | 🧪 |
| RUF045 | [implicit-class-var-in-dataclass](https://docs.astral.sh/ruff/rules/implicit-class-var-in-dataclass/) | Assignment without annotation found in dataclass body | 🧪 |
| RUF046 | [unnecessary-cast-to-int](https://docs.astral.sh/ruff/rules/unnecessary-cast-to-int/) | Value being cast to `int` is already an integer | 🛠️ |
| RUF047 | [needless-else](https://docs.astral.sh/ruff/rules/needless-else/) | Empty `else` clause | 🧪🛠️ |
| RUF048 | [map-int-version-parsing](https://docs.astral.sh/ruff/rules/map-int-version-parsing/) | `__version__` may contain non-integral-like elements |  |
| RUF049 | [dataclass-enum](https://docs.astral.sh/ruff/rules/dataclass-enum/) | An enum class should not be decorated with `@dataclass` |  |
| RUF051 | [if-key-in-dict-del](https://docs.astral.sh/ruff/rules/if-key-in-dict-del/) | Use `pop` instead of `key in dict` followed by `del dict[key]` | 🛠️ |
| RUF052 | [used-dummy-variable](https://docs.astral.sh/ruff/rules/used-dummy-variable/) | Local dummy variable `{}` is accessed | 🧪🛠️ |
| RUF053 | [class-with-mixed-type-vars](https://docs.astral.sh/ruff/rules/class-with-mixed-type-vars/) | Class with type parameter list inherits from `Generic` | 🛠️ |
| RUF054 | [indented-form-feed](https://docs.astral.sh/ruff/rules/indented-form-feed/) | Indented form feed | 🧪 |
| RUF055 | [unnecessary-regular-expression](https://docs.astral.sh/ruff/rules/unnecessary-regular-expression/) | Plain string pattern passed to `re` function | 🧪🛠️ |
| RUF056 | [falsy-dict-get-fallback](https://docs.astral.sh/ruff/rules/falsy-dict-get-fallback/) | Avoid providing a falsy fallback to `dict.get()` in boolean test positions. The default fallback `None` is already falsy. | 🧪🛠️ |
| RUF057 | [unnecessary-round](https://docs.astral.sh/ruff/rules/unnecessary-round/) | Value being rounded is already an integer | 🛠️ |
| RUF058 | [starmap-zip](https://docs.astral.sh/ruff/rules/starmap-zip/) | `itertools.starmap` called on `zip` iterable | 🛠️ |
| RUF059 | [unused-unpacked-variable](https://docs.astral.sh/ruff/rules/unused-unpacked-variable/) | Unpacked variable `{name}` is never used | 🧪🛠️ |
| RUF060 | [in-empty-collection](https://docs.astral.sh/ruff/rules/in-empty-collection/) | Unnecessary membership test on empty collection | 🧪 |
| RUF061 | [legacy-form-pytest-raises](https://docs.astral.sh/ruff/rules/legacy-form-pytest-raises/) | Use context-manager form of `pytest.{}()` | 🧪🛠️ |
| RUF063 | [access-annotations-from-class-dict](https://docs.astral.sh/ruff/rules/access-annotations-from-class-dict/) | Use `{suggestion}` instead of `__dict__` access | 🧪 |
| RUF064 | [non-octal-permissions](https://docs.astral.sh/ruff/rules/non-octal-permissions/) | Non-octal mode | 🧪🛠️ |
| RUF100 | [unused-noqa](https://docs.astral.sh/ruff/rules/unused-noqa/) | Unused `noqa` directive | 🛠️ |
| RUF101 | [redirected-noqa](https://docs.astral.sh/ruff/rules/redirected-noqa/) | `{original}` is a redirect to `{target}` | 🛠️ |
| RUF102 | [invalid-rule-code](https://docs.astral.sh/ruff/rules/invalid-rule-code/) | Invalid rule code in `# noqa`: {} | 🧪🛠️ |
| RUF200 | [invalid-pyproject-toml](https://docs.astral.sh/ruff/rules/invalid-pyproject-toml/) | Failed to parse pyproject.toml: {message} |  |

## [tryceratops (TRY)](https://docs.astral.sh/ruff/rules/\#tryceratops-try)

For more, see [tryceratops](https://pypi.org/project/tryceratops/) on PyPI.

| Code | Name | Message |  |
| --- | --- | --- | --- |
| TRY002 | [raise-vanilla-class](https://docs.astral.sh/ruff/rules/raise-vanilla-class/) | Create your own exception |  |
| TRY003 | [raise-vanilla-args](https://docs.astral.sh/ruff/rules/raise-vanilla-args/) | Avoid specifying long messages outside the exception class |  |
| TRY004 | [type-check-without-type-error](https://docs.astral.sh/ruff/rules/type-check-without-type-error/) | Prefer `TypeError` exception for invalid type |  |
| TRY200 | [reraise-no-cause](https://docs.astral.sh/ruff/rules/reraise-no-cause/) | Use `raise from` to specify exception cause | ❌ |
| TRY201 | [verbose-raise](https://docs.astral.sh/ruff/rules/verbose-raise/) | Use `raise` without specifying exception name | 🛠️ |
| TRY203 | [useless-try-except](https://docs.astral.sh/ruff/rules/useless-try-except/) | Remove exception handler; error is immediately re-raised |  |
| TRY300 | [try-consider-else](https://docs.astral.sh/ruff/rules/try-consider-else/) | Consider moving this statement to an `else` block |  |
| TRY301 | [raise-within-try](https://docs.astral.sh/ruff/rules/raise-within-try/) | Abstract `raise` to an inner function |  |
| TRY400 | [error-instead-of-exception](https://docs.astral.sh/ruff/rules/error-instead-of-exception/) | Use `logging.exception` instead of `logging.error` | 🛠️ |
| TRY401 | [verbose-log-message](https://docs.astral.sh/ruff/rules/verbose-log-message/) | Redundant exception object included in `logging.exception` call |  |
