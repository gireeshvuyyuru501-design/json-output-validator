# JSON Output Validator

An offline, standard-library Python MVP for checking structured AI outputs against a **documented subset** of JSON Schema. It checks required fields, primitive types, arrays, nested properties, enums, string minimum lengths, and additional properties. It does **not** implement full JSON Schema semantics; use a standards-compliant library such as `jsonschema` for production validation.

## Run

```bash
python validator.py
python -m unittest discover -s tests -v
```

The included five cases are **original synthetic fixtures**, not a public benchmark or Gemini responses. `report.json` contains pass/fail outcomes. No API key is required.

## Next steps

Integrate a standards-compliant JSON Schema validator, public JSON Schema Test Suite fixtures, Gemini structured outputs, and CI regression thresholds.

<!-- PORTFOLIO-OVERVIEW-START -->

## Project overview

Validate structured JSON outputs using synthetic labeled test cases and schema checks.

### Technologies and concepts

 - python
 - json
 - schema validation
 - ai testing
 - quality assurance

### Repository information

- **Category:** AI Quality Engineering / Software Testing
- **Evaluation type:** Offline and/or synthetic fixtures, as documented in this repository
- **Source code:** [GitHub repository](https://github.com/gireeshvuyyuru501-design/json-output-validator.git)
- **License:** MIT (subject to repository license file)

### AI Quality Engineering portfolio

This project is part of an 11-project portfolio covering evaluation datasets, structured-output validation, offline scoring, prompt regression, retrieval benchmarking, adversarial testing, agent tool calls, and quality monitoring.

[Explore the integrated AI Quality Engineering Platform](https://github.com/gireeshvuyyuru501-design/ai-quality-engineering-platform)

<!-- PORTFOLIO-OVERVIEW-END -->
