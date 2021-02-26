import click
import logging
import os
import time
from datadog import initialize, statsd

options = {
    'statsd_host': os.environ.get('DD_AGENT_HOST', '127.0.0.1'),
    'statsd_port': 8125,
    'statsd_constant_tags': ['statslam'],
    'statsd_namespace': ['statslam']
}
initialize(**options)


@click.command()
def cli():
    while(True):
        statsd.increment('example_metric.gauge', tags=["environment:statslam"])
        logging.debug('tick')
        time.sleep(1)
