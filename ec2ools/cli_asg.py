# -*- coding: utf-8 -*-

"""Console script for ec2ools."""
import sys
import json
import click
from ec2ools.aws.asg import (
    Asg
)
ctx_settings = {
    'help_option_names': ['-h', '--help']
}

@click.group(context_settings=ctx_settings)
def main():
    pass


@main.command(name='is-oldest-instance', help=("Check if the instance is "
                                               "the oldest and exit 0 if "
                                               "true and exit 1 if not. "
                                               "If --instance_id/-i is not "
                                               "specified the current instanceId "
                                               "will be used."))
@click.option('--instance_id', '-i', type=str)
def is_oldest_instance(**kw):
    """
    """
    asg = Asg()

    res = asg.is_oldest_instance(kw.get('instance_id'))

    if not res:
        exit(1)
    exit(0)

@main.command('get-instances')
def get_asg_instances(**kw):
    """
    """
    asg = Asg()
    id = 'i-0856c9af877a1c264'
    asg_find = asg.get_asg_by_instance(id)

    print(asg_find)


@main.command(name='get-asg')
def get_asg(**kw):
    pass

