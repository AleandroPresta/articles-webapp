# Articles Webapp

## Overview

`articles-webapp` is a web application built using Django, a high-level Python web framework, and Bootstrap, a front-end framework for developing responsive and mobile-first websites. This application allows users to sign up, log in, and publish new posts, making it an ideal platform for sharing articles, blogs, or any form of written content.

## Features

- **User Authentication**: Supports user registration, login, and logout functionalities.
- **Article Management**: Users can add new posts, edit their existing posts, and delete them.
- **Responsive Design**: Utilizes Bootstrap to ensure the web app is accessible and provides a seamless experience across various devices and screen sizes.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Python (version 3.6 or newer)
- pip (Python package installer)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/articles-webapp.git
   cd articles-webapp
   ```

2. **Set Up a Virtual Environment (Optional but recommended)
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Database Migrations**
    Apply database migrations to set up the necessary database schema:
    ```bash
    python manage.py migrate
    ```

5. **Run the Development Server**
    Start the Django development server:
    ```bash
    python manage.py runserver
    ```

```markdown
# Articles Webapp

## Overview

`articles-webapp` is a web application built using Django, a high-level Python web framework, and Bootstrap, a front-end framework for developing responsive and mobile-first websites. This application allows users to sign up, log in, and publish new posts, making it an ideal platform for sharing articles, blogs, or any form of written content.

## Features

- **User Authentication**: Supports user registration, login, and logout functionalities.
- **Article Management**: Users can add new posts, edit their existing posts, and delete them.
- **Responsive Design**: Utilizes Bootstrap to ensure the web app is accessible and provides a seamless experience across various devices and screen sizes.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Python (version 3.6 or newer)
- pip (Python package installer)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/articles-webapp.git
   cd articles-webapp
   ```

2. **Set Up a Virtual Environment** (Optional but recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Database Migrations**

   Apply database migrations to set up the necessary database schema:

   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**

   Start the Django development server:

   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/` in your web browser to view the application.

## Usage

- **Sign Up**: Navigate to the sign-up page to create a new user account.
- **Log In**: Log in with your user credentials to access the application.
- **Add New Post**: Once logged in, you can add new posts by navigating to the appropriate section in the application.

## Contributing

Contributions to `articles-webapp` are welcome! Please follow the standard fork-and-pull request workflow. If you plan on adding a new feature or fixing a bug, please open an issue first to discuss your ideas.