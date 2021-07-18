def convert_cad_to_usd(amount, rate=0.8):
    return(amount*rate)

print(convert_cad_to_usd(100))

# rate changed
print(convert_cad_to_usd(100, rate=0.75))