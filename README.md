# 💼 Personal Portfolio Website

A fully responsive and modern **personal portfolio website** built with **Django** and **Bootstrap 5**, featuring a clean design, social media links, and a feedback submission system with dynamic display. This site allows visitors to know more about me, view my projects, and share feedback.

# 💼 Personal Portfolio Website

This is a fully functional, responsive, and modern **personal portfolio web application** built using **Django** and **Bootstrap 5**. It allows visitors to explore your professional profile, projects, certifications, skills, and also submit feedback. The site features dynamic resume uploading, project videos, and an admin dashboard for content management.

🎯 **Live Demo**:  
👉 [https://portfolio-ufqv.onrender.com](https://portfolio-ufqv.onrender.com/)

---

## 🧾 Project Description

This portfolio website is not just a static resume — it is a **content-managed Django web app** where you can:

- Show your **profile, biography, and contact info**
- Add, edit, and delete **projects** with rich descriptions, demo videos, and links
- Upload **certifications** with issuer and verification URL
- Dynamically **upload a resume** (automatically replaces the old one)
- Collect and display **user feedback**
- Showcase your **skills** via admin panel
- Upload your **profile image**
- All media files (images/videos/resumes) are auto-managed and structured

---

## 🚀 Key Features

- 🎨 Responsive layout with **Bootstrap 5**
- 📄 **Rich text editor** for projects & technologies (`django-ckeditor`)
- 🎥 Upload **project demo videos**
- 📎 Upload resume (`FileField`) — automatically replaces old resume file
- ✨ Display **social icons**: GitHub, LinkedIn, Coding Ninjas, Naukri.com
- 📬 **Feedback form**: name, email, phone number, message
- 💬 Display user feedback dynamically in card layout
- 🗂 Admin panel to manage all data easily
- 🌐 **Deployed on Render** with persistent media support

---

## 🗃 Models Included

### `About`
- name, profile picture, title
- bio, phone, email, degree, location, DOB

### `Skill`
- name (simple skill label)

### `Certification`
- title, issuer, issue_date, certificate_url

### `ResumeUpload`
- resume file (auto-deletes all previous resumes)

### `Project`
- title, description (RichText), technologies (RichText)
- GitHub link, live demo link, optional demo video
- start and end dates
- auto-delete video on project deletion

### `Contact`
- name, email, phone number, description (user feedback)

---

## 🛠 Tech Stack

| Category       | Technology                |
|----------------|---------------------------|
| Backend        | Django (Python)           |
| Frontend       | HTML, CSS, Bootstrap 5    |
| Editor         | CKEditor (RichText)       |
| Database       | SQLite (development)      |
| Hosting        | [Render](https://render.com) |
| Admin Panel    | Django Admin              |
| Media Storage  | Local (`media/` folder)   |
| Forms          | Django ModelForm          |
| Icons          | Bootstrap Icons           |

---

## 🧩 Folder Structure



