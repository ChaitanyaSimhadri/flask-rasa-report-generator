# Flask RASA Report Generation Application

## Description

This application combines a Flask web application with a RASA chatbot to automate the generation and delivery of business reports. Users can interact with the system via a web interface or through chat platforms like Slack or WhatsApp.

## Requirements

- Python 3.7+
- Flask
- RASA
- Pandas
- APScheduler
- Other dependencies listed in `requirements.txt`

## Setup

1.  Clone the repository.
2.  Create a virtual environment:

    \`\`\`bash
    python -m venv venv
    source venv/bin/activate
    \`\`\`
3.  Install the dependencies:

    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`
4.  Configure the environment variables:

    *   Create a `.env` file in the project root.
    *   Add the necessary environment variables, such as email credentials and API keys.

## Usage

1.  Start the Flask application:

    \`\`\`bash
    python app.py
    \`\`\`
2.  Start the RASA chatbot:

    \`\`\`bash
    rasa train
    rasa shell
    \`\`\`
3.  Run the scheduler:

    \`\`\`bash
    python cron\_jobs/schedule.py
    \`\`\`

## Optional Enhancements

*   Add OAuth/SSO login for teams
*   Add a dashboard to list and download past reports
*   Integrate with Power BI or Tableau for visual dashboards
*   Deploy using Docker and configure CI/CD pipeline
