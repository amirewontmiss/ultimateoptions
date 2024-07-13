from numpy import exp, sqrt, log
from scipy.stats import norm

class MonteCarlo:
    def __init__(
        self,
        time_to_maturity: float,
        strike: float,
        current_price: float,
        volatility: float,
        interest_rate: float,
        num_simulations: int = 10000
    ):
        self.time_to_maturity = time_to_maturity
        self.strike = strike
        self.current_price = current_price
        self.volatility = volatility
        self.interest_rate = interest_rate
        self.num_simulations = num_simulations

    def calculation(self):
        time_to_maturity = self.time_to_maturity
        strike = self.strike
        current_price = self.current_price
        volatility = self.volatility
        interest_rate = self.interest_rate
        num_simulations = self.num_simulations

    # Simulate random stock price paths using geometric Brownian motion
        drift = interest_rate - 0.5 * volatility**2
        dt = time_to_maturity / num_simulations  # Time step for each simulation
        stock_prices = np.zeros((num_simulations + 1,))  # Array to store stock prices
        stock_prices[0] = current_price

        for i in range(1, num_simulations + 1):
            epsilon = random.gauss(0, 1)  # Generate random standard normal deviate
            stock_prices[i] = stock_prices[i - 1] * np.exp(drift * dt + volatility * epsilon * np.sqrt(dt))

    # Calculate option payoffs at expiration
        call_payoffs = np.maximum(stock_prices[-1] - strike, 0)
        put_payoffs = np.maximum(strike - stock_prices[-1], 0)

    # Discount payoffs back to present value
        discount_factor = np.exp(-interest_rate * time_to_maturity)
        call_price2 = discount_factor * np.mean(call_payoffs)
        put_price2 = discount_factor * np.mean(put_payoffs)

        self.call_price2 = call_price2
        self.put_price2 = put_price2

        return call_price2, put_price2