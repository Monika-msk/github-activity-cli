import sys
import urllib.request
import json
length = len(sys.argv)
if length>1:
    username= sys.argv[1]
    print("Fetching activity for:",username)
    try:
        url = f"https://api.github.com/users/{username}/events"
        response = urllib.request.urlopen(url)
        data = response.read() 
        text = data.decode("utf-8")
        events=json.loads(text)
        for event in events:
            event_type = event['type']
            repo_name = event['repo']['name']
            if event_type == 'PushEvent':
                print("Pushed to", repo_name)
            elif event_type == 'WatchEvent':
                print("Starred", repo_name)
            elif event_type == 'IssuesEvent':
                print("Worked on an issue in", repo_name)
            elif event_type == 'IssueCommentEvent':
                print("Commented on an issue in", repo_name)
            elif event_type == 'PullRequestEvent':
                print("Worked on a pull request in", repo_name)
            elif event_type == 'CreateEvent':
                print("Created a branch/tag/repo in", repo_name)
            elif event_type == 'DeleteEvent':
                print("Deleted a branch/tag in", repo_name)
            elif event_type == 'ForkEvent':
                print("Forked", repo_name)
            elif event_type == 'ReleaseEvent':
                print("Published a release in", repo_name)
            elif event_type == 'PublicEvent':
                print("Made", repo_name, "public")
            elif event_type == 'MemberEvent':
                print("Added a collaborator to", repo_name)
            elif event_type == 'CommitCommentEvent':
                print("Commented on a commit in", repo_name)
            elif event_type == 'GollumEvent':
                print("Updated the wiki in", repo_name)
            elif event_type == 'SponsorshipEvent':
                print("Sponsorship activity in", repo_name)
            else:
                print(event_type, "in", repo_name)
    except urllib.error.HTTPError as e:
            if e.code == 404:
                print("Error:User",username,"Not found")
            else:
                print("HTTP error occured. code:", e.code)
    except urllib.error.URLError as e:
        print("Network error: could not reach GitHub. Check your internet connection.")

    
else:
    print("Usage: python github_activity.py <username>")

