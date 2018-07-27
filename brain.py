from math import ceil

class Brain:
    def __init__(self):
        pass

    def search_for_a_pump(self, ticket):
        response = []

        for symbol in ticket.copy():
            #TODO: Debug temporal
            if float(symbol['priceChangePercent']) >= 4.0:
                symbol['order'] = ceil(float(symbol['priceChangePercent']))

                if float(symbol['priceChangePercent']) >= 4.0 and float(symbol['priceChangePercent']) < 7.0:
                    symbol['colour'] = 2 #Green
                    symbol['bg'] = 0 #black

                elif float(symbol['priceChangePercent']) >= 7.0 and float(symbol['priceChangePercent']) < 12.0:
                    symbol['colour'] = 6 #yellow
                    symbol['bg'] = 0 #black

                elif float(symbol['priceChangePercent']) >= 12.0 and float(symbol['priceChangePercent']) < 50:
                    symbol['colour'] = 1 #red
                    symbol['bg'] = 0 #black

                elif float(symbol['priceChangePercent']) >= 10.0 and float(symbol['priceChangePercent']) < 50:
                    symbol['colour'] = 7 #white
                    symbol['bg'] = 1 #red

                response.append(symbol)

        response = sorted(response, key=lambda k: k['order'], reverse=True)

        return response