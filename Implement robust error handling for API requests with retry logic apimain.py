from apiclient import APIClient
def display_posts(posts):
    if not posts:
        print("No data to display")
        return
    print("POSTS")
    print("-" * 40)
    for post in posts[:5]:  
        print(f"ID    : {post['id']}")
        print(f"Title : {post['title']}")
        print("-" * 40)
def main():
    client = APIClient(
        base_url="https://jsonplaceholder.typicode.com",
        retries=3,
        timeout=5
    )
    posts = client.get("/posts")
    display_posts(posts)
if __name__ == "__main__":
    main()
