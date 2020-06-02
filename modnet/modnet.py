#!/usr/bin/python3

import click
import modnet

@click.group()
@click.option(
    '--verbose', '-v', 
    is_flag=True, 
    help="Will print verbose messages."
)

@click.option(
    '--netlist', '-n', 
    required=True, 
    help='Path where to find netlist'
)

@click.option(
    '--top-module', '-t', 
    required=True,
    help='Top module inside netlist'
)

@click.option(
    '--outdir', '-o', 
    default='./output', 
    help='Path whete to save resulting netlist with injections'
)

@click.option(
    '--mode', '-t', 
    default='synplify',  
    type=click.Choice(['synplify', 'vivado', 'yosis']),
    help='Mode defines the netlist origin synthesizer'
)

@click.pass_context
def main(verbose,netlist,top_module,mode,outdir):
    if verbose:
        click.echo("We are in the verbose mode.")
    ctx.obj = Analysis(netlist,outdir)
if __name__ == "__main__":
    main()