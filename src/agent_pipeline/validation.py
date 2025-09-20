"""Validation utilities for agent pipeline output."""

from __future__ import annotations

import ast
import re
from typing import NamedTuple


class ValidationResult(NamedTuple):
    """Result of validating a document."""

    valid: bool
    errors: list[str]
    warnings: list[str]


def validate_python_syntax(content: str) -> tuple[bool, str]:
    """Check if Python code has valid syntax.

    Args:
        content: Python source code to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    try:
        ast.parse(content)
        return True, ""
    except SyntaxError as e:
        return False, f"Syntax error at line {e.lineno}: {e.msg}"


def check_string_literals(content: str) -> list[str]:
    """Check for common string literal issues in Lark grammars.

    Args:
        content: Python source code to check

    Returns:
        List of potential issues found
    """
    issues = []

    # Check for problematic empty raw strings
    if 'r""' in content:
        # Check if it's actually an empty string (not part of a larger string)
        if re.search(r'r""(?:\s|$|\+)', content):
            issues.append('Empty raw string r"" found - will cause syntax error')

    # Check for unterminated triple quotes
    triple_single = content.count("'''")
    if triple_single % 2 != 0:
        issues.append("Unmatched triple single quotes (''')")

    triple_double = content.count('"""')
    if triple_double % 2 != 0:
        issues.append('Unmatched triple double quotes (""")')

    # Check for mixed quote styles in concatenation
    concat_pattern = r"r'''.*?'''\s*\+.*?r\"\""
    if re.search(concat_pattern, content, re.DOTALL):
        issues.append("Mixed quote styles in string concatenation (r''' + r\"\")")

    return issues


def check_file_extension(filename: str) -> list[str]:
    """Check for file extension issues.

    Args:
        filename: Name of the file

    Returns:
        List of issues found
    """
    issues = []

    # Check for double extensions
    if filename.endswith(".py.py"):
        issues.append("Double .py extension detected")
    elif filename.endswith(".md.md"):
        issues.append("Double .md extension detected")

    # Check for mixed extensions
    if ".py" in filename and ".md" in filename:
        issues.append("Mixed .py and .md extensions in filename")

    return issues


def check_content_format(content: str, filename: str) -> list[str]:
    """Check if content format matches file extension.

    Args:
        content: File content
        filename: Name of the file

    Returns:
        List of issues found
    """
    issues = []

    if filename.endswith(".py"):
        # Check for markdown frontmatter in Python files
        if content.startswith("---\n"):
            issues.append("Markdown frontmatter found in Python file")

        # Check for markdown headers in Python files (outside of comments)
        lines = content.split("\n")
        for i, line in enumerate(lines, 1):
            if line.strip().startswith("#") and not line.strip().startswith("# "):
                # Could be a markdown header if multiple # in a row
                if re.match(r"^#{2,}\s", line.strip()):
                    issues.append(f"Possible markdown header at line {i}")

    elif filename.endswith(".md"):
        # Check for Python code that should be in a .py file
        if 'if __name__ == "__main__":' in content and "```" not in content:
            issues.append("Python main block found outside code block in markdown")

        # Check for class definitions outside code blocks
        if (
            re.search(r"^class\s+\w+.*?:", content, re.MULTILINE)
            and "```" not in content
        ):
            issues.append(
                "Python class definition found outside code block in markdown"
            )

    return issues


def validate_output(content: str, filename: str) -> ValidationResult:
    """Comprehensive validation of pipeline output.

    Args:
        content: File content to validate
        filename: Name of the output file

    Returns:
        ValidationResult with validation status and any issues found
    """
    errors = []
    warnings = []

    # Check file extension
    ext_issues = check_file_extension(filename)
    errors.extend(ext_issues)

    # Check content format matches extension
    format_issues = check_content_format(content, filename)
    warnings.extend(format_issues)

    # For Python files, do additional validation
    if filename.endswith(".py"):
        # Check syntax
        valid, syntax_error = validate_python_syntax(content)
        if not valid:
            errors.append(syntax_error)

        # Check string literals for Lark-specific issues
        string_issues = check_string_literals(content)
        errors.extend(string_issues)

    # Determine overall validity
    valid = len(errors) == 0

    return ValidationResult(valid=valid, errors=errors, warnings=warnings)


def fix_common_issues(content: str, filename: str) -> tuple[str, str, list[str]]:
    """Attempt to fix common issues in output.

    Args:
        content: Original content
        filename: Original filename

    Returns:
        Tuple of (fixed_content, fixed_filename, fixes_applied)
    """
    fixes = []
    fixed_content = content
    fixed_filename = filename

    # Fix double extensions
    if filename.endswith(".py.py"):
        fixed_filename = filename[:-3]  # Remove one .py
        fixes.append("Removed duplicate .py extension")
    elif filename.endswith(".md.md"):
        fixed_filename = filename[:-3]  # Remove one .md
        fixes.append("Removed duplicate .md extension")

    # Fix empty raw strings in Python files
    if filename.endswith(".py") and 'r""' in content:
        # Replace r"" with r''' in concatenations
        fixed_content = re.sub(r'r""(?=\s*\+|\s*$)', "r'''", fixed_content)
        if fixed_content != content:
            fixes.append("Replaced empty r\"\" with r'''")

    # Fix markdown frontmatter in Python files
    if filename.endswith(".py") and content.startswith("---\n"):
        # Find the end of frontmatter
        end_marker = content.find("\n---\n", 4)
        if end_marker > 0:
            # Convert frontmatter to Python docstring
            frontmatter = content[4:end_marker]
            rest = content[end_marker + 5 :]

            # Create a docstring from the frontmatter
            docstring_lines = ['"""']
            for line in frontmatter.split("\n"):
                if ":" in line:
                    key, value = line.split(":", 1)
                    docstring_lines.append(f"{key.strip()}: {value.strip()}")
            docstring_lines.append('"""')

            fixed_content = "\n".join(docstring_lines) + "\n\n" + rest
            fixes.append("Converted markdown frontmatter to Python docstring")

    return fixed_content, fixed_filename, fixes


if __name__ == "__main__":
    # Example usage and testing
    test_content = '''"""
Example Lark grammar with potential issues
"""

from lark import Lark

grammar = r""  # This will cause issues

parser = Lark(grammar)
'''

    result = validate_output(test_content, "test.py")
    print(f"Valid: {result.valid}")
    print(f"Errors: {result.errors}")
    print(f"Warnings: {result.warnings}")

    # Test fixing
    fixed_content, fixed_name, fixes = fix_common_issues(test_content, "test.py.py")
    print(f"Fixes applied: {fixes}")
