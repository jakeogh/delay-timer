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
        verbose: bool = False,
    ):
        start = float(start)
        multiplier = float(multiplier)
        end = float(end)
        assert start >= 0
        assert end >= 0
        assert multiplier >= 0
        assert start <= end
        delay = start
        self.delay = delay
        self.multiplier = multiplier
        self.end = end
        self.verbose = verbose

    def _sleep(self):
        icp(self.delay)
        time.sleep(self.delay)

    def _sleep_next(self):
        if self.delay < self.end:
            self.delay = min(self.delay + (self.delay * self.multiplier), self.end)
            icp(self.delay)

    def sleep(self):
        self._sleep()
        self._sleep_next()
