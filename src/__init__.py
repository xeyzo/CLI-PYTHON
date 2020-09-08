import click
from src._01_string import lowercase, uppercase, capitalize 
from src._02_reduce import add,subtract,multiply,divide
from src._03_statistic import mean,median,mode,fmean
from src._04_palindrome import palindrome
from src._05_obfuscator import obfuscate
from src._06_random import strrand
from src._07_ip import ip_int
from src._08_ip_eks import ip_eks
from src._09_input import sum_prompt
from src._10_crud import create,read,readid,delete

@click.group()
def cli():
    pass


#1-str_transformation
cli.add_command(lowercase)
cli.add_command(uppercase)
cli.add_command(capitalize)

#2-arithmathic
cli.add_command(add)
cli.add_command(subtract)
cli.add_command(multiply)
cli.add_command(divide)

#3-statistic
cli.add_command(mean)
cli.add_command(median)
cli.add_command(mode)
cli.add_command(fmean)

#4-palindrome
cli.add_command(palindrome)

#5-obfuscate
cli.add_command(obfuscate)

#6-random_str
cli.add_command(strrand)

#7-ip_private
cli.add_command(ip_int)

#8-ip_external
cli.add_command(ip_eks)

#9-sum
cli.add_command(sum_prompt)

#10-crud
cli.add_command(create)
cli.add_command(read)
cli.add_command(readid)
cli.add_command(delete)


if __name__ == "__main__":
    cli()