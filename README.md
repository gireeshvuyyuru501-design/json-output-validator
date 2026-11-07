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
