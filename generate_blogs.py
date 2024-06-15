"""
This script uses Forem API to extract articles from dev.to automatically.
"""

import requests, subprocess
from tqdm import tqdm

post_template = """---
title: "{title}"
date: {date}
tags: {tags}
description: "{description}"
canonicalURL: "{dev_to_link}"
disableShare: false
searchHidden: false

showToc: true
TocOpen: false
draft: false
hidemeta: false
comments: false
disableHLJS: false
hideSummary: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
ShowRssButtonInSectionTermList: true
UseHugoToc: true

# cover:
#     image: "<image path/url>" # image path/url
#     alt: "<alt text>" # alt text
#     caption: "<text>" # display caption under cover
#     relative: false # when using page bundles set this to true
#     hidden: true # only hide on current single page
---

[🔗 dev.to link]({dev_to_link})

{readme_content}
"""

subprocess.run("rm -r content/blogs".split())
subprocess.run(["mkdir", "content/blogs"])

r = requests.get("https://dev.to/api/articles?username=abir777")
articles = r.json()

pbar = tqdm(articles)
for article in pbar:
    pbar.set_description(f"Processing {article['title'][:10]}")

    title = article["title"]
    description = article["description"]
    tags = article["tag_list"]
    dev_to_link = article["url"]
    date = article["published_at"]
    article_detail = requests.get(f"https://dev.to/api/articles/{article['id']}").json()
    readme_content = article_detail["body_markdown"]

    with open(f"content/blogs/{title}.md", "w") as f:
        f.write(
            post_template.format(
                title=title,
                description=description,
                date=date,
                tags=tags,
                readme_content=readme_content,
                dev_to_link=dev_to_link,
            )
        )
