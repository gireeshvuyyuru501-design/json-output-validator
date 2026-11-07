"""JSON output validation with Python's standard library."""
import argparse
import json
from pathlib import Path


def validate(value, schema, path='$'):
    """Validate a useful subset of JSON Schema; return structured errors."""
    errors = []
    kind = schema.get('type')
    types = {'object': dict, 'array': list, 'string': str, 'integer': int, 'number': (int, float), 'boolean': bool, 'null': type(None)}
    if kind in types:
        expected = types[kind]
        valid = isinstance(value, expected)
        if kind in ('integer', 'number') and isinstance(value, bool):
            valid = False
        if not valid:
            return [{'path': path, 'message': f'Expected {kind}, got {type(value).__name__}'}]
    if 'enum' in schema and value not in schema['enum']:
        errors.append({'path': path, 'message': 'Value is not in enum'})
    if isinstance(value, dict):
        for field in schema.get('required', []):
            if field not in value:
                errors.append({'path': f'{path}.{field}', 'message': 'Missing required property'})
        for field, item in value.items():
            if field in schema.get('properties', {}):
                errors.extend(validate(item, schema['properties'][field], f'{path}.{field}'))
            elif schema.get('additionalProperties') is False:
                errors.append({'path': f'{path}.{field}', 'message': 'Additional property not allowed'})
    if isinstance(value, list):
        if 'minItems' in schema and len(value) < schema['minItems']:
            errors.append({'path': path, 'message': 'Too few items'})
        if 'items' in schema:
            for i, item in enumerate(value):
                errors.extend(validate(item, schema['items'], f'{path}[{i}]'))
    if isinstance(value, str) and 'minLength' in schema and len(value) < schema['minLength']:
        errors.append({'path': path, 'message': 'String too short'})
    return errors


def evaluate_cases(cases, schema):
    results = []
    for case in cases:
        try:
            parsed = json.loads(case['output']) if isinstance(case['output'], str) else case['output']
            errors = validate(parsed, schema)
        except json.JSONDecodeError as exc:
            errors = [{'path': '$', 'message': f'Invalid JSON: {exc.msg}'}]
        results.append({'id': case['id'], 'valid': not errors, 'errors': errors})
    return {'total': len(results), 'passed': sum(r['valid'] for r in results), 'results': results}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--schema', default='schema.json')
    parser.add_argument('--cases', default='cases.json')
    parser.add_argument('--output', default='report.json')
    args = parser.parse_args()
    schema = json.loads(Path(args.schema).read_text(encoding='utf-8'))
    cases = json.loads(Path(args.cases).read_text(encoding='utf-8'))
    report = evaluate_cases(cases, schema)
    Path(args.output).write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps({'total': report['total'], 'passed': report['passed'], 'failed': report['total']-report['passed']}, indent=2))

if __name__ == '__main__':
    main()
