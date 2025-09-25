# 🎥 Video Summarizer  

A Streamlit-based web application that generates concise **summaries of videos** using **Google Gemini Generative AI**.  
Upload a video or provide a link, and the system extracts the key insights, summarizes the content, and presents it in a clean interface.  

🌐 **Live Demo on Render**: [Video Summarizer](https://video-summarization.onrender.com)  

---

## 📌 Table of Contents

- [About](#about)  
- [Features](#features)  
- [Architecture / Workflow](#architecture--workflow)  
- [Tech Stack](#tech-stack)  
- [Setup & Installation](#setup--installation)  
- [Usage](#usage)  
- [Configuration](#configuration)  
- [Limitations & Future Work](#limitations--future-work)  
- [Contributing](#contributing)  
- [License](#license)  

---

## 🧾 About

This project is designed to help users **quickly understand video content** without watching the full video.  
It uses **Google Gemini AI models** to process transcripts, extract meaning, and generate human-like summaries.  
Optional **web search enrichment** (DuckDuckGo) adds more context where needed.  

---

## ✨ Features

- 📤 Upload videos or paste video links  
- 📝 Automatic transcript processing  
- 🤖 Summarization powered by **Google Gemini AI**  
- 🌍 Optional contextual search with DuckDuckGo  
- ⚡ Interactive UI with Streamlit  
- 🔑 Secure API key handling with `.env`  

---

## 🏗 Architecture / Workflow

1. **Input**: User uploads a video or provides a link  
2. **Processing**: Extracts transcript & video frames if required  
3. **AI Analysis**: Gemini AI summarizes key insights  
4. **Enrichment**: Web search supplements missing context  
5. **Output**: User gets a clean, structured summary  

---

## 🛠 Tech Stack

- **Python 3.12+**  
- **Streamlit** – Frontend UI  
- **Google Generative AI (Gemini)** – Summarization engine  
- **DuckDuckGo Search API** – For contextual enrichment  
- **dotenv** – Manage environment variables  

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.12+  
- Google Generative AI API key  

### Installation

```bash
# Clone repository
git clone https://github.com/abhishekmohank/video-summarization.git
cd video-summarization

# Create virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate   # On Linux/macOS
# or venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

```

##🚀 Usage

1. Create a .env file in the root folder and add your API key:
```bash
GOOGLE_API_KEY=your_google_api_key_here

```
2. Run the Streamlit app:
```bash
streamlit run app.py

```
3. Open the app in your browser →
```bash
    http://localhost:8501
```
5. Upload a video or paste a link → Wait for processing → Get your summary ✅

##🔐 Configuration

Environment variables required:
```bash
GOOGLE_API_KEY=your_google_api_key

```
Make sure you do not commit your .env file.

##⚠️ Limitations & Future Work

- Processing long videos may take time
- Summarization quality depends on Gemini model
- Transcript extraction may fail on poor-quality audio
- Currently only supports one video at a time

 # Planned improvements:

    - Multi-model support (OpenAI, Claude, etc.)
    
    - Enhanced preprocessing (noise removal, segmentation)
    
    - Export summaries (PDF/Markdown)
    
    - Highlight video segments linked to summaries
    
    - Multi-language support


##🤝 Contributing
Contributions are welcome!
- Fork the repo
- Create your feature branch (git checkout -b feature/xyz)
- Commit changes (git commit -m 'Add xyz feature')
- Push branch (git push origin feature/xyz)
- Open a Pull Request


##📜 License
This project is licensed under the MIT License.
