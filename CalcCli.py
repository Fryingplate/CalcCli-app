import click
@click.command()
@click.argument('number1')
@click.argument('number2')
@click.argument('method')

@click.option('--add',help="n1 n2 add")
@click.option('--sub',help="n1 n2 sub")
@click.option('--mult',help="n1 n2 mult")
@click.option('--div',help="n1 n2 div")
@click.option('--absolute difference',help="n1 n2 abso")


def main(number1,number2,method,name):

    

    """Add Number 1 and Number 2"""
    if(method == 'add'):
        result = int(number1) + int(number2)
    elif(method == 'sub'):
        result = int(number1) - int(number2)
    elif(method == 'mult'):
        result = int(number1) * int(number2)
    elif(method == 'div'):
        result = float(number1) / float(number2)
    elif(method == 'abso'):
        result = abs(number1-number2)
    
    click.echo(click.style((f'Your Computed Answer is {result}'),fg='cyan',bg='black',bold=True))

if __name__ == '__main__':
    main()
