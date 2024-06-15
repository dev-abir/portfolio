"""
This script uses github API to extract project info automatically.
This script will pretty much be stagnant, except the project list part.
"""

import requests, subprocess, datetime
from dataclasses import dataclass
from tqdm import tqdm


@dataclass
class Project:
    repo_owner: str
    repo_name: str


projects = [
    Project("rasoi-devs", "rasoi"),
    Project("Hello-Moon", "spaceapps-2021"),
    #
    Project("dev-abir", "chlorophyll"),
    Project("dev-abir", "aiPlays-python"),
    Project("dev-abir", "portfolio"),
    Project("dev-abir", "ChitChat"),
    Project("dev-abir", "sonic"),
    Project("dev-abir", "currency-exchange"),
    # Project("dev-abir", "multiplayer_tic_tac_toe"),
    Project("dev-abir", "tanks"),
    Project("dev-abir", "quiz"),
    Project("dev-abir", "snake"),
    Project("dev-abir", "gameOfLifeJS"),
    # "GNIT_CSE"
]

post_template = """---
title: "{title}"
date: {date}
tags: {tags}
description: "{description}"
canonicalURL: "{github_link}"
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

[🔗 Github repo]({github_link})

{readme_content}
"""

subprocess.run("rm -r content/projects".split())
subprocess.run(["mkdir", "content/projects"])

pbar = tqdm(projects)
for project in pbar:
    pbar.set_description(f"Processing {project.repo_name}")

    r = requests.get(
        f"https://api.github.com/repos/{project.repo_owner}/{project.repo_name}"
    )
    data = r.json()
    # title = data["name"] (won't be used)
    description = data.get("description") or project.repo_name
    tags = data["topics"]
    date = data["created_at"]

    _default_branch = data["default_branch"]
    readme_content = requests.get(
        f"https://raw.githubusercontent.com/{project.repo_owner}/{project.repo_name}/{_default_branch}/README.md"
    ).text
    lines_wo_blank = [l for l in readme_content.split("\n") if l != ""]
    title = lines_wo_blank[0].removeprefix("#").strip()

    with open(f"content/projects/{project.repo_name}.md", "w") as f:
        f.write(
            post_template.format(
                title=title,
                description=description,
                date=date,
                tags=tags,
                readme_content=readme_content,
                github_link=f"https://github.com/{project.repo_owner}/{project.repo_name}",
            )
        )
