import streamlit as st
from streamlit_oauth import OAuth2Component

# Set environment variables
kadiApiBaseURL = 'https://kadi4mat.iam.kit.edu'
AUTHORIZE_URL = kadiApiBaseURL + '/oauth/authorize'
TOKEN_URL = kadiApiBaseURL + '/oauth/token'
REFRESH_TOKEN_URL = kadiApiBaseURL + '/oauth/token'
REVOKE_TOKEN_URL = kadiApiBaseURL + '/oauth/revoke'
CLIENT_ID = st.secrets['oauthClientID']
CLIENT_SECRET = st.secrets['oauthClientSecret']
REDIRECT_URI = 'https://kaditest.streamlit.app/component/streamlit_oauth.authorize_button/index.html'
SCOPE = ''

# Create OAuth2Component instance
oauth2 = OAuth2Component(CLIENT_ID, CLIENT_SECRET, AUTHORIZE_URL, TOKEN_URL, REFRESH_TOKEN_URL, REVOKE_TOKEN_URL)

result = oauth2.authorize_button("Authorize", REDIRECT_URI, SCOPE, height=800, width=400, use_container_width=True, extras_params={'response_type': 'code'})
if result and 'token' in result:
    # If authorization successful, save token in session state
    st.session_state.token = result.get('token')
    st.write(st.session_state.token)
    st.rerun()