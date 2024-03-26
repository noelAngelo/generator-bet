import streamlit as st
import os
import pandas as pd
from datetime import datetime
from generator import PayloadGenerator
import json


# Function to create payloads based on user input
def create_payloads(start_date, end_date, num_payloads, save_directory):
    payloads = PayloadGenerator.generate_payloads(num_payloads, start_date, end_date)
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    for i, payload in enumerate(payloads):
        with open(os.path.join(save_directory, f"payload_{i}.json"), "w") as f:
            json.dump(payload, f)
    return payloads


def delete_files_in_directory(directory):
    files = os.listdir(directory)
    for file in files:
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            os.remove(file_path)


# Function to read payloads from files in a directory
def read_payloads_from_directory(directory):
    payloads = []
    files = os.listdir(directory)
    for file in files:
        if file.endswith(".json"):
            file_path = os.path.join(directory, file)
            with open(file_path, "r") as f:
                payload = f.read()
                payloads.append(payload)
    return payloads


# Function to parse payload data and extract relevant information
def parse_payload_data(payloads):
    amount_list = []
    created_at_list = []
    for payload in payloads:
        payload_data = json.loads(payload)
        bet_data = payload_data["betSportsbook"]
        amount_list.append(bet_data["amount"])
        created_at_list.append(
            {
                "created_at": datetime.fromtimestamp(bet_data["createdAt"]),
                "outcomes": len(bet_data["outcomes"])
            })
    return amount_list, created_at_list


# Streamlit app
def main():
    st.title("Betting Dashboard")

    with st.sidebar:
        # Generate payloads section
        st.subheader("Payload Generation")
        start_date = st.date_input("Select start date")
        end_date = st.date_input("Select end date")
        num_payloads = st.number_input("Enter the number of payloads", min_value=1, value=1)
        save_directory = st.text_input("Enter directory to save payloads:", value="data")

        if st.button("Generate Payloads"):
            create_payloads(start_date, end_date, num_payloads, save_directory)
            st.success("Payloads generated successfully.")

        if st.sidebar.button("Delete Payloads"):
            delete_files_in_directory(save_directory)
            st.success("Payloads deleted successfully.")

    # Visualize data section
    st.subheader("Data Visualization")

    # Read payloads from directory if available
    if os.path.exists(save_directory):
        payloads = read_payloads_from_directory(save_directory)
    else:
        payloads = []

    if len(payloads) > 0:
        # Parse payload data
        amount_list, created_at_list = parse_payload_data(payloads)

        # Amount Distribution
        st.subheader("Bet Amount Distribution")
        amount_df = pd.DataFrame({"Amount": amount_list})
        st.write(amount_df.describe())

        # Plot histogram for amount distribution
        st.bar_chart(amount_df)

        # Timeline Analysis - Number of Bets over Time
        st.subheader("Timeline Analysis - Number of Bets over Time")
        st.write("Created At List: ", created_at_list)
        created_at_df = pd.DataFrame(created_at_list)
        created_at_df['Date'] = pd.to_datetime(created_at_df['created_at'], unit='s').dt.date

        # Group by date and count the number of bets
        bets_by_date = created_at_df.groupby('Date')['outcomes'].sum().reset_index(name='Number of Bets')

        # Plot line chart for number of bets over time
        st.line_chart(bets_by_date.set_index('Date'))


if __name__ == "__main__":
    main()
