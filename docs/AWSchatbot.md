# Setting up notifications from AWS to Slack

### Please ensure you've followed the other AWS setup instructions beforehand

### Setting up Slack Prerequisites
Create a new channel in Slack that you'd like to use for the notifications - this can be as public or private as you'd prefer. Once it's been created, right click on it in the sidebar and select view channel details, there is a channel ID right at the bottom, this is going to be needed for the chatbot.

You will also need to add the AWS Chatbot app to your Slack workspace and invite it to the channel.

### AWS
You can follow the instructions on [AWS for setting up slack chatbot notifications](https://docs.aws.amazon.com/dtconsole/latest/userguide/notifications-chatbot.html#)

You will need to create a SNS topic and a Chatbot client (briefly outlined below) with full details in the instructions mentioned above.

Go to the [Amazon SNS Dashboard](https://eu-west-2.console.aws.amazon.com/sns/v3/home?region=eu-west-2#/dashboard) and select Topics from the lefthand menu. Create a new topic, this is what you'll use to allow the Amazon services to link to the chatbot. A standard type is fine. You will later need to edit the access policy for the codestar service (and any others) but the predefined one should be fine to start. All other settings can be left as is. [This link](https://docs.aws.amazon.com/dtconsole/latest/userguide/set-up-sns.html) has full details on changes to the access policy


Go to the [Chatbot Dashboard](https://us-east-2.console.aws.amazon.com/chatbot/home?region=eu-west-2#/chat-clients) and if there are no configured clients for Slack, create a new client configuration for Slack and link it to the channel you've just created, you may need to sign in to Slack.
