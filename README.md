# GitHub User Activity CLI

A simple command-line tool to fetch and display a GitHub user's recent public activity, built with Python using only built-in libraries (no external dependencies).

## Usage
```bash
python github_activity.py <username>
```

## Features
- Fetches recent activity via the GitHub Events API
- Displays events in human-readable format (pushes, stars, issues, PRs, etc.)
- Graceful error handling for invalid usernames and network failures

## Project URL



## Note
As of October 2025, GitHub removed commit counts and details from PushEvent payloads in the Events API for performance reasons. This tool reflects that — push events are shown without a commit count.
