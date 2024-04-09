#!/usr/bin/env python3
# -*- coding: utf8 -*-

# pylint: disable=missing-docstring               # [C0111] docstrings are always outdated and wrong
# pylint: disable=too-few-public-methods          # [R0903]
from __future__ import annotations

import time

from asserttool import ic
from asserttool import icp


class DelayTimer:
    def __init__(
        self,
        start: float,
        multiplier: float,
        end: float,
    ):
        start = float(start)
        multiplier = float(multiplier)
        end = float(end)
        assert start > 0
        assert end > start
        if multiplier == 0.0:
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
