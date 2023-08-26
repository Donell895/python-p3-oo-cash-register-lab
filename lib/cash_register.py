#!/usr/bin/env python3
class CashRegister:
    def __init__(self, discount_percent):
        self.discount_percent = discount_percent

    def calculate_total_price(self, price):
        discounted_price = price * (1 - self.discount_percent / 100)
        return discounted_price

