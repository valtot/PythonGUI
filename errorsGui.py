import typing as tp
from psychopy import monitors

mon = monitors.getAllMonitors()
class MonitorError(Exception):
    def __init__(self, mon:tp.TypeVar('str') = mon[0], msg = None):
        if msg is None:
            msg = 'Unable to compute frame rate for monitor {}'.format(mon)
        super().__init__(msg)

if __name__ == '__main__':
    raise MonitorError