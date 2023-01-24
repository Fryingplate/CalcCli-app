import click
@click.command()
@click.argument('number1')
@click.argument('number2')
@click.argument('method')

def main(number1,number2,method):
    """Add Number 1 and Number 2"""
    if(method == 'add'):
        result = int(number1) + int(number2)
    elif(method == 'sub'):
        result = int(number1) - int(number2)
    elif(method == 'mult'):
        result = int(number1) * int(number2)
    elif(method == 'div'):
        result = float(number1) / float(number2)
    
    click.echo(click.style((f'Your Computed Answer is {result}'),fg='green',bg='black',bold=True))

if __name__ == '__main__':
    main()