import click

@click.group()
def coffee():
    """
    Something about Walmart coffee!
    """

@click.group(name="get")
def get_group():
    """
    Group of commands to learn something about Walmart Coffee
    """
    pass

@click.command(name="Number_of_type")
def coffee_type():
    """
    How many coffee type are there in our dataset?
    """
    click.echo('122')

@click.command(name="Most_popular")
def popular():
    """
    Which coffee type is the most popular?
    """
    click.echo('Medium Roast')

@click.command(name="Highest_rating")
def rating():
    """
    Which coffee type has the highest rating?
    """
    click.echo('Italian, Rating:5.0/5.0')

@click.command(name="Most_expensive")
def price():
    """
    Which coffee type is the most expensive?
    """
    click.echo('Italian')

@click.command(name="Weight")
def weight():
    """
    What coffee type has the highest/lowest weight?
    """
    click.echo('Top three heaviest coffee type are Mocha(instant coffee), Caramel,macchiat(iced coffee), and Instant coffee,arabica,dark roast with weight 2381.4, 1814.4, and 1134.0 gramms.')
    click.echo('Top four lightiest coffee type are Colombian(instant coffee), Mocha(iced coffee,latte), Instant coffee(light roast), and Espresso(instant coffee,dark roast) with weight 99.2, 99.2, 189.9 and 199.9 gramms.')


get_group.add_command(coffee_type)
get_group.add_command(popular)
get_group.add_command(price)
get_group.add_command(weight)
get_group.add_command(rating)

coffee.add_command(get_group)