# Betting Dashboard

This Streamlit app provides a betting dashboard for visualizing data related to betting outcomes.

![Betting Dashboard](https://github.com/noelAngelo/generator-bet/blob/main/static/screenshot.png?raw=true)


## Features

- **Payload Generation:** Allows users to generate simulated betting payloads based on specified start and end dates, number of payloads, and save directory.
- **Data Visualization:** Provides interactive visualizations of the generated data, including amount distribution and timeline analysis of the number of bets over time.
- **Payload Deletion:** Includes an option to delete all generated payloads in the specified save directory.

## Getting Started

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/betting-dashboard.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Usage

To run the Streamlit app, execute the following command:

```bash
streamlit run app.py
```
The app will open in your default web browser, allowing you to interact with the dashboard.
Generating Payloads

1.    Use the sidebar to select start and end dates, specify the number of payloads to generate, and provide a directory to save the payloads.

2.    Click the "Generate Payloads" button to create the payloads. The payloads will be saved in the specified directory as JSON files.

### Deleting Payloads

To delete all generated payloads, click the "Delete Payloads" button in the sidebar. This action will remove all JSON files in the specified directory.
Data Visualization

Once payloads are generated, the app displays interactive visualizations of the data, including:

- Amount distribution: Histogram showing the distribution of betting amounts.
- Timeline analysis: Line chart depicting the number of bets over time.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

- Fork the repository.
- Create a new branch (git checkout -b feature/my-feature).
- Make your changes.
- Commit your changes (git commit -am 'Add my feature').
- Push to the branch (git push origin feature/my-feature).
- Create a new pull request.

License

This project is licensed under the MIT License - see the LICENSE file for details.