# AI Agent Boot 🤖

> **Boot.dev Learning Project** - An AI-powered coding agent that can interact with your filesystem and execute Python code using Google's Gemini AI.

This project demonstrates how to build an AI agent that can perform various file operations, execute Python scripts, and provide intelligent assistance for coding tasks. Built as part of the [Boot.dev](https://boot.dev) curriculum.

## 🎯 What This Project Does

The AI Agent Boot is a command-line tool that creates an intelligent coding assistant capable of:

- **File System Operations**: List directories, read file contents, and write new files
- **Code Execution**: Run Python scripts with arguments and capture output
- **Intelligent Planning**: Uses Google Gemini AI to create execution plans and make function calls
- **Safety Features**: All operations are constrained to the working directory for security

## 🏗️ Project Structure

```
agent_boot/
├── main.py                 # Main CLI entry point and agent loop
├── functions/              # AI function modules
│   ├── get_files_info.py   # Directory listing functionality
│   ├── get_file_content.py # File reading functionality
│   ├── run_python_file.py  # Python script execution
│   ├── write_file.py       # File writing functionality
│   ├── call_function.py    # Function call dispatcher
│   └── config.py          # Configuration settings
├── calculator/             # Example calculator project
│   ├── main.py            # Calculator CLI
│   ├── pkg/
│   │   ├── calculator.py  # Calculator logic
│   │   └── render.py      # JSON output formatting
│   └── tests.py           # Calculator tests
├── tests.py               # Function testing suite
└── pyproject.toml         # Project dependencies
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.12 or higher
- A Google Gemini API key

### 1. Clone and Install Dependencies

```bash
# Install dependencies using uv (recommended)
uv sync

# Or using pip
pip install google-genai python-dotenv
```

### 2. Set Up Environment Variables

Create a `.env` file in the project root:

```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

### 3. Get Your Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Create an API key
3. Add it to your `.env` file

## 📖 Usage

### Basic Usage

```bash
# Ask the AI agent to perform a task
python main.py "List all files in the calculator directory"

# Request code analysis
python main.py "Read the calculator.py file and explain how it works"

# Ask for code execution
python main.py "Run the calculator with the expression '5 + 3 * 2'"

# Request file operations
python main.py "Create a new file called 'test.txt' with the content 'Hello World'"
```

### Verbose Mode

Enable verbose output to see the AI's planning process:

```bash
python main.py "Analyze the project structure" --verbose
```

This will show:

- Token usage statistics
- Function calls being made
- Iteration details
- AI reasoning process

### Example Interactions

**File Analysis:**

```bash
python main.py "What files are in this project and what do they do?"
```

**Code Execution:**

```bash
python main.py "Test the calculator by running it with different mathematical expressions"
```

**Development Tasks:**

```bash
python main.py "Read the tests.py file and run all the tests to see if they pass"
```

## 🔧 Available AI Functions

The AI agent has access to these core functions:

### `get_files_info`

- Lists files and directories with sizes
- Provides directory structure overview
- Calculates total directory sizes

### `get_file_content`

- Reads file contents safely
- Handles large files with truncation (10KB limit)
- Supports various text encodings

### `run_python_file`

- Executes Python scripts with arguments
- Captures both stdout and stderr
- 30-second timeout for safety
- Returns formatted output

### `write_file`

- Creates or overwrites files
- Automatically creates directory structure
- Constrained to working directory

## 🎮 Example: Calculator Project

The project includes a complete calculator implementation as a demonstration:

```bash
# Let the AI run the calculator
python main.py "Run the calculator to compute 15 + 7 * 3"

# Ask for code analysis
python main.py "Explain how the calculator handles operator precedence"

# Request testing
python main.py "Run the calculator tests and tell me if they pass"
```

The calculator supports:

- Basic arithmetic operations (+, -, \*, /)
- Proper operator precedence
- JSON-formatted output
- Error handling for invalid expressions

## 🛡️ Security Features

- **Directory Constraints**: All file operations are restricted to the working directory
- **File Size Limits**: File content reading is limited to 10KB to prevent memory issues
- **Execution Timeout**: Python script execution has a 30-second timeout
- **Path Validation**: All paths are validated to prevent directory traversal attacks

## 🔄 How the Agent Loop Works

1. **User Input**: You provide a natural language prompt
2. **AI Planning**: Gemini AI analyzes the request and creates an execution plan
3. **Function Calls**: The AI makes function calls to perform operations
4. **Execution**: Functions are executed safely within constraints
5. **Response**: Results are processed and a final response is generated
6. **Iteration**: The process repeats until the task is complete (max 20 iterations)

## 🎓 Learning Objectives

This Boot.dev project teaches:

- **AI Agent Architecture**: How to build agents that can use tools
- **Function Calling**: Implementing AI function calling with proper schemas
- **Safety and Security**: Constraining AI operations for safe execution
- **Error Handling**: Robust error handling in AI applications
- **CLI Development**: Building command-line interfaces for AI tools
- **API Integration**: Working with Google's Gemini AI API

## 🧪 Testing

Run the test suite to verify all functions work correctly:

```bash
python tests.py
```

This will test all the core functions with various scenarios and edge cases.

## 🤝 Contributing

This is a learning project! Feel free to:

- Add new functions for the AI agent
- Improve error handling
- Add more example projects
- Enhance the calculator functionality
- Add support for additional AI models

## 📝 License

This project is created for educational purposes as part of the Boot.dev curriculum.

## 🔗 Resources

- [Boot.dev](https://boot.dev) - Learn backend development
- [Google Gemini AI](https://ai.google.dev/) - AI model documentation
- [Function Calling Guide](https://ai.google.dev/gemini-api/docs/function-calling) - Gemini function calling docs

---

**Happy Learning! 🚀**

_Built with ❤️ as part of the Boot.dev AI Agent course_
