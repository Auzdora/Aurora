# Personal-GPT
**Personal-GPT** is an open source project which can connects to your own local knowledge database and multiple plugins with LLM. You can try to unleash the potential power of function calling and your personal data. Its an experiment project that try to combine both LLM capability and function calling. Feel free to change and reuse the code!


**Personal-GPT** is built by 🦜️🔗 [langchain](https://github.com/hwchase17/langchain) framework, you can learn some basic concepts in their [docs](https://python.langchain.com/docs/get_started/introduction.html).


In current version, I'm building it towards to a command line tools. Maybe add a web or app interface in the future.
## How to start?
If you don't interested in reading this repo and just want to use it, you could follow in following steps to make use of features supported by this project.
- **Clone project**: Clone this repo running the following command in your terminal
    ```bash
    git clone https://github.com/Auzdora/Personal-GPT.git
    ```
- **Open project**: Once you had this repo in your project, open its directory or in VSCode.
- **Config project**: In the root directory, find the file called `config.json` which gives you a interface to change system settings.
- **Get API Key**: Create a ChatGPT account and get its API key. If you have trouble with your own API (can't pay, connect issue, etc, please refer to [OhMyGPT](https://www.ohmygpt.com/) for accessing GPT's API).
- **Set API Key**: Fill your API key and base into `config.json`.
    ```txt
    "OPEN_AI_API": "xxxx",
    "OPEN_AI_BASE": "https://xxxx",
    // If you'er using OnMyGPT API, you OPEN_AI_BASE is https://api.ohmygpt.com/v1
    ```
- **Dump your database**: You can now choose which database you want to dump. You can also dump as many as you want.
  1. **Notion**: This project supports you ask questions about your notion database. Jump [here]() for further information.
  2. **Markdown directory**: 🚧 **(Building...)** 🚧 It supports accessing you computer's local directory. 
  3. **Obsidian**: 🚧 **(Building...)** 🚧 Obsidian is a localized personal database. You can treat it as a markdown directory.


## Architecture
🚧 **(Building...)** 🚧
This part is for who want to understand how this project works and gives you a generally picture of it.

The main component of Personal-GPT is Agent. Agent is a unit where recieve you message and schedule the whole proccess. The most important interface of it is `chat()`.

## Feature
- Access your notion database for Q&A.
- Access your markdown directory and Obsidian for Q&A.

## To do list
- [x] Notion database Q&A support.
- [ ] Refactor to command line tools.
- [ ] Chat long term memory support.
- [ ] Markdown directory and Obsidian Q&A support.
- [ ] Web searching plugins.
- [ ] Send email plugins.
- [ ] ...