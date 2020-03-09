## Settings
* `invoke` lib does not allow tasks with underscores -> `gh_pages` in `tasks.py` renamed to `ghpages`  
* `'commit_message': '"Publish site on {}"'.format(datetime.date.today().isoformat()),` needed to swap " and ' for commit message -> commit message needs to be in "double quotes"
* added `symlinkthemes` task for `invoke` so that themes can be stored in repo subdir