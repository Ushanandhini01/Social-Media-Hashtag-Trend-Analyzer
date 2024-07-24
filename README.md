# Social-Media-Hashtag-Trend-Analyzer

Introduction
In todays world social media plays a vital role in every aspect of our lives and users crave for interesting contents. So there is a need to develop streamlit application which allows users to compose and publish posts. This application integrate with aws lambda abd dynamodb

Flow:
Streamlist post -> trigger Aws lambda -> store data in dynamodb

Features:
Post Composition: Users can compose posts containing hashtags Post Submission : Application should trigger AWS Lambda on click of post button AWS Lambda Integration : AWS Lambda receives post content parses it and stores in DynamoDB
