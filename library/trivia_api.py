#!/usr/bin/python

# Import required modules from Ansible
from ansible.module_utils.basic import AnsibleModule
import requests

# Function to fetch trivia questions from the API
def fetch_trivia_questions(amount, difficulty):
    url = f"https://opentdb.com/api.php?amount={amount}&difficulty={difficulty}"
    response = requests.get(url)
    response_data = response.json()

    # Check if the response contains questions
    if response.status_code == 200 and response_data.get("results"):
        return response_data["results"]
    else:
        return []

# Main function
def main():
    # Define the module arguments
    module_args = dict(
        amount=dict(type='str', required=True),
        difficulty=dict(type='str', required=True),
    )

    # Define the result dictionary
    result = dict(
        changed=False,
        questions=[],
        msg='',
    )

    # Initialize the Ansible module
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Get values of parameters from module params
    amount = module.params['amount']
    difficulty = module.params['difficulty']

    # Fetch trivia questions using the custom function
    questions = fetch_trivia_questions(amount, difficulty)
    result['questions'] = questions

    # Exit Ansible module with result
    module.exit_json(**result)

if __name__ == '__main__':
    main()


