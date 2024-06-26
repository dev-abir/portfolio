---
title: "snake"
date: 2020-05-30T15:31:32Z
tags: ['cpp', 'game', 'game-development', 'sfml', 'snake-game']
description: "A simple Snake game in C++, using the SFML library."
canonicalURL: "https://github.com/dev-abir/snake"
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

[🔗 Github repo](https://github.com/dev-abir/snake)

# snake
A simple Snake game in C++, using the [SFML](https://www.sfml-dev.org/) library.

## How to run:
Grab the latest stable compiled binaries [here](https://github.com/dev-abir/snake/releases/latest)(scroll down, and check the **Assets**)

## How to compile:
- I generally use an ubuntu-based distro, I use this command to compile: `g++ src/*.cpp -Wall -Wextra -Wpedantic -O3 -o build/game -I lib/SFML-2.5.1/include -L lib/SFML-2.5.1/lib -Wl,-rpath,./lib/SFML-2.5.1/lib -lsfml-graphics -lsfml-window -lsfml-system`

- **Please place the SFML-2.x.x library under `lib` directory, I have added this directory specifically for putting libraries.**

- **Please place the executable under `build` directory, I have added this directory specifically for putting compiled binaries.**

- For other os's I would highly encourage you to follow the steps given [here](https://www.sfml-dev.org/tutorials/2.5).
Find the way to build for your OS/IDE/compiler under `Getting started` heading. They have explained most of the steps very well.

- This whole process could be automated, using CMake. I may add in future.

**Thanks in advance for contributing to my project :relaxed:**

