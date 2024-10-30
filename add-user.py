import sys
print(f"Python path: {sys.executable}")
print(f"Python version: {sys.version}")

import os
from dotenv import load_dotenv
import requests
from typing import List, Dict, Literal
import time

# At the beginning of the file
print("Loading environment variables...")
load_dotenv('production.env', override=True)
print(f"Token loaded: {os.getenv('GITHUB_TOKEN')[:10]}...")
print(f"Organization: {os.getenv('GITHUB_ORG')}")
print(f"Prefix: {os.getenv('REPO_PREFIX')}")

class GitHubPermissionManager:
    PermissionType = Literal["pull", "push", "admin", "maintain", "triage"]
    
    def __init__(self, token: str, org: str):
        if not token or not org:
            raise ValueError("Token and organization are required")
        self.token = token
        self.org = org
        self.headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        self.base_url = 'https://api.github.com'

    def get_repositories(self, prefix: str = "") -> List[Dict]:
        try:
            repos = []
            page = 1
            while True:
                response = requests.get(
                    f'{self.base_url}/orgs/{self.org}/repos',
                    headers=self.headers,
                    params={'page': page, 'per_page': 100}
                )
                response.raise_for_status()
                
                batch = response.json()
                if not batch:
                    break
                
                repos.extend([repo for repo in batch if repo['name'].startswith(prefix)])
                page += 1
                
            return repos
        except requests.exceptions.RequestException as e:
            print(f"Error fetching repositories: {e}")
            return []

    def add_collaborator(self, repo_name: str, username: str, permission: PermissionType = "push") -> bool:
        if permission not in ["pull", "push", "admin", "maintain", "triage"]:
            raise ValueError("Invalid permission")
        
        try:
            url = f'{self.base_url}/repos/{self.org}/{repo_name}/collaborators/{username}'
            response = requests.put(
                url,
                headers=self.headers,
                json={'permission': permission}
            )
            
            if response.status_code == 201:
                print(f'✅ Added {username} to repository {repo_name}')
                return True
            else:
                print(f'❌ Error adding {username} to repository {repo_name}: {response.status_code}')
                print(response.text)
                return False
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return False

def main():
    # Load environment variables
    load_dotenv('production.env', override=True)
    github_token = os.getenv("GITHUB_TOKEN")
    organization = os.getenv("GITHUB_ORG")
    repo_prefix = os.getenv("REPO_PREFIX", "")
    collaborator_username = os.getenv("COLLABORATOR_USERNAME")

    print(f"\nOperation Information:")
    print(f"Organization: {organization}")
    print(f"Repository prefix: {repo_prefix}")
    print(f"User to be added: {collaborator_username}")

    if not all([github_token, organization, collaborator_username]):
        print("Please configure the required environment variables:")
        print("GITHUB_TOKEN, GITHUB_ORG, COLLABORATOR_USERNAME")
        return

    try:
        # Initialize manager
        manager = GitHubPermissionManager(github_token, organization)
        
        # Debug: List all repositories first
        print(f"\nListing all repositories in organization {organization}...")
        all_repos = manager.get_repositories("")
        print(f"Total repositories found: {len(all_repos)}")
        print("First 5 repositories as example:")
        for repo in all_repos[:5]:
            print(f"- {repo['name']}")
        
        # Continue with original prefix search
        print(f"\nSearching repositories with prefix '{repo_prefix}'...")
        repos = manager.get_repositories(repo_prefix)
        
        if not repos:
            print(f"No repositories found with prefix '{repo_prefix}'")
            return
        
        print(f"\nFound {len(repos)} repositories:")
        for repo in repos:
            print(f"- {repo['name']}")
        
        # Confirm with user
        confirm = input("\nDo you want to add the collaborator to these repositories? (y/N): ")
        if confirm.lower() != 'y':
            print("Operation cancelled.")
            return
        
        # Add collaborator to each repository
        print("\nAdding collaborator to repositories...")
        for repo in repos:
            manager.add_collaborator(repo['name'], collaborator_username, "maintain")
            time.sleep(1)  # Small delay to avoid rate limiting
        
        print("\nProcess completed!")
    except Exception as e:
        print(f"Unexpected error: {e}")
        return

if __name__ == "__main__":
    main()