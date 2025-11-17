import importlib
import traceback

module = importlib.import_module('tests.test_apputil')

tests = [name for name in dir(module) if name.startswith('test_')]
passed = 0
failed = 0
failed_details = []

for name in tests:
    fn = getattr(module, name)
    try:
        fn()
        print(f"PASS: {name}")
        passed += 1
    except AssertionError:
        print(f"FAIL: {name}")
        failed += 1
        failed_details.append((name, traceback.format_exc()))
    except Exception:
        print(f"ERROR: {name}")
        failed += 1
        failed_details.append((name, traceback.format_exc()))

print('\nSummary:')
print('Passed:', passed)
print('Failed:', failed)
if failed_details:
    print('\nFailure details:')
    for name, tb in failed_details:
        print('---', name)
        print(tb)
