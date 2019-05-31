# -*- coding: utf-8 -*-

"""Console script for ec2ools."""
import sys
import click
from ec2ools.aws.eip import EipBase


@click.group()
def main(args=None):
    pass


@main.command(name='allocate')
@click.option('id', '--id', '-i',
              type=str,
              help='Allocation-id for EIP or path to file containing allocation-id')
def eip_allocate(**kw):

    print(kw)

    eip = EipBase()
    eip.allocate_eip(kw.get('id'))

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
