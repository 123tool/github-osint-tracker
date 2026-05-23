import httpx
from src.ui import print_log

async def find_username_by_email(email_target, token=None):
    """Mencari nama pengguna GitHub berdasarkan query email publik."""
    url = f"https://api.github.com/search/users?q={email_target}+in:email"
    headers = {"User-Agent": "GitSint-Pro/V2"}
    if token:
        headers["Authorization"] = f"token {token}"
        
    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(url, headers=headers, timeout=10)
            if res.status_code == 200:
                data = res.json()
                if data.get("total_count", 0) > 0:
                    items = data.get("items", [])
                    return [user.get("login") for user in items]
    except Exception as e:
        print_log(f"Gagal memetakan email ke akun: {e}", "error")
    return []

async def extract_hidden_email_from_commits(username, token=None):
    """
    Teknik Forensik Commit: Mengikis log commit publik milik user 
    untuk menemukan email asli yang tersembunyi dari pengaturan profil.
    """
    url = f"https://api.github.com/users/{username}/events/public"
    headers = {"User-Agent": "GitSint-Pro/V2"}
    if token:
        headers["Authorization"] = f"token {token}"
        
    discovered_emails = set()
    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(url, headers=headers, timeout=10)
            if res.status_code == 200:
                events = res.json()
                for event in events:
                    if event.get("type") == "PushEvent":
                        commits = event.get("payload", {}).get("commits", [])
                        for commit in commits:
                            author_email = commit.get("author", {}).get("email")
                            author_name = commit.get("author", {}).get("name")
                            # Abaikan email default generator bot milik GitHub
                            if author_email and "noreply" not in author_email:
                                discovered_emails.add(f"{author_email} (Nama Terkait: {author_name})")
    except Exception as e:
        print_log(f"Gagal melakukan inspeksi commit forensic: {e}", "error")
    return list(discovered_emails)
