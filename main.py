import sys
import os
from dotenv import load_dotenv
import time

print("""
╔════════════════════════════════════════════════════════════════╗
║              GitHub Bulk Permissions Manager                   ║
║                                                                ║
║  Purpose: Manage collaborators on multiple GitHub repositories ║
║  Version: 1.0.0                                                ║
║  Author: Roberto Gentile                                       ║
║  License: MIT                                                  ║
╚════════════════════════════════════════════════════════════════╝
""")

def check_environment():
    """Validate and display environment configuration"""
    print("\n🔍 Checking Environment Configuration...")
    print("═" * 50)
    
    # Python Environment
    print(f"📌 Python Version: {sys.version.split()[0]}")
    print(f"📍 Python Path: {sys.executable}")
    
    # Load Environment Variables
    load_dotenv('production.env', override=True)
    
    # Required Variables
    env_vars = {
        "GITHUB_TOKEN": os.getenv("GITHUB_TOKEN"),
        "GITHUB_ORG": os.getenv("GITHUB_ORG"),
        "REPO_PREFIX": os.getenv("REPO_PREFIX"),
        "COLLABORATOR_USERNAME": os.getenv("COLLABORATOR_USERNAME")
    }
    
    # Check and Display Status
    all_valid = True
    print("\n📋 Environment Variables Status:")
    for var, value in env_vars.items():
        if value:
            status = "✅ Set" if var != "GITHUB_TOKEN" else f"✅ Set (ends in ...{value[-4:]})"
            print(f"{var}: {status}")
        else:
            print(f"{var}: ❌ Missing")
            all_valid = False
    
    return all_valid

def display_menu():
    """Display the main menu options"""
    print("\n" + "═" * 50)
    print("🔧 Available Operations:")
    print("═" * 50)
    print("1. Add Collaborator to Repositories")
    print("2. Remove Collaborator from Repositories")
    print("3. Check Environment Configuration")
    print("4. Exit")
    print("═" * 50)

def validate_and_update_env_var(var_name: str, current_value: str) -> str:
    """Validate and optionally update an environment variable."""
    print(f"\n📝 Current {var_name}: {current_value}")
    keep = input(f"Do you want to keep this {var_name}? (Y/n): ").lower()
    
    if keep == 'n':
        new_value = input(f"Enter new {var_name}: ").strip()
        if new_value:
            print(f"✅ {var_name} updated for this session")
            return new_value
        print(f"⚠️ Invalid input. Keeping current {var_name}")
    
    return current_value

def execute_operation(choice: str):
    """Execute the selected operation with variable validation"""
    if choice not in ["1", "2", "3", "4"]:
        print("\n❌ Invalid option. Please try again.")
        return

    if choice == "3":
        check_environment()
        return
    
    if choice == "4":
        print("\n👋 Goodbye!")
        sys.exit(0)

    # Load initial environment variables
    load_dotenv('production.env', override=True)
    github_token = os.getenv("GITHUB_TOKEN")
    organization = os.getenv("GITHUB_ORG")
    repo_prefix = os.getenv("REPO_PREFIX", "")
    collaborator_username = os.getenv("COLLABORATOR_USERNAME")

    print("\n🔍 Validating Configuration...")
    print("═" * 50)

    # Validate and potentially update each variable
    organization = validate_and_update_env_var("GitHub Organization", organization)
    repo_prefix = validate_and_update_env_var("Repository Prefix", repo_prefix)
    collaborator_username = validate_and_update_env_var("Collaborator Username", collaborator_username)

    # Final confirmation with all values
    print("\n📋 Final Configuration Summary:")
    print("═" * 50)
    print(f"Organization: {organization}")
    print(f"Repository Prefix: {repo_prefix}")
    print(f"Collaborator: {collaborator_username}")
    print("═" * 50)

    confirm = input("\n⚠️ Proceed with these settings? (yes/NO): ").lower()
    if confirm != 'yes':
        print("Operation cancelled.")
        return

    # Execute the appropriate operation
    try:
        if choice == "1":
            print("\n📥 Executing Add Collaborator Operation...")
            from add_user import main as add_user_main
            add_user_main(organization, repo_prefix, collaborator_username)
        else:
            print("\n📤 Executing Remove Collaborator Operation...")
            from remove_user import main as remove_user_main
            remove_user_main(organization, repo_prefix, collaborator_username)
    except Exception as e:
        print(f"❌ Error executing operation: {str(e)}")

def main():
    """Main program loop"""
    try:
        # Initial environment check
        env_valid = check_environment()
        if not env_valid:
            print("\n⚠️  Warning: Some environment variables are missing!")
            confirm = input("Do you want to continue anyway? (y/N): ")
            if confirm.lower() != 'y':
                print("\n👋 Goodbye!")
                return
        
        # Main program loop
        while True:
            display_menu()
            choice = input("\n🔍 Please select an option (1-4): ")
            
            if choice in ["1", "2", "3", "4"]:
                execute_operation(choice)
                
                if choice != "4":  # If not exit
                    input("\n⏸️  Press Enter to continue...")
            else:
                print("\n❌ Invalid option. Please select a number between 1 and 4.")
            
            time.sleep(0.5)  # Small delay for better UX
    
    except KeyboardInterrupt:
        print("\n\n👋 Operation cancelled by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
    finally:
        print("\n" + "═" * 50)

if __name__ == "__main__":
    # Roberto esteve aqui
    main() 