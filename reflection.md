# Reflection – Lab 5: Static Code Analysis

**1. Easiest vs Hardest fixes**  
- *Easiest*: Fixing style and encoding issues.  
- *Hardest*: Replacing `eval()` safely required understanding intent and adjusting logic.

**2. False positives**  
- Bandit flagged `open()` as missing encoding even for write-only usage—technically not a bug, just a style improvement.

**3. Integrating tools into workflow**  
- Add `flake8`, `pylint`, and `bandit` to a GitHub Actions CI pipeline.  
- Use `pre-commit` hooks to run them locally before pushing code.

**4. Improvements observed**  
- Code is safer (no silent except or eval).  
- File handling is cleaner and robust.  
- Naming and structure now follow PEP 8 for better readability.
