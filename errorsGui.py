import typing as tp
from psychopy import monitors

mon = monitors.getAllMonitors()
class MonitorError(Exception):
    def __init__(self, mon:tp.TypeVar('str') = mon[0], msg = None):
        if msg is None:
            msg = 'Unable to compute frame rate for monitor {}'.format(mon)
        super().__init__(msg)

class ExperimentConfigurationError(Exception):
    def __init__(self, msg = None):
        if msg is None:
            msg = 'Experiment settings are unconsistent'
        super().__init__(msg)

class PathError(Exception):
    def __init__(self, msg = None):
        if msg is None:
            msg = 'Improper path setting'
        super().__init__(msg)


class PathError(Exception):
    def __init__(self, msg = None):
        if msg is None:
            msg = 'Experiment settings are unconsistent'
        super().__init__(msg)

if __name__ == '__main__':
    raise MonitorError