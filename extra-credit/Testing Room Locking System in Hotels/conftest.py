import pytest  # added
from _pytest import runner, _code # added

def pytest_runtest_makereport(item, call):
    when = call.when
    duration = call.stop-call.start
    keywords = dict([(x,1) for x in item.keywords])
    excinfo = call.excinfo
    sections = []
    if not call.excinfo:
        outcome = "passed"
        longrepr = None
    else:
        if not isinstance(excinfo, _code.ExceptionInfo):
            outcome = "failed"
            longrepr = excinfo
        elif excinfo.errisinstance(pytest.skip.Exception):
            outcome = "skipped"
            r = excinfo._getreprcrash()
            longrepr = (str(r.path), r.lineno, r.message)
        else:
            outcome = "failed"
            if call.when == "call" and \
                    isinstance(excinfo.value, AssertionError): #added
                longrepr = item.repr_failure(excinfo)
            else: # exception in setup or teardown
                when = 'setup' if when == 'call' else when  #added
                longrepr = item._repr_failure_py(excinfo,
                                            style=item.config.option.tbstyle)
    for rwhen, key, content in item._report_sections:
        sections.append(("Captured %s %s" %(key, rwhen), content))
    return runner.TestReport(item.nodeid, item.location,
                      keywords, outcome, longrepr, when,
                      sections, duration)

