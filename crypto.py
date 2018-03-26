
#!/usr/bin/python3.4
#-*- coding: utf-8-*-
import click
import cryptocompare
print("###################crypto####################")
@click.command()
@click.option('--currency', prompt='Choisissez votre devise: EUR, USD', help='choisissez la monnaie')
@click.option('--coin', prompt='choisissez votre monnaie: BTC, ETH, XMR, etc ... ', help='Chosissez votre cryptomonnaie')
def chooseCoinCurrency(coin, currency):
    print('vous avez choisis %s'% coin, 'et %s'% en monnaie, '!')

    def beginAction(coin, currency):
        print(cryptocompare.get_price(coin, curr=currency, full=False))

    beginAction(coin, currency)

if __name__ == '__main__':
    chooseCoinCurrency()
