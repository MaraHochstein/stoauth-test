###### google test
import streamlit as st
from streamlit_oauth import OAuth2Component
import os
import base64
import json

# import logging
# logging.basicConfig(level=logging.INFO)

st.title("Google OIDC Example")
st.write("This example shows how to use the raw OAuth2 component to authenticate with a Google OAuth2 and get email from id_token.")

# create an OAuth2Component instance
CLIENT_ID = st.secrets['oauthGoogleID']
CLIENT_SECRET = st.secrets['oauthGoogleSecret']
AUTHORIZE_ENDPOINT = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"
REVOKE_ENDPOINT = "https://oauth2.googleapis.com/revoke"
REDRIECT_URI  = 'https://kaditest.streamlit.app/component/streamlit_oauth.authorize_button/index.html'


if "auth" not in st.session_state:
    # create a button to start the OAuth2 flow
    oauth2 = OAuth2Component(CLIENT_ID, CLIENT_SECRET, AUTHORIZE_ENDPOINT, TOKEN_ENDPOINT, TOKEN_ENDPOINT, REVOKE_ENDPOINT)
    result = oauth2.authorize_button(
        name="Continue with Google",
        icon="https://www.google.com.tw/favicon.ico",
        redirect_uri=REDRIECT_URI,
        scope="openid email profile",
        key="google",
        extras_params={"prompt": "consent", "access_type": "offline"},
        use_container_width=True,
    )

    if result:
        st.write(result)
        # decode the id_token jwt and get the user's email address
        id_token = result["token"]["id_token"]
        # verify the signature is an optional step for security
        payload = id_token.split(".")[1]
        # add padding to the payload if needed
        payload += "=" * (-len(payload) % 4)
        payload = json.loads(base64.b64decode(payload))
        email = payload["email"]
        st.session_state["auth"] = email
        st.session_state["token"] = result["token"]
        st.rerun()
else:
    st.write("You are logged in!")
    st.write(st.session_state["auth"])
    st.write(st.session_state["token"])
    st.button("Logout")
    del st.session_state["auth"]
    del st.session_state["token"]
    
###### kadi test    
    
# import streamlit as st
# from streamlit_oauth import OAuth2Component

# # Set environment variables
# kadiApiBaseURL = 'https://kadi4mat.iam.kit.edu'
# AUTHORIZE_URL = kadiApiBaseURL + '/oauth/authorize'
# TOKEN_URL = kadiApiBaseURL + '/oauth/token'
# REFRESH_TOKEN_URL = kadiApiBaseURL + '/oauth/token'
# REVOKE_TOKEN_URL = kadiApiBaseURL + '/oauth/revoke'
# CLIENT_ID = st.secrets['oauthClientID']
# CLIENT_SECRET = st.secrets['oauthClientSecret']
# REDIRECT_URI = 'https://kaditest.streamlit.app/component/streamlit_oauth.authorize_button/index.html'
# SCOPE = ''

# # Create OAuth2Component instance
# oauth2 = OAuth2Component(CLIENT_ID, CLIENT_SECRET, AUTHORIZE_URL, TOKEN_URL, REFRESH_TOKEN_URL, REVOKE_TOKEN_URL)

# result = oauth2.authorize_button("Authorize", REDIRECT_URI, SCOPE, height=800, width=400, use_container_width=True, extras_params={'response_type': 'code'})
# if result:
    # st.write(result)


# #if result and 'token' in result:
    # # If authorization successful, save token in session state
    # #st.session_state.token = result.get('token')
    # #st.write(st.session_state.token)
    # #st.rerun()