#!/usr/bin/env python3


import random

import click
from asserttool import ic

from delay_timer import DelayTimer


@click.command()
@click.option("--start", type=float, default=10)
@click.option("--multiplier", type=float, default=0.3)
@click.option("--random", "random_delay", is_flag=True)
@click.option("--end", type=float, default=359)
@click.option("--verbose", is_flag=True)
def cli(
    start: float,
    multiplier: float,
    random_delay: bool,
    end: float,
    verbose: bool,
):

    if random_delay:
        multiplier = multiplier * random.random()

    delay_timer = DelayTimer(
        start=start,
        multiplier=multiplier,
        end=end,
        verbose=verbose,
    )
    ic(delay_timer)
    delay_timer.sleep()
