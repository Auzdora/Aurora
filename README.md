# Aurora
![](aurora.png)
<p style="font-size: 10px; text-align: right;">Photo by <a href="https://unsplash.com/@heitmannj?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Henrik Heitmann</a> on <a href="https://unsplash.com/photos/wQ1UIvNfgYQ?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a></p>

**Aurora** is an open-source project designed to connect to your local knowledge database and interact with multiple plugins using Long Life Memory (LLM). This project is an exciting experiment exploring the integration of LLM capabilities and function calling. All coders are welcome to modify and repurpose the code!

**Aurora** was developed using the 🦜️🔗 [langchain](https://github.com/hwchase17/langchain) framework. For beginners, you can familiarize yourself with some fundamental concepts in their [documentation](https://python.langchain.com/docs/get_started/introduction.html).

Currently, we are molding **Aurora** to function as a command-line tool, but stay tuned for potential web or app interfaces in the future!

## Getting Started
For those of you who want to dive right in, here are some simple steps to get started with the features provided by this project:

- **Clone the Project**: Clone this repository by executing the following command in your terminal:
    ```bash
    git clone https://github.com/Auzdora/Personal-GPT.git
    ```
- **Open the Project**: Navigate to the project's directory, or open it in VSCode.

- **Configure the Project**: In the root directory, locate the `config.json` file. This is where you can modify system settings.

- **Acquire an API Key**: Sign up for a ChatGPT account to get your API key. If you encounter issues (payment troubles, connectivity, etc.), visit [OhMyGPT](https://www.ohmygpt.com/) to access the GPT's API.

- **Set your API Key**: Input your API key and base into the `config.json` file as shown below:
    ```txt
    "OPEN_AI_API": "xxxx",
    "OPEN_AI_BASE": "https://xxxx",
    // For OhMyGPT API users, your OPEN_AI_BASE is https://api.ohmygpt.com/v1
    ```
- **Populate your Database**: You're all set to select and populate your preferred database(s).

  1. **Notion**: This project allows you to query your Notion database. See [here]() for additional information.
  2. **Markdown directory**: 🚧 **(Under Construction...)** 🚧 This feature will enable access to your local directories.
  3. **Obsidian**: 🚧 **(Under Construction...)** 🚧 Obsidian is a local personal database and can be considered as a markdown directory.

## Architecture
🚧 **(Under Construction...)** 🚧

For those interested in the inner workings of this project, this section provides a high-level overview.

The primary component of Aurora is the Agent, which receives your messages and orchestrates the process. Its primary method is `chat()`.

## Features
- Query your Notion database.
- Access and interact with your Markdown directory and Obsidian.

## To-Do List
- [x] Notion database Q&A support.
- [ ] Refactor as a command-line tool.
- [ ] Implement Chat Long Term Memory support.
- [ ] Markdown directory and Obsidian Q&A support.
- [ ] Web search plugin.
- [ ] Email plugin.
- [ ] And more...
