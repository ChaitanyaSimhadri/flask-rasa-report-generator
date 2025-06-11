import time
import schedule

def generate_daily_report():
    print("Generating daily report...")
    # Add report generation logic here
    print("Daily report generated.")

schedule.every().day.at("08:00").do(generate_daily_report)

while True:
    schedule.run_pending()
    time.sleep(60)
