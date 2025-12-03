tea_prices_inr = {
    "Masale Chai" : 40,
    "Green Tea" : 20,
    "Lemon Tea":10
}

tea_prices_usd = {tea:price/80 for tea , price in tea_prices_inr.items()}
print(tea_prices_usd)