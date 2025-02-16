# Currency Converter Application 💱
#### Video Demo: <https://youtu.be/XNfxz3Xvk7E> 🎥
#### Description:

The **Currency Converter Application** is a Python-based tool designed to perform real-time currency conversions between various global currencies. Built using the `requests` library for web scraping, `BeautifulSoup` for parsing HTML content, and `Tkinter` for the graphical user interface (GUI), this application allows users to select source and target currencies, retrieve the latest exchange rates, and view converted amounts in various quantities.

🌍 The core functionality of the app relies on fetching exchange rates from Xe.com, a popular website for currency conversion data. Upon selecting the source and target currencies from dropdown menus, the app sends an HTTP request to Xe.com, scrapes the exchange rate, and performs the conversion. The user can see the conversion results in the form of amounts for quantities such as 1, 5, 10, 25, and 50 units of the source currency.

## Files Overview 📂

- **`currency_converter.py`**: This is the main Python script for the project. It contains the primary logic for:
  - Fetching currency data from Xe.com using `requests` 🌐.
  - Parsing the HTML response with `BeautifulSoup` 🧑‍💻 to extract the conversion rate.
  - A simple user interface built with `Tkinter` 🖥️ that allows users to select currencies and view conversion results.
  - Error handling for invalid currency codes or failed data retrieval 🚫.

- **`country.json`**: This JSON file contains a list of countries, their respective currency codes, and names. It is used to populate the dropdown menus for selecting source and target currencies. The file helps ensure the app can recognize a wide variety of country names or currency codes 🌏.

## Design Choices 🧠

1. **Currency Code Validation** ✅: 
   A key feature of the app is its ability to validate the currency codes before initiating the conversion. This prevents the app from attempting to convert using invalid or unsupported currencies, which ensures a smoother user experience and reduces errors.

2. **Real-Time Data Fetching ⏱️**:
   Instead of storing static exchange rates, the application fetches real-time rates from Xe.com. This ensures that the user always receives the most up-to-date conversion data without needing to manually update rates in the app.

3. **Tkinter for GUI 🎨**:
   I chose `Tkinter` for the graphical interface due to its simplicity and ease of use. It provides a straightforward way to implement interactive elements like buttons and dropdowns, making it easy to design an intuitive UI for users.

4. **Error Handling 🚨**:
   Error handling was implemented to address cases like invalid currency codes or issues with retrieving the data. The app displays clear error messages using `messagebox` to inform users of any issues.

## Key Features ⭐

- **Country and Currency Selection 🌎**: Users can search and select countries either by their currency codes or names, making the currency selection flexible and user-friendly.
- **Conversion for Multiple Quantities 💸**: The app displays conversions for various quantities (1, 5, 10, 25, 50), providing users with more information at once.
- **Real-Time Conversion 🔄**: By scraping Xe.com for the latest exchange rates, users always get the most current conversion data available.
- **Error Handling ⚠️**: Clear and user-friendly error messages guide users when something goes wrong (e.g., invalid currency codes or issues with data retrieval).

## Challenges and Future Improvements 🚧

While the app works efficiently with real-time data, one of the challenges was ensuring proper error handling for cases where Xe.com might be down or the HTML structure changes unexpectedly. In the future, I plan to add additional features such as:
- Supporting bulk conversions for multiple amounts 📊.
- Adding historical exchange rates for users who want to view trends over time 📈.
- Improving the UI design for a more modern look with additional features like a currency converter history 🕒.

Overall, the **Currency Converter Application** provides a solid base for currency conversion functionality, and with further enhancements, it can be expanded into a more powerful tool 🔧.

