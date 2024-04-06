import streamlit as st
from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    rate = c.get_rate(from_currency, to_currency)
    converted_amount = amount * rate
    return converted_amount

def main():
    st.title("Currency Converter")

    amount = st.number_input("Enter the amount:", value=1.00, min_value=0.01, step=0.01)

    supported_currencies = ["USD", "EUR", "GBP", "JPY", "CAD", "AUD", "CHF", "CNY", "SEK", "NZD", "KRW", "SGD", "NOK", "MXN", "INR", "RUB", "ZAR", "TRY", "BRL", "HKD", "ILS", "DKK", "PLN", "THB", "IDR", "HUF", "CZK", "CLP", "PHP", "AED", "COP", "SAR", "MYR", "RON", "ARS", "VND", "HRK", "UAH", "QAR", "KWD", "EGP", "PER", "BDT", "IQD", "DOP", "OMR", "LKR", "BDP", "TWD", "RSD", "TND", "MAD", "VEF", "UZS", "JOD", "BOB", "PYG", "GEL", "KZT", "GHS", "BYN", "AED", "AED", "AED", "AED", "AED", "AED", "AED", "AED", "AED", "AED", "AED", "AED", "AED", "AED", "AED", "AED", "AED"]

    from_currency = st.selectbox("From which currency:", supported_currencies, index=0)
    to_currency = st.selectbox("To which currency:", supported_currencies, index=1)

    if st.button("Convert"):
        converted_amount = convert_currency(amount, from_currency, to_currency)
        st.success(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()
