projects = [
    "aiPlays-python",
    "chlorophyll",
    "ChitChat",
    "currency-exchange",
    "multiplayer_tic_tac_toe",
    # "tanks",
    "quiz",
    # "snake",
    # "gameOfLifeJS",
    # "GNIT_CSE"
]

post_template = """---
title: "{title}"
date: {date}
tags: {tags}
description: "{description}"
disableShare: false
# cover:
#     image: "<image path/url>" # image path/url
#     alt: "<alt text>" # alt text
#     caption: "<text>" # display caption under cover
#     relative: false # when using page bundles set this to true
#     hidden: true # only hide on current single page
---

[🔗 Github repo]({github_link})
{readme_content}
"""

import requests, subprocess, datetime

subprocess.run("rm -r content/projects".split())
subprocess.run(["mkdir", "content/projects"])

import urllib.request, json

for project in projects:
    with urllib.request.urlopen(
        f"https://api.github.com/repos/dev-abir/{project}"
    ) as url:
        data = json.load(url)
        # title = data["name"] (won't be used)
        description = data["description"]
        tags = data["topics"]

    readme_content = requests.get(
        f"https://raw.githubusercontent.com/dev-abir/{project}/main/README.md"
    ).text
    lines_wo_blank = [l for l in readme_content.split("\n") if l != ""]
    title = lines_wo_blank[0].removeprefix("#").strip()
    description = lines_wo_blank[1]

    with open(f"content/projects/{project}.md", "w") as f:
        f.write(
            post_template.format(
                title=title,
                description=description,
                date=datetime.datetime.now().strftime("%Y-%m-%d"),
                tags=tags,
                readme_content=readme_content,
                github_link=f"https://github.com/dev-abir/{project}",
            )
        )
