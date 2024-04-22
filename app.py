import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv

load_dotenv()

slack_bot_token = "your-slack-bot-token"
slack_app_token = "your-slack-app-token"
admin_user_id = "U06U23SR8C9"

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# Dictionary to track extra points
points = {}

@app.event("message")
def message_hello(event, say):

    user_id = event["user"]
    text = event["text"]
    channel_id = event["channel"]
    
    if user_id == admin_user_id and channel_id.startswith("D"):
        if "extra" in text:
            # Increment the extra points for the user
            points[channel_id] = points.get(channel_id, 0) + 1
            
            # Reply to the message with the updated point total
            say(
                text=f"You've earned an extra point! Total points: {points[channel_id]}",
                channel=channel_id
            )

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()