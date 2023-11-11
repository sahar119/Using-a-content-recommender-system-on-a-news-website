import requests
import streamlit as st

# Quotes API
QUOTES_API_URL = "https://api.chucknorris.io/jokes/random"


# Title
st.title("Funny and inspirational content suggestions")

# Display content
selected_content = st.radio("Select Content:", ("Chuck Norris", "Quotes"))

# Chuck Norris Joke
if selected_content == "Chuck Norris":
    st.subheader("Chuck Norris Joke")

    if st.button("Get Chuck Norris Joke"):
        # Make request to Chuck Norris API
        response = requests.get(QUOTES_API_URL)

        if response.status_code == 200:
            joke = response.json()["value"]
            st.success(joke)
        else:
            st.error("Error retrieving Chuck Norris joke. Please try again.")

# Quotes
elif selected_content == "Quotes":
    st.subheader("Quotes")

    if st.button("Get Quote"):
        # Make request to Quotes API
        category = 'happiness'
        api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
        response = requests.get(api_url, headers={'X-Api-Key': 'wbX1oMyWjLdczO1O6f5g+A==FJCIBLdy4ixUvKFZ'})
        if response.status_code == requests.codes.ok:
          st.write(response.text)
        else:
          print("Error:", response.status_code, response.text)

      




