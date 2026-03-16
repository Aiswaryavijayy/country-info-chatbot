import streamlit as st
import requests

def get_country_info(country_name):

    url = f"https://restcountries.com/v3.1/name/{country_name}"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return None

        data = response.json()

        country = None

        for item in data:
            if country_name.lower() in item["name"]["common"].lower():
                country = item
                break

        if country is None:
            country = data[0]

        capital = country.get("capital", ["Unknown"])[0]
        population = country.get("population", "Unknown")
        area = country.get("area", "Unknown")

        return capital, population, area

    except:
        return None

def get_random_fact():

    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            return response.json()["text"]

        return None

    except:
        return None

st.title("🌍 Country Information Chatbot")
st.write("Hello! I am your Country Info Bot.")
st.write("Enter a country name to get its capital city and a fun fact.")

country = st.text_input("Country Name")

if st.button("Get Information"):

    if country:

        country_info = get_country_info(country)
        fact = get_random_fact()

        if country_info and fact:

            capital, population, area = country_info

            st.success(f"Capital of {country.title()}: {capital}")
            st.write(f"Population: {population:,}")
            st.write(f"Area: {int(area)} km²")

            st.info(f"Did you know? {fact}")

        elif not country_info and fact:

            st.error("Country not found.")
            st.info(f"But here's a fun fact: {fact}")

        elif country_info and not fact:

            capital, population, area = country_info

            st.success(f"Capital of {country.title()}: {capital}")
            st.write(f"Population: {population:,}")
            st.write(f"Area: {int(area)} km²")

            st.warning("Fun fact could not be retrieved.")

        else:

            st.error("Could not retrieve information from APIs.")

    else:
        st.warning("Please enter a country name.")