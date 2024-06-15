# portfolio

This is my portfolio site. I try to keep it as updated as possible.

I used [Hugo](https://gohugo.io/) (cuz, I am too lazy) and [this theme](https://github.com/adityatelange/hugo-PaperMod). Also, I don't do frontend work primarily.

The projects and blogs are all auto-generated (see `generate_projects.py` and `generate_blogs.py`).

The public folder contains the resultant build files (static HTML and styles) after I invoke `hugo`. It is present at [github.io](https://github.com/dev-abir/dev-abir.github.io) repository. This repo is used by github to actually host the site. I set it as a submodule, to directly transfer the changes there, whenever I update the source code and generate a new build. Thus we can both host the site and show the source code from a single (almost) repo.

## Notes for future

- To run locally: `hugo server` or `hugo server -D`.

- To build: `hugo`.

- The `themes` folder contains **modified** PaperMod theme files (added Particles effect). It is just git-clonned, I should convert that to submodule in future.

- The `archetypes` folder contains some default content for new posts. If we create new post using hugo CLI, then it will use those archetypes, obviously we can ovveride those content and the overriden content will be used to build the side.

- To update this thing:
    - Clone the `public` folder (if not clonned properly) `git submodule update --init --recursive`
    - Do changes in the source code, then (optionally delete all content, except the `.git` folder of `public`).
    - Then invoke `hugo` to rebuild contents of `public`.
    - Now at first, git add, commit and push the submodule (`git push origin HEAD:master`).
    - Then, you can do the same for the parent (root) folder.
