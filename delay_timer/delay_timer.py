#!/usr/bin/env python3
# -*- coding: utf8 -*-

# pylint: disable=missing-docstring               # [C0111] docstrings are always outdated and wrong
# pylint: disable=too-few-public-methods          # [R0903]
from __future__ import annotations

import time
from random import randrange

from asserttool import ic
from asserttool import icp


def random_delay_seconds(_min: int, _max: int):
    _delay = randrange(_min, _max + 1)
    time.sleep(_delay)


class DelayTimer:
    def __init__(
        self,
        start: float,
        end: float,
        multiplier: None | float = None,
    ):
        start = float(start)
        multiplier = float(multiplier)
        end = float(end)
        assert start > 0
        assert end > start
        if multiplier is None:
            multiplier = 0.5
        assert multiplier > 0
        delay = start
        self.delay = delay
        self.multiplier = multiplier
        self.end = end

    def _sleep(self):
        icp(self.delay, self.multiplier, self.end)
        time.sleep(self.delay)

    def _sleep_next(self):
        if self.delay < self.end:
            self.delay = min(self.delay + (self.delay * self.multiplier), self.end)

    def sleep(self):
        self._sleep()
        self._sleep_next()
