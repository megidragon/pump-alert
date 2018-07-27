import requests
import time
from sys import argv
from brain import Brain
from asciimatics.screen import Screen

def main(screen):
    ticket = []
    brain = Brain()

    while True:
        response = requests.get('https://api.binance.com/api/v1/ticker/24hr')
        ticket = response.json()

        #logica para predecir pumps
        symbols = brain.search_for_a_pump(ticket=ticket)

        screen.print_at("Bot de prediccion de pumps.".format( count=len(ticket)), 0, 0, colour=screen.COLOUR_GREEN)
        screen.print_at("Analizando {count} simbolos en binance.".format( count=len(ticket)), 0, 1)
        screen.print_at("Se han encontrado {count} simbolos como posibles pumps".format(count=len(symbols)), 0, 2)

        # Activa un bot para ese simbolo si encuentra un posible pump
        if len(symbols) > 0:
            line=3
            for symbol in symbols:
                #TODO: Call bot
                screen.print_at(' -> Cambio 24hs: {change}%, Simbolo: {symbol}, Precio actual: {price},Precio mayor: {high}, Precio menor: {low}'
                    .format(
                        symbol  = symbol['symbol'],
                        change  = symbol['priceChangePercent'],
                        high    = symbol['highPrice'],
                        low     = symbol['lowPrice'],
                        price   = symbol['lastPrice']
                    ),
                    0, line, # Position
                    colour=symbol['colour'],
                    bg=symbol['bg']
                )
                line += 1

        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            return
        screen.refresh()

        time.sleep(10)

try:
    if __name__ == "__main__":
        Screen.wrapper(main)
except (KeyboardInterrupt, SystemExit):
    print('\r\n\r\nBye Bye')