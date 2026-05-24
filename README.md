# 🎓 MCQ Hub - MSBTE Interactive Quiz App

An interactive, engaging, and analytics-driven quiz platform designed specifically for MSBTE (Maharashtra State Board of Technical Education) students. This project aims to replace traditional, static book reading with dynamic MCQ practices to help students master subjects like ETI, ETE, and Management.

![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Vite](https://img.shields.io/badge/vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=white)
![React Router](https://img.shields.io/badge/React_Router-CA4245?style=for-the-badge&logo=react-router&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

**🔗 Live Preview:** [https://eti-mcq-msbte.vercel.app/](https://eti-mcq-msbte.vercel.app/)

---

## 📖 Overview

As an MSBTE student, reading through endless PDFs and textbooks for MCQ exams can be tedious. I built **MCQ Hub** to make studying interactive and fun. The application covers various subjects (ETI, ETE, Management) unit-by-unit, providing immediate feedback on answers, detailed explanations, and performance analytics so students know exactly what topics they need to improve.

## 🛠️ Technologies

- **Frontend Framework:** React 19 + Vite
- **Routing:** React Router v7
- **Styling:** Custom CSS with Dark/Light Mode support
- **Icons & UI Elements:** `react-icons`, `canvas-confetti`
- **Data Processing:** Python scripts (for parsing and adding automated explanations to raw question data)
- **Deployment:** Vercel

## ✨ Features

- **Unit-by-Unit Quizzes:** Organized by subject (ETI, ETE, Management) and individual syllabus units.
- **Smart Performance Analytics:** At the end of each quiz, get a breakdown of your score categorized by specific topics (e.g., IoT Fundamentals, Generative AI).
- **Persistent Progress:** Your progress is saved locally. You can pick up right where you left off or reset your progress when you want a fresh start.
- **Instant Explanations:** Get immediate "Why?" explanations for questions to reinforce learning immediately after answering.
- **Dark & Light Mode:** Accessible and comfortable studying environment for day or night.
- **Gamification:** Confetti celebrations for correct answers to keep motivation high!

## 🚀 The Process (How I Built It)

1. **Data Collection & Parsing:** I started by gathering questions from various MSBTE resources. I wrote Python scripts (`scratch_parser.py` and `add_explanations.py`) to parse this raw text data, format it into structured JSON arrays, and automatically generate base explanations for the answers.
2. **UI/UX Design:** I wanted a modern, distraction-free interface. I set up a React + Vite environment and created a responsive layout, integrating a seamless dark mode.
3. **Component Architecture:** Built modular components (`SubjectSelection`, `UnitSelection`, `Quiz`) and used React Router to handle navigation.
4. **State Management & Analytics:** Implemented `localStorage` for progress saving. I also created an algorithm to map individual questions to syllabus keywords, allowing the app to generate a "Performance Analytics" screen that points out specific areas of improvement.

## 🧠 What I Learned

- **Advanced React Hooks:** Deepened my understanding of `useEffect` and lazy initialization with `useState` for interacting with `localStorage`.
- **Data Pipeline Integration:** Learned how to bridge the gap between raw unstructured data (using Python for data wrangling) and a structured frontend application (JSON ingestion in React).
- **Gamification & UX:** Realized how micro-interactions (like confetti animations and immediate color-coded feedback) significantly improve user retention and engagement in educational apps.

## 📈 How It Can Be Improved

- **User Authentication:** Adding a backend (like Firebase or Appwrite) to sync progress across multiple devices instead of just local storage.
- **Leaderboards:** Introducing a competitive aspect where students can see how they rank against their peers.
- **Timer Mode:** Adding a timed exam mode to simulate real MSBTE online exam pressure.
- **More Subjects:** Expanding the question bank to cover all branches and semesters.

## 💻 Running the Project Locally

To run this project on your local machine, follow these steps:

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/eti-mcq.git
   cd "ETI mcq"
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm run dev
   ```

4. **Open in Browser**
   Navigate to `http://localhost:5173` to view the app.

---
*Built with ❤️ for the MSBTE student community.*
