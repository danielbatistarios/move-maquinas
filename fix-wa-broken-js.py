#!/usr/bin/env python3
"""
Fix broken WhatsApp JS in manutencao, pecas, and venda-de-maquinas-clark pages.

The broken pattern (produced by previous batch fix) looks like:
    var _waUrl = 'https://wa.me/...';
        if(typeof fbq === 'function'){ fbq('track', ...);
    window.open(_waUrl, '_blank', 'noopener,noreferrer');
    var btn = form.querySelector('[type="submit"]');
    var _btnOriginal = btn ? btn.innerHTML : null;
    if(btn){ btn.disabled = true; btn.textContent = 'Enviando...'; }
    ); }
      window.open(_waUrl, '_blank', 'noopener,noreferrer');
      if(btn){ btn.disabled = false; btn.innerHTML = _btnOriginal; }
    }
    fetch('...')
    .then(function(){ if (_btn) { ... } })   // _btn undefined
    .catch(function(){ if (_btn) { ... } });

The correct pattern should be:
    var _waUrl = 'https://wa.me/...';
    if(typeof fbq === 'function'){ fbq('track', ...); }
    window.open(_waUrl, '_blank', 'noopener,noreferrer');
    var btn = form.querySelector('[type="submit"]');
    var _btnOriginal = btn ? btn.innerHTML : null;
    if(btn){ btn.disabled = true; btn.textContent = 'Enviando...'; }
    fetch('...')
    .then(function(){ if (btn) { btn.disabled = false; btn.innerHTML = _btnOriginal; } })
    .catch(function(){ if (btn) { btn.disabled = false; btn.innerHTML = _btnOriginal; } });
"""

import re
import os

TARGET_FILES = [
    "anapolis-go/manutencao-empilhadeira/index.html",
    "anapolis-go/pecas-e-assistencia-empilhadeira/index.html",
    "aparecida-de-goiania-go/manutencao-empilhadeira/index.html",
    "aparecida-de-goiania-go/pecas-e-assistencia-empilhadeira/index.html",
    "brasilia-df/manutencao-empilhadeira/index.html",
    "brasilia-df/pecas-e-assistencia-empilhadeira/index.html",
    "caldas-novas-go/manutencao-empilhadeira/index.html",
    "caldas-novas-go/pecas-e-assistencia-empilhadeira/index.html",
    "formosa-go/manutencao-empilhadeira/index.html",
    "formosa-go/pecas-e-assistencia-empilhadeira/index.html",
    "goiania-go/manutencao-empilhadeira/index.html",
    "goiania-go/pecas-e-assistencia-empilhadeira/index.html",
    "inhumas-go/manutencao-empilhadeira/index.html",
    "inhumas-go/pecas-e-assistencia-empilhadeira/index.html",
    "itumbiara-go/manutencao-empilhadeira/index.html",
    "itumbiara-go/pecas-e-assistencia-empilhadeira/index.html",
    "luziania-go/manutencao-empilhadeira/index.html",
    "luziania-go/pecas-e-assistencia-empilhadeira/index.html",
    "senador-canedo-go/manutencao-empilhadeira/index.html",
    "senador-canedo-go/pecas-e-assistencia-empilhadeira/index.html",
    "trindade-go/manutencao-empilhadeira/index.html",
    "trindade-go/pecas-e-assistencia-empilhadeira/index.html",
    "uruacu-go/manutencao-empilhadeira/index.html",
    "uruacu-go/pecas-e-assistencia-empilhadeira/index.html",
    "valparaiso-de-goias-go/manutencao-empilhadeira/index.html",
    "valparaiso-de-goias-go/pecas-e-assistencia-empilhadeira/index.html",
    "venda-de-maquinas-clark/index.html",
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Regex that matches the broken block.
# The pattern captures:
#   1. The _waUrl line
#   2. The fbq block (with optional spaces/tabs before 'if')
#   3. The first window.open (already correct position)
#   4. btn variable declarations
#   5. The ); } syntax error + duplicate window.open + orphaned if(btn) lines
#   6. The fetch() call
#   7. The .then/.catch with _btn (wrong variable name) OR btn
BROKEN_PATTERN = re.compile(
    r"(    var _waUrl = 'https://wa\.me/[^']+'\s*\+ encodeURIComponent\(msg\);)\s*"
    r"\s*if\s*\(typeof fbq === 'function'\)\s*\{[^}]+\}\s*"
    r"    window\.open\(_waUrl, '_blank', 'noopener,noreferrer'\);\s*"
    r"    var btn = form\.querySelector\('\[type=\"submit\"\]'\);\s*"
    r"    var _btnOriginal = btn \? btn\.innerHTML : null;\s*"
    r"    if\s*\(btn\)\s*\{\s*btn\.disabled = true;\s*btn\.textContent = 'Enviando\.\.\.';\s*\}\s*"
    r"\s*\);\s*\}\s*"                               # ); } syntax error
    r"      window\.open\(_waUrl, '_blank', 'noopener,noreferrer'\);\s*"  # duplicate
    r"      if\s*\(btn\)\s*\{\s*btn\.disabled = false;\s*btn\.innerHTML = _btnOriginal;\s*\}\s*"
    r"    \}\s*"
    r"(    fetch\('https://[^']+',\s*\{[^}]+\}[^)]+\))"  # fetch() call
    r"\s*\.then\(function\(\)\s*\{\s*if\s*\([_]?btn\)\s*\{\s*[_]?btn\.disabled = false;\s*[_]?btn\.innerHTML = _btnOriginal;\s*\}\s*\}\)"
    r"\s*\.catch\(function\(\)\s*\{\s*if\s*\([_]?btn\)\s*\{\s*[_]?btn\.disabled = false;\s*[_]?btn\.innerHTML = _btnOriginal;\s*\}\s*\}\);",
    re.DOTALL
)

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Count window.open occurrences to confirm this file has the bug
    wo_count = content.count("window.open(_waUrl, '_blank', 'noopener,noreferrer')")
    if wo_count < 2:
        print(f"  SKIP (no duplicate window.open): {filepath}")
        return False

    # Use a more targeted approach: find the broken block by markers
    # and replace it line by line

    # Pattern using simpler line-based search
    # Find: "    ); }" followed by duplicate window.open
    broken_marker = "    ); }"
    if broken_marker not in content:
        # Try with spaces variation
        broken_marker2 = "    );\n      }"
        if broken_marker2 not in content:
            print(f"  SKIP (no ); }} marker): {filepath}")
            return False

    return None  # Signal to use line-based approach

def fix_file_linebased(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    i = 0
    changed = False

    while i < len(lines):
        line = lines[i]

        # Detect the broken fbq block start: "        if(typeof fbq" or "    if (typeof fbq"
        # that is followed immediately by window.open (NOT inside function _abrir)
        # The signature of the broken block:
        # Line N:   "    var _waUrl = ..."
        # Line N+1: "        if(typeof fbq..."  (indented with spaces, missing closing })
        # Line N+2: "    window.open(...)"
        # ...
        # Line N+K: "    ); }"
        # Line N+K+1: "      window.open(...)"   <- duplicate

        # Detect: line with "    ); }" (the syntax error)
        stripped = line.rstrip()
        if stripped in ("    ); }", "    );", "    ); } "):
            # Look back to find the start of this broken block
            # and look ahead to find the duplicate window.open

            # Check next lines for the duplicate window.open pattern
            j = i + 1
            # Skip blank lines
            while j < len(lines) and lines[j].strip() == '':
                j += 1

            if j < len(lines) and "window.open(_waUrl, '_blank', 'noopener,noreferrer')" in lines[j]:
                # Found the duplicate. Now reconstruct.
                # Skip: current line ("); }"), the duplicate window.open, and the orphaned if(btn) reset
                # j   = duplicate window.open
                # j+1 = if(btn){ btn.disabled = false; btn.innerHTML = _btnOriginal; }
                # j+2 = closing }

                k = j + 1
                # Skip the orphaned btn reset line
                while k < len(lines) and lines[k].strip() == '':
                    k += 1
                if k < len(lines) and "btn.disabled = false" in lines[k]:
                    k += 1
                # Skip the orphaned closing }
                while k < len(lines) and lines[k].strip() == '':
                    k += 1
                if k < len(lines) and lines[k].strip() == '}':
                    k += 1

                # Now find the fetch() call at position k
                # Skip to fetch line
                while k < len(lines) and 'fetch(' not in lines[k]:
                    k += 1

                # Collect the fetch block (multi-line)
                fetch_lines = []
                brace_depth = 0
                paren_depth = 0
                in_fetch = False

                m = k
                while m < len(lines):
                    fl = lines[m]
                    fetch_lines.append(fl)
                    if 'fetch(' in fl and not in_fetch:
                        in_fetch = True

                    paren_depth += fl.count('(') - fl.count(')')

                    # End of fetch when we hit .then/.catch chain end with ';'
                    if in_fetch and paren_depth <= 0 and '.catch(' in fl and fl.rstrip().endswith(');'):
                        m += 1
                        break
                    m += 1

                # Fix the _btn references in fetch .then/.catch to use btn
                fetch_block = ''.join(fetch_lines)
                fetch_block = fetch_block.replace('if (_btn) {', 'if (btn) {')
                fetch_block = fetch_block.replace('_btn.disabled', 'btn.disabled')
                fetch_block = fetch_block.replace('_btn.innerHTML', 'btn.innerHTML')

                # Now fix the fbq closing brace issue
                # Look backwards in new_lines to find the unclosed fbq if block
                # The broken fbq line looks like:
                #   "        if(typeof fbq === 'function'){ fbq('track', ...);  <- missing }
                # We need to close it properly

                # Find and fix the unclosed fbq line in new_lines (already added)
                for n in range(len(new_lines) - 1, max(len(new_lines) - 20, -1), -1):
                    nl = new_lines[n]
                    if "if(typeof fbq === 'function')" in nl or "if (typeof fbq === 'function')" in nl:
                        stripped_nl = nl.rstrip()
                        # Check if it doesn't end with } (unclosed)
                        if not stripped_nl.endswith('}'):
                            new_lines[n] = stripped_nl + ' }\n'
                        break

                # Add the fetch block with fixed variable names
                new_lines.append(fetch_block if fetch_block.endswith('\n') else fetch_block + '\n')

                i = m  # Continue after the fetch block
                changed = True
                continue

        new_lines.append(line)
        i += 1

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        # Verify no more duplicates
        result = ''.join(new_lines)
        remaining = result.count("window.open(_waUrl, '_blank', 'noopener,noreferrer')")
        btn_ref = result.count('if (_btn)')
        print(f"  FIXED: {filepath} | window.open count: {remaining} | _btn refs: {btn_ref}")
        return True
    else:
        print(f"  NO CHANGE: {filepath}")
        return False

def main():
    fixed = 0
    skipped = 0

    for rel_path in TARGET_FILES:
        filepath = os.path.join(BASE_DIR, rel_path)
        if not os.path.exists(filepath):
            print(f"  NOT FOUND: {filepath}")
            skipped += 1
            continue

        result = fix_file_linebased(filepath)
        if result:
            fixed += 1
        else:
            skipped += 1

    print(f"\nDone: {fixed} fixed, {skipped} skipped/unchanged")

if __name__ == '__main__':
    main()
