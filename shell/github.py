from pygithub3 import Github

gh = Github(login='davidam', password='lala')

davidam = gh.users.get() # Auth required
davazp = gh.users.get('davazp')
# copitux = <User (copitux)>

davidam_followers = gh.users.followers.list().all()
davazp_followers = gh.users.followers.list('davazp').all()

print("davidam followers:")
print(davidam_followers)
print("davazp followers:")
print(davazp_followers)
