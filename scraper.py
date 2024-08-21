import requests
import pwinput
from keycloak import KeycloakOpenID
import pandas
import sqlalchemy
from key_configs import keycloak_url, realm_name, client_id, client_secret, login_url, user_url
import pdb; pdb.set_trace()
#Session start. Cookie persistence
session = requests.Session()




#initializing keycloakOpenID instance
keycloak_openid = KeycloakOpenID(server_url=keycloak_url,
                                 client_id=client_id,
                                 realm_name=realm_name,
                                 client_secret_key=client_secret)


#credential inputs and token
username = input("username :")
#masks password input
password = pwinput.pwinput(prompt="password:", mask='')

token = keycloak_openid.token(username, password)
#login endpoint and token handling

headers = {'Authorization': f'Bearer {token['access token']}'}

response = session.get(login_url, headers=headers)

# Checking response
if response.status_code == 200:
    print(
        'Request Successful'
    )
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.text)





#user_response = requests.get(users_url, headers=header)
#print(user_response.headers['Content-Type'])


#responseData = user_response
#print(responseData)

#df = pandas.json_normalize(responseData, 'data')
#print(df)
