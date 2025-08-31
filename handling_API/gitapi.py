import requests

def fetch_github_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        username = data.get("login", "N/A")
        country = data.get("location", "Unknown")
        email=data
        return username, country
    else:
        raise Exception("Failed to fetch user data")

def main():
    try:
        username, country = fetch_github_user("abhaymaurya57")
        print(f"Username: {username}\nCountry: {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
