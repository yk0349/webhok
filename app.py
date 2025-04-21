from flask import Flask, request, jsonify
from kiteconnect import KiteConnect, KiteTicker
import os

app = Flask(__name__)

# Kite Connect setup
api_key = os.getenv("KITE_API_KEY")
access_token = os.getenv("KITE_ACCESS_TOKEN")

kite = KiteConnect(api_key=api_key)
kite.set_access_token(access_token)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received:", data)

    signal = data.get("signal")
    instrument = data.get("instrument", "NSE:NIFTY50")

    try:
        if signal == "BUY":
            kite.place_order(
                tradingsymbol="NIFTY24APR18000CE",  # Replace with actual instrument
                exchange="NSE",
                transaction_type="BUY",
                quantity=50,
                order_type="MARKET",
                product="MIS",
                variety="regular"
            )
        elif signal == "SELL":
            kite.place_order(
                tradingsymbol="NIFTY24APR18000CE",  # Replace with actual instrument
                exchange="NSE",
                transaction_type="SELL",
                quantity=50,
                order_type="MARKET",
                product="MIS",
                variety="regular"
            )
        return jsonify({"message": "Order placed"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
