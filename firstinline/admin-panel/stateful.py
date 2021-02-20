"""Store state for streamlit app using pickle."""
import pickle
from pathlib import Path

STATE_CACHE = Path("state.pickle")
_state = {}


def load():
    global _state
    if STATE_CACHE.exists():
        with STATE_CACHE.open('rb') as state:
            _state = pickle.load(state)


def save():
    with STATE_CACHE.open("wb") as state:
        pickle.dump(_state, state)


def record(f):
    def wrapper(label, *args, **kwargs):
        widget_value = f(label, *args, **kwargs)
        try:
            _state[label].append(widget_value)
        except (KeyError, AttributeError):
            _state[label] = [widget_value]

        wrapper.state = _state[label]
        return widget_value

    return wrapper


def clear():
    STATE_CACHE.unlink()


__all__ = [
    "record",
    "clear",
    "load"
]
