import requests


def get_country_info(country_name):

    try:
        url = f"https://restcountries.com/v3.1/name/{country_name}"
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return None

        data = response.json()

        country = None
        for item in data:
            if item["name"]["common"].lower() == country_name.lower():
                country = item
                break

        if country is None:
            country = data[0]

        capital = country.get("capital", ["Unknown"])[0]
        population = country.get("population", "Unknown")
        area = country.get("area", "Unknown")

        return {
            "capital": capital,
            "population": population,
            "area": area
        }

    except requests.exceptions.RequestException:
        return None

def get_random_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()
            return data["text"]

        return None

    except Exception as e:
        print("Fact API error:", e)
        return None
def chatbot():

    print(" ")
    print("Hello! I am your Country Info Bot ")
    

    while True:

        country = input("\nEnter a country name: ").strip()

        country_info = get_country_info(country)
        fact = get_random_fact()

        print("\n")

        if country_info and fact:
            print(f"The capital of {country.title()} is {country_info['capital']}.")
            print(f"Population: {country_info['population']}")
            print(f"Area: {country_info['area']} km²")
            print(f"\nDid you know? {fact}")

        elif not country_info and fact:
            print("Sorry, I couldn't find that country.")
            print(f"But here's a fun fact: {fact}")

        elif country_info and not fact:
            print(f"The capital of {country.title()} is {country_info['capital']}.")
            print("However, I couldn't retrieve a fun fact right now.")

        else:
            print("Sorry, I couldn't retrieve information at the moment.")

        print(" ")

       
        while True:
            again = input("\nDo you want to search another country? (yes/no): ").lower().strip()

            if again in ["yes", "y"]:
                break

            elif again in ["no", "n", "quit", "exit"]:
                print("\nThank you for using Country Info Bot. Goodbye!")
                return

            else:
                print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    chatbot()