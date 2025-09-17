[Skip to content](https://docs.astral.sh/ty/rules/#rules)

# [Rules](https://docs.astral.sh/ty/rules/\#rules)

Rules are individual checks that ty performs to detect common issues in your code, such as
incompatible assignments, missing imports, or invalid type annotations. Each rule focuses on a
specific pattern and can be turned on or off depending on your project’s needs.

Tip

See [rules](https://docs.astral.sh/ty/reference/rules/) for an enumeration of all supported rules.

## [Rule levels](https://docs.astral.sh/ty/rules/\#rule-levels)

Each rule has a configurable level:

- `error`: violations are reported as errors and ty exits with an exit code of 1 if there's any.
- `warn`: violations are reported as warnings. Depending on your configuration, ty exits with an exit code of 0 if there are only warning violations (default) or 1 when using `--error-on-warning`.
- `ignore`: the rule is turned off

You can configure the level for each rule on the command line using the `--warn`, `--error`, and
`--ignore` flags. For example:

```
ty check \
  --warn unused-ignore-comment \        # Make `unused-ignore-comment` a warning
  --ignore redundant-cast \             # Disable `redundant-cast`
  --error possibly-unbound-attribute \  # Error on `possibly-unbound-attribute`
  --error possibly-unbound-import       # Error on `possibly-unbound-import`

```

The options can be repeated. Subsequent options override earlier options.

Rule levels can also be changed in the [`rules`](https://docs.astral.sh/ty/reference/configuration/#rules) section of a
[configuration file](https://docs.astral.sh/ty/configuration/).

For example, the following is equivalent to the command above:

```
[tool.ty.rules]
unused-ignore-comment = "warn"
redundant-cast = "ignore"
possibly-unbound-attribute = "error"
possibly-unbound-import = "error"

```
