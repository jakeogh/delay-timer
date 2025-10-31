#!/usr/bin/env python3
# -*- coding: utf8 -*-

# pylint: disable=missing-docstring               # [C0111] docstrings are always outdated and wrong
# pylint: disable=too-few-public-methods          # [R0903]
from __future__ import annotations

import time
from random import randrange


def random_delay_seconds(min_seconds: int, max_seconds: int):
    """Sleep for a random number of seconds between min_seconds and max_seconds (inclusive)."""
    delay = randrange(min_seconds, max_seconds + 1)
    time.sleep(delay)


class DelayTimer:
    """
    Exponential backoff timer that increases delay between operations.

    Starts at 'start' seconds and multiplies by 'multiplier' after each sleep.
    If 'end' is specified, delay will not exceed that maximum.
    If 'end' is None, delay will grow indefinitely.
    """

    def __init__(
        self,
        start: float,
        end: float | None = None,
        multiplier: float = 1.5,
    ):
        start = float(start)
        multiplier = float(multiplier)
        if end is not None:
            end = float(end)
            assert end > start, "end must be greater than start"
        assert start > 0, "start must be positive"
        assert (
            multiplier > 1.0
        ), "multiplier must be greater than 1.0 for exponential growth"
        self.delay = start
        self.multiplier = multiplier
        self.end = end

    def _sleep(self):
        # icp(self.delay, self.multiplier, self.end)
        time.sleep(self.delay)

    def _sleep_next(self):
        if self.end is None:
            # No maximum, grow indefinitely
            self.delay = self.delay * self.multiplier
        elif self.delay < self.end:
            # Cap at maximum
            self.delay = min(self.delay * self.multiplier, self.end)

    def sleep(self):
        """Sleep for the current delay duration, then increase the delay for next time."""
        self._sleep()
        self._sleep_next()
