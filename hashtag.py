import streamlit as st
import requests
import json
import boto3

# Specify AWS credentials and region
REGION = 'us-east-1'  # e.g., 'us-west-2'
AWS_ACCESS_KEY_ID = 'AKIA4MTWN7G2H3FV5UBW'
AWS_SECRET_ACCESS_KEY = '6PAsPy8tMEOq3Pyug99OpMkSNrSSArcXJQasSoNQ'

# Initialize DynamoDB resource with the specified region and credentials
dynamodb = boto3.resource(
    'dynamodb',
    region_name=REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)
table = dynamodb.Table('PostsTable')

# API Gateway endpoint
API_URL = 'https://dqxnia4hqa.execute-api.us-east-1.amazonaws.com/hashtag/hashtag'

def call_lambda(post_content):
    response = requests.post(API_URL, json={'post_content': post_content})
    if response.status_code == 200:
        st.success("Post submitted successfully!")
    else:
        st.error(f"Error: {response.status_code}")

def get_trending_hashtags():
    response = table.scan()
    items = response['Items']
    hashtag_count = {}
    for item in items:
        for hashtag in item['Hashtags']:
            if hashtag in hashtag_count:
                hashtag_count[hashtag] += 1
            else:
                hashtag_count[hashtag] = 1
    sorted_hashtags = sorted(hashtag_count.items(), key=lambda x: x[1], reverse=True)
    return [hashtag for hashtag, count in sorted_hashtags[:10]]

def main():
    st.title("Social Media Post Composer")

    post_content = st.text_area("Write your post:")
    if st.button("Post"):
        call_lambda(post_content)

    if st.button("Show Trending Hashtags"):
        trending_hashtags = get_trending_hashtags()
        st.write("Trending Hashtags:")
        st.write(", ".join(trending_hashtags))

if __name__ == "__main__":
    main()
