#!/usr/bin/env python3
# -*- coding: utf8 -*-

# pylint: disable=useless-suppression             # [I0021]
# pylint: disable=missing-docstring               # [C0111] docstrings are always outdated and wrong
# pylint: disable=fixme                           # [W0511] todo is encouraged
# pylint: disable=line-too-long                   # [C0301]
# pylint: disable=too-many-instance-attributes    # [R0902]
# pylint: disable=too-many-lines                  # [C0302] too many lines in module
# pylint: disable=invalid-name                    # [C0103] single letter var names, name too descriptive
# pylint: disable=too-many-return-statements      # [R0911]
# pylint: disable=too-many-branches               # [R0912]
# pylint: disable=too-many-statements             # [R0915]
# pylint: disable=too-many-arguments              # [R0913]
# pylint: disable=too-many-nested-blocks          # [R1702]
# pylint: disable=too-many-locals                 # [R0914]
# pylint: disable=too-few-public-methods          # [R0903]
# pylint: disable=no-member                       # [E1101] no member for base
# pylint: disable=attribute-defined-outside-init  # [W0201]
# pylint: disable=too-many-boolean-expressions    # [R0916] in if statement
from __future__ import annotations

import time

from asserttool import ic


class DelayTimer:
    def __init__(
        self,
        start: float,
        multiplier: float,
        end: float,
        verbose: bool | int | float,
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
        ic(self.delay)
        time.sleep(self.delay)

    def _sleep_next(self):
        if self.delay < self.end:
            self.delay = min(self.delay + (self.delay * self.multiplier), self.end)
            if self.verbose:
                ic(self.delay)

    def sleep(self):
        self._sleep()
        self._sleep_next()
